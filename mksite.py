#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import os
import mkdocs.__main__

# We don't install with setup.py hence we have to add the directory [...]/abinit/tests to $PYTHONPATH
pack_dir = os.path.dirname(__file__)
sys.path.insert(0, pack_dir)

# This needed to import doc.tests
sys.path.insert(0, os.path.join(pack_dir, "doc"))

def prof_main(main):
    """
    Decorator for profiling main programs.

    Profiling is activated by prepending the command line options
    supported by the original main program with the one of following keywords:
         [`prof`, `tracemalloc`, `traceopen`]

    Example:

        $ script.py arg --foo=1

    becomes

        $ script.py prof arg --foo=1

    `prof`: profiles the code with `cProfile`.
        In this case the decorated main accepts two new arguments:

        prof_file: Name of the output file with profiling data
            If not given, a temporary file is created.
        sortby: Profiling data are sorted according to this value.
            default is "time". See sort_stats.

    `tracemalloc`: uses the tracemalloc module (py>3.4) to trace memory allocations

    `traceopen`: prints the list of open files before exiting (require `psutil` module)
    """
    from functools import wraps
    @wraps(main)
    def wrapper(*args, **kwargs):
        import sys
        do_prof, do_tracemalloc, do_traceopen = 3 * [False]
        if len(sys.argv) > 1:
            do_prof = sys.argv[1] == "prof"
            do_tracemalloc = sys.argv[1] == "tracemalloc"
            do_traceopen = sys.argv[1] == "traceopen"

        if do_prof or do_tracemalloc or do_traceopen: sys.argv.pop(1)

        if do_prof:
            print("Entering profiling mode...")
            import pstats, cProfile, tempfile
            prof_file = kwargs.pop("prof_file", None)
            if prof_file is None:
                _, prof_file = tempfile.mkstemp()
                print("Profiling data stored in %s" % prof_file)

            sortby = kwargs.pop("sortby", "time")
            cProfile.runctx("main()", globals(), locals(), prof_file)
            s = pstats.Stats(prof_file)
            s.strip_dirs().sort_stats(sortby).print_stats()
            return 0

        elif do_tracemalloc:
            print("Entering tracemalloc mode...")
            # Requires py3.4
            try:
                import tracemalloc
            except ImportError:
                print("Error while trying to import tracemalloc (requires py3.4)")
                raise SystemExit(1)

            tracemalloc.start()
            retcode = main(*args, **kwargs)
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')

            n = min(len(top_stats), 20)
            print("[Top %d]" % n)
            for stat in top_stats[:20]:
                print(stat)

        elif do_traceopen:
            try:
                import psutil
            except ImportError:
                print("traceopen requires psutil module")
                raise SystemExit(1)
            import os
            p = psutil.Process(os.getpid())
            retcode = main(*args, **kwargs)
            print("open_files", p.open_files())

        else:
            retcode = main(*args, **kwargs)

        return retcode

    return wrapper


@prof_main
def main():
    verbose = 1 if "-v" in sys.argv or "--verbose" in sys.argv else 0
    strict = "-s" in sys.argv or "--strict" in sys.argv

    if "--help" in sys.argv or "-h" in sys.argv:
        return mkdocs.__main__.cli()

    from abimkdocs.website import build_website
    if len(sys.argv) > 1 and ("--help" not in sys.argv or "-h" not in sys.argv):
        website = build_website("./doc", verbose=verbose)

    if len(sys.argv) > 1 and sys.argv[1] in ("build", "serve", "gh-deploy"):
        website.generate_markdown_files()
        print(website)

    if len(sys.argv) > 1 and sys.argv[1] == "validate":
        return website.validate_html_build()

    if "--dry-run" in sys.argv: return 0
    mkdocs_retcode = mkdocs.__main__.cli()
    return mkdocs_retcode + len(website.warnings)


if __name__ == '__main__':
    sys.exit(main())