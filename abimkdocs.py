#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os
import mkdocs.__main__

from collections import OrderedDict


from pymods.variables import Variable

# We don't install with setup.py hence we have to add the directory [...]/abinit/tests to $PYTHONPATH
pack_dir, x = os.path.split(os.path.abspath(__file__))
pack_dir, x = os.path.split(pack_dir)
sys.path.insert(0, pack_dir)
#pack_dir, x = os.path.split(pack_dir)
#sys.path.insert(0, pack_dir)

#class MarkdownPage(object):
#
#    def __init__(self, filepath):
#        self.filepath = os.path.abspath(filepath)
#        self.links = []
#        self.refs = []
#        self.meta = {}
#        self.parents = []
#        self.children = []
#
#        with open(self.filepath, "rt") as fh:
#	    text = fh.read()

def generate_markdown():
    print("Generating files")
    #import yaml
    workdir = "./doc/input_variables"
    #with open(os.path.join(workdir, 'abinit_vars.yml'), 'rt') as f:
    #    vlist = yaml.load(f)
    #    items = [(v.abivarname, v) for v in vlist]
    #    varfiles = set(v.varfile for v in vlist)
    #    variables = OrderedDict(sorted(items, key=lambda t: t[0]))

    ## Build markdown
    #for varfile in varfiles:
    #    var_list = [v for v in variables.values() if v.varfile == varfile]
    #    #print(varfile, var_list)
    #    with open(os.path.join(workdir, varfile + ".md"), "wt") as fh:
    #        #head = "[TOC]\n"
    #        #fh.write(head)
    #        for var in var_list:
    #            #print(var.abivarname)
    #            fh.write(var.to_md())

    from pymods.variables import get_code_variables
    variables = get_code_variables()["abinit"]
    variables.write_markdown_files(workdir)


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("build", "serve"):
        generate_markdown()
        return 0

    return mkdocs.__main__.cli()


if __name__ == '__main__':
    sys.exit(main())