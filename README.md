**Proof of concept** website available at <https://gmatteo.github.io/test_abidocs/>

### ** Main features **

The documentation is mainly written in [markdown](https://en.wikipedia.org/wiki/Markdown)
a lightweight markup language with plain text formatting
[syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
The website is automatically generated with [MkDocs](http://www.mkdocs.org/)
starting from a single YAML configuration file (`mkdocs.yml`).

`MkDocs` uses [Python-Markdown](https://pythonhosted.org/Markdown)
to parse the Markdown documentation.
In addition to the basic markdown syntax, we add extensions for
the automatic generation of internal links, bibliographic citations and the
rendering of Latex equations with [MathJax](https://www.mathjax.org/)

[Bootstrap](http://getbootstrap.com/) a popular HTML, CSS, and JS framework 
for developing responsive, mobile first projects on the web.

MkDocs includes a couple built-in themes as well as various third party themes,
all of which can easily be customized with extra CSS or JavaScript or overridden
from the theme directory. See e.g <http://mkdocs.github.io/mkdocs-bootswatch>

### ** Installation **

Install the `mkdocs` package using pip:

    $ pip install mkdocs

Install the [Math extension](https://github.com/mitya57/python-markdown-math) for Python-Markdown with:

    $ pip install python-markdown-math

Install the collection of bootstrap themes with:

    $ pip install mkdocs-bootswatch

### ** Usage **

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

Markdown extensions available

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

```[[Allen1976]]```

Link to [[Allen1976]] paper

## Markdown 

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


## Markdown extensions

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
<p>Here's a simple Plotly plot - <a href="https://bit.ly/1Or9igj">plotly.js documentation</a></p>

<!-- Plots go in blank <div> elements. 
    You can size them in the plot layout, or give the div a size as shown here.
-->
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
      <img src="../tutorials/bse_assets/tbs2_1.png" alt="Uncoverged BSE spectrum">
      <div class="carousel-caption">
        <h3>Unconverged BSE optical spectrum</h3>
        <!-- <p>LA is always so much fun!</p> -->
      </div>
    </div>

    <div class="item">
      <img src="../tutorials/bse_assets/tbs5.png" alt="Converged BSE spectrum">
      <div class="carousel-caption">
        <h3>Convergengeof BSE optical spectrum wrt k-point sampling</h3>
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
