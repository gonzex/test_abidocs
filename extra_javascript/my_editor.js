//function editor_from_id_and_string(id, string)
//{
//    CodeMirror.fromTextArea(id, {
//        value: string,
//        readOnly: true,
//        // height: "350px",
//        // parserfile: "parsexml.js",
//        // stylesheet: "css/xmlcolors.css",
//        // path: "js/",
//        // continuousScanning: 500,
//        lineNumbers: true
//    });
//}
// See also http://jsfiddle.net/igos/qLAvN/
$(function() {
    // That selector matches all spans that have an id attribute and it starts with foo (e.g. fooblah
    $("div[id^=editor]").each(function() {
        var editor = ace.edit(this.id);
        //var editor = ace.edit("editor");
        //editor.setTheme("ace/theme/monokai");
        //editor.setTheme("ace/theme/chrome");
        editor.setTheme("ace/theme/github");
        //editor.getSession().setMode("ace/mode/javascript");
        //editor.setHighlightActiveLine(false);
        editor.setReadOnly(true);  // false to make it editable
    });
});
