---
authors: MG
---
DFT performs reasonably well for the determination of structural properties,
but fails to predict accurate band gaps. A more rigorous framework for the
description of excited states is provided by many-body perturbation theory
(MBPT) [[Fetter1971]],[[Abrikosov1975]], based on the Green's functions
formalism and the concept of quasi-particles [[Onida2002]].

Within MBPT, one can calculate the quasi-particle (QP) energies, E, and
amplitudes, Ψ, by solving a nonlinear equation involving the non-Hermitian,
nonlocal and frequency dependent self-energy operator Σ.

This equation goes beyond the mean-field approximation of independent KS
particles as it accounts for the dynamic many-body effects in the electron-
electron interaction.

Details about the GW implementation in ABINIT can be found
[here](../../theory/generated_files/theorydoc_mbt.html).

A typical GW calculation consists of two different steps (following a DFT
calculation): first the screened interaction ε-1 is calculated and stored on
disk ([[optdriver]]=3), then the KS band structure and W are used to evaluate
the matrix elements of Σ, finally obtaining the QP corrections
([[optdriver]]=4).

The computation of the screened interaction is described in
[[topic_Susceptibility]], while the computation of the self-energy is
described in [[topic_SelfEnergy]]. The frequency meshes, used e.g. for
integration along the real and imaginary axes are described in
[[topic_FrequencyMeshMBPT]].

