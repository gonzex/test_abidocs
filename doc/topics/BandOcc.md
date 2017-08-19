---
authors: FJ
---
  
Metallic as well as insulating systems can be treated, depending on the value
of [[occopt]]. The default value of [[occopt]] corresponds to an insulator (or
finite molecule): the number of bands (or states for a molecule) is deduced
from the number of electrons brought by each pseudopotential ion, and then all
the bands are occupied (by two electrons in case of a non-spin-polarized
system, or by 1 electron in the cas of a spin-polarized system), and a small
number of empty bands are added, e.g. to obtain the band gap.

For a metallic system, use a value of [[occopt]] between 3 and 7. ABINIT will
compute a default number of bands, including some nearly unoccupied ones, and
find the occupation numbers. The different values of [[occopt]] correspond to
different smearing schemes (smearning defined by [[tsmear]] for defining the
occupation numbers, e.g. Fermi broadening, the Gaussian broadening, the
Gaussian-Hermite broadening, as well as the modifications proposed by Marzari.
Finite temperatures can also be treated thanks to a smearing scheme
(Verstraete scheme) using [[tphysel]].

It is possible to define manually the number of bands (input variable
[[nband]]) as well as the occupation numbers (input variable [[occ]]). This
might be useful to perform a Δ-SCF calculation for excited states.

