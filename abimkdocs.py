#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os
import mkdocs.__main__

#from collections import OrderedDict
#from pymods.variables import Variable

# We don't install with setup.py hence we have to add the directory [...]/abinit/tests to $PYTHONPATH
pack_dir = os.path.dirname(os.path.abspath(__file__))
print(pack_dir)
sys.path.insert(0, pack_dir)

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("build", "serve", "gh-deploy"):
        from pymods.website import build_website
        site = build_website("./doc")
        site.generate_markdown()
        print(site)
        #return 0

    return mkdocs.__main__.cli()


if __name__ == '__main__':
    sys.exit(main())