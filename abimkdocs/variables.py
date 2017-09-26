# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import os
import io

from html2text import html2text

try:
    import yaml
except ImportError:
    raise ImportError("pyyaml package is not installed. Install it with `pip install pyyaml`")

from itertools import groupby


def get_ax_fig_plt(ax=None):
    """
    Helper function used in plot functions supporting an optional Axes argument.
    If ax is None, we build the `matplotlib` figure and create the Axes else
    we return the current active figure.

    Returns:
        ax: :class:`Axes` object
        figure: matplotlib figure
        plt: matplotlib pyplot module.
    """
    import matplotlib.pyplot as plt
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
    else:
        fig = plt.gcf()

    return ax, fig, plt


def add_fig_kwargs(func):
    """
    Decorator that adds keyword arguments for functions returning matplotlib
    figures.

    The function should return either a matplotlib figure or None to signal
    some sort of error/unexpected event.
    See doc string below for the list of supported options.
    """
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        # pop the kwds used by the decorator.
        title = kwargs.pop("title", None)
        size_kwargs = kwargs.pop("size_kwargs", None)
        show = kwargs.pop("show", True)
        savefig = kwargs.pop("savefig", None)
        tight_layout = kwargs.pop("tight_layout", False)

        # Call func and return immediately if None is returned.
        fig = func(*args, **kwargs)
        if fig is None:
            return fig

        # Operate on matplotlib figure.
        if title is not None:
            fig.suptitle(title)

        if size_kwargs is not None:
            fig.set_size_inches(size_kwargs.pop("w"), size_kwargs.pop("h"),
                                **size_kwargs)

        if savefig:
            fig.savefig(savefig)
        if tight_layout:
            fig.tight_layout()
        if show:
            import matplotlib.pyplot as plt
            plt.show()

        return fig

    # Add docstring to the decorated method.
    s = "\n" + """\
    keyword arguments controlling the display of the figure:

    ================  ====================================================
    kwargs            Meaning
    ================  ====================================================
    title             Title of the plot (Default: None).
    show              True to show the figure (default: True).
    savefig           'abc.png' or 'abc.eps' to save the figure to a file.
    size_kwargs       Dictionary with options passed to fig.set_size_inches
                      example: size_kwargs=dict(w=3, h=4)
    tight_layout      True if to call fig.tight_layout (default: False)
    ================  ===================================================="""

    if wrapper.__doc__ is not None:
        # Add s at the end of the docstring.
        wrapper.__doc__ += "\n" + s
    else:
        # Use s
        wrapper.__doc__ = s

    return wrapper


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
    varset = None
    range = None
    requires = None
    excludes = None
    # TODO This is not used and should be removed
    executables = None
    topics = None

    yaml_tag = u'!variable'

    def attrs(self):
        return ['vartype', 'characteristic', 'mnemonics', 'dimensions', 'defaultval', 'text',
                'abivarname', 'varset', 'executables', 'topics']

    def __init__(self, vartype=None, characteristic=None,
                 mnemonics=None, dimensions=None, default=None,
                 text=None, abivarname=None, executables=None, varset=None, range=None,
                 commentdefault=None, commentdims=None, topics=None):
        self.vartype = vartype
        self.characteristic = characteristic
        self.mnemonics = mnemonics
        self.dimensions = dimensions
        self.defaultval = default
        self.text = literal(text)
        self.abivarname = abivarname
        self.varset = varset
        self.executables = executables
        self.commentdefault = commentdefault
        self.commentdims = commentdims
        self.range = range
        self.topics = topics

    @property
    def name(self):
        return self.abivarname if "@" not in self.abivarname else self.abivarname.split("@")[0]

    @property
    def executable(self):
        if "@" in self.abivarname:
            code = self.abivarname.split("@")[1]
            assert code == self.varset
        else:
            code = "abinit"
        return code

    @property
    def topic_tribes(self):
        """topic --> list of tribes"""
        assert self.topics is not None
        od = OrderedDict()
        for tok in self.topics.split(","):
            topic, tribe = [s.strip() for s in tok.split("_")]
            if topic not in od: od[topic] = []
            od[topic].append(tribe)
        return od

    @property
    def is_internal(self):
        return self.characteristics is not None and '[[INTERNAL_ONLY]]' in self.characteristics

    @property
    def mdlink(self):
        return "[[%s:%s]]" % (self.executable, self.name)

    @classmethod
    def from_array(cls, array):
        return Variable(vartype=array["vartype"], characteristic=array["characteristic"],
                        mnemonics=array["mnemonics"], dimensions=array["dimensions"],
                        default=array["default"], text=array["text"], abivarname=array["abivarname"],
                        executables=array["executables"],
                        varset=array["varset"], range=array["range"], commentdefault=array["commentdefault"],
                        commentdims=array["commentdims"], topics=array["topics"])

    def __str__(self):
        return "Variable " + str(self.abivarname) + " (default = " + str(self.defaultval) + ")"

    # MG
   # TODO: assume abivarname is unique
    def __hash__(self):
        return hash(self.abivarname)

    def __eq__(self, other):
        if other is None: return False
        return self.abivarname == other.abivarname

    def __ne__(self, other):
        return not (self == other)

    def get_parents(self):
        import re
        parents = []
        WIKILINK_RE = r'\[\[([\w0-9_ -]+)\]\]'
        # TODO
        #    parent = self[parent]
        # KeyError: "'nzchempot'
        #WIKILINK_RE = r'\[\[([^\[]+)\]\]'
        if isinstance(self.dimensions, (list, tuple)):
            for dim in self.dimensions:
                dim = str(dim)
                m = re.match(WIKILINK_RE, dim)
                if m:
                    parents.append(m.group(1))

        if self.requires is not None:
            parents.extend([m.group(1) for m in re.finditer(WIKILINK_RE, self.requires) if m])

        return set(parents)

    def internal_link(self, website, page_rpath, label=None):
        """String with the website internal URL."""
        label = self.name if label is None else str(label)
        #url = "/variables/%s#%s" % (self.varset, self.name)
        #return '<a href="%s">%s</a>' % (url, label)
        token = "%s:%s" % (self.executable, self.name)
        a = website.get_wikilink(token, page_rpath)
        return '<a href="%s" class="%s">%s</a>' % (a.get("href"), a.get("class"), a.text)

    def to_markdown(self, with_hr=True):
        lines = []; app = lines.append

        app("## **%s** \n\n" % self.name)
        app("*Mnemonics:* %s  " % str(self.mnemonics))
        if self.characteristics:
            app("*Characteristics:* %s  " % ", ".join(self.characteristics))
        if self.topic_tribes:
            app("*Mentioned in topic(s):* %s  " % ", ".join("[[topic:%s]]" % k for k in self.topic_tribes))
        app("*Variable type:* %s  " % str(self.vartype))
        if self.dimensions:
           app("*Dimensions:* %s  " % format_dimensions(self.dimensions))
        if self.commentdims:
            app("*commentdims:* %s  " % self.commentdims)
        app("*Default value:* %s  " % self.defaultval)
        if self.commentdefault:
            app("*Comment:* %s  " % self.commentdefault)
        if self.requires:
            app("*Only relevant if:* %s  " % str(self.requires))
        if self.excludes:
            app("*The use of this variable forbids the use of:* %s  " % self.excludes)

        # Add links to tests.
        if hasattr(self, "tests") and not self.is_internal:
            # Constitutes an usage report e.g.
            # Rarely used, in abinit tests [8/888], in tuto abinit tests [2/136].
            assert hasattr(self, "tests_info")
            tests_info = self.tests_info
            ratio_all = len(self.tests) / tests_info["num_all_tests"]
            frequency = "Rarely used"
            if ratio_all > 0.5:
                frequency = "Very frequently used"
            elif ratio_all > 0.01:
                frequency = "Moderately used"

            info = "%s, [%d/%d] in all %s tests, [%d/%d] in %s tutorials" % (
                frequency, len(self.tests), tests_info["num_all_tests"], self.executable,
                tests_info["num_tests_in_tutorial"], tests_info["num_all_tutorial_tests"], self.executable)

            # Use https://facelessuser.github.io/pymdown-extensions/extensions/details/
            # TODO?
            #if len(self.tests) <= 10:
            app('\n??? note "Test list (click to open). %s"' % info)
            tlist = sorted(self.tests, key=lambda t: t.suite_name)
            for suite_name, tests_in_suite in groupby(tlist, key=lambda t: t.suite_name):
                ipaths = [os.path.join(*splitall(t.inp_fname)[-4:]) for t in tests_in_suite]
                s = "- " + suite_name + ":  " + ", ".join("[[%s|%s]]" % (p, os.path.basename(p)) for p in ipaths)
                #s = "- " + suite_name + ":  " + ", ".join("[[%s]]" % p for p in ipaths)
                app("    " + s)
            app("\n\n")

        # Add text with description.
        if self.text is not None:
            md_text = html2text(self.text)
            app(2 * "\n")
            app(md_text)
        else:
            print("WARNING: Variable:", self.name, "with None text")

        if with_hr:
            app("* * *" + 2*"\n")
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
        # Add whitespace after `[` or before `]` to avoid [[[ and ]]] pattersn
        # that enter into conflict with wikiling syntax [[...]]
        if self.start is not None and self.stop is not None:
            return "[ " + str(self.start) + " ... " + str(self.stop) + " ]"
        if self.start is not None:
            return "[ " + str(self.start) + "; ->"
        if self.stop is not None:
            return "<-;" + str(self.stop) + " ]"
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
        yaml_path = os.path.join(os.path.dirname(__file__), "..", "doc", "variables", "abinit_vars.yml")
        _VARS = VarDatabase.from_file(yaml_path)
    return _VARS


class VarDatabase(OrderedDict):

    @classmethod
    def from_file(cls, yaml_path):
        with io.open(yaml_path, 'rt', encoding="utf-8") as f:
            vlist = yaml.load(f)

        new = cls()
        # Read list of strings with possible character of variables.
        with io.open(os.path.join(os.path.dirname(yaml_path), "characteristics.yml"), "rt", encoding="utf-8") as f:
            new.characteristics = yaml.load(f)

        # Read list of `external_params` i.e. external parameters that are not input variables,
        # but that are used in the documentation of other variables
        # then convert to dict {name --> description}
        with io.open(os.path.join(os.path.dirname(yaml_path), "list_externalvars.yml"), "rt", encoding="utf-8") as f:
            d = {k: v for k, v in yaml.load(f)}
            new.external_params = OrderedDict([(k, d[k]) for k in sorted(d.keys())])

        for exname in sorted(set(v.executable for v in vlist)):
            items = [(v.name, v) for v in vlist if v.executable == exname]
            vd = InputVariables(sorted(items, key=lambda t: t[0]))
            vd.executable = exname
            vd.all_varset = sorted(set(v.varset for v in vd.values()))
            new[exname] =  vd

        return new

    def iter_allvars(self):
        for vd in self.values():
            for var in vd.values():
                yield var


class InputVariables(OrderedDict):

    def groupby_first_letter(self):
        keys = sorted(self.keys(), key=lambda n: n[0].lower())
        od = OrderedDict()
        for char, group in groupby(keys, key=lambda n: n[0].lower()):
            od[char] = [self[name] for name in group]
        return od

    def get_vartabs_html(self, website, page_rpath):
        ch2vars = self.groupby_first_letter()
        ch2vars["All"] = self.values()
        # http://getbootstrap.com/javascript/#tabs
        html = """\
<div>
<!-- Nav tabs -->
<ul class="nav nav-pills" role="tablist">\n"""

        idname = self.executable + "-tabs"
        for i, char in enumerate(ch2vars):
            id_char = "#%s-%s" % (idname, char)
            if i == 0:
                html += """\n
<li role="presentation" class="active"><a href="%s" role="tab" data-toggle="tab">%s</a></li>\n""" % (id_char, char)
            else:
                html += """\
<li role="presentation"><a href="%s" role="tab" data-toggle="tab">%s</a></li>\n""" % (id_char, char)
        html += """\
</ul>
<!-- Tab panes -->
<div class="tab-content">
        """

        for i, (char, vlist) in enumerate(ch2vars.items()):
            id_char = "%s-%s" % (idname, char)
            p = " ".join(v.internal_link(website, page_rpath) for v in vlist)
            if i == 0:
                html += '<div role="tabpanel" class="tab-pane active" id="%s">\n%s\n</div>\n' % (id_char, p)
            else:
                html += '<div role="tabpanel" class="tab-pane" id="%s">\n%s\n</div>\n' % (id_char, p)

        return html + "</div></div>"

    @add_fig_kwargs
    def plot_networkx(self, mode="network", with_edge_labels=False, ax=None,
                      node_size="num_cores", node_label="name_class", layout_type="spring", **kwargs):
        """
        Use networkx to draw the flow with the connections among the nodes and
        the status of the tasks.

        Args:
            mode: `networkx` to show connections, `status` to group tasks by status.
            with_edge_labels: True to draw edge labels.
            ax: matplotlib :class:`Axes` or None if a new figure should be created.
            node_size: By default, the size of the node is proportional to the number of cores used.
            node_label: By default, the task class is used to label node.
            layout_type: Get positions for all nodes using `layout_type`. e.g. pos = nx.spring_layout(g)

        .. warning::

            Requires networkx package.
        """
        import networkx as nx
        import collections

        # Build the graph
        g, edge_labels = nx.Graph(), {}
        counter = collections.Counter()
        for i, (name, var) in enumerate(self.items()):
            #if i == 5: break
            if var.varset != "varbas": continue
            g.add_node(var, name=name)
            counter[var] += 1
            for parent in var.get_parents():
                print(parent, "is parent of ", name)
                parent = self[parent]
                g.add_edge(parent, var)
                counter[parent] += 1
                counter[var] += 1

                # TODO: Add getters! What about locked nodes!
                #i = [dep.node for dep in child.deps].index(task)
                #edge_labels[(task, child)] = " ".join(child.deps[i].exts)

        # Get positions for all nodes using layout_type.
        # e.g. pos = nx.spring_layout(g)
        #pos = getattr(nx, layout_type + "_layout")(g) #, scale=100000, iterations=30)
        #pos = nx.spring_layout(g, k=2)

        # nlist (list of lists) – List of node lists for each shell.
        nlist = []
        vals = set(counter.values())
        for c in vals:
            nlist.append([var for var in g if counter[var] == c])
        print(nlist)

        pos = nx.shell_layout(g, nlist=nlist, dim=2, scale=1, center=None)

        # Select function used to compute the size of the node
        #make_node_size = dict(num_cores=lambda task: 300 * task.manager.num_cores)[node_size]
        # Select function used to build the label
        #make_node_label = dict(name_class=lambda task: task.pos_str + "\n" + task.__class__.__name__,)[node_label]

        #labels = {var: make_node_label(var) for var in g.nodes()}
        labels = {var: var.name for var in g.nodes()}
        ax, fig, plt = get_ax_fig_plt(ax=ax)

        # Select plot type.
        if mode == "network":
            nx.draw_networkx(g, pos,
                             labels=labels,
                             #node_color=[task.color_rgb for task in g.nodes()],
                             #node_size=[make_node_size(task) for task in g.nodes()],
                             width=1, style="dotted", with_labels=True, ax=ax)
            # Draw edge labels
            #if with_edge_labels:
            #    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, ax=ax)

        elif mode == "status":
            # Group tasks by status.
            for status in self.ALL_STATUS:
                tasks = list(self.iflat_tasks(status=status))

                # Draw nodes (color is given by status)
                node_color = status.color_opts["color"]
                if node_color is None: node_color = "black"
                #print("num nodes %s with node_color %s" % (len(tasks), node_color))

                nx.draw_networkx_nodes(g, pos,
                                       nodelist=tasks,
                                       node_color=node_color,
                                       node_size=[make_node_size(task) for task in tasks],
                                       alpha=0.5, ax=ax
                                       #label=str(status),
                                       )

            # Draw edges.
            nx.draw_networkx_edges(g, pos, width=2.0, alpha=0.5, arrows=True, ax=ax) # edge_color='r')

            # Draw labels
            nx.draw_networkx_labels(g, pos, labels, font_size=12, ax=ax)

            # Draw edge labels
            if with_edge_labels:
                nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, ax=ax)
                #label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal',
                # alpha=1.0, bbox=None, ax=None, rotate=True, **kwds)

        else:
            raise ValueError("Unknown value for mode: %s" % str(mode))

        ax.axis("off")
        return fig

    def get_plotly_networkx(self, varset="all", layout_type="spring", include_plotlyjs=False):
        # https://plot.ly/python/network-graphs/
        # Build the graph
        import networkx as nx
        g, edge_labels = nx.Graph(), {}
        for i, (name, var) in enumerate(self.items()):
            if varset != "all" and var.varset != varset: continue
            parents = var.get_parents()
            if not parents: continue
            g.add_node(var, name=name)
            for parent in parents:
                #print(parent, "is parent of ", name)
                parent = self[parent]
                g.add_edge(parent, var)

                # TODO: Add getters! What about locked nodes!
                #i = [dep.node for dep in child.deps].index(task)
                #edge_labels[(task, child)] = " ".join(child.deps[i].exts)

        # Get positions for all nodes using layout_type.
        # e.g. pos = nx.spring_layout(g, iterations=80)
        pos = getattr(nx, layout_type + "_layout")(g) #, scale=100000, iterations=30)
        #pos = nx.spring_layout(g, k=2, iterations=100)

        # Add edges as disconnected lines in a single trace and nodes as a scatter trace
        import plotly
        import plotly.graph_objs as go
        from textwrap import fill
        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=go.Line(width=2.0, color='#888', dash="dot"),
            hoverinfo='none',
            mode='lines',
        )

        for edge in g.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace['x'] += [x0, x1, None]
            edge_trace['y'] += [y0, y1, None]

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[v.name for v in g],
            textposition='bottom',
            mode='markers+text',
            hoverinfo='text',
            #hovertext=[fill(html2text(v.text), width=90) for v in g.nodes()],
            hovertext=[v.mnemonics for v in g.nodes()],
            marker=go.Marker(
                showscale=True,
                # colorscale options
                # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
                # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
                colorscale='YIGnBu',
                reversescale=True,
                color=[],
                size=20,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=2)))

        for node in g.nodes():
            x, y = pos[node]
            node_trace['x'].append(x)
            node_trace['y'].append(y)

        # Color node points by the number of connections.
        for node, adjacencies in enumerate(g.adjacency_list()):
            node_trace['marker']['color'].append(len(adjacencies))
            node_info = '# of connections: '+str(len(adjacencies))
            #node_trace['text'].append(node_info)

        fig = go.Figure(data=go.Data([edge_trace, node_trace]),
                     layout=go.Layout(
                        title='<br>Network graph for varset %s' % varset,
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        annotations=[ dict(
                            text="Network for varset %s" % varset,
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002 ) ],
                        xaxis=go.XAxis(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=go.YAxis(showgrid=False, zeroline=False, showticklabels=False)))

        #py.iplot(fig, filename='networkx')
        #plotly.offline.plot(fig)
        s = plotly.offline.plot(fig, include_plotlyjs=include_plotlyjs, output_type='div')
        #print(s)
        return s

    def get_plotly_networkx_3d(self, varset="all", include_plotlyjs=False):
        import networkx as nx
        g, edge_labels = nx.Graph(), {}
        for i, (name, var) in enumerate(self.items()):
            #if i == 5: break
            if varset != "all" and var.varset != varset: continue
            g.add_node(var, name=name)
            for parent in var.get_parents():
                #print(parent, "is parent of ", name)
                parent = self[parent]
                g.add_edge(parent, var)

                # TODO: Add getters! What about locked nodes!
                #i = [dep.node for dep in child.deps].index(task)
                #edge_labels[(task, child)] = " ".join(child.deps[i].exts)

        # Get positions for all nodes using layout_type.
        # e.g. pos = nx.spring_layout(g)
        #pos = getattr(nx, layout_type + "_layout")(g) #, scale=100000, iterations=30)
        pos = nx.spring_layout(g, dim=3)

        import plotly.graph_objs as go
        trace1 = go.Scatter3d(x=[],
                              y=[],
                              z=[],
                              mode='lines',
                              line=go.Line(width=2.0, color='#888'), #, dash="dot"),
                              hoverinfo='none',
                       )

        for edge in g.edges():
            x0, y0, z0 = pos[edge[0]]
            x1, y1, z1 = pos[edge[1]]
            trace1['x'] += [x0, x1, None]
            trace1['y'] += [y0, y1, None]
            trace1['z'] += [z0, z1, None]

        trace2 = go.Scatter3d(
                       x=[],
                       y=[],
                       z=[],
                       name='variable',
                       marker=go.Marker(symbol='dot',
                                     size=10,
                                     #color=group,
                                     colorscale='Viridis',
                                     line=go.Line(width=2)
                                     ),
                       text=[v.name for v in g],
                       textposition='center',
                       mode='markers+text',
                       hoverinfo='text',
                       hovertext=[v.mnemonics for v in g.nodes()],
                       )

        for node in g.nodes():
            x, y, z = pos[node]
            trace2['x'].append(x)
            trace2['y'].append(y)
            trace2['z'].append(z)

        axis=dict(showbackground=False,
                  showline=False,
                  zeroline=False,
                  showgrid=False,
                  showticklabels=False,
                  title=''
                  )

        layout = go.Layout(
            title="Abinit variables (3D visualization)",
            width=1000,
            height=1000,
            showlegend=False,
            scene=go.Scene(
                xaxis=go.XAxis(axis),
                yaxis=go.YAxis(axis),
                zaxis=go.ZAxis(axis),
            ),
            margin=go.Margin(t=100),
            hovermode='closest',
            annotations=go.Annotations([go.Annotation(
                showarrow=False,
                #text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1]</a>",
                text="Hello",
                xref='paper',
                yref='paper',
                x=0,
                y=0.1,
                xanchor='left',
                yanchor='bottom',
                font=go.Font(size=14),
                )]),
            )

        data = go.Data([trace1, trace2])
        fig = go.Figure(data=data, layout=layout)

        import plotly
        s = plotly.offline.plot(fig, include_plotlyjs=include_plotlyjs, output_type='div')
        return s


def splitall(path):
    import os, sys
    allparts = []
    while True:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts