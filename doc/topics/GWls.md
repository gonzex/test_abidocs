---
authors: JL
---
** This functionality is not in production.**

A high performance G0W0 implementation [[Janssen2015]] has been developed
within ABINIT. It is more efficient than the traditional implementation
[[Gonze2009]],[[Giantomassi2011]] thanks to the treatment of the two major
bottlenecks: the summations over conduction states and the inversion of the
dielectric matrix. However, note that this implementation has only limited
applicability at present (see below).

* The first bottleneck is circumvented by converting the summations into Sternheimer equations. Note that the introduction of approximations beyond the G0W0 (such as analytic continuation [[Rieger1999]]) is avoided thanks to use of the simplified quasiminimal residual (SQMR) algorithm [[Freund1995]].
* Then, the second bottleneck is assessed by expressing the dielectric matrix in a Lanczos basis, which reduces the matrix size by orders of magnitude with respect to a plane wave basis.
A model dielectric operator has also been developed [[Janssen2015]] and can
optionally be used to further reduce the dielectric matrix size. The resulting
implementation exhibits a 500-fold speedup for the silane molecule, without
introducing approximations beyond the G0W0 formalism and the pseudopotential
method.

At the time of writing, the implementation supports simulations of molecular
systems only (only one k-point).

Furthermore, it does not supports PAW and spinors.

However, it supports parallelism over bands and FFTs [[Bottin2008]].

To compute G0W0 corrections to DFT eigenenergies, one needs to set
[[optdriver]]= 66 in the input file. This type of calculation requires that
the ground state density and wavefunctions be available from disk (using
[[getden]] and [[getwfk]]). It also requires the user to specify the state to
be corrected ([[gwls_band_index]]), the maximum allowed residual when solving
the Sternheimer equations ([[tolwfr]]), and the number of Lanczos vectors used
to express the dielectric matrix ([[gwls_stern_kmax]]). Note that a
convergence study on the latter value is required to check the accuracy of the
results. Since only molecular systems are currently supported, the calculation
also requires that the Coulomb potential be spherically truncated
([[icutcoul]]= 0) with a radius [[rcut]] that should be validated with a
convergence study.

