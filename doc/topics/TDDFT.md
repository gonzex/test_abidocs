---
authors: FJ
description: 'TDDFT Abinit topic'
rpath: '/topics/TDDFT.md'
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to perform time-dependent density-functional theory calculations of neutral
excitation energies with the ABINIT package.

## Introduction

For finite systems (atoms and molecules), excited states can be computed
within TDDFT (Casida approach - only norm-conserving pseudopotentials). See
the explanations given in the [[lesson:tddft]] lesson of tutorial. The
[[iscf]] input variable must be set to -1.

In the non-spin-polarized case, spin-singlet as well as spin-triplet
excitations are computed. Spin-polarized case is also available.



## Related Input Variables

*basic:*

- [[abinit:boxcenter]]  BOX CENTER
 
*compulsory:*

- [[abinit:iscf]]  Integer for Self-Consistent-Field cycles
 
*useful:*

- [[abinit:ixc]]  Index of eXchange-Correlation functional
- [[abinit:td_maxene]]  Time-Dependent dft : MAXimal kohn-sham ENErgy difference
- [[abinit:td_mexcit]]  Time-Dependent dft : Maximal number of EXCITations
- [[abinit:xclevel]]  eXchange Correlation functional LEVEL
 

## Selected Input Files

*paral:*

- [[tests/paral/Input/t05.in]]
 
*v1:*

- [[tests/v1/Input/t69.in]]
- [[tests/v1/Input/t70.in]]
 
*v2:*

- [[tests/v2/Input/t42.in]]
 
*v3:*

- [[tests/v3/Input/t55.in]]
 
*v5:*

- [[tests/v5/Input/t61.in]]
- [[tests/v5/Input/t62.in]]
 

## Tutorials

* [The lesson on TDDFT](../../tutorial/generated_files/lesson_tddft.html) deals with the computation of the excitation spectrum of finite systems, thanks to the Time-Dependent Density Functional Theory approach, in the Cassida formalism.

