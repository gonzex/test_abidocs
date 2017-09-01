#!/usr/bin/env python

import sys
import os
import yaml
import io
from html2text import html2text

# We don't install with setup.py hence we have to add the directory [...]/abinit/tests to $PYTHONPATH
pack_dir = os.path.dirname(__file__)
sys.path.insert(0, pack_dir)

from abimkdocs.variables import Components

NUMBERED_SECTIONS = True


class Yaml2Md(object):
    def __init__(self, abidoc_root, mkdocs_root=None):
        self.abidoc_root = os.path.abspath(abidoc_root)
        assert "topics" in os.listdir(self.abidoc_root)

        self.mkdocs_root = None
        if mkdocs_root is not None:
            self.mkdocs_root = os.path.abspath(mkdocs_root)
            assert "extra_javascript" in os.listdir(self.mkdocs_root)

        # $ find . -name origin_files
        # ./biblio/origin_files
        # ./input_variables/origin_files
        # ./theory/origin_files
        # ./topics/origin_files
        # ./tutorial/origin_files
        # ./users/origin_files

        dir_names = [
            # dir with origin files, yml file with components, prefix for yaml files in origin, directory of new website
            ["theory", "theorydocs.yml", "theorydoc_", "theory"],
            #"topics", "topics", # TODO
            ["tutorial", "lessons.yml", "lesson_", "tutorials"],
            ["users",  "helps.yml", "help_", "user-guide"],
        ]

        for d, comp_name, prefix, dest in dir_names:
            origin_dir = os.path.join(self.abidoc_root, d, "origin_files")
            comp_path = os.path.join(origin_dir, comp_name)
            with io.open(comp_path, "rt", encoding="utf-8") as f:
                components = yaml.load(f)

            for comp in components:
                if comp.name == "default": continue
                yaml_path = os.path.join(origin_dir, prefix + comp.name) + ".yml"
                md = lesson2md(yaml_path)
                if self.mkdocs_root is None: continue
                workdir = os.path.join(self.mkdocs_root, dest)
                mdpath = os.path.join(workdir, comp.name + ".md")
                print("Writing markdown file to", mdpath)
                with io.open(mdpath, "wt", encoding="utf-8") as f:
                    f.write(md)


def md_from_comp(comp):
    md = "---\nauthors: %s\n---\n\n" % ", ".join(comp.authors.split(","))
    md += "# %s  \n\n" % comp.keyword
    md += "## %s  \n\n" % comp.subtitle
    return md


def order_sections(d):
    # (key, secnum as string)
    items = [(k, k.replace("sec", ""), float(k.replace("sec", ""))) for k in d if k.startswith("sec")]
    if NUMBERED_SECTIONS:
        return [item[0:2] for item in sorted(items, key=lambda t: t[2])]
    else:
        return [(item[0], "") for item in sorted(items, key=lambda t: t[2])]


def text_from_d(data):
    md = html2text(data.pop("intro")) + "\n"
    appendix = data.pop("secAppendix", None)
    for sec, sec_name in order_sections(data):
        d = data.pop(sec)
        #print(sec)
        md += "## %s %s  \n" % (sec_name, html2text(d.pop("title")))
        if "body" in d:
            md += html2text(d.pop("body"))
        md += "\n\n"
        d.pop("tag")
        if d:
            for sub, sub_name in order_sections(d):
                sd = d.pop(sub)
                md += "### %s %s  \n" % (sub_name, html2text(sd.pop("title")))
                md += html2text(sd.pop("body"))
                md += "\n\n"
                sd.pop("tag")

        if d:
            raise ValueError("In %s. Remaing d keys: %s" % (d.keys()))

    if appendix:
        md += "## %s   \n" % html2text(appendix.pop("title"))
        md += html2text(appendix.pop("body"))
        appendix.pop("tag")
        if appendix:
            raise ValueError("Remaing d keys in appendix: %s" % appendix.keys())

    if data:
        raise ValueError("Remaing keys in data: %s" % data.keys())

    return md


def oldlesson2md(yaml_path, comp):

    with io.open(yaml_path, "rt", encoding="utf-8") as f:
        data = yaml.load(f)
    if set(data.keys()) != set(["intro", "body"]):
        print(data.keys())
        raise ValueError("Found other keys: %s" % str(data.keys()))

    md = md_from_comp(comp)
    md += html2text(data.pop("intro") + data.pop("body"))
    #print(md)

    if data:
        raise ValueError("In %s. Remaing keys: %s" % (yaml_path, data.keys()))

    return md

def lesson2md(yaml_path):

    yaml_path = os.path.abspath(yaml_path)
    with io.open(yaml_path, "rt", encoding="utf-8") as f:
        data = yaml.load(f)

    if "/doc/tutorial/" in yaml_path:
        comp_path = os.path.join(os.path.dirname(yaml_path), "lessons.yml")
        name = os.path.basename(yaml_path).replace("lesson_", "").replace(".yml", "")
    elif "/doc/users/" in yaml_path:
        comp_path = os.path.join(os.path.dirname(yaml_path), "helps.yml")
        name = os.path.basename(yaml_path).replace("help_", "").replace(".yml", "")
    elif "/doc/theory/" in yaml_path:
        comp_path = os.path.join(os.path.dirname(yaml_path), "theorydocs.yml")
        name = os.path.basename(yaml_path).replace("theorydoc_", "").replace(".yml", "")

    with io.open(comp_path, "rt", encoding="utf-8") as f:
        components = yaml.load(f)

    for comp in components:
        if comp.name == name:
            break
    else:
        raise ValueError("Cannot find %s in Components" % name)

    if "body" in data:
        return oldlesson2md(yaml_path, comp)

    md = md_from_comp(comp)
    md += text_from_d(data)

    if data:
        raise ValueError("In %s. Remaing keys: %s" % (yaml_path, data.keys()))

    #print(md)
    return md


def main():
    Yaml2Md(sys.argv[1], mkdocs_root=sys.argv[2])
    return
    for yaml_path in sys.argv[1:]:
        try:
            lesson2md(yaml_path)
        except:
            print("Exception in", yaml_path)
            raise
    return 0



if __name__ == "__main__":
    sys.exit(main())
