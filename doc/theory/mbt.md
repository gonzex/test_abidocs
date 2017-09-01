---
!!python/object/apply:collections.OrderedDict
-   -   - authors
        - MG, MS
    -   - rpath
        - theory/mbt.md
---

# Many-Body Theory in ABINIT  

##   

The aim of this section is to introduce the Green's function formalism, the
concept of self-energy and the set of coupled equations proposed by Hedin
whose self-consistent solution, in principle, gives the exact Green's function
of the interacting system. We mainly focus on the aspects of the theory that
are important for understanding the different steps of the calculation and the
role played by the input variables used to control the run. A much more
consistent and rigorous introduction to the physical concept of Green's
function and self-energy can be found in any standard textbook on Many-Body
theory, see for example [1,2,3].


## 1 Green's function and self-energy

  
The time-ordered Green's function $G(12)$, also called the propagator, defines
the probability amplitude for the propagation of an added or removed electron
in a many-body system. Since the probability amplitude is simply given by the
overlap between the final and the initial state, $G(12)$ can be expressed as
$$ \begin{equation} G(1,2)=-i\left\langle \Theta_0^N \left| \hat{T} \left[
\hat{\psi}(1)\hat{\psi}^{\dagger}(2) \right] \right| \Theta_0^N \right\rangle,
\end{equation} $$

where the matrix element is taken in the Heisenberg representation, $\hat{T}$
is the time-ordering operator and the creation and annihilation field
operators act on the ground state of the $N$-electron many-body Hamiltonian
(the conventions used in the equations are explained in the section on
[[#notations]]). The propagator contains only part of the full information
carried by the many-body wave function, but it includes the relevant part for
the study of charged excitations. Also, any single-particle operator acting on
the system can be evaluated once the Green's function is known.

Useful physical information about the charged excitation energies of the many-
body system can be obtained by expressing the propagator in the so-called
Lehmann representation [1-2-3]. To this purpose it is useful to introduce the
following notation to denote the charged excitation energies of the
$N$-electron system[5]: $$ \begin{equation} \varepsilon_i = \begin{cases}
E_i^{(N+1)}-E_0^N & \text{if $\varepsilon_i$ > $\mu$} \\\ E_0^N-E_i^{(N-1)} &
\text{if $\varepsilon_i$ < $\mu$} , \end{cases} \end{equation} $$

where _E0N_ is the ground state energy of the electron system with _N_
electrons, and _i_ is the set of quantum numbers labeling the excited states
with _N±_1 electrons. Finally, _μ_ is the chemical potential of the system.
Other important quantities that will be used in the following are the so-
called Lehmann amplitudes defined, in the Schrodinger representation, by

![](../documents/theory_mbt/lehmann_ampl.png)

The Lehmann representation of the Green's function

![](../documents/theory_mbt/Lehmann.png)

makes it clear that, in the frequency domain, the time-ordered Green's
function contains the complete excitation spectrum corresponding to
excitations of an (_N_-1)-particle and an (_N_+1)-particle system. Hence,
locating the poles of the Green's function in the complex plane provides the
information needed to interpret those processes measured in experiments in
which a single electron is inserted to or removed from the system. The figure
below gives a schematic representation of the location of the poles of the
time-ordered Green's function.

![](../documents/theory_mbt/poles_G.png)

Where the ionisation potential is the energy required to remove an electron
from the system, the electron affinity to add an electron, and the chemical
potential is typically taken to be in the middle of the gap. For a metallic
system these energies are all equal to each other, and there is no gap.

The Dyson equation

![](../documents/theory_mbt/G_Dyson.png)

establishes a connection between the fully interacting _G_ and the propagator,
_G0_, of an approximate non-interacting system through a (non-local, non-
Hermitian and time dependent) potential called the self-energy, Σ. Since _G0_
is supposed to be known exactly, the problem of calculating _G_(12) has now
been reduced to the calculation of the self-energy.

The self-energy is not a mere mathematical device used in a roundabout way to
obtain _G_ but is has a direct physical meaning. The knowledge of the self-
energy operator, allows one to describe the quantum-mechanical state of a
renormalized electron in the many-body system by solving the quasiparticle
(QP) equation[5]:

![](../documents/theory_mbt/qp_equation.png)

The QP eigenstates so obtained can be used to construct _G_ according to the
Lehmann representation. Note that the QP equation departs from the Kohn Sham
equation since the QP eigenvectors and eigenvalues do have a direct physical
meaning: they can be used to obtain both the charge density of the interacting
system and to describe the properties of charged excitations.



## 2 Hedin's equations

  
In 1965 Hedin[6] showed how to derive a set of coupled integro-differential
equations whose self-consistent solution, in principle, gives the exact self-
energy of the system and therefore the exact _G_.

The fundamental building blocks employed in the formalism are the irreducible
polarizability:

![](../documents/theory_mbt/tchi_def.png)

which describes the linear response of the density to changes in the total
effective potential (the superposition of the external potential plus the
internal classical Hartree potential) and the dynamically screened
interaction, _W_, that is related to the bare Coulomb interaction, _v_, and to
the inverse dielectric function through:

![](../documents/theory_mbt/W_def.png)

The dielectric matrix є(12) is related to the irreducible polarizability
_χ_(12) by the following relation:

![](../documents/theory_mbt/e_from_tchi.png)

The pentagon sketched in the figure below shows how the various physical
quantities are interrelated:

![](../documents/theory_mbt/hedin_pentagon.png)

The polarization function renormalises the bare interaction resulting in the
screened interaction _W_(12). The screened interaction, _W_(12), the many-body
propagator _G_(12), and the vertex function, Γ(12;3), which describe the
interactions between virtual hole and electron excitations [5], are the
essential ingredients for the determination of Σ(12).

The iteration starts by setting _G_ = _G0_. Then the set of equations should
in principle be iterated until self-consistency in all terms is reached.



## 3 The GW approximation

  
The practical solution of Hedin's equations is extremely complicated as they
are not just numerical relations but contain a functional derivative in the
equation for the vertex. The direct evaluation of the vertex function is very
challenging. The set of equations can, however, be iterated assuming that only
a few iterations are actually needed to obtain physically meaningful results.

A widely used approach to the approximate solution of Hedin's equations is the
so-called _GW_ approximation[6], which consists in approximating the vertex
function with a local and instantaneous function:

![](../documents/theory_mbt/gamma_GW.png)

This approximated vertex, once inserted in the full set of Hedin's equations,
leads to a considerable simplification in the set of equations:

![](../documents/theory_mbt/gw_pentagon.png)

Thanks to the neglect of vertex corrections, the irreducible polarizability
_χ_(12) is now given by

![](../documents/theory_mbt/RPA_chi.png)

which, once rewritten in terms of orbitals and energies, reduces to the RPA
expression proposed by Adler [7] and Wiser [8].

In real space, the self-energy reduces to a simple direct product of the
dressed electron propagator, _G_(12), and the dynamically screened
interaction, _W_(12):

![](../documents/theory_mbt/gwsigma_rt_domain.png)

The self-energy, a simple product in the space-time domain, becomes a
convolution when expressed in frequency-space:

![](../documents/theory_mbt/self_def.png)

Ideally, the set of GW equations should still be iterated until self-
consistency in all terms is reached; this is the fully self-consistent GW
method (SCGW).  However SCGW calculations for real systems are still very
challenging, and very few have been reported in the literature  Moreover, the
utility of fully SCGW results are still under debate within the scientific
community.

The problem is that self-consistency typically improves total energies, but
worsens spectral properties (such as band gaps and optical spectra). Since
obtaining the spectral information is often the main reason for doing such
difficult calculations in the first place, many authors agree that a useful
self-consistent approach would need the inclusion of some kind of vertex
correction during the solution of the equations.

For this reason, the most common approach employed in the _ab initio_
community consists of using the best available approximation for _G _and _W_
as a starting point and performing only a single-iteration of the
parallelogram (the so-called one-shot _GW_ method, or _G0W0_). In this case
the self-energy is simply given by:

![](../documents/theory_mbt/G0W0.png)

where _G0KS_(12) is the independent-particle propagator of the Kohn-Sham (KS)
Hamiltonian, and the screened interaction is approximated with the RPA
calculated with KS energies and wave functions:

![](../documents/theory_mbt/G0G0.png)



## 4 Perturbative approach

  
Despite all the fundamental differences between many-body theory and DFT, the
Kohn-Sham exchange-correlation potential can be seen as a static, local and
Hermitian approximation to the self-energy. Indeed, in many cases the Kohn-
Sham energies already provide a reasonable estimate of the band structure and
are usually in qualitative agreement with experiment.

This observation suggests that a simple, albeit accurate, solution for the QP
energies can be obtained using first-order perturbation theory, treating the
exchange and correlation potential, _Vxc_, as a zeroth-order approximation to
the non-local and energy dependent self-energy [11,12]

Under the assumption that the QP wavefunctions equal the KS orbitals, we can
expand the self-energy operator around _εKS_ obtaining a closed expression for
_εQP_ :

![](../documents/theory_mbt/qpene_perturbative.png)

where

![](../documents/theory_mbt/Z_def.png)

is the so-called renormalization factor. This corresponds to making a Taylor
expansion of the self-energy matrix element around the KS energy, as depicted
below.

![](../documents/theory_mbt/self_energy_taylor.png)



## 5 The RPA polarizability in Fourier space

  
In the reciprocal space and frequency domain (implying a Fourier transform
(FT) of the real space coordinates and time variables), the independent-
particle polarizability assumes the form:

![](../documents/theory_mbt/chi0_sc_tr.png)

where only the transitions between valence (_v_) and conduction states (_c_)
contribute (for simplicity we have assumed a semiconductor with time-reversal
invariance, the conventions used for the Fourier transform are discussed in
the [[#notations|notation]] section).

The number of bands used to compute the polarizability is specified by
[[nband]], while [[zcut]] gives the small complex shift used to avoid the
divergences in the denominators. The frequency mesh is defined by the set of
variables [[nfreqre]], [[nfreqim]], [[freqremax]], and [[freqremin]] (a number
of more exotic grid choices are available through input variables beginning
with gw_... or cd_..., e.g. [[gw_frqim_inzgrid]]).

_M_ is a shorthand notation to denote the matrix element of a plane wave
sandwiched between two wavefunctions (i.e. oscillator matrix elements). The
number of planewaves (PW) used to describe the wavefunctions is determined by
[[ecutwfn]] while the number of _G_-vectors used to describe the
polarizability (i.e. the number of _G_ vectors in the oscillator matrix
elements) is determined by [[ecuteps]]. The oscillators are ubiquitous in the
Many-Body part of ABINIT and their calculation represents one of the most CPU
intensive part of the execution. For this reason we devote [[#6|section 6]] to
the discussion of some important technical details concerning their
computation.

In principle, the set of **q**-points in the screening matrix is given by all
the possible differences between two crystalline momenta of the wavefunctions
stored in the KSS file, so it is controlled by the chosen **k**-point grid.
The code, however, exploits the invariance of the two-point function under the
action of any symmetry operation of the crystalline space group:

![](../documents/theory_mbt/chi0_symmetry.png)  

so that only the **q**-points in the irreducible Brillouin zone (IBZ) have to
be calculated explicitly.

In frequency and reciprocal space, the microscopic dielectric function is
related to the irreducible polarizability by the following relation

![](../documents/theory_mbt/epsilon_vs_tchi.png)

from which the inverse dielectric function is obtained via matrix inversion.
Following Adler [7,8], the macroscopic dielectric function, єMLF(ω), can be
directly related to the inverse of the microscopic dielectric matrix by means
of:

![](../documents/theory_mbt/emacro_lfe.png)

The optical absorption spectrum -- the quantity one can compare with
experiments -- is given by the imaginary part: Im[єMLF(ω)].

Note that the equation above differs from

![](../documents/theory_mbt/emacro_nlfe.png)

due to the so called local-field effects introduced by the presence of the
crystalline environment. These spectra, if calculated, are typically output as
...**_LF** and ...**_NLF** files during the course of a calculation.



## 6 Notes on the calculation of the oscillator matrix elements

  
Many body calculations require the evaluation of integrals involving the
oscillator matrix elements

![](../documents/theory_mbt/oscillator_longv.png)

where the **k**-point belongs to the full Brillouin zone.

These terms are evaluated by performing a Fast Fourier Transform (FFT) of the
real space product of the two wavefunctions (the second expression in the
equation above). Thanks to the FFT algorithm, the CPU-time requirement scales
almost linearly with the number of points in the FFT box, moreover the code
implements refined algorithms (for instance zero-padded FFTs, FFTW3 interface)
to optimize the computation.

There can be a significant speed-up in this component depending on the
numerical FFT library used. If possible, it should always be advantageous to
link and use the FFTW3 library in GW calculations (controlled by setting
[[fftalg]] 312). The performance of the various FFT libraries for a given type
of calculation can be benchmarked with the **fftprof** utility.

For a given set of indices (_b1_, _b2_, **k**, **q**), the calculation of the
oscillator is done in four different steps:

  1. The two wavefunctions in the irreducible wedge are FFT transformed from the **G**-space to the real space representation, 
  2. The orbitals are rotated in real space on the FFT mesh to obtain the points **k** and **k-q** in the full Brillouin zone. 
  3. Computation of the wavefunction product. 
  4. FFT transform of the product to obtain _M_

Each oscillator thus requires three different FFTs (two transforms to
construct the product, one FFT to get M). The number of FFTs can be
significantly reduced by precomputing and storing in memory the real space
representation of the orbitals at the price of a reasonable increase of the
memory allocated. However, for very memory demanding calculations, the real
space orbitals can be calculated on the fly with an increase in computational
time instead. This option is controlled by the second digit of the input
variable [[gwmem]].

The third term in the equation defining the oscillators makes it clear that
the product of the periodic part of the orbitals has non-zero Fourier
components in a sphere whose radius is 2×_Rwfn_ where _Rwfn_ is the radius of
the **G**-sphere used for the wavefunctions (set by [[ecutwfn]]). To avoid
aliasing errors in the FFT one should therefore use an FFT box that encloses
the sphere with radius 2×_Rwfn_, but this leads to a significant increase in
the computing effort as well as in the memory requirements. The input variable
[[fftgw]] specifies how to setup the FFT box for the oscillators and should be
used to test how the aliasing errors affect the final results. The default
setting of **fftgw 21** is safe, a setting of **fftgw 11** is fast but can be
inaccurate, and a setting of **fftgw 31** gives the maximum possible accuracy
at a significant computational cost.



## 7 Hilbert transform method

  
The computational effort for the evaluation of the RPA polarizability with the
Adler-Wiser expression scales linearly with the number of frequencies computed
([[nfreqre]] and [[nfreqim]]), albeit with a large prefactor which increases
with the fourth power of the number of atoms. The main reason for the linear
scaling is that the frequency dependence cannot be factorised out of the sum
over transitions, hence a distinct and expensive summation over transitions
has to be performed separately for each frequency.

This linear scaling represents a serious problem, especially when many
frequencies are wanted, for example when computing QP corrections within the
contour deformation technique described in the [[lesson_gw2|second lesson]] of
the GW tutorial.

This computational bottleneck can be removed, under certain circumstances, by
employing an efficient algorithm proposed in [13] and subsequently revisited
in [14], in which only the spectral function

![](../documents/theory_mbt/sf_chi0.png)

has to be evaluated in terms of electronic transitions between valence and
conduction states. The Dirac delta function can be approximated either by
means of a triangular function centered at the energy transition following
[14] or a gaussian approximant following [13] (see the related input variables
[[spmeth]], and [[spbroad]]). The spectral function is evaluated on a linear
frequency mesh which covers the entire set of transition energies included in
the calculation. The number of points in the mesh is given by [[nomegasf]].

The evaluation of the spectral function is rather efficient thanks to the
presence of the delta-function in the expression above. For example, when
[[spmeth]]=1, the CPU time required to compute the spectral function on an
arbitrarily dense frequency mesh is just twice that required by a single
static computation based on the standard Adler-Wiser expression.

The full polarizability is then efficiently retrieved by means of a less
expensive frequency integration (a Hilbert transform):

![](../documents/theory_mbt/hilbert_transform.png)

The price to be paid, however, is that a large table for the spectral function
has to be stored in memory and a Hilbert transform has to be performed for
each pair (**G**1, **G**2). Since the computing time required for the
transform scales quadratically with the number of vectors in the
polarizability (governed by [[ecuteps]]), the CPU time spent in this part will
overcome the computing time of the standard Adler-Wiser formalism for large
[[ecuteps]]. A theoretical estimate of the crossover point is hard to give
because it depends on many factors. However, if many frequencies are needed,
such as for the evaluation of optical spectra, or accurate contour deformation
integrations, or even mapping full grids in the complex plane, the Hilbert
transform method can be significantly faster, and its use is well worth
considering.



## 8 Evaluation of the GW self-energy

  
Following the standard approach, we separate the screened interaction into the
static bare Coulomb term and a frequency-dependent contribution according to:

![](../documents/theory_mbt/W_partition_simple.png)

where matrix notation is used.

This particular decomposition of _W_, once inserted in the convolution
defining Σ, leads to the split of the self-energy into two different
contributions (exchange and correlation):

![](../documents/theory_mbt/self_energy.png)

The exchange part is static and turns out to have the same mathematical
structure as the Fock operator in Hartree-Fock theory, albeit constructed with
quasiparticle amplitudes

![](../documents/theory_mbt/self_x.png)

while the dynamic part Σc(ω) accounts for correlation effects beyond Σx.

It is important to stress that, for computational efficiency, the code does
not compute the full self-energy operator by default. Only its matrix elements
for the states specified by [[kptgw]] and [[bdgw]] are computed and used to
obtain the QP corrections.

When expressed in reciprocal space, the diagonal matrix elements of the
exchange part are given by:

![](../documents/theory_mbt/self_x_mel.png)

The evaluation of these terms represents a minor fraction of the overall CPU
time since only occupied states are involved. However we should always keep in
mind that, due to the long range of the bare Coulomb interaction, the
convergence with respect to the number of plane waves used in the oscillators
_M_ ([[ecutsigx]]) is usually slow, much slower than the convergence of the
correlation part, which is short-ranged. This plane wave cutoff can be
converged independently of others if necessary, and given a much larger value
in comparison to [[ecut]], [[ecutwfn]] and [[ecuteps]].

Another point worth noting is the presence in the expression of the Coulomb
singularity for |**q**+**G**| -&gt; 0\. From a mathematical point of view, the
integral is well-defined since the singularity is integrable in three-
dimensional space once the thermodynamical limit, _N_**q** -&gt; ∞, is
reached. On the other hand, only a finite number of **q**-points can be used
for practical applications, and a careful numerical treatment is needed to
avoid an exceedingly slow convergence with respect to the BZ sampling. To
accelerate the convergence in the number of **q**-points, the code implements
several techniques proposed in the literature. We refer to the documentation
of [[icutcoul]] for a more extensive discussion.

The expression for the matrix elements of the correlation part is instead
given by:

![](../documents/theory_mbt/self_c_mel.png)

where all dynamical effects are now contained in the frequency convolution
integral _J_.

The explicit expression for _J_ depends on the method used to treat the
screened interaction. The code implements four different plasmon-pole
techniques to model the frequency dependence of **W** in an efficient but
approximate way, alternatively, it is possible to use the more sophisticated
frequency integration of the contour deformation method [15] for accurate QP
calculations (see the related variables [[ppmodel]] and [[gwcalctyp]]).

The double sum over **G**-vectors is performed for all the plane waves
contained within a sphere of energy [[ecuteps]] (it cannot be larger than the
value used to generate the SCR file). For each state, the correlated matrix
elements are evaluated on a linear frequency mesh centered around the initial
KS energy and the derivative needed for the renormalization factor is obtained
numerically (see [[nomegasrd]] and [[omegasrdmax]]).

Note that here, in contrast to the exchange term, the sum over the band index
_n_ should extend up to infinity although in practice only a finite number of
states can be used (specified by [[nband]]).



## 9 Plasmon-pole models

  
One of the major computational efforts in self-energy calculations is
represented by the calculation of the frequency dependence of the screened
interaction, which is needed for the evaluation of the convolution. Due to the
ragged behavior of _G_(ω) and _W_(ω) along the real axis, numerous real
frequencies are in principle required to converge the results (note that the
maximum frequencies needed are now reported if [[prtvol]] &gt; 9). On the
other hand, since the fine details of _W_(ω) are integrated over, it is
reasonable to expect that approximate models, able to capture the main
physical features of the screened interaction, should give sufficiently
accurate results with a considerably reduction of computational effort. This
is the basic idea behind the so-called plasmon-pole models in which the
frequency dependence of _W_(ω) is modelled in terms of analytic expressions
depending on coefficients that are derived from first principles, i.e. without
any adjustable external parameters.

Four different plasmon-pole techniques are available in ABINIT and the input
variable [[ppmodel]] selects the method to be used.

When [[ppmodel]]=1,2 the frequency dependence of the inverse dielectric
function is modeled according to

![](../documents/theory_mbt/ppmodel_imag.png)

![](../documents/theory_mbt/ppmodel_real.png)

The two models differ in the approach used to compute the parameters.
[[ppmodel]]=1 derives the parameters such that the inverse dielectric matrix
is correctly reproduced at two different explicitly calculated frequencies:
the static limit (ω = 0) and an additional imaginary point located at
[[ppmfrq]]. Unless the user overrides this, the default value is calculated
from the average electronic density of the system. The plasmon-pole parameters
of [[ppmodel]]=2 are calculated so as to reproduce the static limit exactly
and to fulfill a generalized frequency sum rule relating the imaginary part of
the many-body inverse dielectric matrix to the plasma frequency and the charge
density [12]

For a discussion of the models corresponding to [[ppmodel]]=3,4 we refer the
reader to the original papers cited in the documentation of the variable.



## 10 Contour deformation technique

  
The contour deformation method was proposed in order to avoid having to deal
with quantities close to the real axis as much as possible [15]. The integral
over the real frequency axis can be transformed into an integral over the
contour depicted in red in the figure below. The integral over real frequency
is traded with an integration along the imaginary axis plus contributions
coming from the poles of the integrand lying inside the contour:

![](../documents/theory_mbt/contour.png)

![](../documents/theory_mbt/GW_CD.png)

In the above equation, the first sum is restricted to the poles lying inside
the path _C_. _W_c(_z_) represents the frequency dependent part of the
screened interaction, whose expression in reciprocal space is given by:

![](../documents/theory_mbt/Wc.png)

The integration along the imaginary axis is expected to converge quickly with
respect to the number of sampled frequencies since the integrand is typically
very smooth. Only the residues of the integrand have to be evaluated at the
complex poles contributed by the Green's function whose frequency dependence
is known.



## 11 Notations

  
The following shorthand notations are employed:

![](../documents/theory_mbt/notation_1.png)

where _v_(**r**1,**r**2) represents the bare Coulomb interaction, and η is a
positive infinitesimal.

The Fourier transforms for periodic lattice quantities are defined as

![](../documents/theory_mbt/notation_2.png)

The volume of the unit cell is denoted with Ω, while _V_ is the total volume
of the crystal simulated employing Born-von Karman periodic boundary
condition. Unless otherwise specified, Hartree atomic units will be used
throughout.



## 12 References

  
  1. Abrikosov, Gorkov, and Dzyaloshinskii. Methods of quantum field theory in statistical physics, Dover, New York, (1975) 
  2. Fetter, and Walecka. Quantum Theory of Many-Particle Systems, McGraw-Hill, New York, (1971) 
  3. R.D Mattuck. A guide to Feynman diagrams in the many-body problem, Dover, New York, (1992) 
  4. W. G. Aulbur, L. Jonsson and J. W. Wilkins, Solid State Physics **54**, 1 (2000) 
  5. G. Onida et al. Phys. Rev. Lett. **75**, 818 (1995) 
  6. L. Hedin Phys. Rev. **139**, A796, (1965) 
  7. S. L. Adler, Phys. Rev. **126**, 413 (1962)
  8. N. Wiser, Phys. Rev. **129**, 72 (1963)
  9. A. Kutepov, S. Y. Savrasov and G. Kotliar Phys. Rev. B **80**, 041103(R) (2009) 
  10. A. Kutepov, S. Y. Savrasov and G. Kotliar Phys. Rev. B **80**, 041103(R) (2009) 
  11. M.S. Hybertsen, and S.G Louie. Phys. Rev. Lett. **55**, 1418 (1985) 
  12. M.S. Hybertsen, and S.G Louie. Phys. Rev. B **34**, 5390 (1986) 
  13. T. Miyake, and F. Aryasetiawan. Phys. Rev. B, **61**, 7172 (2000) 
  14. M. Shishkin, and G. Kresse. Phys. Rev. B, **74**, 035101 (2006) 
  15. S. Lebegue, B. Arnaud, M. Alouani, and P.E. Bloechl. Phys. Rev. B, **67**, 155208 (2003) 



