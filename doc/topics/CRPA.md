---
authors: BAmadon
---
LDA+U as well as DFT+DMFT requires as input values the effective Coulomb
interaction. Two ways to compute them are available in ABINIT.

Firstly, the constrained Random Phase Approximation [[Aryasetiawan2004]]
[[ucrpa]] allows one to take into account the screening of the Coulomb
interaction between correlated electrons, by non-interacting electrons. For
non-entangled bands ([[ucrpa]]= 1), the bands excluded from the polarisability
can be specified either by a band index ([[ucrpa_bands]]) or an energy window
([[ucrpa_window]]) [[Amadon2014]].

For entangled bands ([[ucrpa]]= 2}), the scheme used in ABINIT
[[Shih2012]],[[Sakuma2013]],[[Amadon2014]] uses a band and k-point dependent
weight to define the polarisability, using Wannier orbitals as correlated
orbitals.

This method is well adapted to compute the effective interaction for the same
orbitals used in DFT+DMFT. To use the same orbitals as in DFT+U, the Wannier
functions should be defined with a very large energy window
[[Amadon2014]],[[Amadon2012]].

Secondly, a linear response method [[Cococcioni2005]] is implemented. The
implementation is not yet in production. The implementation in ABINIT takes
into account the truncated atomic orbitals from PAW and therefore differs from
the original work [[Cococcioni2005]] treating full atomic orbitals. In
particular, considerably higher effective values for U are found.

