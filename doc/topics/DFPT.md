---
authors: MT
---
Density-Functional Perturbation Theory (DFPT) allows one to address a large
variety of physical observables. Many properties of interest can be computed
directly from the derivatives of the energy, without the use of finite
differences: phonons modes, elastic tensors, effective charges, dielectric
tensors, etc... Even non-linear properties can be computed, like the Raman
intensities (for the latter, see [[topic_nonlinear]])..

A DFPT calculation workflow is conducted as follows:

* Run a Ground-State calculation in order to extract the Kohn-Sham pseudo wave-functions; these must be extremely well converged.
* If necessary, e.g., for the application of the derivative of the Hamiltonian with respect to an electric field, determine the derivatives of the wave functions with respect to the wave vector **k**, and keep them in a file. The keyword [[rfddk]] is used to perform this type of calculation.
* Compute the 2nd-order derivative matrix (i.e., 2nd derivatives of the energy with respect to different perturbations λ). This can be done thanks to the keywords [[rfphon]] (λ=atomic displacement), [[rfstrs]] (λ=strain), [[rfelfd]] (λ=electric field) or [[rfmagn]] (λ=magnetic field). 
* Launch the anaddb tool (distributed with ABINIT) to analyse the derivative database and compute relaxed tensors and thermodynamical properties.

Note that for PAW calculation, when performing the post-processing with
anaddb, it is recommended to include all the keywords enforcing the sum rules
(acoustic sum and charge neutrality). Indeed the PAW formalism involves, for
each atom, the calculation of a large number of real space integrals, whose
numerical effect may be to break the translational invariance.

Thanks to the locality provided by PAW partial wave basis, it is possible to
perform response function calculations for correlated electron materials. The
LDA+U formalism is usable without any restriction for the PAW+DFPT
calculations.

All the tutorials dedicated to response functions can be followed both with
norm-conserving pseudopotentials and with PAW atomic datasets.

More detailed explanations to perform a response calculation are given in the
[help_respfn ](../../users/generated_files/help_respfn.html)file.

