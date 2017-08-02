# Abinit documentation (proof of concept)

Website available at <https://gmatteo.github.io/test_abidocs/>

# Main features:

The documentation is mainly written in [markdown](https://en.wikipedia.org/wiki/Markdown)
a lightweight markup language with plain text formatting
[syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

The website is automatically generated with [MkDocs](http://www.mkdocs.org/)
using a single YAML configuration file (```mkdocs.yml```)

`MkDocs` uses [Python-Markdown](https://pythonhosted.org/Markdown/index.html)
to parse the Markdown documentation.
In addition to the basic markdown syntax, we add extensions for
the automatic generation of internal links, bibliographic citations and the
display of Latex equations with [MathJax](https://www.mathjax.org/)

MkDocs includes a couple built-in themes as well as various third party themes,
all of which can easily be customized with extra CSS or JavaScript or overridden
from the theme directory. See e.g <http://mkdocs.github.io/mkdocs-bootswatch>

# Installation

Install the `mkdocs` package using pip:

    pip install mkdocs

Install the [Math extension](https://github.com/mitya57/python-markdown-math) for Python-Markdown with:

    pip install python-markdown-math

Install the collection of bootstrap themes with:

    pip install mkdocs-bootswatch

# Usage

There's a single configuration file named mkdocs.yml, and a folder named docs that will contain 
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

Open up `http://127.0.0.1:8000/` in your browser, and you'll see the default home page being displayed:


# Markdown extensions available

## Internal links


## Citations 

## Admonition

```
!!! warning
    text goes here
```

## Latex support via Mathjax

```
$$ G(12) = -i \langle \Theta^N_0|T\bigl[\Psi(1)\Psi^\dagger(2)\bigr]|\Theta^N_0 \rangle
\label{eq:GreenDef} $$
```

The propagator in Eq.\ref{eq:GreenDef} contains ...


## Modal

```
modal
\{!tests/v1/Input/t01.in!\}
```
