# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os
import io
import time
import re
import yaml
import markdown

from collections import OrderedDict, defaultdict
from itertools import groupby
from html2text import html2text
from pybtex.database import parse_file, Entry, BibliographyData
from markdown.util import etree
from .variables import Variable


def escape(text):
    # Recent Python 3.2 have html module with html.escape() and html.unescape() functions.
    # html.escape() differs from cgi.escape() by its defaults to quote=True
    try:
        import html
        return html.escape(text)
    except ImportError:
        import cgi
        return cgi.escape(text)


def gen_id(n=1, pre="uuid-"):
    # The HTML4 spec says:
    # ID and NAME tokens must begin with a letter ([A-Za-z]) and may be followed by any number of letters,
    # digits ([0-9]), hyphens ("-"), underscores ("_"), colons (":"), and periods (".").
    import uuid
    if n == 1:
        return pre + str(uuid.uuid4())
    elif n > 1:
        return [pre + str(uuid.uuid4()) for i in range(n)]
    else:
        raise ValueError("n must be > 0 but got %s" % str(n))


def splitall(path):
    """Return list with the components of a `path`."""
    allparts = []
    while True:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


class MyEntry(Entry):
    """https://bitbucket.org/pybtex-devs/pybtex/"""

    def to_markdown(self):
        # Entry('article', fields=[('Title', 'Efficient Interpolation Technique for {B}ethe-{S}alpeter Calculation of Optical Spectra'), ('Year', '2016'), ('volume', '203C'), ('pages', '83-93'), ('Journal', 'Comput. Phys. Comm.'), ('Doi', '10.1016/j.cpc.2016.02.008'), ('Owner', 'yannick'), ('Timestamp', '2015.08.27')], persons=OrderedCaseInsensitiveDict([('Author', [Person('Gillet, Y.'), Person('Giantomassi, M.'), Person('Gonze, X.')])]))
        # Entry('book', fields=[('title', 'Electrons and phonons'), ('publisher', 'Oxford University Press'), ('year', '1960')], persons=OrderedCaseInsensitiveDict([('author', [Person('Ziman, J. M.')])]))

        fields = self.fields
        title = fields["title"]

        if sys.version[0:3] <= '2.7':
            authors = ", ".join(unicode(p) for p in self.persons["author"])
        else:
            authors = ", ".join(str(p) for p in self.persons["author"])

        if self.type == "article":
            s = '{}  \n{}  \n'.format(authors, title)
            if "eprint" in fields:
                s += "{} **{}**, {} ({})".format(fields["journal"], fields.get("archivePrefix", ""), fields["eprint"], fields["year"])
            else:
                s += "{} **{}**, {} ({})".format(fields["journal"], fields["volume"], fields["pages"], fields["year"])

        elif self.type in ("book", "incollection"): # FIXME Better treatment for incollection
            #editors = ", ".join(str(e) for e in self.persons["editor"]])
            s = '{}  \n{}  \n'.format(authors, title)
            s += "{} ({})".format(fields["publisher"], fields["year"])
            if "isbn" in fields:
                s += "isbn: %s" % fields["isbn"]

        elif self.type in ("phdthesis", "mastersthesis"):
            s = '{}  \n{}  \n{} ({})'.format(authors, title, fields["school"], fields["year"])

        elif self.type == "misc":
            s = '{}  \n{} ({})'.format(authors, title, fields["year"])

        else:
            raise TypeError("Don't know how to convert type: `%s` into markdown string" % self.type)

        s += "  \n"
        if "url" in fields:
            s += 'URL: <a href="{url}" target="_blank">{url}</a>'.format(url=fields["url"])
        elif "doi" in fields:
            doi = fields["doi"]
            doi_root = "https://doi.org/"
            if not doi.startswith(doi_root): doi = doi_root + doi
            s += 'DOI: <a href="{doi}" target="_blank">{doi}</a>'.format(doi=doi)

        # Add modal window with bibtex entry.
        link, modal = self.get_bibtex_linkmodal()
        s += link + modal

        return s

    #def to_html(self):
    #    return markdown.markdown(self.to_markdown())

    def to_bibtex(self):
        """Return the data as a unicode string in the given format."""
        return BibliographyData({self.key: self}).to_string("bibtex")

    def get_bibtex_linkmodal(self):
        # https://v4-alpha.getbootstrap.com/components/modal/#examples
        text = "<pre>" + escape(self.to_bibtex()) + "</pre>"
        # Construct ids from self.key as they are unique.
        modal_id, modal_label_id = "modal-id-%s" % self.key, "modal-label-id-%s" % self.key

        link = """<!-- Links -->
<a data-toggle="modal" href="#{modal_id}">bibtex</a>""".format(**locals())

        modal = """\
<!-- Modal -->
<div class="modal fade" id="{modal_id}" tabindex="-1" role="dialog" aria-labelledby="{modal_label_id}">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="{modal_label_id}">bibtex</h4>
      </div>
      <div class="modal-body"> {text} </div>
    </div>
  </div>
</div>""".format(**locals())

        return link, modal


_WEBSITE = None

def build_website(root, verbose=0):
    global _WEBSITE
    assert _WEBSITE is None
    _WEBSITE = Website(root, verbose=verbose)
    return _WEBSITE


def get_website():
    global _WEBSITE
    assert _WEBSITE is not None
    return _WEBSITE


class Website(object):

    #WIKILINK_RE = r'\[\[([\w0-9_ -]+)\]\]'
    #WIKILINK_RE = r'\[\[([\w0-9_ -\./]+)\]\]'
    WIKILINK_RE = r'\[\[([^\[]+)\]\]'

    def __init__(self, root, verbose=0):
        start = time.time()
        self.root = os.path.abspath(root)
        self.verbose = verbose

        # Read mkdocs configuration file.
        with io.open(os.path.join(self.root, "../", "mkdocs.yml"), "rt", encoding="utf-8") as fh:
            self.config = yaml.load(fh)

        # Build database with Abinit input variables
        from .variables import get_variables_code
        self.variables_code = get_variables_code()

        # Get bibtex references and cast to MyEntry instance.
        self.bib_data = parse_file(os.path.join(self.root, "abiref.bib"), bib_format="bibtex")
        for entry in self.bib_data.entries.values():
            entry.__class__ = MyEntry

        # Get code statistics.
        self.abinit_stats = AbinitStats(os.path.join(self.root, "statistics.txt"))
        self.abinit_stats.json_dump(os.path.join(self.root, "data", "statistics.json"))

        # Build AbinitTestSuite object.
        from doc import tests as tmod
        from doc.tests.pymods.testsuite import ChainOfTests
        tests = []
        for t in tmod.abitests.select_tests(suite_args=[], regenerate=True):
            #if isinstance(t, ChainOfTests):  # FIXME?
            if hasattr(t, "tests"):
                tests.extend(t.tests)
            else:
                #print(type(t))
                tests.append(t)
        #if hasattr(test, "topics"): print(test.topics)

        #self.rpath2test = {os.path.relpath(t.inp_fname, self.root): t for t in tests}
        #self.rpath2test = {t.inp_fname: t for t in tests}
        self.rpath2test = {}
        for t in tests:
            toks = splitall(t.inp_fname)[-4:]
            key = os.path.join(*toks)
            self.rpath2test[key] = t
        #print(self.rpath2test.keys())

        def test_get_varnames(test, varnames):
            """This should become a method of BaseTest."""
            with io.open(test.inp_fname, "rt", encoding="utf-8") as fh:
                s = fh.read()
            vused = [v for v in varnames if v in s] # TODO This can be improved.
            return vused

        # Find variables used in tests.
        for vd in self.variables_code.values():
            for var in vd.values():
                assert not hasattr(var, "tests")
                var.tests = []

        for test in tests:
            vd = self.variables_code.get(test.executable, None) # FIXME Multibinit, conducti?
            if vd is None: continue
            for vname in test_get_varnames(test, list(vd.keys())):
                var = vd[vname]
                var.tests.append(test)
                # TODO
                #ratio_all
                #ratio_in_tuto

        print("Initial website generation completed in %.2f [s]" % (time.time() - start))

    #def __str__(self):
    #    lines = []
    #    app = lines.append
    #    return "\n".join(lines)

    def generate_markdown_files(self):
        start = time.time()

        # Write files with the description of the input variables.
        workdir = os.path.join(self.root, "input_variables")
        with io.open(os.path.join(workdir, "index.md"), "wt", encoding="utf-8") as fh:
            for code, vd in self.variables_code.items():
                fh.write("## **%s** variables   \n\n" % code)
                fh.write(vd.get_vartabs_html())
                fh.write(2*"\n" + "* * *\n")

        for code, vd in self.variables_code.items():
            vd.write_markdown_files(workdir)

        # Add plotly figures.
        with io.open(os.path.join(workdir, "connections.md"), "wt", encoding="utf-8") as fh:
            fh.write("---\nplotly: true\n---\n\n")
            for code, vd in self.variables_code.items():
                for varset in vd.all_varset:
                    fh.write("## %s, varset: %s  \n\n" % (code, varset))
                    fh.write(vd.get_plotly_networkx(varset=varset, include_plotlyjs=False))
                    #fh.write(vd.get_plotly_networkx_3d(varset=varset, include_plotlyjs=False))
                    fh.write(2*"\n" + "* * *\n")

        #Input variables, statistics:
        #occurrences in the input files provided with the package
        #This document lists the input variables for ABINIT and three post-processors of ABINIT,
        #in order of number of occurrence in the input files provided with the package.

        with io.open(os.path.join(workdir, "varset_stats.md"), "wt", encoding="utf-8") as fh:
            for code, vd in self.variables_code.items():
                num_tests = len([test for test in self.rpath2test.values() if test.executable == code])
                fh.write("\n\n# **%s** \n\n" % code)
                fh.write("%d tests\n\n" % num_tests)
                # TODO The number of tests is smaller than ecut! Count Tutorial
                items = sorted([(len(v.tests), v) for v in vd.values()], key=lambda t: t[0], reverse=True)
                # https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
                lines = ['<ul class="list-group">']
                for count, group in groupby(items, key=lambda t: t[0]):
                    vlist = [item[1] for item in sorted(group, key=lambda t: t[1].name)]
                    s = ", ".join(v.website_ilink() for v in vlist)
                    # Set color depending on coverage.
                    ratio = 100 * count / num_tests
                    if ratio > 40:
                        cls = "list-group-item-success"
                    elif ratio > 2:
                        cls = "list-group-item-warning"
                    else:
                        cls = "list-group-item-danger"
                    lines.append('<li class="list-group-item %s"> %s <span class="badge"> %d </span></li>' % (cls, s, count))

                fh.write("\n".join(lines) + "</ul>")

        print("Generating Markdown files with topics ...")
        workdir = os.path.join(self.root, "topics")

        # FIXME: this won't find all topics e.g AbiPy
        all_topics = set()
        for code, vd in self.variables_code.items():
            for var in vd.values():
                all_topics.update(var.topic_tribes.keys())
        all_topics = sorted(all_topics)

        index_md = ["Alphabetical list of topics"]
        for firstchar, group in groupby(all_topics, key=lambda t: t[0]):
            index_md.append("## *%s*" % firstchar)
            index_md.extend("- [[topic:%s]]" % topic for topic in group)

        with io.open(os.path.join(workdir, "index.md"), "wt", encoding="utf-8") as fh:
            fh.write("\n".join(index_md))

        for code, vd in self.variables_code.items():
            # Get list of topics for this `code`.
            topics = set()
            for var in vd.values():
                topics.update(var.topic_tribes.keys())

            # Read template and prepare markdown string
            repo_root = "/Users/gmatteo/git_repos/gitlab_trunk_abinit/doc/topics/origin_files/"
            for topic in sorted(topics):
                with io.open(os.path.join(repo_root, "topic_" + topic + ".yml"), "rt", encoding="utf-8") as fh:
                    tmpl = yaml.load(fh)[0]
                    front = """\
---
authors: {}
---
""".format(tmpl.authors)

                    introduction = html2text(tmpl.introduction)

                    # Find variables associated to this topic
                    # Group vlist by tribes and write list with links.
                    # TODO: Can we have multiple tribes with the same topic?
                    vlist = [var for var in vd.values() if topic in var.topic_tribes]
                    related_variables = "No variable associated to this topic."
                    if vlist:
                        lines = []
                        items = sorted([(v.topic_tribes[topic][0], v) for v in vlist], key=lambda t: t[0])
                        #print([item[0] for item in items])
                        for tribe, group in groupby(items, key=lambda t: t[0]):
                            lines.append("*%s:*\n" % tribe)
                            lines.extend("- %s  %s" % (v.mdlink, v.mnemonics) for (_, v) in group)
                            lines.append(" ")
                        related_variables = "\n".join(lines)

                    # Find tests associated to this `topic`
                    # Group tests by `suite_name` and write list with links.
                    items = [(rpath, test) for (rpath, test) in self.rpath2test.items() if topic in test.topics]
                    selected_input_files = "No input file associated to this topic."
                    if items:
                        items = sorted(items, key=lambda t: t[1].suite_name)
                        lines = []
                        for suite_name, group in groupby(items, key=lambda t: t[1].suite_name):
                            lines.append("*%s:*\n" % suite_name)
                            lines.extend("- [[%s]]" % rpath for (rpath, test) in group)
                            lines.append(" ")
                        selected_input_files = "\n".join(lines)

                    # Build front + markdown and write md file.
                    text = front + """
## ** Introduction **

{introduction}

## ** Related Input Variables **

{related_variables}

## ** Selected Input Files **

{selected_input_files}

""".format(**locals())

                with io.open(os.path.join(workdir, topic + ".md"), "wt", encoding="utf-8") as fh:
                    fh.write(text)

        # Build page with full list of tests grouped by `suite_name`.
        print("Generating Markdown file with tests ...")
        items = [(rpath, test) for (rpath, test) in self.rpath2test.items()]
        items = sorted(items, key=lambda t: t[1].suite_name)
        workdir = os.path.join(self.root, "developers")
        with io.open(os.path.join(workdir, "testsuite.md"), "wt", encoding="utf-8") as fh:
            for suite_name, group in groupby(items, key=lambda t: t[1].suite_name):
                fh.write('##  %s  \n\n' % suite_name)
                for rpath, test in group:
                    fh.write('### <a href="{url}">{rpath}</a>   \n\n'.format(url="/" + rpath, rpath=rpath))
                    #fh.write(test.listoftests())
                    fh.write(test.description)
                    fh.write("\n\n")
                    fh.write("Executable: %s   \n" % test.executable)
                    if test.keywords:
                        fh.write("Keywords(s): %s   \n" % ", ".join(k for k in test.keywords))
                    if test.topics:
                        fh.write("Topic(s): %s  \n" % ", ".join("[[topic:%s]]" % t for t in test.topics))
                    if test.authors and "Unknown" not in test.authors:
                        fh.write("Author(s): %s  \n" % ", ".join(a for a in test.authors))
                    fh.write("\n\n* * *\n\n")

        # All markdown files have been generated.
        # Now find all wikilinks, in particular the
        # bibliographic references needed to generate backlinks.
        self.analyze_pages()

        # Now generate page with bibliography
        print("Generating Markdown file with bibliographic entries ...")
        citation2pages = defaultdict(list)
        for page in self.md_pages:
            for citation in page.citations:
                citation2pages[citation].append(page)

        with io.open(os.path.join(self.root, "theory", "bibliography.md"), "wt", encoding="utf-8") as fh:
            lines = []
            for name in sorted(self.bib_data.entries.keys()):
                entry = self.bib_data.entries[name]
                lines.append("\n\n## **%s** \n\n" % name)
                try:
                    lines.append(entry.to_markdown())
                except Exception as exc:
                    raise ValueError("Exception while trying to convert bibtex entry `%s`\n%s\n" % (name, str(exc)))
                if citation2pages[name]:
                    lines.append("Referred to in: %s" % ", ".join('<a href="{url}"> {url} </a>'.format(url=page.url)
                        for page in citation2pages[name]))
                lines.append("* * *")
            fh.write("\n".join(lines))

        print("Markdown files generation completed in %.2f [s]" % (time.time() - start))

    def analyze_pages(self):
        print("Analyzing markdown pages ...")
        start = time.time()
        self.md_pages, self.html_pages = [], []
        for root, dirs, files in os.walk(self.root):
            if root in ("site", "tests"): continue
            for f in files:
                if f.startswith("_"): continue
                path = os.path.join(root, f)
                if f.endswith(".md"):
                    self.md_pages.append(MarkdownPage(path, self))
                elif f.endswith(".html") or f.endswith(".htm"):
                    self.html_pages.append(HtmlPage(path, self))

        print("Completed in %.2f [s]" % (time.time() - start))

    def get_citation_aelement(self, key, text=None, html_class=None):
        # Handle citation
        ref = self.bib_data.entries[key]
        url = "/theory/bibliography/#%s" % self.slugify(key)
        # Popover https://www.w3schools.com/bootstrap/bootstrap_popover.asp
        a = etree.Element('a')
        a.set("data-toggle", "popover")
        a.set("title", ref.fields["title"])
        a.set("data-placement", "auto bottom")
        a.set("data-trigger", "hover")
        #a.set("data-content", ref.to_html())
        a.set('href', url)
        a.text = key if text is None else text
        if html_class: a.set('class', html_class)
        return a

    def slugify(self, value):
        """ Slugify a string, to make it URL friendly. """
        from markdown.extensions.toc import slugify
        return slugify(value, separator="-")

    def preprocess_mdlines(self, lines):
        INC_SYNTAX = re.compile(r'^\{%\s*(.+?)\s*%\}')
        new_lines = []
        for line in lines:
            m = INC_SYNTAX.search(line)
            if not m:
                new_lines.append(line)
            else:
                args = m.group(1).split()
                action = args.pop(0)
                if self.verbose:
                    print("Triggering action:", action, "with args:", str(args))
                if action == "editor":
                    if len(args) > 1:
                        new_lines.extend(self.editor_tabs(args, title=None).splitlines())
                    else:
                        new_lines.extend(self.editor_panel(args[0], title=None).splitlines())
                elif action == "modal":
                    if len(args) > 1:
                        new_lines.extend(self.modal_with_tabs(args).splitlines())
                    else:
                        new_lines.extend(self.modal_from_filename(args[0]).splitlines())

                elif action == "cite":
                    #new_lines.extend([str(website.get_citation_aelement(arg)) for arg in args])
                    new_lines.extend(["[[" + arg + "]]" for arg in args])

                else:
                    raise ValueError("Don't know how to handle action: `%s` in token: `%s`" % (action, m.group(1)))

        # Add `return to top arrow` after meta section.
        # Based on https://codepen.io/rdallaire/pen/apoyx
        if len(new_lines) > 50:
            i = 0
            if new_lines[0].startswith("---"):
                for i, l in enumerate(new_lines[1:]):
                    if l.startswith("---"):
                        i += 1
                        break
            new_lines.insert(i, """<!-- Return to Top -->
<a href="javascript:" id="return-to-top"><i class="glyphicon glyphicon-chevron-up"></i></a>""")

        return new_lines

    @staticmethod
    def _parse_wikilink(token):
        # namespace:name#section|text
        # where namespace, section and text are optional
        text = None
        if "|" in token:
            token, text = token.split("|")
            text = text.strip()

        section = None
        if "#" in token:
            token, section = token.split("#")
            section = section.strip()

        namespace = None
        if ":" in token:
            namespace, name = token.split(":")
            namespace, name = namespace.strip(), name.strip()
        else:
            name = token.strip()
            if not name: name = None

        return namespace, name, section, text

    def anchor_from_wikilink(self, token):
        #token = token.strip()
        #if not token:
        #    print("Warning: empty wikilink", token)
        #    return ""

        html_class = "wikilink"
        a = etree.Element("a")
        a.set("class", html_class)

        if any(token.startswith(prefix) for prefix in ("www.", "http://", "https://", "ftp://", "file://")):
            # Handle [[www.google.com|text]]
            url, text = token, token
            if "|" in token:
                url, text = token.split("|")
            a.set('href', url)
            a.text = text
            return a

        # [[namespace:name#section|text]]
        try:
            namespace, name, section, text = self._parse_wikilink(token)
        except ValueError:
            raise ValueError("Cannot parse wikilink token `%s`" % token)

        if namespace is not None and name is None:
            raise ValueError("Wrong wikilink token: `%s`. namespace is not None and name is None" % token)

        # Find url and text
        if namespace is None:
            if name is None:
                # Handle [[#internal_link|text]]
                assert section is not None
                url = ""
                if text is None: text = section
            else:
                if name.startswith("lesson_"):
                    # Handle [[lesson_gw1|text]]
                    url = "/tutorials/%s" % name.replace("lesson_" , " ", 1).strip()
                    if text is None: text = name

                elif name.startswith("topic_"):
                    # Handle [[topic_SelfEnergy|text]]
                    url = "/topics/%s" % name.replace("topic_" , " ", 1).strip()
                    if text is None: text = name

                elif name.startswith("help_"):
                    # Handle [[help_abinit|text]]
                    code = name.replace("help_" , " ", 1).strip()
                    url = "/user-guide/%s" % code
                    if text is None: text = "%s help file" % code

                elif "@" in name:
                    # Handle [[dipdip@anaddb|text]]
                    vname, code = name.split("@")
                    var = self.variables_code[code][vname]
                    url = "/input_variables/%s/#%s" % (var.varset, var.name)
                    if text is None: text = name

                elif name in self.variables_code["abinit"]:
                    # Handle link to Abinit variable e.g. [[ecut|text]]
                    var = self.variables_code["abinit"][name]
                    url = "/input_variables/%s/#%s" % (var.varset, var.name)
                    if text is None:
                        text = var.name if not var.is_internal else "%%s" % var.name

                elif name in self.bib_data.entries:
                    # Handle citation
                    return self.get_citation_aelement(name, text=text, html_class=html_class)

                elif name.startswith("tests/") or name.startswith("~abinit/tests/"):
                    # Handle [[tests/tutorial/Refs/tbase1_2.out|text]]
                    assert section is None
                    text = name if text is None else text
                    #if not text.startswith("~abinit/"): text = "~abinit/" + text
                    nm = name.replace("~abinit/", "")
                    url = "/" + nm
                    # Add popover with test description if input file.
                    if nm in self.rpath2test:
                        a.set("data-toggle", "popover")
                        a.set("title", self.rpath2test[nm].description)
                        a.set("data-placement", "auto bottom")
                        a.set("data-trigger", "hover")
                else:
                    msg = "Don't know how to handle wikilink token `%s`" % token
                    print("WARNING:", msg)
                    url, text = "FAKE_URL", "FAKE_URL"
                    #raise ValueError(msg)

        else:
            # namespace is defined
            if namespace in self.variables_code:
                # Handle [[anaddb:asr|text]] or [[abinit:ecut|text]]
                assert section is None
                var = self.variables_code[namespace][name]
                url = "/input_variables/%s/#%s" % (var.varset, var.name)
                if text is None:
                    text = var.name if not var.is_internal else "%%s" % var.name

            elif namespace == "lesson":
                # Handle [[lesson:wannier90|text]]
                url = "/tutorials/%s" % name
                if text is None: text = "%s %s" % (name, namespace)

            elif namespace == "help":
                # [[help:optic|text]
                # %%[[help_codename]]%% is echoed "codename help file" :
                url = "/user-guide/help_%s" % name
                if text is None: text = "%s help file" % name

            elif namespace == "topic":
                # Handle [[topic:BSE|text]]
                url = "/topics/%s" % name
                if text is None: text = "%s_%s" % (namespace, name)

            elif namespace == "bib":
                # Handle [[bib:Amadon2008]]
                return self.get_citation_aelement(name, text=text, html_class=html_class)

            elif namespace == "theorydoc":
                # Handle [[theorydoc:mbpt|text]]
                url = "/theory/%s" % name
                if text is None: text = name

            elif namespace == "varset":
                # Handle [[varset:BSE|text]]
                assert section is None
                url = "/input_variables/%s" % name
                if text is None: text = "%s varset" % name

            else:
                msg = "Don't know how to handle wikilink token `%s`" % token
                #raise ValueError(msg)
                print("WARNING:", msg)
                url, text = "FAKE_URL", "FAKE_URL"

        if section is not None: url = "%s/#%s" % (url, section)
        a.set('href', url)
        a.text = text
        return a

    def validate_html_build(self):
        print("Validating website build")
        # https://bitbucket.org/nmb10/py_w3c
        # import HTML validator and create validator instance
        from py_w3c.validators.html.validator import HTMLValidator
        vld = HTMLValidator()

        from tidylib import tidy_document
        sitedir = os.path.join(os.path.dirname(self.root), "site")
        from pprint import pprint

        for root, dirs, files in os.walk(sitedir):
            for f in files:
                if not (f.endswith(".html") or f.endswith(".htm")): continue
                path = os.path.join(root, f)
                print("Validating", path)
                # validate file (Accept both - filename or file pointer.)
                vld.validate_file(path)
                # look for warnings
                #print(vld.warnings)
                # look for errors
                for e in vld.errors:
                    if e["message"] == "The “center” element is obsolete. Use CSS instead.":
                        continue
                    pprint(e)  # list with dicts

                #with io.open(path, "rt", encoding="utf-8") as fh:
                #    document, errors = tidy_document(fh.read())
                #    #print(errors)

    def modal_from_filename(self, path, title=None):
        # https://v4-alpha.getbootstrap.com/components/modal/#examples
        title = path if title is None else title
        with io.open(os.path.join(self.root, path), "rt", encoding="utf-8") as fh:
            text = "<pre>" + escape(fh.read()) + "</pre>"

        s = """\
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#{modal_id}">
  View {path}
</button>

<!-- Modal -->
<div class="modal fade" id="{modal_id}" tabindex="-1" role="dialog" aria-labelledby="{modal_label_id}">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="{modal_label_id}">{title}</h4>
      </div>
      <div class="modal-body">
        {text}
      </div>
    </div>
  </div>
</div>""".format(modal_id=gen_id(), modal_label_id=gen_id(), **locals())

        return s


    def modal_with_tabs(self, paths, title=None):
        # Based on http://jsfiddle.net/n__o/19rhfnqm/
        title = title if title else ""
        apaths = [os.path.join(self.root, p) for p in paths]
        button_label = "View " + ", ".join(paths)

        text_list = []
        for p in apaths:
            with io.open(p, "rt", encoding="utf-8") as fh:
                text_list.append("<pre>" + escape(fh.read()) + "</pre>")
        tab_ids = gen_id(n=len(text_list))

        s = """\
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#{modal_id}">{button_label}</button>

<!-- Modal -->
<div class="modal fade" id="{modal_id}" tabindex="-1" role="dialog" aria-labelledby="{modal_label_id}" aria-hidden="true">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span>
                </button>
                 <h4 class="modal-title" id="{modal_label_id}">{title}</h4>
            </div>
            <div class="modal-body">
                <div role="tabpanel">
                    <!-- Nav tabs -->
                    <ul class="nav nav-tabs" role="tablist">""".format(
                            modal_id=gen_id(), modal_label_id=gen_id(), **locals())

        for i, (path, tid) in enumerate(zip(paths, tab_ids)):
            s += """\
                    <li role="presentation" class="{li_class}">
                    <a href="{href}" aria-controls="uploadTab" role="tab" data-toggle="tab">{path}</a>
                    </li> """.format(li_class="active" if i == 0 else " ", href="#%s" % tid, path=path)

        s +=  """</ul>
                 <!-- Tab panes -->
                 <div class="tab-content">"""

        for i, (text, tid) in enumerate(zip(text_list, tab_ids)):
            s += """<div role="tabpanel" class="tab-pane {active}" id="{tid}">{text}</div>""".format(
                    active="active" if i == 0 else " ", tid=tid, text=text)

        s += 6 * " </div> "

        return s

    def editor_panel(self, path, title=None):
        title = path if title is None else str(title)

        path = os.path.join(self.root, path)
        with io.open(os.path.join(path), "rt", encoding="utf-8") as fh:
            text = escape(fh.read())

        s = """\
<div class="panel panel-default">
    <div class="panel-heading">{title}</div>
    <div class="panel-body"><div class="editor" hidden id="{editor_id}">{text}</div></div>
</div>""".format(editor_id=gen_id(), **locals())

        return s

    def editor_tabs(self, paths, title=None):
        title = "EditorTabs" if title is None else str(title)
        apaths = [os.path.join(self.root, p) for p in paths]

        text_list = []
        for path in apaths:
            with io.open(path, "rt", encoding="utf-8") as fh:
                text_list.append(escape(fh.read()))
        tab_ids = gen_id(n=len(text_list))
        editor_ids = gen_id(n=len(text_list))

        # https://codepen.io/wizly/pen/BlKxo?editors=1000
        s = """\
<div><{title}</div>
<div id="exTab1">
<!-- Nav tabs -->
<ul class="nav nav-pills nav-justified">""".format(title=title)

        for i, (path, tid) in enumerate(zip(paths, tab_ids)):
            s += """\
                    <li class="{li_class}">
                    <a href="{href}" data-toggle="pill">{path}</a>
                    </li> """.format(li_class="active" if i == 0 else " ", href="#%s" % tid, path=path)
        s +=  """</ul>
                 <!-- Tab panes -->
                 <div class="tab-content clearfix">"""

        for i, (text, tid, editor_id) in enumerate(zip(text_list, tab_ids, editor_ids)):
            s += """<div class="tab-pane {active}" id="{tid}">
                <div id="{editor_id}" class="editor" hidden>{text}</div></div>""".format(
                    active="fade in active" if i == 0 else "fade", tid=tid, editor_id=editor_id, text=text)

        s +=  2 * "</div> "
        return s


class Page(object):

    def __init__(self, path, website):
        self.path = os.path.abspath(path)
        self.website = website
        self.html_links = []
        self.wiki_links = []
        self.citations = set()

    @property
    def relpath(self):
        return os.path.relpath(self.path, self.website.root)

    @property
    def url(self):
        return ("/" + self.relpath).replace(".md", "")

    def __str__(self):
        lines = ["Page: %s" % self.relpath]
        if self.wiki_links:
            lines.extend("wiki_links: %s" % wl for wl in self.wiki_links)

        return "\n".join(lines)


class MarkdownPage(Page):

    def __init__(self, path, website):
        super(MarkdownPage, self).__init__(path, website)
        self.meta = {}
        with io.open(self.path, "rt", encoding="utf-8") as fh:
           string = fh.read()

        for m in re.finditer(website.WIKILINK_RE, string):
            token = m.group(1).strip()
            if token in self.website.bib_data.entries:
                self.wiki_links.append(token)
                self.citations.add(token)

        #print(self)


class HtmlPage(Page):
    def __init__(self, path, websiste):
        super(HtmlPage, self).__init__(path, website)


class AbinitStats(object):

    def __init__(self, path):
        self.path = os.path.abspath(path)

        """
        =====================================================================
        Version  Date       Size         Number        Number        Number
                 released   tar.gz       of F90 files  of F90 lines  of tests
                            (10e6Bytes)
        =====================================================================
        4.3      2004 Feb   14.5          726          252602        432
        """
        keys = ("versions", "dates", "targz_sizes", "num_f90files", "num_f90lines", "num_tests")
        self.data = OrderedDict([(k, []) for k in keys])

        with io.open(self.path, "rt", encoding="utf-8") as fh:
            indata = False
            for line in fh:
                indata = indata or line.startswith("4.3")
                if indata:
                    tokens = line.split()
                    values = [tokens[0], "-".join([tokens[1], tokens[2]])] + tokens[3:]
                    for k, v in zip(keys, values):
                        if k not in ("versions", "dates"): v = float(v)
                        self.data[k].append(v)

    def update(self):
        """
        Size of tar.gz      : ls -l *tar.gz    (on shiva)
        Number of F90 files : ls src/*/*.F90 | wc
        Number of F90 lines : cat src/*/*.F90 | wc
        Number of tests     : ls tests/*/Input/t*in | wc
        """
        root = os.path.join(os.path.dirnname(self.path), "..", "..")
        src_dir = os.path.join(root, "src")
        if not os.path.isdir(src_dir):
            raise RuntimeError("Cannot find Abinit src directory. Someone moved statistics.txt file!")
        from subprocess import check_output
        num_f90files = int(check_output(["ls -l %s/*/*.F90 | wc" % src_dir], shell=True))
        num_f90lines = int(check_output(["cat %s/*/*.F90 | wc" % src_dir], shell=True))
        num_tests = int(check_output(["ls %s/tests/*/Input/t*in | wc" % src_dir], shell=True))

    def json_dump(self, path):
        import json
        with open(path, "wt") as fh:
            json.dump(self.data, fh)
