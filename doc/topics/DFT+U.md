---
authors: BAmadon
---
This feature is available only in PAW. The DFT+U framework is described in
[[Anisimov1991]] and [[Liechtenstein1995]]. In ABINIT, the DFT+U approximation
is implemented inside the PAW atomic spheres only. Two choices of double
counting are provided: the Full Localized limit and the Around Mean Field
approximation. Our implementation is described in [[Amadon2008a]]. It follows
the main lines of [[Bengone2000]]. See als [[Czyzyk1994]]. Forces and stress
are implemented. For details on keywords
([[lpawu]],[[upawu]],[[jpawu]],[[usedmatpu]],[[dmatpuopt]],[[dmatudiag]]) see
keyword [[usepawu]] in input variables.

In both the output and log files, we can find:

\- The DFT+U contribution of energy which is contained inside the PAW
Spherical terms in the output file.

\- The Decomposition of the LDA+U energy is given (Interaction energy, Double
counting term, and sum of the two) in the log file.

\- The orbital density matrix (n_{m,m'}^{\sigma}), also called occupation
matrix (corresponding to Eq.(9) of [[Bengone2000]] and Eq.(1) of
[[Liechtenstein1995]], see also [5] and variable [[dmatpuopt]]) is also given
for each atom in the basis of real spherical harmonics. It is given at each
SCF step in the log file: one can thus check the convergency of the
calculation.

Consistency between total energy and forces in DFT+U have been checked.

