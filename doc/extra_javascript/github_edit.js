// https://github.com/mkdocs/mkdocs/wiki/MkDocs-Recipes#associate-github-page-with-current-mkdoc-page
$(document).ready(function(){
    var git = 'http://github.com/abinit/abinit/edit/master/docs'
    var t1 = window.location.pathname
    var url = null
    if (t1=='/'){
        url = git + '/index.md'
    }else{
        url = git+t1.substr(0, t1.length-1)+'.md'
    }   
    a_git = $('[href="https://github.com/abinit/abinit"]')
    a_git.attr('href', url).attr('target', '_blank')
})