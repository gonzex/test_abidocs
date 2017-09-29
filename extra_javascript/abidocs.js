
$(function() {

    // Enable all popovers and tooltips in the document:
    $('[data-toggle="popover"]').popover(); 
    $('[data-toggle="tooltip"]').tooltip();

    // This is for https://bootsnipp.com/snippets/featured/inbox-by-gmail
    $('.fab').hover(function () {
        $(this).toggleClass('active');
    });

    // When arrow is clicked scroll to top of body
    $('#return-to-top').click(function() {      
        $('body,html').animate({
            scrollTop: 0                       
        }, 500);
    });

    // That selector matches all spans that have an id attribute and it starts with foo (e.g. fooblah
    $(".editor").each(function(index, element) {
        element.removeAttribute("hidden")
        var editor = ace.edit(element.id);
        //editor.setTheme("ace/theme/monokai");
        editor.setTheme("ace/theme/github");
        //editor.getSession().setMode("ace/mode/javascript");
        editor.setHighlightActiveLine(true);
        editor.setAutoScrollEditorIntoView(true);
        editor.setReadOnly(true);  // false to make it editable
    });
});


// https://github.com/mkdocs/mkdocs/wiki/MkDocs-Recipes#associate-github-page-with-current-mkdoc-page
/*
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
*/


// Return to top arrow. https://codepen.io/rdallaire/pen/apoyx
/*
$(window).scroll(function() {
    if ($(this).scrollTop() >= 100) {        // If page is scrolled more than 100px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});
*/

// https://facelessuser.github.io/pymdown-extensions/extensions/details/
(function () {
'use strict';
/**
 * Converts details/summary tags into working elements in browsers that don't yet support them.
 * @return {void}
 */
var details = (function () {

  var isDetailsSupported = function () {
    // https://mathiasbynens.be/notes/html5-details-jquery#comment-35
    // Detect if details is supported in the browser
    var el = document.createElement("details");
    var fake = false;

    if (!("open" in el)) {
      return false;
    }

    var root = document.body || function () {
      var de = document.documentElement;
      fake = true;
      return de.insertBefore(document.createElement("body"), de.firstElementChild || de.firstChild);
    }();

    el.innerHTML = "<summary>a</summary>b";
    el.style.display = "block";
    root.appendChild(el);
    var diff = el.offsetHeight;
    el.open = true;
    diff = diff !== el.offsetHeight;
    root.removeChild(el);

    if (fake) {
      root.parentNode.removeChild(root);
    }

    return diff;
  }();

  if (!isDetailsSupported) {
    var blocks = document.querySelectorAll("details>summary");
    for (var i = 0; i < blocks.length; i++) {
      var summary = blocks[i];
      var details = summary.parentNode;

      // Apply "no-details" to for unsupported details tags
      if (!details.className.match(new RegExp("(\\s|^)no-details(\\s|$)"))) {
        details.className += " no-details";
      }

      summary.addEventListener("click", function (e) {
        var node = e.target.parentNode;
        if (node.hasAttribute("open")) {
          node.removeAttribute("open");
        } else {
          node.setAttribute("open", "open");
        }
      });
    }
  }
});

(function () {
  var onReady = function onReady(fn) {
    if (document.addEventListener) {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      document.attachEvent("onreadystatechange", function () {
        if (document.readyState === "interactive") {
          fn();
        }
      });
    }
  };

  onReady(function () {
    details();
  });
})();

}());


// This for the table of variables implemented by Jordan

function TabLetterLinkDeactive() {
  // Get all elements with class="TabLetterLink" and remove the class "active"
  TabLetterLink = document.getElementsByClassName("TabLetterLink");
  for (i = 0; i < TabLetterLink.length; i++) {
    TabLetterLink[i].className = TabLetterLink[i].className.replace(" active", "");
  }
}

function openLetter(evt, letter) {
  // Declare all variables
  var i, TabContentLetter, TabLetterLink;

  // Get all elements with class="TabContentLetter" and hide them
  TabContentLetter = document.getElementsByClassName("TabContentLetter");
  for (i = 0; i < TabContentLetter.length; i++) {
    TabContentLetter[i].style.display = "none";
  }

  TabLetterLinkDeactive();

  // Show the current tab, and add an "active" class to the button that opened the tab
  var myLetter = document.getElementById(letter)
  myLetter.style.display = "block";
  myLetter.getElementsByClassName('HeaderLetter')[0].style.display = "none";
  evt.currentTarget.className += " active";
} 

function searchInput() {
  // Declare variables
  var input, filter, ul, li, a, i, allLetters, letter;
  var TabContentLetter;

  TabLetterLinkDeactive();

  TabContentLetter = document.getElementsByClassName("TabContentLetter");
  for (i = 0; i < TabContentLetter.length; i++) {
    TabContentLetter[i].style.display = "none";
    TabContentLetter[i].getElementsByClassName("HeaderLetter")[0].style.display = "none";
  }

  input = document.getElementById('InputSearch');
  filter = input.value.toUpperCase();
  var ulLetters = document.getElementById('Letters');
  allLetters = ulLetters.getElementsByTagName('li');
  for (letter = 0; letter < allLetters.length; letter++) {
    liul = allLetters[letter];
    li = liul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    // Start at 1 to avoid finding the letters themselve
    for (i = 1; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
        liul.getElementsByTagName('ul')[0].style.display = "block";
        li[0].style.display = "block";
        li[i].style.display = "block";
      } else {
        li[i].style.display = "none";
      }
    }
  }
}

function defaultClick(first) {
  if ( !first) {
    document.getElementById('InputSearch').value = '';
    searchInput();
  }
  if ( window.location.hash && ( /^#[a-zA-Z]$/.test(window.location.hash) ) ) {
    document.getElementById('click'+window.location.hash[1]).click();
  }
  else {
    document.getElementById("clickA").click();
  }
}


$(function() {
    defaultClick(true);
});

$("#InputSearch").keydown(function() {
  //alert( "Handler for .keydown() called." );
});

