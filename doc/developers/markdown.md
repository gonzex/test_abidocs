---
authors: MG, XG
plotly: true
rpath: /developers/markdown.md
---

# Writing Documentation

This page is intended as a quick reference to the Markdown syntax used to write the Abinit documentation.
Markdown can be used **almost everywhere** including the description of the input variables
stored in `abinit_vars.yml` and the description of the automatic tests given in the `TEST_INFO` section.
For a more complete introduction to Markdown, see 
[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

## Markdown quick reference

### Inline styles

| Markdown | Result | Extension required |
| :-- | :-- | :-- |
| `*italics*` | *italics* | --
| `**bold**` | **bold** |  --
| `***bold and italic***` | ***bold and italic*** |  --
| `` `monospace` `` | `monospace` |  --
| `~~strikethrough~~` | ~~strikethrough~~ | [Tilde](http://facelessuser.github.io/pymdown-extensions/extensions/tilde/) 
| `CH~3~CH~2~OH` | CH~3~CH~2~OH |  [Tilde](https://facelessuser.github.io/pymdown-extensions/extensions/tilde/) 
| `==highlight==` | ==highlight== | [Mark](http://facelessuser.github.io/pymdown-extensions/extensions/mark/) 
| `^^underline me^^` | ^^underline me^^ | [Caret](https://facelessuser.github.io/pymdown-extensions/extensions/caret/) 


### Code and syntax highlighting

Blocks of code are either fenced by lines with three back-ticks ``` or are indented with four spaces. 
For example, the Markdown text:

```
Inline `code` has `back-ticks around` it.
```

produces: Inline `code` has `back-ticks around` it.

The fastest way to include shell commands is to indent the code with four space:

```md
    $ abinit < tbase1_x.files 2> log &
```

that produces:

    $ abinit < tbase1_x.files 2> log &

Fenced blocks allow the specification of the language used for syntax highlighting.
Fortran code, for example, can be included with:

~~~md
```fortran
do ii=1, 10
  write(*,*)"Hello world"
end do
```
~~~

that is displayed as:

```fortran
do ii=1, 10
  write(*,*)"Hello world"
end do
```

### Tables

To create a table in Markdown use the syntax:

```md
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```

that produces:

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


### Figures

To include figures, use the standard Markdown syntax:

```md
![](/tutorials/bse_assets/tbs2_1.png)
```

![](/tutorials/bse_assets/tbs2_1.png)

For figures with a caption use the [markdown-figures extension](https://github.com/helderco/markdown-figures):

```md
![](/tutorials/bse_assets/tbs5.png)
:   Convergenge of BSE optical spectrum wrt $\kk$-point sampling. 
    See also [[ngkpt]] and [[shiftk]].
```

![](/tutorials/bse_assets/tbs5.png)
:   Convergenge of BSE optical spectrum wrt $\kk$-point sampling. 
    See also [[ngkpt]] and [[shiftk]].

!!! note
     The caption can contain Latex equations as well as [Abinit wiki links](#wiki-links).
    `<img>` and `<figure>` elements are automatically centered via CSS directives declared in `extra.css`.


## Links

The Markdown syntax for links is:

| Markdown | Result | Extension required |
| :-- | :-- | :--
| `[The Abinit website](https://www.abinit.org)` | [The Abinit website](https://www.abinit.org)  | --
| `<https://www.abinit.org>` | <https://www.abinit.org> | --
| `https://www.abinit.org` | https://www.abinit.org | [MagicLink](https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/)


This is the **recommended** approach to create links to external resources and internal links to other pages/sections
of the website.
There are however cases in which we would like to have an even simpler syntax to generate automatically 
links in the documentation pages, in particular links to:

* The input variables declared in `abinit_vars.yml`.
* The bibliographic citations declared in `abiref.bib`.
* Input files of the Abinit test suite.
* Website pages commonly used e.g. a topic page.

For this reason, we extend the Markdown syntax to account for typical cases
that are discussed in the next sections.


### Wiki links

The DokuWiki syntax is used, with two pairs of brackets and possible separators (:, # and |).
In the simple case, this gives `[[name]]` but, more generally `[[namespace:name#section|text]]`
where `namespace`, `section` and `text` are optional (in such case, the adequate separator should not be mentioned). 
The namespace is not echoed in the Web page, while if a `text` is given, it will supercede the echo of the 
`name` in the Web page (see examples below).

!!! warning
    Do not use parentheses within the pair of double brackets, the whole expression will not be recognized.

When an internal link is recognized, the dokuwiki item is replaced by the adequate HTML link 
There are a couple of names immediately recognized:

* as "ecut" above, the name of an abinit input variable (provided it is mentioned in `abinit_vars.yml`)
* the name of a bibliographical reference (provided it is mentioned in `abiref.bib`)
* the path to a file in one of the `~abinit/tests/*/Input` directory
* the path to a reference output file in a ~abinit/tests/tuto*/Refs directory
* the label of a section inside the own file

Examples:

| Markdown | Result 
| :-- | :-- 
| `[[ecut]]` | [[ecut]] 
| `[[abinit:ecut]]` | [[abinit:ecut]] 
| `[[anaddb:dipdip]]` | [[anaddb:dipdip]] 
| `[[dipdip@anaddb]]` | [[dipdip@anaddb]] 
| `[[Amadon2008]]` | [[Amadon2008]] 
| `[[~abinit/tests/tutorial/Input/tbase1_1.in]]` | [[~abinit/tests/tutorial/Input/tbase1_1.in]] 
| `[[tests/tutorial/Input/tbase1_1.in]]` | [[tests/tutorial/Input/tbase1_1.in]] 
| `[[test:libxc_41]]` | [[test:libxc_41]] 
| `[[tests/tutorial/Refs/tbase1_1.out]]` |  [[tests/tutorial/Refs/tbase1_1.out]] 
| `[[~abinit/tests/tutorial/Refs/tbase1_1.out]]` |  [[~abinit/tests/tutorial/Refs/tbase1_1.out]] 
| `[[~abinit/tests/Psps_for_tests/6c.lda.atompaw]]` | [[~abinit/tests/Psps_for_tests/6c.lda.atompaw]]
| `[[tests/Psps_for_tests/6c.lda.atompaw]]` | [[tests/Psps_for_tests/6c.lda.atompaw]]

!!! note
    Note the difference between `[[anaddb:dipdip]]` and `[[dipdip@anaddb]]`.
    In the first case, only `dipdip` is echoed,  while in the second case, `dipdip@anaddb` is echoed.
    This syntax is needed because there's also a `dipdip` variable in Abinit.

    The links to input files have a popover with the description of the test.
    Hovering on a citation opens a popover with the title of the Bibtex entry.

Also, the input variables for anaddb, optic and aim(bader) will be recognized if they are used with 
the namespaces `anaddb`, `optic` and `aim`. 
For the latter input variables, one has thus also the choice between the syntax 

To specify the name of the anchor in a bibliographic citation use the syntax with the `|` separator:

    Please consult [[Gonze2016 | the last generic ABINIT article]].

that in rendered in HTML as: Please consult [[Gonze2016 | the last generic ABINIT article]].

The script generate_doc.py does a bit of formatting in these examples: it keeps one pair of square brackets 
in the case of a bibliographic reference, and add "~abinit/" in the case of a path.


### Internal links with namespace

Other internal links can be recognized thanks to the namespace. 
A first set of allowed internal namespaces are: 

* `lesson`
* `topic`
* `help`
* `bib`
* `theorydoc`
* `varset`
* `ac`
* `src`

In such cases, provided there is a corresponding generated HTML file 
in one of the ~abinit/doc/*/generated_files subdirectories, 
that has a name that start with the namespace and end with the name, the link will be established.

Examples:

| Markdown | Result |
| :-- | :-- |
| `[[lesson:gw1]]` | [[lesson:gw1]] 
| `[[topic:BSE]]` | [[topic:BSE]] 
| `[[help:abinit]]` | [[help:abinit]] 
| `[[bib:Amadon2008]]` | [[bib:Amadon2008]] 
| `[[theorydoc:mbpt]]` | [[theorydoc:mbpt]] 
| `[[varset:bse]]` | [[varset:bse]] 
| `[[varset:bse]]` | [[varset:bse]] 
| `[[src:94_scfcv/scfcv.F90]]` | [[src:94_scfcv/scfcv.F90]]
| `[[ac:abiref_gnu_5.3_debug.ac]]` | [[ac:abiref_gnu_5.3_debug.ac]]

`[[topic:PIMD#1|Introduction]]` becomes [[topic:PIMD#1|Introduction]]

`[[#markdown-quick-reference|quick reference]]` becomes [[#markdown-quick-reference|quick reference]]
  
Actually, using the real name of the file without suffix, e.g. `lesson_gw1` will also be recognized, 
although this real name is echoed, instead of the name without namespace.

`[[lesson_gw1]]` becomes [[lesson_gw1]]
lesson_gw1
  
There is an added formatting by generate_doc.py, in the case of the help files: 
`[[help_codename]]`is echoed "codename help file":

`[[help_abinit]]` becomes [[help_abinit]]
abinit help file

### External links

As for dokuwiki, some external links are also recognized. The following case are treated:

* a link that starts with `www.`
* the namespaces `http`, `https`, `ftp`, `file`

| Markdown | Result |
| :-- | :-- |
| `[[www.abinit.org]]` | [[www.abinit.org]] 
| `www.abinit.org` | www.abinit.org 

It's also possible to specify the name of the link with the `|` separator:
`[[https://wiki.abinit.org | The ABINIT Wiki]]` that gives [[https://wiki.abinit.org | The ABINIT Wiki]] 


### Permalinks

Permalinks are a feature of the [Table of Contents extension](https://pythonhosted.org/Markdown/extensions/toc.html), 
which is part of the standard Markdown library. 
The extension inserts an anchor at the end of each headline, which makes it possible to directly link to a subpart of the document.

By default, all headers will automatically have unique id attributes generated based upon the text of the header. 
The name of the anchor is constructed from the header by converting the string to lower-case and replacing
white spaces with `-`.
For instance, `#wiki-links` is the anchor associated to the "Wiki Links" section 
of this page and we can refer to it with the Markdown syntax:

```md
As we have seen in the [previous section](#wiki-links)
```

that produces: As we have seen in the [previous section](#wiki-links)

!!! tip 
    Hover with the mouse on the header in the HTML page to show the permalink in the browser.

Links to external pages are a little bit more difficult to handle because
you need to know how to locate the external page with respect to the present one.
There are two possible approaches: *relative links* and *root-relative links*.
In the first case

```md 
An example of [relative link](abimkdocs/#getting-started)
```

produces: An example of [relative link](abimkdocs/#getting-started)

while

```md 
An example of [root-relative link](/developers/abimkdocs/#getting-started)
```

produces: An example of [root-relative link](/developers/abimkdocs#getting-started)

!!! note
    It is also possible to generate automatically the Table of Contents by just 
    placing the `[TOC]` marker in the document where you would like the Table of Contents to appear. 
    Then, a nested list of all the headers in the document will replace the marker. 
    Note, however, the use of `[TOC]` in the Abinit Markdown pages is not recomended as
    the Table of Contents is automatically generated by the Mkdocs them and displayed 
    inside the website navigation bar.


## MathJax

Formulas written in LaTeX are interpreted automatically (at visualization time) thanks to the 
[MathJax](http://docs.mathjax.org/en/latest/mathjax.html) on-the-flight processor
while the math extension for Python-Markdown is provided by 
[python-markdown-math](https://github.com/mitya57/python-markdown-math).

Latex equations can be used **everywhere** in the documentation including the description of the variables
reported in `abinit_vars.yml` and the description of the tests gives in the `TEST_INFO` section.
For the ABINIT documentation, the conventions are:

* `$...$`  yields an *onlinecite* translation of the LaTeX formula.
* `$$...$$` yields *display* mode, the LaTeX formula being rendered on one dedicated line (moreover, centered).
* To have the equations numbered, use the display mode above, and (inside the markers) declare your equation 
  within the standard `\begin{equation}...\end{equation}` markers.
* When a `$` sign is inside a `#!html <pre>...</pre>` HTML section, MathJax does not interpret it.
* Use `\$` to prevent a real \$ to be interpreted.

For instance `#!latex $|\Phi\rangle$` produces $|\Phi\rangle$ while `#!latex $$\Phi_\kq(\rr)$$` produces

$$\Phi_\kq(\rr)$$ 

Equations enclosed by `$$...$$` or `\begin{equation}...\end{equation}` markers are automatically numbered 
and can be referenced inside the Markdown text using the standard Latex syntax:

```latex
\begin{equation}
G(12) = -i \langle \Theta^N_0|T\bigl[\Psi(1)\Psi^\dagger(2)\bigr]|\Theta^N_0 \rangle \label{eq:GreenDef}
\end{equation}
```

that produces:

\begin{equation}
G(12) = -i \langle \Theta^N_0|T\bigl[\Psi(1)\Psi^\dagger(2)\bigr]|\Theta^N_0 \rangle \label{eq:GreenDef}
\end{equation}

Equations can be referenced with:

    The propagator in Eq.\ref{eq:GreenDef}

that produces: The propagator in Eq.\ref{eq:GreenDef}

Note that MathJax is configured with Latex macros to facilitate the insertion of symbols
commonly used in our domain:

| Markdown | Result 
| :--      | :-- 
| `$\rr$`  | $\rr$
| `$\GG$`  | $\GG$
| `$\kk$`  | $\kk$
| `$\qq$`  | $\qq$
| `$\kq$`  | $\kq$

Please consult the preamble in `abinit_theme/main.html` for the complete list of macros.

## Markdown extensions

### SmartSymbols

[SmartSymbols](https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/) 
adds syntax for creating special characters such as trademarks, arrows, fractions, etc. 
The list of symbols supported by the extension is:

Markdown       | Result
-------------- |--------
`(tm)`         | (tm)
`(c)`          | (c)
`(r)`          | (r)
`c/o`          | c/o
`+/-`          | +/-
`-->`          | -->
`<--`          | <--
`<-->`         | <-->
`=/=`          | =/=
`1/4, etc.`    | 1/4, etc.
`1st 2nd etc.` |1st 2nd etc.


### Admonitions

[Admonitions](https://pythonhosted.org/Markdown/extensions/admonition.html) are useful
to stress important statements (useful e.g. in lessons).
Admonition are created using the Markdown syntax:

```md
!!! note
    Here is a note for you.
```

and 

```md
!!! danger "Don't try this at home!"
    Stand back. I'm about to try science!
```

for an admonition with a custom title (make sure to quote the title).

The types of admonitions available for use in MkDocs depend on the theme being used. 
The Material theme [supports](http://squidfunk.github.io/mkdocs-material/extensions/admonition/#types) the following types:

!!! note
    I am a "note" admonition and look the same as "seealso".

!!! tip
    I am a "tip" admonition and look the same as "hint" and "important".

!!! warning
    I am a "warning" admonition and look the same as "attention" and "caution".

!!! danger
    I am a "danger" admonition and look the same as "error".

!!! summary
    I am a "summary" admonition and look the same as "tldr".

!!! success
    I am a "success" admonition and look the same as "check" and "done".

!!! failure
    I am a "failure" admonition and look the same as "fail" and "missing".

!!! bug
    I am a "bug" admonition.


For the complete list, consult the mkdocs-material 
[documentation](/http://squidfunk.github.io/mkdocs-material/extensions/admonition/)

### Details

[Detail](https://facelessuser.github.io/pymdown-extensions/extensions/details/)
is an extension that creates collapsible elements that hide their content. 
It uses the HTML5 `#!html <details><summary>` tags to accomplish this. 
It supports nesting and you can also force the default state to be open. 
This extension is used in the documentation of the input variable to generate 
a container with the list of tests associated to the variable. 

Examples:

```md
???+ note "List of variables"
     [[ecut]] [[asr@anaddb]]
```

produces the *open* element:

???+ note "List of variables"
     [[ecut]] [[asr@anaddb]]


while 

```md
??? note "Click to open!"
     [[ecut]] [[asr@anaddb]]
```

creates a *closed* element:

??? note "Click to open!"
     [[ecut]] [[asr@anaddb]]


### MagicLink

[MagicLink](https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/)
scans for URLs and emails and generates proper HTML links for them.  
No special syntax is required, you just type or paste the links and they get converted.  
MagicLink auto-links HTML, FTP, and email links.

If you happen to have some conflicts with syntax for a specific case, you can always revert 
to the old auto-link format as well: `<https://www.link.com>`.  

For even more magic, enable `repo_url_shortener` for shorter concise links for popular source code hosts.  
Issue, pull request, and commit links will be shortened in the style of GFM. 
Issues are shortened to `user/repo#1` for repositories external to `base_repo_url` and `#1` for internal links.  
For commit links, external commits will show as `` user/repo@`abc1234` `` and internal commits 
will show as `` `abc1234` ``. Currently supports GitHub, GitLab, and Bitbucket.
Links require no special syntax.

To refer to a particular git commit inside a Markdown document use:

    Solved in https://github.com/abinit/abinit/commit/f74dba1ed8346ca586dc95fd10fe4b8ced108d5e

that produces: Solved in https://github.com/abinit/abinit/commit/f74dba1ed8346ca586dc95fd10fe4b8ced108d5e

It's also possible to mention a particular github issue with the syntax:

    Fix https://github.com/abinit/abinit/issues/1

that produces: Fix https://github.com/abinit/abinit/issues/1

!!! note
    This extension is useful to generate nice changelogs and release notes.

### Abinit extensions

It's also possbile to create a button that opens a modal window containing 
the input file with the syntax:

```
    {% modal tests/v1/Input/t01.in %}
```

that produces:

{% modal tests/v1/Input/t01.in %}

This is useful for lessons to give direct access to the input files.
If multiple files are used such as in: 

```
    {% modal tests/v1/Input/t01.in tests/v1/Input/t02.in %}
```

a modal window with tabs is produced

{% modal tests/v1/Input/t01.in tests/v1/Input/t02.in %}

To create a panel with the output file use:

```
    {% editor tests/v1/Refs/t01.out %}
```

that gives:

{% editor tests/v1/Refs/t01.out %}

Also in this case, a multi-tab panel is produced if multiple files are used such as in:

```
    {% editor tests/v1/Refs/t01.out tests/v1/Refs/t02.out %}
```

that produces:

{% editor tests/v1/Refs/t01.out tests/v1/Refs/t02.out %}


## Plotly

[plotly](https://plot.ly/api/) is a high-level, declarative charting library built on top of d3.js and stack.gl.
plotly.js ships with over 20 chart types, including scientific charts, 3D graphs, statistical charts, SVG maps, 
financial charts, and more.
Note that plotly is deactivated by default so you have to activate plotly support inside a Markdown page by
adding

```yaml
---
plotly: true
---
```

to the front matter. This option will load the javascript library in the HTML page
so that one can include HTML+javascript code to generate nice interactive plots
inside the Markdown documentation.
For example the HTML + javascript code:

```html
<!-- Plots go in blank <div> elements. 
     You can size them in the plot layout, or give the div a size as shown here.-->
<p>Here's a simple Plotly plot - <a href="https://bit.ly/1Or9igj">plotly.js documentation</a></p>

<div id="plotly_plot" style="width:90%;height:250px;"></div>
<script>
$(function() {
    Plotly.plot(document.getElementById('plotly_plot'), [{
        x: [1, 2, 3, 4, 5],
        y: [1, 2, 4, 8, 16] }], 
        {margin: {t: 0}} 
    );
});
</script>
```

produces the following plot:

<p>Here's a simple Plotly plot - <a href="https://bit.ly/1Or9igj">plotly.js documentation</a></p>

<div id="plotly_plot" style="width:90%;height:250px;"></div>
<script>
$(function() {
    Plotly.plot(document.getElementById('plotly_plot'), [{
        x: [1, 2, 3, 4, 5],
        y: [1, 2, 4, 8, 16] }], 
        {margin: {t: 0}} 
    );
});
</script>

plotly is used to plot the [connection network](/input_variables/connections) for the input variables
and the [code statistics](/developers/codestats).


## Media content

Links to videos can be included with the standard Markdown syntax:

```md
The video below gives an overwiew of the command line options of `runtests.py`

[![asciicast](https://asciinema.org/a/40324.png)](https://asciinema.org/a/40324)
```

that produces:

The video below gives an overwiew of the command line options of `runtests.py`

[![asciicast](https://asciinema.org/a/40324.png)](https://asciinema.org/a/40324)


<div id="myCarousel" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#myCarousel" data-slide-to="1"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="../../tutorials/bse_assets/tbs2_1.png" alt="Uncoverged BSE spectrum">
      <div class="carousel-caption">Unconverged BSE optical spectrum</div>
    </div>
    <div class="item">
      <img src="../../tutorials/bse_assets/tbs5.png" alt="Converged BSE spectrum">
      <div class="carousel-caption">Convergenge of BSE optical spectrum wrt k-point sampling</div>
    </div>
  </div>

  <!-- Left and right controls -->
  <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>


The propagator in Eq.\ref{eq:GreenDef}
