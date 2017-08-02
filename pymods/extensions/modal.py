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
        for line in lines:
            m = INC_SYNTAX.search(line)
            if not m:
                new_lines.append(line)
            else:
                path = m.group(1)
                print("path:", path)
                new_lines.extend(modal_from_filename(path))

        return new_lines


def makeExtension(*args,**kwargs):
    return MarkdownInclude(kwargs)


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
    #text = "<p>Modal body text goes here.</p>"
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
