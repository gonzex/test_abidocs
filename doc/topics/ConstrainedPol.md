---
authors: MT
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to optimize the geometry under constrained polarization with the ABINIT package.

## Introduction

Compute polarization in cartesian coordinates, and update lattice constants
and atomic positions in order to perform a structural optimization at
constrained polarization, following the formalism described in Na Sai et al,
PRB 66, 104108 (2002). More details in [[anaddb:polflag]]. The geometry
optimization is done in ANADDB.



## Related Input Variables

*compulsory:*

- [[anaddb:polflag]]  POLarization FLAG
 
*useful:*

- [[anaddb:iatfix]]  Indices of the AToms that are FIXed
- [[anaddb:istrfix]]  Index of STRain FIXed
- [[anaddb:natfix]]  Number of AToms FIXed
- [[anaddb:nstrfix]]  Number of STRain components FIXed
- [[anaddb:relaxat]]  RELAXation of AToms
- [[anaddb:relaxstr]]  RELAXation of STRain
- [[anaddb:targetpol]]  TARGET POLarization
 

## Selected Input Files

*v4:*

- [[tests/v4/Input/t71.in]]
- [[tests/v4/Input/t74.in]]
- [[tests/v4/Input/t77.in]]
 
