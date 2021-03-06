---
authors: XG
description: 'Artificial Abinit topic'
rpath: '/topics/Artificial.md'
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to perform some artificial modifications of the physics with the ABINIT package.

## Introduction

With a computer, one can consider non-physical modifications of the system to
help the understanding the physics ...

The nuclear masses and free electron mass can be modified. A fake space
dependent chemical potenial can be added, see [[chempot]], as well as the
electrostatic potential of a slab, [[jellslab]]. A simple sine/cosine
potential with a wavevector compatible with the (super)call can also be added,
see [[qprtrb]].



## Related Input Variables

*basic:*

- [[abinit:amu]]  Atomic Mass Units
 
*expert:*

- [[abinit:chempot]]  spatially varying CHEMical POTential
- [[abinit:effmass_free]]  EFFective MASS for the FREE electron
- [[abinit:jellslab]]  include a JELLium SLAB in the cell
- [[abinit:nzchempot]]  Number of Z reduced coordinates that define the spatial CHEMical POTential
- [[abinit:slabwsrad]]  jellium SLAB Wigner-Seitz RADius
- [[abinit:slabzbeg]]  jellium SLAB BEGinning edge along the Z direction
- [[abinit:slabzend]]  jellium SLAB ENDing edge along the Z direction
 
*useful:*

- [[abinit:qprtrb]]  Q-wavevector of the PERTurbation
- [[abinit:vprtrb]]  potential -V- for the PeRTuRBation
 

## Selected Input Files

*v1:*

- [[tests/v1/Input/t25.in]]
 

