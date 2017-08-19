---
authors: FJ
---
ABINIT has some (non-graphical) capabilities to manipulate atoms and group of
atoms, to help establishing the set of atomic positions in the input file when
big cells are considered.

Explicitly, one or two groups of atoms, forming e.g. a molecule, a cluster, or
a small primitive cell, can be repeated in arbitrary number, then translated
and rotated. Then, atoms can be removed, to form e.g. vacancies. See [[nobj]]
as entry point.

The related input variables being used for preprocessing of the input file,
they are not echoed in the output file ([[NO_INTERNAL]] characteristics).

