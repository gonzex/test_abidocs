---
authors: BAmadon
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to calculate the effective Coulomb interaction with the ABINIT package.

## Introduction

LDA+U as well as DFT+DMFT requires as input values the effective Coulomb
interaction. Two ways to compute them are available in ABINIT.

Firstly, the constrained Random Phase Approximation [[Aryasetiawan2004]]
[[ucrpa]] allows one to take into account the screening of the Coulomb
interaction between correlated electrons, by non-interacting electrons. For
non-entangled bands ([[ucrpa]]= 1), the bands excluded from the polarisability
can be specified either by a band index ([[ucrpa_bands]]) or an energy window
([[ucrpa_window]]) [[Amadon2014]].

For entangled bands ([[ucrpa]]= 2}), the scheme used in ABINIT
[[Shih2012]],[[Sakuma2013]],[[Amadon2014]] uses a band and k-point dependent
weight to define the polarisability, using Wannier orbitals as correlated
orbitals.

This method is well adapted to compute the effective interaction for the same
orbitals used in DFT+DMFT. To use the same orbitals as in DFT+U, the Wannier
functions should be defined with a very large energy window
[[Amadon2014]],[[Amadon2012]].

Secondly, a linear response method [[Cococcioni2005]] is implemented. The
implementation is not yet in production. The implementation in ABINIT takes
into account the truncated atomic orbitals from PAW and therefore differs from
the original work [[Cococcioni2005]] treating full atomic orbitals. In
particular, considerably higher effective values for U are found.



## Related Input Variables

*basic:*

- [[abinit:ucrpa_bands]]  For the calculation of U with the Constrained RPA method, gives correlated BANDS
- [[abinit:ucrpa_window]]  For the calculation of U with the Constrained RPA method, gives energy WINDOW
 
*compulsory:*

- [[abinit:ucrpa]]  calculation of the screened interaction U with the Constrained RPA method
 

## Selected Input Files

*v7:*

- [[tests/v7/Input/t23.in]]
- [[tests/v7/Input/t24.in]]
- [[tests/v7/Input/t25.in]]
- [[tests/v7/Input/t78.in]]
- [[tests/v7/Input/t79.in]]
 

## Tutorials

* [The lesson on the calculation of effective interactions U and J by the cRPA method](../../tutorial/generated_files/lesson_ucalc_crpa.html) shows how to determine the U value with the constrained Random Phase Approximation [[Aryasetiawan2004]] using projected Wannier orbitals. Prerequisite : DFT+U.
* [The lesson on the determination of U for DFT+U](../../tutorial/generated_files/lesson_udet.html) shows how to determine the U value with the linear response method [[Cococcioni2005]], to be used in the DFT+U approach. Prerequisite : DFT+U.
