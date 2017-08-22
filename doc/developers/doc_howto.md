---
authors: MG, XG
plotly: true
---

# ** Main features **

*Proof of concept* website available at <https://gmatteo.github.io/test_abidocs/>

The documentation is mainly written in [markdown](https://en.wikipedia.org/wiki/Markdown)
a lightweight markup language with plain text formatting
[syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
The website is automatically generated with [MkDocs](http://www.mkdocs.org/)
starting from a single YAML configuration file (`mkdocs.yml`).

`MkDocs` uses [Python-Markdown](https://pythonhosted.org/Markdown) to parse the Markdown documentation.
In addition to the basic markdown syntax, we add extensions for
the automatic generation of internal links, bibliographic citations and the
rendering of Latex equations with [MathJax](https://www.mathjax.org/)

[Bootstrap](http://getbootstrap.com/) a popular HTML, CSS, and JS framework 
for developing responsive, mobile first projects on the web.

MkDocs includes a couple built-in themes as well as various third party themes,
all of which can easily be customized with extra CSS or JavaScript or overridden
from the theme directory. See e.g <http://mkdocs.github.io/mkdocs-bootswatch>

## ** Installation **

Install the `mkdocs` package using pip:

    $ pip install mkdocs

Install the [Math extension](https://github.com/mitya57/python-markdown-math) for Python-Markdown with:

    $ pip install python-markdown-math

Install the collection of bootstrap themes with:

    $ pip install mkdocs-bootswatch

## ** Usage **

There's a single configuration file named `mkdocs.yml`, and a folder named `docs` that will contain 
your documentation source files. 
Right now the docs folder just contains a single documentation page, named index.md.

MkDocs comes with a built-in dev-server that lets you preview your documentation as you work on it. 
Make sure you're in the same directory as the mkdocs.yml configuration file, and then start the server 
by running the mkdocs serve command:

```sh
$ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
[I 160402 15:50:43 server:271] Serving on http://127.0.0.1:8000
[I 160402 15:50:43 handlers:58] Start watching changes
[I 160402 15:50:43 handlers:60] Start detecting changes
```

Open up `http://127.0.0.1:8000/` in your browser, and you'll see the default home page being displayed.

## Markdown quick reference

### ** Internal links and citations **

To add a link to an Abinit input variable use:

```text
This is a link to the [[ecut]] input variable.
```

that produces:

This is a link to the [[ecut]] input variable.

[[tests/tutorial/Input/tbase1_1.in]]

[[tests/tutorial/Refs/tbase1_1.out]]

citations:

```
[[Allen1976]]
```

Link to [[Allen1976]] paper


```
[[ecut]]
```

### ** Markdown **

Markdown Table

```
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


Can include videos with:

```
[![asciicast](https://asciinema.org/a/40324.png)](https://asciinema.org/a/40324)
```

The video below gives an overwiew of the command line options of `runtests.py`

[![asciicast](https://asciinema.org/a/40324.png)](https://asciinema.org/a/40324)


## ** Markdown extensions **

modal window

```{% modal tests/v1/Input/t01.in %}```

{% modal tests/v1/Input/t01.in %}

modal window with tabs:

```{% modal tests/v1/Input/t01.in tests/v1/Input/t02.in %}```

{% modal tests/v1/Input/t01.in tests/v1/Input/t02.in %}

Single editor

```{% editor tests/v1/Refs/t01.out %}```

{% editor tests/v1/Refs/t01.out %}

Multi-tab editor

```{% editor tests/v1/Refs/t01.out tests/v1/Refs/t02.out %}```

{% editor tests/v1/Refs/t01.out tests/v1/Refs/t02.out %}

### ** Admonition **

```text
!!! warning
    Before reading the present file, and get some grasp about the main ABINIT
    application, you should get some theoretical background. In case you have
    ...
```

!!! warning
    Before reading the present file, and get some grasp about the main ABINIT
    application, you should get some theoretical background. 


### ** Latex support via Mathjax **

```
$$ G(12) = -i \langle \Theta^N_0|T\bigl[\Psi(1)\Psi^\dagger(2)\bigr]|\Theta^N_0 \rangle
\label{eq:GreenDef} $$
```

The propagator in Eq.\ref{eq:GreenDef} contains ...

\begin{equation}
G(12) = -i \langle \Theta^N_0|T\bigl[\Psi(1)\Psi^\dagger(2)\bigr]|\Theta^N_0 \rangle \label{eq:GreenDef}
\end{equation}
```

$$ G(12) = -i \langle \Theta^N_0|T\bigl[\Psi(1)\Psi^\dagger(2)\bigr]|\Theta^N_0 \rangle \label{eq:GreenDef} $$

The propagator in Eq.\ref{eq:GreenDef} contains ...


### ** Plotly **

[plotly](https://plot.ly/api/)

```html
```

<!-- Plots go in blank <div> elements. 
    You can size them in the plot layout, or give the div a size as shown here.
-->

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


<div id="myCarousel" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#myCarousel" data-slide-to="1"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="/tutorials/bse_assets/tbs2_1.png" alt="Uncoverged BSE spectrum">
      <div class="carousel-caption">
        <h3>Unconverged BSE optical spectrum</h3>
        <!-- <p>LA is always so much fun!</p> -->
      </div>
    </div>

    <div class="item">
      <img src="/tutorials/bse_assets/tbs5.png" alt="Converged BSE spectrum">
      <div class="carousel-caption">
        <h3>Convergenge of BSE optical spectrum wrt k-point sampling</h3>
        <!-- <p>Thank you, Chicago!</p> -->
      </div>
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

### Front matter

Front matter is the first section of the markdown file and must take the form of valid YAML 
document enclosed between triple-dashed lines. Here is a basic example:

```yaml
---
title: Blogging Like a Hacker
authors: MG
---
```

Between these triple-dashed lines, you can set predefined variables (see below for a reference) 
or even create custom ones of your own. 
These variables will then be available to you to access using Liquid tags both further down in the 
file and also in any layouts or includes that the page or post in question relies on.

### Permalinks

Permalinks refer to the URLs (excluding the domain name or directory folder) for your pages.
Jekyll supports a flexible way to build permalinks, allowing you to leverage various template variables 
or choose built-in permalink styles (such as date) that automatically use a template-variable pattern.

### The ABINIT HTML doc

List of variables, lessons of the tutorial, help files, ABINIT topics, bibliography, theory documents 
are all important documentation files, posted on the Web, to help the users. 
The `~abinit/doc/abimkdocs` script generates most of these files by converting markdown and YAML files to HTML.

Usage : <color blue>python generate_doc.py [-h|--help]</color>
(No options are allowed at present, except the help ones)

This script:

  - Reads information from: (i) a set of YAML files, (ii) a bibtex file, 
    (iii) input files contained in tests/*/Input. Files (i) and (ii) are contained in subdirectories */origin_files.
  - Performs some checks.
  - Establishes intermediate dictionaries and databases.
  - Expands special strings, of the form %%"[[tag]]"%%, to create HTML links.
  - Creates the needed HMTL files (all contained in different subdirectories */generated_files).

The expansion of special strings is documented in [[developers:link_shortcuts]]. 
It can be used in all the YAML files mentioned below. 
For equations/formulas, [Mathjax](http://docs.mathjax.org/en/latest/mathjax.html) is activated, and allows
to process and visualize LaTeX formulas, see also [[developers:link_shortcuts]].

### Input variables: How to add/modify?

Edit the file ~abinit/doc/input_variables/origin_files/abinit_vars.yml, thanks to the GUI Abivars.jar, with the command:

    $ java -jar Abivars.jar
  
A window should open, and you can fill the requested information.
To add a new variable, click on "Edit" (upper right) then click on "Add new variable".

Note that input variables for the executables other than the main abinit (e.g. anaddb, aim, optic) are 
denoted "input_variable_name"@"executable", e.g. dipdip@anaddb 
(this allows to waive the ambiguity with the  dipdip input variable for the main abinit).

After having edited the info related to one input variable (see the infos at [[developers:abivars.yml|Specs for abivars.yml]]), 
you must still SAVE THE ENTIRE FILE (click on "File" (upper right) then "Save"). 
Just editing one input variable and saving the changes will only go to some internal variable, and this is 
NOT saving your modifications in the YAML storage file.
Then, build the HTML using generate_doc.py.

### Bibliographic reference: how to add/modify?

Edit the file `~abinit/doc/bibliography/origin_files/abiref.bib` with your preferred editor. 
It is a standard bibtex file.
Note that the ID must be of the form "FirstauthornameYEAR", e.g. "Amadon2008" 
(start with an uppercase letter, then lower case, then four-digit year). 
Possibly, a letter might be added in case of ambiguity: e.g. there exists also `Amadon2008a`
Then, build the HTML using `abimkdocs`.

### Topics: how to add/modify?

The topic HTML files are "assembled" by generate_doc.py from different sources.

The high-level information is contained in ~abinit/doc/topics/origin_files/topic_NAME.yml,
where NAME is the name of the topic. The first section ("introduction") is also found in this file,
as well as the information on lessons of the tutorial that are relevant for this topic. The "text" content of
the "introduction" section is in plain HTML.

At variance, the other sections of the topic_NAME.html are created from other sources. 
The list of input variables that are relevant to this topics is assembled from the information
given for these input variables, see [[#input variableshow_to_add_modify|Input variables : how_to_add_modify]], 
as well as [[developers:topics_and_tribes]], while the list of relevant input files
is assembled from the information in each of these input files (add a line "#%% topics = " in the last section of the input file.). 
The bibliography list is assembled from the references cited in the "introduction" section, 
that use [[developers:link_shortcuts|Shortcuts for Web links]].

Note the file default_topic.yml, whose components are used in case they are not specified explicitly 
in the more specific file topic_NAME.yml.

The list of topics is found in the file ~abinit/doc/topics/origin_files/list_of_topics.yml .

Thus, if you want to a modify "topic" Web page, the "introduction" and "tutorial" sections as well as 
the name and some other high level info can be modified by editing ~abinit/doc/topics/origin_files/topic_NAME.yml, 
while you have to edit the relevant input variables and input files to modify the next sections. 
You can modify the bibliography section only through a modification of the "introduction" and "tutorial" sections. 

To add a new topic, add the name in list_of_topics.yml, and then create a corresponding topic_NAME.yml file.
The different components are used by the script generate_doc.py as follows:

* name: must be the name of the topics, also used in the name of file (topic_name.yml)
* keyword: will be inserted in the HTML header to create the Web name of the HTML page, if the default header is used
* authors: will be inserted in the copyright, if the default copyright is used
* howto: will be inserted in the subtitle of the Web page "How to ... ?" if the default subtitle is ised
* header: the HTML header (usually, take the default, that uses the component "keyword")
* title: the title that will be echoed in the HTML page
* subtitle: the subtitle (usually, take the default, that uses the component "howto")
* copyright: the copyright (usually, take the default, that uses the component "authors")
* links: list of links to other pages (usually, take the default)
* introduction: see above
* tutorials: see above
* end: final tags, take the default

Then, build the HTML using `abimkdocs`.

### Lessons of the tutorial: how to add/modify?

The major part of each lesson HTML file comes from ~abinit/doc/topics/origin_files/lesson_NAME.yml,
although selected high-level information (name, keyword, author and subtitle) 
is contained in ~abinit/doc/topics/origin_files/lessons.yml. 
Note the last section of the latter file, that gives a default value for each component of a lesson file 
that would not have been specified in either lesson_NAME.yml or the specific section of lessons.yml.

The content of ~abinit/doc/topics/origin_files/lesson_NAME.yml is either:

* an "intro" section and a "body" section,
* or (this is preferred), an "intro" section and a list of sections, each having a "title" and a "body".

In the latter case, a table of content is automatically generated by generate_doc.py .
The latter structure can be seen in lesson_dmft.yml.

The "text" content of these section is in plain HTML.
Note that the indentation is important in YAML. 
The "text" lines in lesson_NAME.yml must be indented by at least two blanks.

In order to add a new lesson, introduce a new section in lessons.yml, and create a new 
~abinit/doc/topics/origin_files/lesson_NAME.yml .

Then, build the HTML using `abimkdocs`.

### Help files: how to add/modify?

The structuration for help files is very similar to the one for the lessons of the tutorial.
The major part of comes from ~abinit/doc/users/origin_files/help_NAME.yml,
although selected high-level information (name, keyword, author and subtitle) 
is contained in ~abinit/doc/topics/origin_files/helps.yml.

Do not forget to build the HTML using generate_doc.py.

### Theory documents: how to add/modify?

The structuration for theory documents is very similar to the one for the lessons of the tutorial.
The major part of comes from ~abinit/doc/users/origin_files/theorydoc_NAME.yml,
although selected high-level information (name, keyword, author and subtitle) 
is contained in ~abinit/doc/topics/origin_files/theorydocs.yml.

Do not forget to build the HTML using generate_doc.py.

### Shortcuts for Web links

This page concerns the YAML files in ~abinit/doc/*/origin_files,
that are processed by the script ~abinit/doc/generate_doc.py 
to automatically generate HTML files in ~abinit/doc/*/generated_files.

Thanks to this processing, it has been possible to introduce shortcuts
to ease the writing of many different hyperlinks in these YAML files.
Also, [[http://docs.mathjax.org/en/latest/mathjax.html|MathJax]] for equations
in LaTeX is activated, and the (few) specificities of its usage in the ABINIT doc are explained 
in the section [[#MathJax]] of the present document.

### Syntax

The [[wiki:syntax#links|DokuWiki syntax]] is used, with two pairs of brackets and possible separators (:,# and |).\\
In the simple case, this gives

  [[name]]
  
but, more generally

  [[namespace:name#section|text]]
  
where namespace, section and text are optional (in such case, the adequate separator should not be mentioned). 
The namespace is not echoed in the Web page, while if a "text" is given, it will supercede the echo of the 
name in the Web page (see examples below).
Limitation: do not use parentheses within the pair of double brackets, the whole expression will not be recognized.

### Simple allowed internal links

When an internal link is recognized, the dokuwiki item is replaced by the adequate HTML link 
by the script generate_doc.py.
Example :

  [[ecut]] becomes `<a href="../../input_variables/generated_files/varbas.html#ecut>ecut</a>`

This will point to [[http://www.abinit.org/doc/helpfiles/for-v8.4/input_variables/html_automatically_generated/varbas.html#ecut|ecut]]. 

There are a couple of names immediately recognized:

* as "ecut" above, the name of an abinit input variable (provided it is mentioned in abinit_vars.yml)
* the name of a bibliographical reference (provided it is mentioned in abiref.bib)
* the path to a file in a `~abinit/tests/*/Input` directory
* the path to a reference output file in a ~abinit/tests/tuto*/Refs directory
* the label of a section inside the own file

Examples:
  
  [[Amadon2008]] becomes <a href="../../bibliography/generated_files/bibliography.html#Amadon2008>[Amadon2008]</a>
  
this will point to [[http://www.abinit.org/doc/helpfiles/for-v8.4/users/bibliography.html#Amadon2008|Amadon2008]].
  
  [[Gonze2016|The last generic ABINIT article]] becomes <a href="../../bibliography/generated_files/bibliography.html#Gonze2016>The last generic ABINIT article</a>

this will point to [[http://www.abinit.org/doc/helpfiles/for-v8.4/users/bibliography.html#Gonze2016|The last generic ABINIT article]] 
(note the use of the | separator !).
  
  [[tests/v1/Input/t01.in]] becomes <a href="../../tests/v1/Input/t01.in>~abinit/tests/v1/Input/t01.in</a>
  
and also
  
  [[#notations|this section]] becomes <a href="#notations">this section</a>
  
The script generate_doc.py does a bit of formatting in these examples: it keeps one pair of square brackets in the case of a bibliographic reference, and add "~abinit/" in the case of a path.

### Internal links with a namespace

Other internal links can be recognized thanks a namespace. 
A first set of allowed internal namespaces are "lesson", "topic", "help", "bib", "theorydoc", and "varset". 
In such cases, provided there is a corresponding generated HTML file 
in one of the ~abinit/doc/*/generated_files subdirectories, 
that has a name that start with the namespace and end with the name,  the link will be established.

Examples:
    
  [[lesson:gw1]] becomes <a href="../../tutorial/generated_files/lesson_gw1.html>gw1</a>
  
  [[topic:PIMD#1|Introduction]] becomes <a href="../../topics/generated_file/topic_PIMD.html#1>Introduction</a>
  
Actually, using the real name of the file without suffix, e.g. lesson_gw1 will also be recognized, 
although this real name is echoed, instead of the name without namespace.

  [[lesson_gw1]] becomes <a href="../../tutorial/generated_files/lesson_gw1.html>lesson_gw1</a>
  
There is an added formatting by generate_doc.py, in the case of the help files: 
%%[[help_codename]]%% is echoed "codename help file" :

  [[help_abinit]] becomes <a href="../../tutorial/generated_files/help_abinit.html>abinit help file</a>

Also, the input variables for anaddb, optic and aim(bader) will be recognized if they are used with 
the namespaces "anaddb", "optic" and "aim". For the latter input variables, one has thus also the choice 
between the syntax %%[[executable:input_variable_name]] or [[input_variable_name@executable]]. 
For example [[anaddb:dipdip]] or [[dipdip@anaddb]]%%. 
In the first case, only dipdip is echoed, while in the second case, dipdip@anaddb is echoed.

  [[anaddb:dipdip]] becomes <a href="../../input_variables/generated_files/varset_anaddb.html>dipdip</a>
  
  [[dipdip@anaddb]] becomes <a href="../../input_variables/generated_files/varset_anaddb.html>dipdip@anaddb</a>
  
### External links

As for dokuwiki, some [[wiki:syntax#external|external links]] are also recognized. The following case are treated :

* a link that starts with `www.`
* the namespaces `http`, `https`, `ftp`, `file`

Examples:
    
  [[www.abinit.org]] becomes <a href="http://www.abinit.org">www.abinit.org</a>
  
  [[https://wiki.abinit.org|The ABINIT Wiki] becomes <a href="https://wiki.abinit.org">The ABINIT Wiki</a>
  
### MathJax

Formulas written in LaTeX are interpreted automatically (at visualization time) thanks to the 
[[http://docs.mathjax.org/en/latest/mathjax.html|MathJax]] on-the-flight processor. 
For the ABINIT documentation, the conventions are :

* \$...\$  yields an "onlinecite" translation of the LaTeX formula;
* \$\$...\$\$ yields "display" mode, the LaTeX formula being rendered on one dedicated line (moreover, centered);
* to have the equations numbered, use the display mode above, and (inside the markers) declare your equation 
  with the standard %%\b%%egin{equation} and %%\ %%end{equation}
* when a \$ sign is inside a <pre> ... </pre> HTML section, MathJax does not interpret it
* to prevent a real \$ to be interpreted, use \\\$

Examples:

  $|\phi \ angle$
  $$|\phi \ angle$$
  $$\begin{equation} |\phi \ angle \end{equation}$$


### Topics and tribes

Since the beginning of the ABINIT HTML documentation, every input variable 
has been required to belong to a **varset** (set of variables, e.g. `varbas`, `varfil`).
However, starting in Summer 2017, we require every input variable to be also mentioned in at least one of the
documentation "topics" and, for such topic, to be characterized by a "tribe".

The allowed list of tribes (a generic list, irrespective of the topic) is contained in the file 
~abinit/doc/topics/origin_files/list_tribes.yml. 
Standard names are:

- "compulsory" (when such input variable MUST be present in the input file when the "feature" of the topic is activated);
- "basic" (when such input variable is usually explicitly specified in the standard usage, although the default might be adequate);
- "useful" (when the default value is used most of the time);
- "expert" (when only expert users should use other values than the default).

Other tribe names have been allowed for specific topics, in which such a classification 
(compulsory/basic/useful/expert) is not a relevant one.

In order to specify the (possibly several) combinations of topic+tribe to which an input variable is rattached,
the field "topics" is used inside the ~abinit/doc/input_variables/generated_doc/abinit_vars.yml file
(and can be filled thanks to the use of the Abivars.jar GUI).

Some examples:

* for dmatpawu: "DFT+U_useful"
* for mdwall: "MolecularDynamics_expert"
* for gwpara: "parallelism_useful, GW_basic"

The latter is a case where one input variable is associated to two topics, with a different tribe 
for topic "parallelism" and topic "GW".

### Specifications for the abinit_vars.yml file

As values in the ~abinit/doc/input_variables/origin_files/abinit_vars.yml file, 
you can specify numbers, string, arrays, following the standard specification of YAML:

* [[http://en.wikipedia.org/wiki/YAML| Wikipedia YAML page]]
* [[http://www.yaml.org/|The official YAML page]]

Several "types" are defined to allow sufficient flexibility in the specifications, as follows.

### !variable

It is the type that contains the other fields.  

* abivarname: the name of the variable. Note that the name for input variables of the executables anaddb, aim and optic is always finished with @anaddb, @aim or @optic.
* characteristics: possibly, a specific characteristics of the input variable. To be chosen among the names in ~abinit/doc/input_variables/origin_files/characteristics.yml .
* commentdefault: possibly, some comment about a default value.
* commentdims: possibly, some comment about the dimension of an array.
* defaultval: must be an integer or real value, possibly specified using the types presented below (e.g. !multiplevalue)
* dimensions: either scalar or a list of dimensions, using YML syntax.
* excludes: possible excluded values
* mnemonics: a longer description of the variable role, in a few words
* requires: the input variable is relevant only if this condition is fulfilled
* text: free text describing the input variable
* topics: a string, specified in [[developers:topics_and_tribes]]
* varset: a unique "set of variables" to which the variable belong. To be chosen among the names in ~abinit/doc/input_variables/origin_files/varsets.yml .
* vartype: to be chosen among integer, real or string
    If there is no information of a type for a specific variable, its value must be "null".

### !multiplevalue

This is the equivalent to the X * Y syntax in fortran.

<code>
  X*Y
</code>

will become

<code>
  !multiplevalue
    number : X
    value : Y
</code>

If X is null, it means that you want to do *Y (all Y)

### !range

<code>
  !range
     start: 1
     stop: N
</code>

As a default value, it means that the default value is 1,2, ... N

### !valuewithconditions

This type allows to specify conditions on values:

<code>
!valuewithconditions
    defaultval: -[[diemix]]
    '70 < [[iprcel]] and [[iprcel]] < 80': '[[diemix]]'
    '[[iscf]]<10': '[[diemix]]'
    '[[iprcel]]==0': '[[diemix]]'
</code>

defaultval is the default value if no condition is fulfilled.
As condition, please use strings with the most basic expressions, 
containing <, < =, >, >=, ==, !=, +, -, *, /, etc to allow for further simple parsing !

As a convention, we use "pythonic" way for expressions, so you can use "or", "and" and "in" 
also as %%[[varname]]%% in [1,2,5] for example ...

### !valuewithunit

This type allows to specify values with units:

<code>
 !valuewithunit
        units: eV
        value: 100.0
</code>

means "100 eV".

### Constraints between variables

In the YML file (and via the GUI), there are some constraints between variables that have been introduced.
You can specifiy "requires: CONDITION" and "excludes: CONDITION" in the YML file 
(or fill the fields requires and excludes in the GUI).

If a varname has "requires: CONDITION", it means that the variable is only relevant when CONDITION is fulfilled.
If a varname has as "excludes: CONDITION", it means that the specification of the variable in the input file forbids 
the CONDITION to be fulfilled.

### Strings

Pay attention to strings. If it is recognized as string directly, you don't need ticks (' ').
Otherwise, you need to put ticks. 
For example, if you want to use a link as a value, use a link shortcut like <nowiki>[[abivarname]]</nowiki>. 
See the doc about link shortcuts at [[developers:link_shortcuts]]. 
