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

import re

from abimkdocs.website import get_website
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
        wikilinkPattern = WikiLinks(website.WIKILINK_RE, self.getConfigs())
        wikilinkPattern.md = md
        #md.inlinePatterns.add('wikilink', wikilinkPattern, "<not_strong")
        # This needed to treat [[ngfft]](1:3) before []() markdown syntax
        md.inlinePatterns.add('wikilink', wikilinkPattern, "<link")


class WikiLinks(Pattern):
    def __init__(self, pattern, config):
        super(WikiLinks, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m):
        token = m.group(2).strip()
        if token:
            base_url, end_url, html_class = self._getMeta()
            #url = self.config['build_url'](token, base_url, end_url)
            rpath = "??"
            if hasattr(self.md, 'Meta') and "rpath" in self.md.Meta:
                rpath = self.md.Meta["rpath"][0]

            try:
                a = website.get_wikilink(token)
                if a.get("href") == "FAKE_URL":
                    print("Invalid wikilink `%s` in rpath `%s`" % (token, rpath))
                return a
            except Exception as exc:
                print("Exception while trying to handle wikilink `%s` in rpath `%s`" % (token, rpath))
                return ""

                raise
        else:
            print("Warning: empty wikilink in rpath `%s`", (m.group(0), rpath))
            return ''

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
