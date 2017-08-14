from __future__ import absolute_import, unicode_literals, print_function
import re
import os.path
from codecs import open
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

INC_SYNTAX = re.compile(r'\{!\s*(.+?)\s*!\}')


class MarkdownInclude(Extension):
    def __init__(self, configs={}):
        self.config = {
            'base_path': ['.', 'Default location from which to evaluate ' \
                'relative paths for the include statement.'],
            'encoding': ['utf-8', 'Encoding of the files used by the include statement.']
        }
        for key, value in configs.items():
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add(
            'include', IncludePreprocessor(md,self.getConfigs()),'_begin')


class IncludePreprocessor(Preprocessor):
    '''
    This provides an "include" function for Markdown, similar to that found in
    LaTeX (also the C pre-processor and Fortran). The syntax is {!filename!},
    which will be replaced by the contents of filename. Any such statements in
    filename will also be replaced. This replacement is done prior to any other
    Markdown processing. All file-names are evaluated relative to the location
    from which Markdown is being called.
    '''
    def __init__(self, md, config):
        super(IncludePreprocessor, self).__init__(md)
        self.base_path = config['base_path']
        self.encoding = config['encoding']

    def run(self, lines):
        new_lines = []

        # Add return to top arrow. https://codepen.io/rdallaire/pen/apoyx
        new_lines.append("""<!-- Return to Top -->
<a href="javascript:" id="return-to-top"><i class="glyphicon glyphicon-chevron-up"></i></a>""")

        for line in lines:
            m = INC_SYNTAX.search(line)
            if not m:
                new_lines.append(line)
            else:
                path = m.group(1)
                print("path:", path)
                if path == "editor":
                    new_lines.extend(editor_panel(path))
                elif path == "editors":
                    new_lines.extend(editor_tabs(path))
                else:
                    new_lines.extend(modal_from_filename(path))

        return new_lines


def makeExtension(*args,**kwargs):
    return MarkdownInclude(kwargs)


def escape(text):
    # Recent Python 3.2 have html module with html.escape() and html.unescape() functions.
    # html.escape() differs from cgi.escape() by its defaults to quote=True:
    #return text
    try:
        import html
        return html.escape(text)
    except ImportError:
        import cgi
        return cgi.escape(text)


def gen_id(n=1, pre="uuid-"):
    # The HTML4 spec says:
    # ID and NAME tokens must begin with a letter ([A-Za-z]) and may be followed by any number of letters,
    # digits ([0-9]), hyphens ("-"), underscores ("_"), colons (":"), and periods (".").
    import uuid
    if n == 1:
        return pre + str(uuid.uuid4())
    elif n > 1:
        return [pre + str(uuid.uuid4()) for i in range(n)]
    else:
        raise ValueError("n must be > 0 but got %s" % str(n))


def modal_from_filename(path, title=None):
    # https://v4-alpha.getbootstrap.com/components/modal/#examples
    title = path if title is None else title
    with open(os.path.join("/Users/gmatteo/git_repos/gitlab_trunk_abinit", path)) as fh:
        text = "<pre>" + fh.read() + "</pre>"

    s = """\
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#{modal_id}">
  Open {path}
</button>

<!-- Modal -->
<div class="modal fade" id="{modal_id}" tabindex="-1" role="dialog" aria-labelledby="{modal_label_id}">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="{modal_label_id}">{title}</h4>
      </div>
      <div class="modal-body">
        {text}
      </div>
    </div>
  </div>
</div>""".format(**locals(), modal_id=gen_id(), modal_label_id=gen_id())

    s += " ".join(modal_with_tabs([]))

    return s.splitlines()


def modal_with_tabs(paths, title=None):
    # Based on http://jsfiddle.net/n__o/19rhfnqm/
    title = "hello modal"
    paths = ["hello_path", "bar_path"]
    text_list = ["hello", "bar"]
    tab_ids = gen_id(n=len(text_list))

    s = """\
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#{modal_id}">Open files</button>

<!-- Modal -->
<div class="modal fade" id="{modal_id}" tabindex="-1" role="dialog" aria-labelledby="{modal_label_id}" aria-hidden="true">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span>
                </button>
                 <h4 class="modal-title" id="{modal_label_id}">{title}</h4>
            </div>
            <div class="modal-body">
                <div role="tabpanel">
                    <!-- Nav tabs -->
                    <ul class="nav nav-tabs" role="tablist">""".format(title=title, modal_id=gen_id(), modal_label_id=gen_id())

    for i, (path, tid) in enumerate(zip(paths, tab_ids)):
        s += """\
                <li role="presentation" class="{li_class}">
                <a href="{href}" aria-controls="uploadTab" role="tab" data-toggle="tab">{path}</a>
                </li> """.format(li_class="active" if i == 0 else " ", href="#%s" % tid, path=path)

    s +=  """</ul>
             <!-- Tab panes -->
             <div class="tab-content">"""

    for i, (text, tid) in enumerate(zip(text_list, tab_ids)):
        s += """<div role="tabpanel" class="tab-pane {active}" id="{tid}">{text}</div>""".format(
                active="active" if i == 0 else " ", tid=tid, text=text)

    s += 6 * " </div> "

    return s.splitlines()


def editor_panel(path, title=None):
    title = "Editor" if title is None else str(title)

    path = "tests/v1/Refs/t01.out"
    with open(os.path.join("/Users/gmatteo/git_repos/gitlab_trunk_abinit", path)) as fh:
        text = escape(fh.read())

    s = """\
<div class="panel panel-default">
    <div class="panel-heading">{title}</div>
    <div class="panel-body"><div class="editor" hidden id="{editor_id}">{text}</div></div>
</div>""".format(**locals(), editor_id=gen_id())

    return s.splitlines()


def editor_tabs(path, title=None, footer=""):
    title = "EditorTabs" if title is None else str(title)
    paths = ["tests/v1/Refs/t01.out", "tests/v1/Refs/t02.out"]

    text_list = []
    for path in paths:
        with open(os.path.join("/Users/gmatteo/git_repos/gitlab_trunk_abinit", path)) as fh:
            text_list.append(escape(fh.read()))
    tab_ids = gen_id(n=len(text_list))
    editor_ids = gen_id(n=len(text_list))

    # https://codepen.io/wizly/pen/BlKxo?editors=1000
    s = """\
<div><{title}</div>
<div id="exTab1">
<!-- Nav tabs -->
<ul class="nav nav-pills nav-justified">""".format(title=title)

    for i, (path, tid) in enumerate(zip(paths, tab_ids)):
        s += """\
                <li class="{li_class}">
                <a href="{href}" data-toggle="pill">{path}</a>
                </li> """.format(li_class="active" if i == 0 else " ", href="#%s" % tid, path=path)
    s +=  """</ul>
             <!-- Tab panes -->
             <div class="tab-content clearfix">"""

    for i, (text, tid, editor_id) in enumerate(zip(text_list, tab_ids, editor_ids)):
        s += """<div class="tab-pane {active}" id="{tid}">
            <div id="{editor_id}" class="editor" hidden>{text}</div></div>""".format(
                active="fade in active" if i == 0 else "fade", tid=tid, editor_id=editor_id, text=text)

    s +=  2 * "</div> "
    return s.splitlines()
