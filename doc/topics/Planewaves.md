---
authors: FJ
---
The numerical precision of the calculations depends on many settings, among
which the definition of a basis set is likely the most important. With
planewaves, there is one single parameter, [[ecut]] that governs the
completeness of the basis set.

The wavefunction, density, potentials are represented in both reciprocal space
(plane waves) and real space, on a homogeneous grid of points. The
transformation from reciprocal space to real space and vice-versa is made
thanks to the Fast Fourier Transform (FFT) algorithm. With norm-conserving
pseudopotential, [[ecut]] is also the main parameter to define the real space
FFT grid, In PAW, the sampling for such quantities is governed by a more
independent variable, [[pawecutdg]]. More precise tuning might be done by
using [[boxcutmin]] and [[ngfft]].

Avoiding discontinuity issues with changing the size of the planewave basis
set is made possible thanks to [[ecutsm]].

The [[accuracy]] variable enables to tune the accuracy of a calculation by
setting automatically up to seventeen variables.

Many more parameters govern a PAW computation than a norm-conserving
pseudopotential calculation. They are described in a specific page
[[topic_PAW]]. For the settings related to wavelets, see [[topic:Wavelets]].

