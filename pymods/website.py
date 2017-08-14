# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os

from pymods.variables import Variable
from collections import OrderedDict

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

        self.abinit_stats = AbinitStats(os.path.join(self.top, "statistics.txt"))
        self.abinit_stats.json_dump(os.path.join(self.top, "statistics.json"))

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
        #with open(self.filepath, "rt") as fh:
        #    text = fh.read()


class HtmlPage(Page):

    def __init__(self, filepath):
        super(HtmlPage, self).__init__(filepath)
        #with open(self.filepath, "rt") as fh:
        #    text = fh.read()



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
