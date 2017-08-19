---
authors: FJ
---
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

