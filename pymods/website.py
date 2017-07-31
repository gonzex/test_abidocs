# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os

#from collections import OrderedDict
from pymods.variables import Variable

_WEBSITE = None


def build_website(top, verbose=0):
    global _WEBSITE
    assert _WEBSITE is None
    _WEBSITE = Website(top, verbose=verbose)
    return _WEBSITE


def get_website():
    global _WEBSITE
    assert _WEBSITE is not None
    return _WEBSITE


class Website(object):

    def __init__(self, top, verbose=0):
        self.top = os.path.abspath(top)
        self.verbose = verbose
        self.pages = []
        from pymods.variables import get_variables_code
        self.variables_code = get_variables_code()

        from pybtex.database import parse_file
        self.bib_data = parse_file(os.path.join(self.top, "abiref.bib"), bib_format="bibtex")
        #for name, entry in self.bib_data.entries.items():
        #   print(name, entry)

    #def __str__(self):
    #    lines = []
    #    app = lines.append
    #    return "\n".join(lines)

    def generate_markdown(self):
        print("Generating markdown files ...")

        workdir = os.path.join(self.top, "input_variables")
        for code, vardb in self.variables_code.items():
            print("Writing variables for code:", code)
            vardb.write_markdown_files(workdir)

        print("Generating bibliography file ...")
        with open(os.path.join(self.top, "bibliography.md"), "wt") as fh:
            for name, entry in self.bib_data.entries.items():
                lines = []
                app = lines.append
                app("\n\n## **%s** \n\n" % name)
                app(str(entry))
                fh.write("\n".join(lines))

        #with open(os.path.join(self.top, "acknowledgments.md") as fh

    def analyze_pages(self):
        print("Analyzing pages ...")
        for root, dirs, files in os.walk(self.root):
            if root == "site": continue
            for f in files:
                path = os.path.join(root, f)
                if f.endswith(".md"):
                    self.pages.append(MarkdownPage(path))
                elif f.endswith(".html"):
                    self.pages.append(HtmlPage(path))


class Page(object):

    def __init__(self, filepath):
        self.filepath = os.path.abspath(filepath)
        self.links = []
        self.refs = []
        #self.parents = []
        #self.children = []

    #def __str__(self):
    #    lines = []
    #    app = lines.append
    #    return "\n".join(lines)


class MarkdownPage(Page):

    def __init__(self, filepath):
        super(MarkdownPage, self).__init__(filepath)
        self.md_meta = {}
        with open(self.filepath, "rt") as fh:
            text = fh.read()


class HtmlPage(Page):

    def __init__(self, filepath):
        super(HtmlPage, self).__init__(filepath)
        #with open(self.filepath, "rt") as fh:
        #    text = fh.read()
