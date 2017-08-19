---
authors: MT
---
The computation of the second-order derivative of the total energy with
respect to atomic displacements at an arbitrary wavevector, using
[[topic:DFPT]], opens the possibility to compute the dynamical matrix at that
wavevector, and hence, to compute the phonon eigenfrequency and
eigendisplacements. When the wavevector is (0,0,0), usually denoted as the
Gamma point, the combination of the atomic displacements and electric field
type perturbations opens also the access to Born effective charges, electronic
(for frequencies lower than the electronic band gap) dielectric constants, and
then, to infra-red reflectivity of materials (in the infinite lifetime
approximation). See [[Gonze1997a]] for the presentation of the theory with
DFPT.

In ABINIT, with one dataset for a fixed wavevector (see [[topic_q-points]]),
one can compute all such second-order derivatives. ABINIT will already perform
some post-processing treatment of the second-order derivatives (e.g.
computation of the dynamical matrix, and corresponding eigenenergies and
eigendisplacements), although the most extended post-processing treatment is
provided by ANADDB. Thus, there is some overlap of the two executables, with
some common input variables. Usually, the action of an input variable with the
same name in the two executables is very similar, although there are some
input variables that govern more options in ANADDB then in ABINIT, because of
the previously mentioned difference in capabilities. In the database of input
variables, the input variables related to ABINIT or ANADDB are clearly
distinguished.

The band-by-band decomposition of the Born effective charge tensors can be
computed thanks to [[prtbbb]]. The related localization tensor (see
[[Veithen2002]] can also be computed.

Phonon calculations are arbitrary q-points can be done under finite electric
field ([[topic_Berry]]).

It will be the easiest to discover the capabilities of these two executables
through the [[lesson_rf1]] of the tutorial.

See [[topic_DFPT]] for the general information about DFPT, [[topic_q-points]]
for the specification of q-points, and [[topic_PhononBands]] for the
computation of full phonon bands.

