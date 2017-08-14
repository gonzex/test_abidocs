#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os
import mkdocs.__main__

# We don't install with setup.py hence we have to add the directory [...]/abinit/tests to $PYTHONPATH
pack_dir = os.path.dirname(os.path.abspath(__file__))
print(pack_dir)
sys.path.insert(0, pack_dir)


def validate_html_build(top):
    # https://bitbucket.org/nmb10/py_w3c
    # import HTML validator
    import os
    from py_w3c.validators.html.validator import HTMLValidator

    # create validator instance
    vld = HTMLValidator()

    from tidylib import tidy_document
    #document, errors = tidy_document('''<p>f&otilde;o <img src="bar.jpg">''',
    #options={'numeric-entities':1})
    #print(document)
    #print(errors)

    for root, dirs, files in os.walk(top):
        for f in files:
            if not (f.endswith(".html") or f.endswith(".htm")): continue
            path = os.path.join(root, f)
            print("Validating", path)

            # validate file (Accept both - filename or file pointer.)
            #vld.validate_file(path)
            # look for warnings
            #print(vld.warnings)
            # look for errors
            #print(vld.errors)  # list with dicts

            with open(path, "rt") as fh:
                document, errors = tidy_document(fh.read())
                #print(document)
                print(errors)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "validate":
        return validate_html_build("./site")

    if len(sys.argv) > 1 and sys.argv[1] in ("build", "serve", "gh-deploy"):
        from pymods.website import build_website
        site = build_website("./doc")
        site.generate_markdown()
        print(site)
        #return 0

    return mkdocs.__main__.cli()


if __name__ == '__main__':
    sys.exit(main())