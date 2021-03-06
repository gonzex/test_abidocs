---
authors: FJ
description: 'GSintroduction Abinit topic'
rpath: '/topics/GSintroduction.md'
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to build an input file for a ground state calculation with the ABINIT package.

## Introduction

The computation of the ground state energy of an assembly of nuclei and
electrons placed in a repeated cell can be done using (1) plane waves and
norm-conserving pseudopotentials, or, (2) so-called "Projector-Augmented
Waves" (PAW method), with appropriate pseudoatomic data, or (3) wavelets. The
wavelet framework is described [here](topic_Wavelets.html).  
In the plane wave framework, the program admits many different types of
pseudopotentials. There are several complete sets of norm-conserving
pseudopotentials available for most elements of the periodic table. The
recommended one (GGA) comes from the ONCVPSP generator (with spin-orbit
coupling). For PAW calculation,the recommended one (GGA and LDA) is the JTH
table in the PAW XML format. The choice between norm-conserving
pseudopotentials or PAW is deduced automatically by the choice of the
pseudopotential in the "files" file. An input file must specify the following
items:

  
\- the [crystalline structure and symmetries](topic_crystal.html).  
\- the set of [k-points](topic_k-points.html) used.  
\- the [exchange and correlation ](topic_xc.html) functional.  
\- [convergency settings ](topic_convergency.html).  
\- possibly, [PAW](topic_PAW.html) special settings.  
\- possibly, input variables for [ spin-polarized systems and spin orbit
coupling](topic_spinpolarisation.html) calculations.



## Related Input Variables

No variable associated to this topic.

## Selected Input Files

No input file associated to this topic.

## Tutorials

* [The lesson 1](../../tutorial/generated_files/lesson_base1.html) deals with the H2 molecule : get the total energy, the electronic energies, the charge density, the bond length, the atomisation energy 
* [The lesson 2](../../tutorial/generated_files/lesson_base2.html) deals again with the H2 molecule: convergence studies, LDA versus GGA 
* [The lesson 3](../../tutorial/generated_files/lesson_base3.html) deals with crystalline silicon (an insulator): the definition of a k-point grid, the smearing of the cut-off energy, the computation of a band structure, and again, convergence studies ...
* [The lesson 4](../../tutorial/generated_files/lesson_base4.html) deals with crystalline aluminum (a metal), and its surface: occupation numbers, smearing the Fermi-Dirac distribution, the surface energy, and again, convergence studies ...

