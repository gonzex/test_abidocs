---
authors: FJ
---

## ** Introduction **

In addition to the [[topic:UnitCell|Specification of the unit cell]] and
[[topic:AtomTypes|Atom types]], ABINIT must know the number of atoms inside
the cell, their type, and position. This is described by [[natom]], [[typat]]
and one of [[xred]], [[xcart]] and [[xangst]].

ABINIT can automatically detect the Bravais lattice and space group, and
generate symmetries (e.g. [[nsym]],[[symrel]],[[tnons]]), from the primitive
cell and the position of atoms (provided they are not too inaccurate, see
[[tolsym]]). For this purpose, in the magnetic case, ABINIT will also take
into account the input atomic spin, through the knowledge of [[spinat]].

Alternatively, ABINIT can start from the specification of symmetries (either
from [[spgroup]] or from the list of symmetries -
[[nsym]],[[symrel]],[[tnons]]) and generate the atomic positions from the
asymmetric (irreducible) part of the primitive cell. This is described in the
[[topic:SmartSymm|Smart Symmetrizer]] topic.

ABINIT can treat antiferromagnetic symmetry operations, see [[symafm]].

In ABINIT, a database with the 230 spatial groups of symmetry (see
[[spgroup]]) and the 1191 Shubnikov anti-ferromagnetic space groups is present
(see also [[spgroupma]] and [[genafm]]).

There is also a (non-graphical) atom manipulator in ABINIT, see
[[topic:AtomManipulator]].

ABINIT can read XYZ files, see [[xyzfile]].

Atomic positions can also be generated at random, see [[random_atpos]].

Details about the way the crystal structure is defined in ABINIT can be found
[here](../documents/geometry.pdf).



## ** Related Input Variables **

*basic:*

- [[abinit:natom]]  Number of ATOMs
- [[abinit:ntypat]]  Number of TYPes of AToms
- [[abinit:typat]]  TYPe of AToms
 
*compulsory:*

- [[abinit:xangst]]  vectors (X) of atom positions in cartesian coordinates -length in ANGSTrom-
- [[abinit:xcart]]  vectors (X) of atom positions in CARTesian coordinates
- [[abinit:xred]]  vectors (X) of atom positions in REDuced coordinates
 
*expert:*

- [[abinit:maxnsym]]  MAXimum Number of SYMetries
- [[abinit:random_atpos]]  RANDOM ATomic POSitions
- [[abinit:symmorphi]]  SYMMORPHIc symmetry operation selection
 
*useful:*

- [[abinit:chkprim]]  CHecK whether the cell is PRIMitive
- [[abinit:nsym]]  Number of SYMmetry operations
- [[abinit:spgroup]]  SPace GROUP number
- [[abinit:spinat]]  SPIN for AToms
- [[abinit:symrel]]  SYMmetry in REaL space
- [[abinit:tnons]]  Translation NON-Symmorphic vectors
- [[abinit:tolsym]]  TOLERANCE for SYMmetries
- [[abinit:xyzfile]]  XYZ FILE input for geometry
 

## ** Selected Input Files **

*v3:*

- [[tests/v3/Input/t21.in]]
- [[tests/v3/Input/t23.in]]
- [[tests/v3/Input/t39.in]]
 
*v5:*

- [[tests/v5/Input/t14.in]]
 

