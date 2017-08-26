---
authors: MG, XG
---

*Proof of concept* website available at <https://gmatteo.github.io/test_abidocs/>

This page describes the details of the documentation system of Abinit and how to contribute. 
We also have a more basic overview on how to contribute to this guide or the user guide.

Most of the Abinit documentation is written in [Markdown](https://en.wikipedia.org/wiki/Markdown)
a lightweight markup language with plain text 
[formatting syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
For documentation, we mean the Abinit lessons, the User Guide, the Abinit topics 
written by the Abinit developers as well as pages that are generated automatically in python using the information about
the input variables stored in `abinit_vars.yml` and the bibliographic citations given in `abiref.bib`.

The website, indeed, is automatically generated with [MkDocs](http://www.mkdocs.org/)
a static site generator geared towards project documentation. 
starting from a single YAML configuration file (`mkdocs.yml`) that describes the 
organization of the pages on the website.
MkDocs uses [Python-Markdown](https://pythonhosted.org/Markdown) to parse the Markdown documentation
and can generate automatically the navigation bars and the Table of Contents (TOC) for the different pages
thanks to the [jinja template engine](http://jinja.pocoo.org/).

In addition to the basic markdown syntax, the Abinit documentation supports extensions/shortcuts
to ease the writing of hyperlinks and the inclusion of bibliographic citations stored in bibtex format
in the `abiref.bib` file.
A detailed description of *our markdown dialect* is given in [our markdown page](markdown).
Also [MathJax](https://www.mathjax.org/) for equations in LaTeX is activated, 
and the (few) specificities of its usage in the ABINIT docs are explained [here](markdown#MathJax).
As a net result, Abinit developers can write nice-looking documentation working in an environment that 
is Abinit-aware and without having to use HTML directly. 

[Bootstrap](http://getbootstrap.com/) a popular HTML, CSS, and JS framework 
for developing responsive, mobile first projects on the web.
MkDocs includes a couple built-in themes as well as various third party themes,
all of which can easily be customized with extra CSS or JavaScript or overridden from the theme directory. 
[Material](http://squidfunk.github.io/mkdocs-material/) is a theme for MkDocs, 
It is built using Google's [Material Design](https://www.google.com/design/spec/material-design) guidelines.
Other mkdocs themes are available at <http://mkdocs.github.io/mkdocs-bootswatch>.


## Getting started

Install the python packages required to build the static website with:

```sh
$ cd ~abinit/docs
$ pip install -r requirements.txt
```

MkDocs comes with a built-in dev-server that lets you preview your documentation as you work on it. 
Make sure you are in `~abinit/docs`, and then start *our customized* server 
by running the `mksite.py` serve command:

```console
$ cd ~abinit/docs
$ ./mksite.py serve
Regenerating database...
Saving database to /Users/gmatteo/git_repos/abidocs/doc/tests/test_suite.cpkl
Initial website generation completed in 9.17 [s]
Generating markdown files with input variables of code: `abinit`...
...
...
INFO    -  Building documentation...
INFO    -  Cleaning site directory
[I 170826 03:37:05 server:283] Serving on http://127.0.0.1:8000
[I 170826 03:37:05 handlers:60] Start watching changes
[I 170826 03:37:05 handlers:62] Start detecting changes
```

Open up `http://127.0.0.1:8000/` in your browser, and you'll see the default home page being displayed.

!!! tip
    Use `mksite.py serve --dirtyreload` to enable the live reloading in the development server, 
    but only re-build files that have changed. 
    This option is designed for site development purposes and is **much faster** than the default live reloading.

Note that the HTML files will be produced in a temporary directory and therefore are **not** under revision control
(the real source is represented by the `.md` files and the other `.yml` files that can be changed by the developers
and these files under git control).


## The ABINIT HTML doc

List of variables, lessons of the tutorial, help files, ABINIT topics, bibliography, theory documents 
are all important documentation files, posted on the Web, to help the users. 
The `~abinit/doc/mksite.py` script generates most of these files by converting markdown files to HTML.

This script:

- Reads information from: 
    - (i) a set of YAML files, 
    - (ii) a bibtex file, 
    - (iii) input files contained in tests/*/Input. Files (i) and (ii) are contained in subdirectories */origin_files.
- Performs some checks.
- Establishes intermediate dictionaries and databases.
- Expands special strings, of the form %%"[[tag]]"%%, to create HTML links.
- Creates the needed HMTL files 

The expansion of special strings is documented in [[developers:link_shortcuts]]. 
It can be used in all the YAML files mentioned below. 
For equations/formulas, [Mathjax](http://docs.mathjax.org/en/latest/mathjax.html) is activated, and allows
to process and visualize LaTeX formulas, see also [[developers:link_shortcuts]].

## Front matter

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
For instance, the list of authors is reported in the HTML page footer.


## Input variables: How to add/modify?

Edit the file `~abinit/doc/input_variables/origin_files/abinit_vars.yml` using the Abivars.jar GUI:

    $ java -jar Abivars.jar
  
A window should open, and you can fill the requested information.
To add a new variable, click on `Edit` (upper right) then click on `Add new variable`.

Note that input variables for the executables other than the main abinit (e.g. anaddb, aim, optic) are 
denoted `input_variable_name@executable`, e.g. `dipdip@anaddb` 
(this allows to waive the ambiguity with the dipdip input variable for the main abinit).

After having edited the info related to one input variable (see the infos at [[developers:abivars.yml|Specs for abivars.yml]]), 
you must still **save the entire file** (click on "File" (upper right) then "Save"). 
Just editing one input variable and saving the changes will only go to some internal variable, and this is 
NOT saving your modifications in the YAML storage file.
Then, build the HTML using generate_doc.py.

## Bibliographic reference: how to add/modify?

Edit the file `~abinit/doc/bibliography/origin_files/abiref.bib` with your preferred editor. 
It is a standard bibtex file.
Note that the ID must be of the form "FirstauthornameYEAR", e.g. "Amadon2008" 
(start with an uppercase letter, then lower case, then four-digit year). 
Possibly, a letter might be added in case of ambiguity: e.g. there exists also `Amadon2008a`
Then, build the HTML using `mksite.py`.

## Topics: how to add/modify?

The topic HTML files are assembled by generate_doc.py from different sources.

The high-level information is contained in ~abinit/doc/topics/origin_files/topic_NAME.yml,
where NAME is the name of the topic. The first section ("introduction") is also found in this file,
as well as the information on lessons of the tutorial that are relevant for this topic. 
The "text" content of the "introduction" section is in plain HTML.

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

* `name`: must be the name of the topics, also used in the name of file (topic_name.yml)
* `keyword`: will be inserted in the HTML header to create the Web name of the HTML page, if the default header is used
* `authors`: will be inserted in the copyright, if the default copyright is used
* `howto`: will be inserted in the subtitle of the Web page "How to ... ?" if the default subtitle is ised
* `header`: the HTML header (usually, take the default, that uses the component "keyword")
* `title`: the title that will be echoed in the HTML page
* `subtitle`: the subtitle (usually, take the default, that uses the component "howto")
* `copyright`: the copyright (usually, take the default, that uses the component "authors")
* `links`: list of links to other pages (usually, take the default)
* `introduction`: see above
* `tutorials`: see above
* `end`: final tags, take the default

Then, build the HTML using `mksite.py`.

## Lessons of the tutorial: how to add/modify?

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

Then, build the HTML using `mksite.py`.

## Help files: how to add/modify?

The structuration for help files is very similar to the one for the lessons of the tutorial.
The major part of comes from ~abinit/doc/users/origin_files/help_NAME.yml,
although selected high-level information (name, keyword, author and subtitle) 
is contained in ~abinit/doc/topics/origin_files/helps.yml.

Do not forget to build the HTML using generate_doc.py.

## Theory documents: how to add/modify?

The structuration for theory documents is very similar to the one for the lessons of the tutorial.
The major part of comes from ~abinit/doc/users/origin_files/theorydoc_NAME.yml,
although selected high-level information (name, keyword, author and subtitle) 
is contained in ~abinit/doc/topics/origin_files/theorydocs.yml.

Do not forget to build the HTML using generate_doc.py.

## Topics and tribes

Since the beginning of the ABINIT HTML documentation, every input variable 
has been required to belong to a **varset** (set of variables, e.g. `varbas`, `varfil`).
However, starting in Summer 2017, we require every input variable to be also mentioned in at least one of the
documentation "topics" and, for such topic, to be characterized by a "tribe".

The allowed list of tribes (a generic list, irrespective of the topic) is contained in
~abinit/doc/topics/origin_files/list_tribes.yml. 
Standard names are:

- `compulsory` (when such input variable **must** be present in the input file when the "feature" of the topic is activated)
- `basic` (when such input variable is usually explicitly specified in the standard usage, although the default might be adequate)
- `useful` (when the default value is used most of the time)
- `expert` (when only expert users should use other values than the default)

Other tribe names have been allowed for specific topics, in which such a classification 
(compulsory/basic/useful/expert) is not a relevant one.

In order to specify the (possibly several) combinations of topic+tribe to which an input variable is attached,
the field "topics" is used inside the ~abinit/doc/input_variables/generated_doc/abinit_vars.yml file
(and can be filled thanks to the use of the Abivars.jar GUI).

Some examples:

* for dmatpawu: "DFT+U_useful"
* for mdwall: "MolecularDynamics_expert"
* for gwpara: "parallelism_useful, GW_basic"

The latter is a case where one input variable is associated to two topics, with a different tribe 
for topic "parallelism" and topic "GW".

## Specifications for the abinit_vars.yml file

As values in the ~abinit/doc/input_variables/origin_files/abinit_vars.yml file, 
you can specify numbers, string, arrays, following the standard specification of YAML:

* [[http://en.wikipedia.org/wiki/YAML| Wikipedia YAML page]]
* [[http://www.yaml.org/|The official YAML page]]

Several "types" are defined to allow sufficient flexibility in the specifications, as follows.

### !variable

It is the type that contains the other fields.  

* `abivarname`: the name of the variable. Note that the name for input variables 
   of the executables anaddb, aim and optic is always finished with @anaddb, @aim or @optic.
* `characteristics`: possibly, a specific characteristics of the input variable. 
   To be chosen among the names in ~abinit/doc/input_variables/origin_files/characteristics.yml .
* `commentdefault`: possibly, some comment about a default value.
* `commentdims`: possibly, some comment about the dimension of an array.
* `defaultval`: must be an integer or real value, possibly specified using the types presented below (e.g. !multiplevalue)
* `dimensions`: either scalar or a list of dimensions, using YML syntax.
* `excludes`: possible excluded values
* `mnemonics`: a longer description of the variable role, in a few words
* `requires`: the input variable is relevant only if this condition is fulfilled
* `text`: free text describing the input variable
* `topics`: a string, specified in [[developers:topics_and_tribes]]
* `varset`: a unique "set of variables" to which the variable belong. 
   To be chosen among the names in ~abinit/doc/input_variables/origin_files/varsets.yml .
* `vartype`: to be chosen among integer, real or string
   If there is no information of a type for a specific variable, its value must be "null".

### !multiplevalue

This is the equivalent to the X * Y syntax in fortran.

<code>
  X * Y
</code>

will become

```yaml
  !multiplevalue
    number : X
    value : Y
```

If X is null, it means that you want to do *Y (all Y)

### !range

```yaml
  !range
     start: 1
     stop: N
```

As a default value, it means that the default value is 1,2, ... N

### !valuewithconditions

This type allows to specify conditions on values:

```yaml
!valuewithconditions
    defaultval: -[[diemix]]
    '70 < [[iprcel]] and [[iprcel]] < 80': '[[diemix]]'
    '[[iscf]]<10': '[[diemix]]'
    '[[iprcel]]==0': '[[diemix]]'
```

defaultval is the default value if no condition is fulfilled.
As condition, please use strings with the most basic expressions, 
containing <, < =, >, >=, ==, !=, +, -, *, /, etc to allow for further simple parsing !

As a convention, we use "pythonic" way for expressions, so you can use "or", "and" and "in" 
also as %%[[varname]]%% in [1,2,5] for example ...

### !valuewithunit

This type allows to specify values with units:

```yaml
!valuewithunit
    units: eV
    value: 100.0
```

means "100 eV".

### Constraints between variables

In the YML file (and via the GUI), there are some constraints between variables that have been introduced.
You can specifiy "requires: CONDITION" and "excludes: CONDITION" in the YML file 
(or fill the fields requires and excludes in the GUI).

If a varname has "requires: CONDITION", it means that the variable is only relevant when CONDITION is fulfilled.
If a varname has as "excludes: CONDITION", it means that the specification of the variable in the input file forbids 
the CONDITION to be fulfilled.

## Strings

Pay attention to strings. If it is recognized as string directly, you don't need ticks (' ').
Otherwise, you need to put ticks. 
For example, if you want to use a link as a value, use a link shortcut like <nowiki>[[abivarname]]</nowiki>. 
See the doc about link shortcuts at [[developers:link_shortcuts]]. 
