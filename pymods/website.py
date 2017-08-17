# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os

from collections import OrderedDict
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

        from pymods.variables import get_variables_code
        self.variables_code = get_variables_code()

        from pybtex.database import parse_file
        self.bib_data = parse_file(os.path.join(self.top, "abiref.bib"), bib_format="bibtex")
        #for name, entry in self.bib_data.entries.items():
        #   print(name, entry)

        self.abinit_stats = AbinitStats(os.path.join(self.top, "statistics.txt"))
        self.abinit_stats.json_dump(os.path.join(self.top, "statistics.json"))

        #sys.path.insert(0, os.path.join(pack_dir, "doc"))
        #from doc import tests
        #print(tests)
        #abitests = tests.abitests.select_tests(suite_args=[])
        #for test in abitests:
        #    if hasattr(test, "description"):
        #        print(test.description)
        #    if hasattr(test, "topics"):
        #        print(test.topics)

    #def __str__(self):
    #    lines = []
    #    app = lines.append
    #    return "\n".join(lines)

    def generate_markdown_files(self):
        workdir = os.path.join(self.top, "input_variables")
        for code, vardb in self.variables_code.items():
            print("Generating markdown files with %s input variables ..." % code)
            vardb.write_markdown_files(workdir)

        print("Generating Markdown file with bibliographic entries ...")
        with open(os.path.join(self.top, "bibliography.md"), "wt") as fh:
            for name, entry in self.bib_data.entries.items():
                lines = []
                lines.append("\n\n## **%s** \n\n" % name)
                lines.append(str(entry))
                fh.write("\n".join(lines))

        #with open(os.path.join(self.top, "acknowledgments.md") as fh

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

    def validate_html_build(self):
        # https://bitbucket.org/nmb10/py_w3c
        # import HTML validator and create validator instance
        from py_w3c.validators.html.validator import HTMLValidator
        vld = HTMLValidator()

        from tidylib import tidy_document
        top = os.path.join(os.path.dirname(self.top), "site")
        from pprint import pprint

        for root, dirs, files in os.walk(top):
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
