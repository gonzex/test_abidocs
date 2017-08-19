---
authors: FJ
---
Sometimes, the user knows the space group of the system, the conventional cell
vectors, as well as the positions of atoms in the asymmetric (irreducible)
part of the cell. From such data, ABINIT can generate the usual primitive cell
vectors, as well as the coordinates of all the atoms in this cell.

This is activated if [[spgroup]]!=0 and [[brvltt]]=-1. The user needs to
specify the number of atoms to be read [[natrd]] in the asymmetric part of the
cell, as well as the expected number of atoms [[natom]] in the primitive cell.
Some additional information on the axes orientation [[spgaxor]] and the cell
origin [[spgorig]] might also have to be given. See [the space group help
file](../../users/spacegrouphelpfile.html).

The specification of a magnetic space group is even possible
(antiferromagnetic). See [[spgroupma]] and [[genafm]].

See also the [[topic_UnitCell]].

