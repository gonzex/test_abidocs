---
authors: JZ
---

## ** Introduction **

The effect of an homogeneous static electric field on an insulator may be
treated in ABINIT from two perspectives. One is perturbative, and yields the
susceptibility in the form of the second derivative of the total energy with
respect to the electric field, at zero field strength (see [[topic:DFPT]]).

ABINIT can also be used to compute the effect of an electric field of finite
amplitude, using techniques from the Modern Theory of Polarization
[[Resta1994]],[[Nunes2001]],[[Souza2002]]. The latter is based on the notion
of "Berry phase". In this approach, the total energy to minimize includes the
contribution due to the interaction of the external electric field with the
material polarization **P**Tot, as follows:

E = E0 \- Ω**P**Tot**.E**, where E0 is the usual ground state energy obtained
from Kohn-Sham DFT in the absence of the external field **E**, **P**Tot is the
polarization, made up of an ionic contribution and an electronic contribution,
and Ω the volume of the unit cell.

Some details of the implementation of The Modern Theory of Polarization in
ABINIT are given in [[Gonze2016|the 2016 ABINIT publication]].

In the NCPP case, the electric field has no additional contribution to the
Hellmann-Feynman forces, because the electronic states do not depend
explicitly on ionic position [[Souza2002]]. In the PAW case however, as the
projectors do depend on ion location, an additional force and additional
stresses terms arise [[Zwanziger2012]].

The generalisation to fixed D-field or fixed reduced fields are also
available, as described in M. Stengel, N.A. Spaldin and D. Vanderbilt, Nat.
Phys. 5,304 (2009).

The polarization and finite electric field calculation in ABINIT is accessed
through the variables [[berryopt]] and [[efield]]. In addition, displacement
fields and mixed boundary conditions (a mix of electric field and displacement
field) can be computed as well.



## ** Related Input Variables **

*basic:*

- [[abinit:bdberry]]  BanD limits for BERRY phase
- [[abinit:dfield]]  Displacement FIELD
- [[abinit:efield]]  Electric FIELD
- [[abinit:jfielddir]]  electric/displacement FIELD DIRection
- [[abinit:kberry]]  K wavevectors for BERRY phase computation
- [[abinit:nberry]]  Number of BERRY phase computations
 
*compulsory:*

- [[abinit:berryopt]]  BERRY phase OPTions
 
*expert:*

- [[abinit:berrystep]]  BERRY phase : multiple STEP
 
*useful:*

- [[abinit:berrysav]]  BERRY SAVe
- [[abinit:ddamp]]  electric Displacement field DAMPing parameter
- [[abinit:maxestep]]  MAXimum Electric field STEP
- [[abinit:polcen]]  POLarization for CENtrosymmetric geometry
- [[abinit:red_dfield]]  REDuced Displacement FIELD
- [[abinit:red_efield]]  REDuced Electric FIELD
- [[abinit:red_efieldbar]]  REDuced Electric FIELD BAR
 

## ** Selected Input Files **

*paral:*

- [[tests/paral/Input/t07.in]]
 
*v4:*

- [[tests/v4/Input/t66.in]]
- [[tests/v4/Input/t72.in]]
- [[tests/v4/Input/t75.in]]
 
*v5:*

- [[tests/v5/Input/t23.in]]
 
*v6:*

- [[tests/v6/Input/t43.in]]
 
*v7:*

- [[tests/v7/Input/t03.in]]
 

