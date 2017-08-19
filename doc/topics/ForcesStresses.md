---
authors: FJ
---
Hellman-Feynman forces are computed from an analytical formula, and
corresponds exactly to the limit of finite differences of energy for
infinitesimally small atomic displacements when the ground-state calculation
is at convergence. This feature is available for all the cases where the total
energy can be computed. A correction for non-converged cases allows to get
accurate forces with less converged wavefunctions than without it. The
decomposition of the forces in their different components can be provided.

Stress can also be computed. This feature is available for all the cases where
the total energy can be computed (except wavelets). The decomposition of the
stresses in their different components can be provided. A smearing scheme
applied to the kinetic energy [[ecutsm]] allows one to get smooth energy
curves as a function of lattice parameters and angles. A target stress can be
given by the user ([[strtarget]]), the geometry optimization algorithm will
try to find the primitive cell and atomic positions that deliver that target
stress.

The computation of forces and stresses is optional, see [[optforces]] and
[[optstress]]. They are used to define SCF stopping criteria ([[toldff]],
[[tolrff]]) or geometry optimization stopping criteria ([[tolmxf]]). For the
geometry optimization, combined cell shape and atomic position optimization
need a conversion scale, set by [[strprecon]].

