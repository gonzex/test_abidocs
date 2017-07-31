#!/usr/bin/env python

import os

try:
    import yaml
except ImportError:
    raise ImportError("pyyaml package is not installed. Install it with `pip install pyyaml`")

class literal(str): pass

def literal_unicode_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(literal, literal_unicode_representer)

def valuewithunit_representer(dumper, data):
    return dumper.represent_mapping('!valuewithunit', data.__dict__)

####################################################################################################

# Classes

####################################################################################################

class Variable(yaml.YAMLObject):
    vartype = ''  # String containing the type
    characteristic = None  # String containing the characteristics
    mnemonics = None  # String containing the mnemonics
    dimensions = None  # Array containing either int, formula or another variable
    defaultval = None  # Either constant number, formula or another variable
    text = None  # Description (str)
    abivarname = None  # Name of the variable (str)
    commentdefault = None
    commentdims = None
    section = None
    range = None
    requires = None
    excludes = None
    topics = None

    yaml_tag = u'!variable'

    def attrs(self):
        return ['vartype', 'characteristic', 'mnemonics', 'dimensions', 'defaultval', 'text',
                'abivarname', 'section', 'topics']

    def __init__(self, vartype=None, characteristic=None,
                 mnemonics=None, dimensions=None, default=None,
                 text=None, abivarname=None, section=None, range=None,
                 commentdefault=None, commentdims=None, topics=None):
        self.vartype = vartype
        self.characteristic = characteristic
        self.mnemonics = mnemonics
        self.dimensions = dimensions
        self.defaultval = default
        self.text = literal(text)
        self.abivarname = abivarname
        self.section = section
        self.commentdefault = commentdefault
        self.commentdims = commentdims
        self.range = range
        self.topics = topics

    @classmethod
    def from_array(cls, array):
        return Variable(vartype=array["vartype"], characteristic=array["characteristic"],
                        mnemonics=array["mnemonics"], dimensions=array["dimensions"],
                        default=array["default"], text=array["text"], abivarname=array["abivarname"],
                        section=array["section"], range=array["range"], commentdefault=array["commentdefault"],
                        commentdims=array["commentdims"], topics=array["topics"])

    def __str__(self):
        return "Variable " + str(self.abivarname) + " (default = " + str(self.defaultval) + ")"

    # MG
    def website_ilink(self, label=None):
        """String with the URL of the web page."""
        label = self.abivarname if label is None else str(label)
        url = "/input_variables/%s/#%s" % (self.varfile, self.abivarname)
        return '<a href="%s" target="_blank">%s</a>' % (url, label)

    def to_md(self):
        import html2text
        lines = []
        app = lines.append

        # Title
        app("## **%s** \n\n" % self.abivarname)
        # Mnemonics
        app(" Mnemonics: %s  " % str(self.mnemonics))
        # Characteristics
        #if var.characteristics is not None:
        #  chars = ""
        #  for chs in var.characteristics:
        #    chars += chs+", "
        #  chars = chars[:-2]
        #  cur_content += "<br><font id=\"characteristic\">Characteristic: "+make_links(chars,var.abivarname,allowed_link_seeds,backlinks,backlink)+"</font>\n"
        #else:
        #  cur_content += "<br><font id=\"characteristic\">Characteristic: </font>\n"
        # Topics
        #try:
        #  if var.topics is not None :
        #    cur_content += "<br><font id=\"characteristic\">Mentioned in \"How to\": "
        #    vartopics=var.topics
        #    topics_name_tribe = vartopics.split(',')
        #    for i, topic_name_tribe in enumerate(topics_name_tribe):
        #      name_tribe = topic_name_tribe.split('_')
        #      cur_content += '<a href="../../topics/generated_files/topic_'+name_tribe[0].strip()+'.html">'+name_tribe[0].strip()+'</a> '
        #    cur_content += "</font>\n"
        #except:
        #  if debug==1 :
        #    print(" No topic_tribe for abivarname "+var.abivarname)
        # Variable type, including dimensions
        app("Variable type: %s  " % str(self.vartype))
        if self.dimensions is not None:
           app("Dimensions: %s  " % format_dimensions(self.dimensions))
        if self.commentdims is not None and self.commentdims != "":
            app("commentdims %s  " % self.commentdims)
        #  cur_content += " (Comment: "+make_links(var.commentdims,var.abivarname,allowed_link_seeds,backlinks,backlink)+")"
        ## Default
        app("Default value: %s  " % self.defaultval)
        #cur_content += "<br><font id=\"default\">"+make_links(format_default(var.defaultval),var.abivarname,allowed_link_seeds,backlinks,backlink)
        if self.commentdefault is not None and self.commentdefault != "":
            app("Comment: %s  " % self.commentdefault)
        #  cur_content += " (Comment: "+make_links(var.commentdefault,var.abivarname,allowed_link_seeds,backlinks,backlink)+")"
        #cur_content += "</font>\n"
        # Requires
        if self.requires is not None and self.requires != "":
            app("Only relevant if %s  " % self.requires)
        #  cur_content += "<br><br><font id=\"requires\">\nOnly relevant if "+doku2html(make_links(var.requires,var.abivarname,allowed_link_seeds,backlinks,backlink))+"\n</font>\n"
        # Excludes
        if self.excludes is not None and self.excludes != "":
            app("The use of this variable forbids the use of %s  " % self.excludes)
        #  cur_content += "<br><br><font id=\"excludes\">\nThe use of this variable forbids the use of "+doku2html(make_links(var.excludes,var.abivarname,allowed_link_seeds,backlinks,backlink))+"\n</font>\n"
        # Text
        #app("<br><font id=\"text\">\n")
        #app(str(var.text))
        if self.text is not None:
            md_text = html2text.html2text(self.text)
            app(2 * "\n")
            app(str(md_text))
        else:
            print("Var:", self.abivarname, "with None text")
        #cur_content += "<p>\n"+doku2html(make_links(var.text,var.abivarname,allowed_link_seeds,backlinks,backlink))+"\n"
        # End the section for one variable
        #app("</font>\n")
        app(2*"\n")
        #app("<br><br>")
        #app("<br><br><a href=#top>Go to the top</a>")
        #app("<B> | </B><a href=\"allvariables.html#top\">Complete list of input variables</a><hr>\n"
        #
        #all_contents[varfile] = all_contents[varfile] + cur_content + "\n\n"

        return "\n".join(lines)

####################################################################################################

class Components(yaml.YAMLObject):
    name = None  # String containing section name
    keyword = '' # String containing the short description of the topics, to be echoed in the title of the section file.
    authors = '' # String containing the list of authors.
    howto  = ''  # For the 'topics' Should complete the sentence beginning with "How to"
    header = ''  # Header of the file, possibly the 'default' one
    title  = ''  # Title  of the file, possibly the 'default' one
    subtitle  = ''  # Subtitle  of the file, possibly the 'default' one
    purpose   = ''  # Purpose  of the file, possibly the 'default' one
    advice    = ''  # Advice  of the file, possibly the 'default' one
    copyright = ''  # Copyright of the file, possibly the 'default' one
    introduction = ''  # Introduction
    links     = ''  # Links of the file, possibly the 'default' one
    menu      = ''  # Menu of the file, possibly the 'default' one
    tofcontent_header      = ''  # Header of the table of content of the file, possibly the 'default' one
    tutorials    = '' # List of relevant tutorials
    examples     = '' # Relevant examples
    end       = ''  # End of the file, possibly the 'default' one

    yaml_tag = u'!components'

    def attrs(self):
        return ['name', 'keyword', 'authors', 'howto', 'header', 'title', 'subtitle', 'purpose', 'advice',
                'copyright', 'introduction', 'links', 'menu', 'tofcontent_header', 'tutorials', 'examples', 'end']

    #Note that the default values are actually not initialized here, but in the data file, in order to ease the maintenance.
    def __init__(self, name=None, keyword=None, authors=None, howto=None, header=None, title=None, subtitle=None, purpose=None, advice=None,
                 copyright=None, links=None, menu=None, tofcontent_header=None, tutorials=None, examples=None, end=None):
        self.name = name
        self.keyword = keyword
        self.authors = authors
        self.howto = howto
        self.header = header
        self.title  = title
        self.subtitle = subtitle
        self.purpose  = purpose
        self.advice   = advice
        self.copyright= copyright
        self.introduction= introduction
        self.links    = links
        self.menu     = menu
        self.tofcontent_header = tofcontent_header
        self.tutorials = tutorials
        self.examples = examples
        self.end      = end

####################################################################################################

class ValueWithUnit(yaml.YAMLObject):
    value = None
    units = None
    yaml_tag = u'!valuewithunit'

    def __init__(self, value=None, units=None):
        self.value = value
        self.units = units

    def __str__(self):
        return str(self.value) + " " + str(self.units)

    def __repr__(self):
        return str(self)

####################################################################################################

class Range(yaml.YAMLObject):
    start = None
    stop = None

    yaml_tag = u'!range'

    def __init__(self, start=None, stop=None):
        self.start = start
        self.stop = stop

    def isin(self, value):
        isin = True
        if self.start is not None:
            isin = isin and (self.start <= self.value)
        if stop is not None:
            isin = isin and self.stop > self.value
        return str(self)

    def __repr__(self):
        if self.start is not None and self.stop is not None:
            return "[" + str(self.start) + " .. " + str(self.stop) + "]"
        if self.start is not None:
            return "[" + str(self.start) + "; ->"
        if self.stop is not None:
            return "<-;" + str(self.stop) + "]"
        else:
            return None

####################################################################################################

class ValueWithConditions(yaml.YAMLObject):
    yaml_tag = u'!valuewithconditions'

    def __repr__(self):
        s = ''
        for key in self.__dict__.keys():
            if key != 'defaultval':
                s += str(self.__dict__[key]) + ' if ' + str(key) + ',\n'
        s += str(self.defaultval) + ' otherwise.\n'
        return s

    def __str__(self):
        return self.__repr__()

####################################################################################################

class MultipleValue(yaml.YAMLObject):
    number = None
    value = None

    yaml_tag = u'!multiplevalue'

    def __init__(self, number=None, value=None):
        self.number = number
        self.value = value

    def __repr__(self):
        if self.number is None:
            return "*" + str(self.value)
        else:
            return str(self.number) + "*" + str(self.value)


# My Code
from collections import OrderedDict

_VARS = None

def get_variables_code():
    global _VARS
    if _VARS is None:
        _VARS = {}
        root = "/Users/gmatteo/git_repos/abidocs"
        path = os.path.join(root, "doc", "input_variables", "abinit_vars.yml")
        _VARS["abinit"] = InputVariables.from_file(path, "abinit")

    return _VARS


class InputVariables(OrderedDict):

    @classmethod
    def from_file(cls, yaml_path, codename):
        with open(yaml_path, 'rt') as f:
            vlist = yaml.load(f)
            items = [(v.abivarname, v) for v in vlist]
            new = cls(sorted(items, key=lambda t: t[0]))
            new.varfiles = sorted(set(v.varfile for v in vlist))
            new.codename = codename
            return new

    def write_markdown_files(self, workdir):
        # Build list of variables
        with open(os.path.join(workdir, "varlist_" + self.codename + ".md"), "wt") as fh:
            fh.write(self.get_vartabs_html())

        # Build markdown
        for varfile in self.varfiles:
            var_list = [v for v in self.values() if v.varfile == varfile]
            #print(varfile, var_list)
            with open(os.path.join(workdir, varfile + ".md"), "wt") as fh:
                #head = "[TOC]\n"
                #fh.write(head)
                for var in var_list:
                    #print(var.abivarname)
                    fh.write(var.to_md())

    def groupby_first_letter(self):
        keys = sorted(list(self.keys()))
        from itertools import groupby
        od = OrderedDict()
        for char, names in groupby(keys, key=lambda n: n[0].lower()):
            #print(char, list(names))
            od[char] = [self[name] for name in names]
        return od

    def get_vartabs_html(self):
        ch2vars = self.groupby_first_letter()

        # https://jqueryui.com/tabs/
        #idname = self.codename + "-tabs"
        #html = '<div id="%s"> <ul>' % idname
        #for char in ch2vars:
        #    #html += "<li><a href="#tabs-1">Nunc tincidunt</a></li>"
        #    id_char = "#%s-%s" % (idname, char)
        #    html += '<li><a href="%s">%s</a></li>' % (id_char, char)
        #html += "</ul>"
        #for char, vlist in ch2vars.items():
        #    id_char = "%s-%s" % (idname, char)
        #    p = " ".join(v.abivarname for v in vlist)
        #    html += '<div id="%s"><p>%s</p></div>' % (id_char, p)
        #html += "</div>"

        # http://getbootstrap.com/javascript/#tabs
        html = """\
<div>
<!-- Nav tabs -->
<ul class="nav nav-pills" role="tablist">\n"""

        idname = self.codename + "-tabs"
        for i, char in enumerate(ch2vars):
            id_char = "#%s-%s" % (idname, char)
            if i == 0:
                html += '<li role="presentation" class="active"><a href="%s" aria-controls="home" role="tab"\
                         data-toggle="tab">%s</a></li>\n' % (id_char, char)
            else:
                html += '<li role="presentation"><a href="%s" aria-controls="home" role="tab"\
                         data-toggle="tab">%s</a></li>\n' % (id_char, char)
        html += """\
</ul>
<!-- Tab panes -->
<div class="tab-content">
        """

        for i, (char, vlist) in enumerate(ch2vars.items()):
            id_char = "%s-%s" % (idname, char)
            p = " ".join(v.website_ilink() for v in vlist)
            if i == 0:
                html += '<div role="tabpanel" class="tab-pane active" id="%s">\n%s\n</div>\n' % (id_char, p)
            else:
                html += '<div role="tabpanel" class="tab-pane" id="%s">\n%s\n</div>\n' % (id_char, p)

        return html + "</div> </div>"


def format_dimensions(dimensions):

  if dimensions is None:
    s = ''
  elif dimensions == "scalar":
    s = 'scalar'
  else:
    #s = str(dimensions)
    if isinstance(dimensions,list):
      s = '('
      for dim in dimensions:
        s += str(dim) + ','

      s = s[:-1]
      s += ')'
    else:
      s = str(dimensions)

  return s