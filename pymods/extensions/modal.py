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


def modal_from_filename(path, title=None):
    # https://v4-alpha.getbootstrap.com/components/modal/#examples
    title = path if title is None else title
    #text = "<p>Modal body text goes here.</p>"
    with open(os.path.join("/Users/gmatteo/git_repos/gitlab_trunk_abinit", path)) as fh:
        text = "<pre>" + fh.read() + "</pre>"

    s = """\
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
  Open {path}
</button>

<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">{title}</h4>
      </div>
      <div class="modal-body">
        {text}
      </div>
    </div>
  </div>
</div>""".format(**locals())

    return s.splitlines()
