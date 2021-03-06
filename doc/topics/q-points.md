---
authors: FJ
description: 'q-points Abinit topic'
rpath: '/topics/q-points.md'
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to set parameters related to the phonon wavevectors (q-points) in DFPT
calculations with the ABINIT package.

## Introduction

Like the electronic wavefunctions, the collective atomic displacements that
are eigenmodes of the corresponding periodic Hamiltonian can be characterized
by a wavevector, denoted q-point.

In ABINIT, DFPT calculations for one dataset are done for one specific
q-point, that must be specified. In the simplest case, the user gives the
corresponding q-point for each dataset, setting [[nqpt]]=1 and specifying the
corresponding single [[qpt]]. However, very often, it is needed to run
calculations for dozens or hundreds of q-points. Hence, the following
mechanism has been set: the use can specify a set of q points, using input
variables similar to the k-points, and then, for each dataset, the number of
the q-point in the set is indicated thanks to [[iqpt]]. This applies to the
generation of q-point grids as well as to q-point paths to produce phonon band
structures.

The input variables for specifying q-points in ANADDB are specified in
[[topic_Phonons]] and [[topic_PhononBands]].



## Related Input Variables

*basic:*

- [[abinit:iqpt]]  Index for QPoinT generation
- [[abinit:ngqpt]]  Number of Grid pointsfor Q PoinTs generation
- [[abinit:nqpt]]  Number of Q - POINTs
- [[abinit:qptopt]]  QPoinTs OPTion
 
*useful:*

- [[abinit:nshiftq]]  Number of SHIFTs for Q point grids
- [[abinit:ph_intmeth]]  PHonons: INTegration METHod
- [[abinit:ph_ndivsm]]  PHonons: Number of DIVisions for sampling the SMallest segment
- [[abinit:ph_ngqpt]]  PHonons: Number of Grid points for Q-PoinT mesh.
- [[abinit:ph_nqpath]]  PHonons: Number of Q-points defining the PATH
- [[abinit:ph_nqshift]]  PHonons: Number of Q-SHIFTs
- [[abinit:ph_qpath]]  Phonons: Q-PATH
- [[abinit:ph_qshift]]  PHonons: Q-SHIFTs for mesh.
- [[abinit:ph_smear]]  PHonons: SMEARing factor
- [[abinit:ph_wstep]]  PHonons: frequency(W)  STEP.
- [[abinit:qpt]]  Q PoinT
- [[abinit:qptnrm]]  Q PoinTs NoRMalization
- [[abinit:qptrlatt]]  Q - PoinTs grid : Real space LATTice
- [[abinit:shiftq]]  SHIFT for Q points
- [[abinit:wtq]]  WeighTs for the current Q-points
 

## Selected Input Files

No input file associated to this topic.

