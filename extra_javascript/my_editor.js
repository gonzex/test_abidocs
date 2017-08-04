/* That selector matches all spans that have an id attribute and it starts with foo (e.g. fooblah
*/

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
