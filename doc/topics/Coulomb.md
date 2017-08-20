---
authors: FB
---

## ** Introduction **

ABINIT can treat charged systems (e.g. either for molecules, or for dopants in
a supercell), using the [[charge]] input variable. A careful convergence study
with respect to the cell size must however be done.

Depending on the dimension, different treatment of the Coulomb interaction can
be enforced, governed by [[icoulomb]] for grouns-state calculations, and by
[[icutcoul]] for GW calculations. Some development effort is needed in ABINIT
to rationalize the situation.

Additional information concerning [[usepotzero]]. It is well known that the
electrostatic potential (arising from ion-ion, ion-electron, and electron-
electron interactions) is ill-defined within periodic boundary conditions.
However, it is less well known that the total energy of a charged cell is also
ill-defined. In fact, after a careful derivation in [[Bruneval2014]], it was
shown that the above two statements are tightly linked: when the number of
electrons differs from the number of protons in a cell, the necessary
compensating background that enforces the overall charge neutrality is
sensitive to the arbitrary average electrostatic potential.

ABINIT offers the possibility to choose which convention to use for the
average electrostatic potential with the keyword [[usepotzero]].

In PAW, one can choose among 3 options:

* the average of smooth electrostatic potential is set to zero;
* the average of all-electron electrostatic potential is set to zero;
* the average of smooth electrostatic potential is set to a finite value, which follows the Quantum Espresso implementation (see [[Giannozzi2009]] for more details).

Only options 1 and 3 are valid for the NCPP case.

None of these conventions is intrinsically more correct than the other ones.
This is just an arbitrary choice, but ABINIT now permits a straight comparison
to the other codes.



## ** Related Input Variables **

*basic:*

- [[abinit:charge]]  CHARGE
 
*expert:*

- [[abinit:nscforder]]  Nth - SCaling Function ORDER
 
*useful:*

- [[abinit:icoulomb]]  Index for the Coulomb TReaTMenT
- [[abinit:icutcoul]]  Integer that governs the CUT-off for COULomb interaction
- [[abinit:usepotzero]]  USE POTential ZERO
 

## ** Selected Input Files **

*v7:*

- [[tests/v7/Input/t26.in]]
 

