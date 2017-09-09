---
authors: GG
rpath: topics/MolecularDynamics.md
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to perform a molecular dynamics calculation with the ABINIT package.

## Introduction

Three molecular dynamics algorithm (Numerov, Verlet, Blanes and Moanes) allow
to perform simulations in real (simulated) time, see [[ionmov]]. The
displacement of atoms may be computed according to Newton's law, or by adding
a friction force to it. Nose-Hoover thermostat is available with Verlet
algorithm. Langevin dynamics is also available.

Specified lattice parameters, or angles, or atomic positions, can be kept
fixed if needed, see [[topic_GeoConstraints]].

The trajectories can be analyzed thanks to the [[topic:APPA|APPA
postprocessor]].



## Related Input Variables

*basic:*

- [[abinit:nnos]]  Number of NOSe masses
- [[abinit:ntime]]  Number of TIME steps
- [[abinit:qmass]]  Q thermostat MASS
- [[abinit:vel]]  VELocity
- [[abinit:vis]]  VIScosity
 
*compulsory:*

- [[abinit:dtion]]  Delta Time for IONs
- [[abinit:ionmov]]  IONic MOVEs
- [[abinit:mdtemp]]  Molecular Dynamics TEMPeratures
 
*expert:*

- [[abinit:bmass]]  Barostat MASS
- [[abinit:delayperm]]  DELAY between trials to PERMUTE atoms
- [[abinit:densfor_pred]]  DENSity and FORces PREDictor
- [[abinit:diismemory]]  Direct Inversion in the Iterative Subspace MEMORY
- [[abinit:extrapwf]]  flag - EXTRAPolation of the Wave-Functions
- [[abinit:mdwall]]  Molecular Dynamics WALL location
- [[abinit:signperm]]  SIGN of PERMutation potential
 
*useful:*

- [[abinit:friction]]  internal FRICTION coefficient
- [[abinit:nctime]]  NetCdf TIME between output of molecular dynamics informations
- [[abinit:noseinert]]  NOSE thermostat INERTia factor
- [[abinit:restartxf]]  RESTART from (X,F) history
 

## Selected Input Files

*fast:*

- [[tests/fast/Input/t21.in]]
- [[tests/fast/Input/t29.in]]
 
*mpiio:*

- [[tests/mpiio/Input/t21.in]]
- [[tests/mpiio/Input/t22.in]]
 
*paral:*

- [[tests/paral/Input/t21.in]]
- [[tests/paral/Input/t22.in]]
 
*v2:*

- [[tests/v2/Input/t88.in]]
 
*v3:*

- [[tests/v3/Input/t40.in]]
 
*v5:*

- [[tests/v5/Input/t01.in]]
- [[tests/v5/Input/t03.in]]
 
*v8:*

- [[tests/v8/Input/t12.in]]
 

## Tutorials

* [Parallelism for molecular dynamics calculations](../../tutorial/generated_files/lesson_paral_moldyn.html)
