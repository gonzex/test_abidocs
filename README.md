# Abinit documentation (proof of concept)

Website available at <https://gmatteo.github.io/test_abidocs/>

# Main features:

    - The documentation is mainly written in [markdown](https://en.wikipedia.org/wiki/Markdown)
      a lightweight markup language with plain text formatting
      [syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

    - The website is automatically generated with [MkDocs](http://www.mkdocs.org/)
      using a single YAML configuration file (```mkdocs.yml```)

    - `MkDocs` uses [Python-Markdown](https://pythonhosted.org/Markdown/index.html)
       to parse the Markdown documentation.
       In addition to the basic markdown syntax, we support extensions for
       the automatic generation of internal links, bibliographic citations and the 
       display of Latex equations with [MathJax](https://www.mathjax.org/)

    -  MkDocs includes a couple built-in themes as well as various third party themes, 
       all of which can easily be customized with extra CSS or JavaScript or overridden from the theme directory. 
       http://mkdocs.github.io/mkdocs-bootswatch/

# Installation

Install the `mkdocs` package using pip:

    pip install mkdocs

Install the collection of bootstrap themes with:

    pip install mkdocs-bootswatch
