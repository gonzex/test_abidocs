
*Proof of concept* website available at <https://gmatteo.github.io/test_abidocs/>

## Getting started

Install the python packages required to build the static website with:

    $ cd ~abinit/docs
    $ pip install -r requirements.txt

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
