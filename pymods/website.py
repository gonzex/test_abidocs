# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os

from collections import OrderedDict
from pymods.variables import Variable
from html2text import html2text

_WEBSITE = None


def splitall(path):
    import os, sys
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


def build_website(root, verbose=0):
    global _WEBSITE
    assert _WEBSITE is None
    _WEBSITE = Website(root, verbose=verbose)
    return _WEBSITE


def get_website():
    global _WEBSITE
    assert _WEBSITE is not None
    return _WEBSITE


from pybtex.database import Entry, parse_file
class MyEntry(Entry):
    """https://bitbucket.org/pybtex-devs/pybtex/"""

    def to_markdown(self):
        # Entry('article', fields=[('Title', 'Efficient Interpolation Technique for {B}ethe-{S}alpeter Calculation of Optical Spectra'), ('Year', '2016'), ('volume', '203C'), ('pages', '83-93'), ('Journal', 'Comput. Phys. Comm.'), ('Doi', '10.1016/j.cpc.2016.02.008'), ('Owner', 'yannick'), ('Timestamp', '2015.08.27')], persons=OrderedCaseInsensitiveDict([('Author', [Person('Gillet, Y.'), Person('Giantomassi, M.'), Person('Gonze, X.')])]))

        # Entry('book', fields=[('title', 'Electrons and phonons'), ('publisher', 'Oxford University Press'), ('year', '1960')], persons=OrderedCaseInsensitiveDict([('author', [Person('Ziman, J. M.')])]))

        fields = self.fields
        title = fields["title"]

        if self.type == "article":
            authors = ", ".join(str(p) for p in self.persons["author"])
            s = '{}  \n{}  \n'.format(authors, title)
            if "eprint" in fields:
                s += "{} **{}**, {} ({})".format(fields["journal"], fields.get("archivePrefix", ""), fields["eprint"], fields["year"])
            else:
                s += "{} **{}**, {} ({})".format(fields["journal"], fields["volume"], fields["pages"], fields["year"])

        elif self.type in ("book", "incollection"): # FIXME Better treatment for incollection
            authors = ", ".join(str(p) for p in self.persons["author"])
            #editors = ", ".join(str(e) for e in self.persons["editor"]])
            s = '{}  \n{}  \n'.format(authors, title)
            s += "{} ({})".format(fields["publisher"], fields["year"])
            if "isbn" in fields:
                s += "isbn: %s" % fields["isbn"]

        elif self.type in ("phdthesis", "mastersthesis"):
            authors = ", ".join(str(p) for p in self.persons["author"])
            s = '{}  \n{}  \n{} ({})'.format(authors, title, fields["school"], fields["year"])

        elif self.type == "misc":
            authors = ", ".join(str(p) for p in self.persons["author"])
            s = '{}  \n{} ({})'.format(authors, title, fields["year"])

        else:
            raise TypeError("Don't know how to convert type: `%s` into markdown string" % self.type)

        s += "  \n"
        if "url" in fields:
            s += 'URL: <a href={url} target="_black">{url}</a>'.format(url=fields["url"])
        elif "doi" in fields:
            doi = fields["doi"]
            doi_root = "https://doi.org/"
            if not doi.startswith(doi_root): doi = doi_root + doi
            s += 'DOI: <a href={doi} target="_blank">{doi}</a>'.format(doi=doi)

        return s

    def to_html(self):
        import markdown
        return markdown.markdown(self.to_markdown())


class Website(object):

    def __init__(self, root, verbose=0):
        self.root = os.path.abspath(root)
        self.verbose = verbose

        # Get database with input variables
        from pymods.variables import get_variables_code
        self.variables_code = get_variables_code()

        # Get bibtex references and cast to MyEntry instance.
        self.bib_data = parse_file(os.path.join(self.root, "abiref.bib"), bib_format="bibtex")
        for entry in self.bib_data.entries.values():
            entry.__class__ = MyEntry

        # Get code statistics
        self.abinit_stats = AbinitStats(os.path.join(self.root, "statistics.txt"))
        self.abinit_stats.json_dump(os.path.join(self.root, "statistics.json"))

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

        #self.inrpath2test = {os.path.relpath(t.inp_fname, self.root): t for t in tests}
        #self.inrpath2test = {t.inp_fname: t for t in tests}
        self.inrpath2test = {}
        for t in tests:
            toks = splitall(t.inp_fname)[-4:]
            key = os.path.join(*toks)
            self.inrpath2test[key] = t
        #print(self.inrpath2test.keys())

        def test_get_varnames(test, varnames):
            """This should become a method of BaseTest."""
            with open(test.inp_fname, "rt") as fh:
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

    #def __str__(self):
    #    lines = []
    #    app = lines.append
    #    return "\n".join(lines)

    def generate_markdown_files(self):
        workdir = os.path.join(self.root, "input_variables")
        for code, vd in self.variables_code.items():
            vd.write_markdown_files(workdir, with_varlist_page=code in ("abinit",))

        #Input variables, statistics :
        #occurrences in the input files provided with the package
        #This document lists the input variables for ABINIT and three post-processors of ABINIT,
        #in order of number of occurrence in the input files provided with the package.
        from itertools import groupby
        with open(os.path.join(workdir, "varset_stats.md"), "wt") as fh:
            for code, vd in self.variables_code.items():
                fh.write("\n\n# **%s** \n\n" % code)
                num_tests = len([test for test in self.inrpath2test.values() if test.executable == code])
                fh.write("%d tests\n\n" % num_tests)
                # TODO The number of tests is smaller than ecut! Count Tutorial
                # DSU sort
                items = sorted([(len(v.tests), v) for v in vd.values()], key=lambda t: t[0], reverse=True)
                for count, group in groupby(items, key=lambda t: t[0]):
                    vlist = [item[1] for item in sorted(group, key=lambda t: t[1].name)]
                    fh.write("%s: %s<br><br>" % (count, ", ".join(v.website_ilink() for v in vlist)))

        print("Generating Markdown file with bibliographic entries ...")
        with open(os.path.join(self.root, "bibliography.md"), "wt") as fh:
            for name, entry in self.bib_data.entries.items():
                lines = []
                lines.append("\n\n## **%s** \n\n" % name)
                lines.append(entry.to_markdown())
                lines.append("* * *")
                fh.write("\n".join(lines))

        print("Generating Markdown files with topics ...")
        for code, vd in self.variables_code.items():
            # Get list of topics for this code.
            topics = set()
            for var in vd.values():
                topics.update(var.topic_tribes.keys())

            # Read template and prepare markdown string
            repo_root = "/Users/gmatteo/git_repos/gitlab_trunk_abinit/doc/topics/origin_files/"
            import yaml
            for topic in sorted(topics):
                with open(os.path.join(repo_root, "topic_" + topic + ".yml"), "rt") as fh:
                    tmpl = yaml.load(fh)[0]
                    meta = """\
---
authors: {}
---
""".format(tmpl.authors)

                    html = """
{introduction}

""".format(**tmpl.__dict__)

                text = meta + html2text(html)
                workdir = os.path.join(self.root, "topics")
                with open(os.path.join(workdir, topic + ".md"), "wt") as fh:
                    fh.write(text)

    def analyze_pages(self):
        self.pages = []
        print("Analyzing markdown pages ...")
        for root, dirs, files in os.walk(self.root):
            if root in ("site", "tests"): continue
            for f in files:
                path = os.path.join(root, f)
                if f.endswith(".md"):
                    self.pages.append(MarkdownPage(path))
                elif f.endswith(".html") or f.endswith(".htm"):
                    self.pages.append(HtmlPage(path))

    def get_citation_aelement(self, key, html_class=None):
        from markdown.util import etree
        a = etree.Element('a')
        # Handle citation
        ref = self.bib_data.entries[key]
        url = "/bibliography/#%s" % key
        # Popover https://www.w3schools.com/bootstrap/bootstrap_popover.asp
        a.set("data-toggle", "popover")
        a.set("title", ref.fields["title"])
        a.set("data-placement", "auto bottom")
        a.set("data-trigger", "hover")
        #a.set("data-content", "Some content inside the popover")
        #a.set("data-content", str(ref))
        #a.set("data-content", ref.to_html())
        a.set('href', url)
        a.text = key
        if html_class: a.set('class', html_class)
        return a

    def validate_html_build(self):
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

                #with open(path, "rt") as fh:
                #    document, errors = tidy_document(fh.read())
                #    #print(errors)

class Page(object):

    def __init__(self, filepath):
        self.filepath = os.path.abspath(filepath)
        self.links = []
        self.refs = []
        #with open(self.filepath, "rt") as fh:
        #    self.lines = fh.readlines()

    #def __str__(self):
    #    lines = []
    #    app = lines.append
    #    return "\n".join(lines)

    #def _find_links(self):


class MarkdownPage(Page):
    def __init__(self, filepath):
        super(MarkdownPage, self).__init__(filepath)
        self.meta = {}

class HtmlPage(Page):
    def __init__(self, filepath):
        super(HtmlPage, self).__init__(filepath)


class AbinitStats(object):

    def __init__(self, filepath):
        self.filepath = os.path.abspath(filepath)

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

        with open(self.filepath, "rt") as fh:
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
        root = os.path.join(os.path.dirnname(self.filepath), "..", "..")
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
