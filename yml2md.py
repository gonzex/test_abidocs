#!/usr/bin/env python

import sys, os, yaml

yaml_src = sys.argv[1]
#md_dst = sys.argv[2]

with open(yaml_src, "rt") as f:
    d = yaml.load(f)

if set(d.keys()) != set(["intro", "body"]):
    print(d.keys())
    raise ValueError("Found other keys: %s" % str(d.keys()))

html = d["intro"] + d["body"]

import html2text
s = html2text.html2text(html)
#print(str(s.encode("utf-8"))) #, errors="ignore")))
print(s)
