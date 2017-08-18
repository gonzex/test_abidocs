#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os
import mkdocs.__main__

# We don't install with setup.py hence we have to add the directory [...]/abinit/tests to $PYTHONPATH
pack_dir = os.path.dirname(__file__)
#print(pack_dir)
sys.path.insert(0, pack_dir)

# This needed to import doc.tests
sys.path.insert(0, os.path.join(pack_dir, "doc"))


def main():
    from pymods.website import build_website
    website = build_website("./doc")

    if len(sys.argv) > 1 and sys.argv[1] == "validate":
        return website.validate_html_build()

    if len(sys.argv) > 1 and sys.argv[1] in ("build", "serve", "gh-deploy"):
        website.generate_markdown_files()
        print(website)

    if "--dry-run" in sys.argv: return 0
    return mkdocs.__main__.cli()


if __name__ == '__main__':
    sys.exit(main())