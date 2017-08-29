---
authors: YP
rpath: tutorials/source_code.md

---

# Developing for ABINIT  

## Introducing ABINIT to new developers (WARNING : some parts are severely outdated ...).  

This tutorial introduces ABINIT to the new developers. We want here to give a
first insight into the internals of ABINIT. In other words, you will look at
what's under the cap. Being an ABINIT user is not required though it will help
a lot, in particular when writing a test case for your contribution. However
some experience in programming is necessary if you want to take maximum
benefit from this lesson. In particular, some ease with Fortran 90, 95 or 2003
will be truly welcome. Familiarity with the command line will be wonderful
too.

WARNING : some parts are severely outdated.


## 1 Context

  
The ABINIT package is aimed at being used by different groups of people,
without mandatory control by the main contributors of the ABINIT group. In the
same way, the ABINIT development project is fundamentally open to the
contributions of various persons, not located in Louvain-la-neuve or other
major development sites of ABINIT. These external contributors are _de facto_
members of the ABINIT group.

People using the code might consider adding their personal subroutines without
trying to make them part of the official ABINIT package. However, this has two
drawbacks for them: in subsequent versions, their modifications will not be
incorporated, so that they might have to check and modify the interface for
each new version; moreover, their addition is not tested by other users of the
code, then some nasty bugs might remain unnoticed. Our opinion is that it
would also be nicer from them to share the fruits of their coding efforts with
other users of the code.

Of course, a collaborative effort has some drawbacks as well. In particular,
the collaboration between distant developers should be carefully planned,
since orthogonal modifications of the same piece of code by two different
people at the same time is very likely to happen, generating "negative
progress", i.e. a large waste of time when synchronization is to be done. It
is also necessary to use a well-defined coding style, to provide test case
files, and to comment the modifications and additions as much as possible, in
order to facilitate the maintenance and the future modifications.

A lot of information for the ABINIT developers can be found in the
[developer's corner,](http://dev.abinit.org), especially, [How to
contribute](http://dev.abinit.org/doc/for-new-developers/how-to-contribute),
and [Specificities](http://dev.abinit.org/doc/particulars),



## 2 Objectives

  
The main goals of this lesson are to provide you with a useful understanding
of the source tree structure and the build process, as well as sensibilize you
to the rules and procedures followed for the development of ABINIT. In the
example we have chosen, we will suppose that you want to add an input variable
to the code and create the corresponding subroutine. For simplicity, we will
now imagine that you have designed a new exchange-correlation functional and
that you want to test it with ABINIT. Here are the steps we will take:

  1. Get the source and compile the code.
  2. Identify the subroutines to modify.
  3. Add the new input variable and its associated routine.
  4. Add a test to the test suite.
  5. Create a patch for the project leader.

For this lesson, your input variable will be a real number called "_lesson_".
The task devoted to your routine is just to print this variable.



## 3 Tasks

  
#### Get the source and compile the code

There are two ways of getting the source code of ABINIT:

  * directly from the ABINIT web site ([abinit.org/](http://www.abinit.org/)) by downloading the tarball;
  * from the ABINIT gitlab.
  * 

While the first method is straightforward, the second one requires you to know
how to use git(lab). Please see the [ABINIT gitlab Wiki
section](https://wiki.abinit.org/doku.php?id=developers:specificities_git_abinit/).

Once you have got the tarball, uncompress it by typing:

tar xvzf abinit-_&lt;version&gt;_.tar.gz

where _&lt;version&gt;_ is the version number you downloaded, e.g. "7.4.2".
Then go into the newly-created _abinit-&lt;version&gt;_ directory and have a
look at it. To get get more familiar with the source tree structure, have a
closer look at the [Directories and files](http://dev.abinit.org/doc/for-adv-
developers/source-tree) Web page. Then answer the following questions:

Q1. If you need off-line documentation, in which directories will you look
for?

Q2. Where can be found the tests?

Q3. What do the numbers in the names of the "_src_" subdirectories stand for?

Q4. In the source subdirectories, what do the _abinit.src_ files contain? In
your opinion, what is their purpose?

Q5. What kind of tests are available? How important do you think they are?

Now you can try to build ABINIT. Information on how to do it is stored inside
the INSTALL file. Please read it now.

Before actually starting the compilation, type:

./configure --help | more

and read carefully the output. You might then find useful to have a look at
the template for config files stored in _~abinit/doc/build/config-template.ac_
which will provide you with more details on the configuration.

The compilation will likely take more than 10 minutes. In the meantime, you
can proceed to the next task.

#### Identify the subroutines to modify

At this point, you have to discover what parts of the code will have to be
modified in order to have your contribution correctly integrated. First choose
randomly a few subroutines in one of the "_src/*_" subdirectories and have a
look at them, putting emphasis on their headers. Then try to answer the
following questions:

Q6. How would you identify the subroutines involved in the treatment of input
variables?

Q7. Where are the routines handling exchange-correlation? Which input
variables are they strongly related to?

Q8. Which subroutine would you choose as a parent for yours?

Q9. Where is the _wrtout_ subroutine? What is its purpose? How does it work?

#### Add the new input variable and its associated routine

Please examine the file _~abinit/doc/developers/programmer_guide.txt_ and
_~abinit/doc/developers/rules_coding.txt_. This might help writing your own
subroutine. To actually start, go to the subdirectory you've identified before
and type:

sh ../../util/developers/mkroutine.sh handle_lesson

This will create a file named _handle_lesson.F90_, _handle_lesson_ being the
name of your subroutine.

Add treatment code for your input variable to the files you have identified
previously. Then write your subroutine and add a call to it at a suitable
place. When you're done, issue `./config/scripts/makemake` from the top source
directory, to have the build system aware of the presence of your new routine.
Last but not least, rebuild _abinit_.

#### Add a test to the test suite

Since your contribution is to be integrated into the version 7 (8, 9 ...) of
ABINIT, all associated tests should go to the `~`_ABINIT/tests/v7/_ directory
(or v8/ or v9/ .... Wander a little bit around the subdirectories of _tests/_,
and have a look at their content. Examine one of the input files, contained in
the v7 (8, 9 ...) subdirectory. Note content of the bottom of the file. Each
test is identified by an index, attributed after consulting the ABINIT
coordinator. He decided that your contribution will be checked by test #999.
Read [ the Web documentation that describes how to add a new
test](http://dev.abinit.org/environment/buildbot/howto-add-a-new-test-in-the-
test-suite)

Q10. What do you need to do in order to have a new test added?

Implement your test and issue `./Runtests.py v7[999]` in the _tests/_
subdirectory, to check that it works fine.

#### Create a patch for the project leader

There are two ways of creating a patch, depending on whether you are using
Bazaar or not. If yes, you just have to register your new files, write a
change log and commit your changes. This procedure is highly recommended, as
it is very fast and as the project leader will be provided with a lot of
flexibility and information to handle your contribution. If not, you have to
create a patch with a full description of your changes and send it by email or
ftp.

To get some comfort, the project leader needs a patch both in universal format
and where new files are considered empty in the old version.

Q11. Which options will you give to the _diff_ command to produce the patch ?

Q12. How will you proceed exactly to create it ?



## 4 Solutions

  
Even if we provide you here with the answers to some of the questions, we
highly recommend you to try by yourself before looking at them. Please read
this section only as a last resort.

R1. In _~abinit/doc/_, of course.

R2. In _~abinit/tests/_, of course.

R3. According to [Directories and files](http://dev.abinit.org/doc/for-adv-
developers/source-tree), they correspond to a hierarchical structuring of the
dependencies within ABINIT. The higher the level, the more the dependencies on
lower levels.

R4. They contain the list of source files to compile, and allow the developers
to explore several ways at once by giving them the choice of what to put in
ABINIT. Thanks to their presence, no developer needs know all the internals of
the build system.

R5. The available documentation describes all tests in detail and stresses
their importance quite enough. Just read the suggested files.

R6. I would issue a _grep_ command for a random input variable in order to
trace the handling of input variables throughout the code.

R7. These routines can be found in _~abinit/src/56_xc_, and are driven by the
_ixc_ input variable.

R8. The _~abinit/src/56_xc/drivexc.F90_ routine, for instance.

R9. Look in _~abinit/src/14_hidewrite/wrtout.F90_, the header contains
detailed explanations.

R10. You need to follow [ the Web documentation that describes how to add a
new test](http://dev.abinit.org/environment/buildbot/howto-add-a-new-test-in-
the-test-suite)

R11. "-u -r -N".

R12. Supposing that you have downloaded ABINIT 7.4.1, the following set of
commands will do:

  * `cd /path/to/my/source/dir/abinit-7.4.1`
  * `make distclean`
  * `cd ..`
  * `mv abinit-7.4.1 abinit-7.4.1-lesson`
  * `tar xvzf /path/to/abinit/tarball/abinit-7.4.1.tar.gz`
  * `mv abinit-7.4.1 abinit-7.4.1-orig`
  * `diff -urN abinit-7.4.1-orig abinit-7.4.1-lesson > abinit-7.4.1-lesson.patch`
  * `gzip --best abinit-7.4.1-lesson.patch`

_Note: in case you are using Bazaar, you will have to exclude the '.bzr*'
files from the diff by adding "`-x '.bzr*'`" to the other options._



