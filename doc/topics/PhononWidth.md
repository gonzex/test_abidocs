---
authors: MV
---
This topic concerns metals only.

After generating a GKK file (see [[topic_ElPhonInt]]), the Electron-Phonon
Coupling (EPC) analysis is performed in anaddb, setting [[anaddb:elphflag]]
variable to 1. Most of the procedure is automatic, but can be lengthy if a
large number of k-points is being used. The [[anaddb:nqpath]] and
[[anaddb:qpath]] variables must be set, specifying a path in reciprocal space.
anaddb generates files containing the phonon linewidths (suffixed _LWD) and
frequencies ωqj (suffixed _BST) along [[anaddb:qpath]]. One can calculate the
nesting function n(q) = ∑kii' δ(εk,i) δ(εk+q,i') by setting [[anaddb:prtnest]]
to 1 (output to _NEST).

