/* That selector matches all spans that have an id attribute and it starts with foo (e.g. fooblah */
$(function() {
    $(".editor").each(function(index, element) {
        var editor = ace.edit(element.id);
        //editor.setTheme("ace/theme/monokai");
        //editor.setTheme("ace/theme/chrome");
        editor.setTheme("ace/theme/github");
        //editor.getSession().setMode("ace/mode/javascript");
        editor.setHighlightActiveLine(true);
        editor.setAutoScrollEditorIntoView(true);
        editor.setReadOnly(true);  // false to make it editable
    });
});

// https://github.com/mkdocs/mkdocs/wiki/MkDocs-Recipes#associate-github-page-with-current-mkdoc-page
$(function() {
    var git = 'https://github.com/abinit/abinit/edit/master/docs';
    var t1 = window.location.pathname;
    var url = null;
    if (t1 == '/') {
        url = git + '/index.md';
    } else {
        url = git + t1.substr(0, t1.length-1) + '.md';
    }   
    a_git = $('[href="https://github.com/abinit/abinit"]');
    a_git.attr('href', url).attr('target', '_blank');
})
