'''
WikiLinks Extension for Python-Markdown
======================================

Converts [[WikiLinks]] to relative links.

See <https://pythonhosted.org/Markdown/extensions/wikilinks.html>
for documentation.

Original code Copyright [Waylan Limberg](http://achinghead.com/).

All changes Copyright The Python Markdown Project

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
'''
from __future__ import absolute_import, unicode_literals, print_function

from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

import re

from ..website import get_website
website = get_website()


def build_url(label, base, end):
    """ Build a url from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', label)
    #print(clean_label)

    variables = website.variables_code["abinit"]

    if clean_label in variables:
        var = variables[clean_label]
        return "/input_variables/%s/#%s" % (var.varset, var.name)

    if clean_label in website.bib_data.entries:
        return "/bibliography/#%s" % clean_label

    return '%s%s%s' % (base, clean_label, end)


class WikiLinkExtension(Extension):

    def __init__(self, *args, **kwargs):
        self.config = {
            'base_url': ['/', 'String to append to beginning or URL.'],
            'end_url': ['/', 'String to append to end of URL.'],
            'html_class': ['wikilink', 'CSS hook. Leave blank for none.'],
            'build_url': [build_url, 'Callable formats URL from label.'],
        }

        super(WikiLinkExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        self.md = md

        # append to end of inline patterns
        #WIKILINK_RE = r'\[\[([\w0-9_ -]+)\]\]'
        #WIKILINK_RE = r'\[\[([\w0-9_ -\./]+)\]\]'
        WIKILINK_RE = r'\[\[([^\[]+)\]\]'
        wikilinkPattern = WikiLinks(WIKILINK_RE, self.getConfigs())
        wikilinkPattern.md = md
        #md.inlinePatterns.add('wikilink', wikilinkPattern, "<not_strong")
        # This needed to treat [[ngfft]](1:3) before []() markdown syntax
        md.inlinePatterns.add('wikilink', wikilinkPattern, "<link")


class WikiLinks(Pattern):
    def __init__(self, pattern, config):
        super(WikiLinks, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m):
        if m.group(2).strip():
            base_url, end_url, html_class = self._getMeta()
            token = m.group(2).strip()
            #url = self.config['build_url'](token, base_url, end_url)
            #token = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', token)
            #print(token)
            a = etree.Element('a')
            if html_class: a.set('class', html_class)

            # [[namespace:name#section|text]]
            text = None
            if "|" in token:
                token, text = token.split("|")

            if any(token.startswith(prefix) for prefix in ("www.", "http://", "https://", "ftp://", "file://")):
                url = token

            elif ":" in token:
                namespace, value = token.split(":")
                #print("namespace:" ,namespace, "value:", value)

                if namespace in website.variables_code:
                    # Handle link to input variable e.g. [[anaddb:asr]] or [[abinit:ecut]]
                    var = website.variables_code[namespace][value]
                    url = "/input_variables/%s/#%s" % (var.varset, var.name)
                    if text is None:
                        text = var.name if not var.is_internal else "%%s" % var.name

                elif namespace == "lesson":
                    url = "/tutorials/%s" % value

                elif namespace == "help":
                    url = "/user-guide/help_%s" % value
                    #text = value

                elif namespace == "topic":
                    url = "/topics/%s" % value
                    text = value

                #elif namespace == "input"
                #    # Handle link to input e.g. [[input:tests/v1/Input/t01.in]]

                else:
                    msg = "Don't know how to handle namespace `%s` with value `%s`" % (namespace, value)
                    print("Warning", msg)
                    url = "FAKE_URL"
                    #raise ValueError(msg) # FIXME

            elif token.startswith("tests/") or token.startswith("~abinit/tests/"):
                # Handle [[tests/tutorial/Refs/tbase1_2.out]]
                #print("In tests/ with token:", token)
                text = token
                token = token.replace("~abinit/", "")
                url = "/" + token
                # Add popover with test description if input file.
                if token in website.rpath2test:
                    a.set("data-toggle", "popover")
                    a.set("title", website.rpath2test[token].description)
                    a.set("data-placement", "auto bottom")
                    a.set("data-trigger", "hover")

            elif token in website.variables_code["abinit"]:
                # Handle link to Abinit variable e.g. [[ecut]]
                var = website.variables_code["abinit"][token]
                url = "/input_variables/%s/#%s" % (var.varset, var.name)

            elif token in website.bib_data.entries:
                # Handle citation
                return website.get_citation_aelement(token, html_class=html_class)

            else:
                #raise ValueError("Don't know how to handle token: `%s`" % token)
                url = '%s%s%s' % (base_url, token, end_url)

            a.set('href', url)
            a.text = token if text is None else text

        else:
            print("Warning: empty wikilink", m.group(0))
            a = ''

        return a

    def _getMeta(self):
        """ Return meta data or config data. """
        base_url = self.config['base_url']
        end_url = self.config['end_url']
        html_class = self.config['html_class']
        if hasattr(self.md, 'Meta'):
            if 'wiki_base_url' in self.md.Meta:
                base_url = self.md.Meta['wiki_base_url'][0]
            if 'wiki_end_url' in self.md.Meta:
                end_url = self.md.Meta['wiki_end_url'][0]
            if 'wiki_html_class' in self.md.Meta:
                html_class = self.md.Meta['wiki_html_class'][0]
        return base_url, end_url, html_class


def makeExtension(*args, **kwargs):
    return WikiLinkExtension(*args, **kwargs)
