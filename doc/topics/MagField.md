---
authors: EB
description: MagField Abinit topic
rpath: /topics/MagField.md
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to take into account an external magnetic field with the ABINIT package.

## Introduction

An applied external magnetic field has been implemented in ABINIT by
considering the Zeeman spin response only (i.e., neglecting the orbital
contribution).

Following the procedure of Bousquet et al.,[[Bousquet2011]] the applied **B**
field is introduced by adding the "Zeeman term" term in the non-collinear
Kohn-Sham potential:

This contribution is trivial to implement, and also dominant in amplitude, but
has historically been neglected with respect to the orbital responses, which
are rich in more complex physics.

Unlike an applied electric field, such a Zeeman term in the potential is
compatible with periodic boundary conditions. It is also compatible with
collinear calculations by reducing its application on ``up'' and ``down'' spin
channels with **B**=B**e**z.

In ABINIT, the finite Zeeman field is controlled by the keyword
[[zeemanfield]] which allows to control the amplitude of the applied
**B**-field (in Tesla) along the three cartesian directions.

Such an applied Zeeman field allows one to calculate the spin contribution of
the magnetic and magnetoelectric susceptibilities, and to observe phase
transitions under finite magnetic field, if present.



## Related Input Variables

*basic:*

- [[abinit:zeemanfield]]  ZEEMAN FIELD
 
*expert:*

- [[abinit:bfield]]  finite B FIELD calculation
- [[abinit:nucdipmom]]  NUClear DIPole MOMents
 

## Selected Input Files

*v6:*

- [[tests/v6/Input/t17.in]]
 
*v7:*

- [[tests/v7/Input/t32.in]]
 
