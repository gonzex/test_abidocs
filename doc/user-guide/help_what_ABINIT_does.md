This file gives for the beginner an overview of the features implemented in
the ABINIT package, grouped in different topics, also answering the question
"How to ... with ABINIT ?"

[TOC]

* * *

### **1\. Introduction**

ABINIT is a package whose main program allows to find the total energy, charge
density and electronic structure of systems made of electrons and nuclei
(molecules and periodic solids) within Density Functional Theory, using
pseudopotentials and a planewave basis, or augmented plane waves, or even
wavelets. Some possibilities of ABINIT go beyond Density Functional Theory,
i.e. the many-body perturbation theory (GW approximation) and Time-Dependent
Density Functional Theory. ABINIT also includes options to optimize the
geometry according to the DFT forces and stresses, or to perform molecular
dynamics simulation using these forces, or to generate dynamical (vibrations -
phonons) properties, dielectric properties, mechanical properties,
thermodynamical properties, etc . In addition to the main ABINIT code,
different utility programs are provided.

The simplest sort of job computes an electronic structure for a fixed set of
atomic positions within a periodic unit cell. By electronic structure , we
mean a set of eigenvalues and wavefunctions which achieve the lowest (DFT)
energy possible for that basis set (that number of planewaves). The code takes
the description of the unit cell and atomic positions and assembles a crystal
potential from the input atomic pseudopotentials, then uses either an input
wavefunction or simple gaussians to generate the initial charge density and
screening potential, then uses a self-consistent algorithm to iteratively
adjust the planewave coefficients until a sufficient convergence is reached in
the energy.

Analytic derivatives of the energy with respect to atomic positions and unit
cell primitive translations yield atomic forces and the stress tensor. The
code can optionally adjust atomic positions to move the forces toward zero and
adjust unit cell parameters to move toward zero stress. It can performs
molecular dynamics. It can also be used to find responses to atomic
displacements and homogeneous electric field, so that the full phonon band
structure can be constructed...



* * *



### **2\. Ground state static calculations. **

* [1.](../../topics/generated_files/topic_GSintroduction.html) Building an input file. 
* [2.](../../topics/generated_files/topic_GSgeneral.html) General settings. 
* [3.](../../topics/generated_files/topic_crystal.html) Crystalline structure and symmetries. 
* [4.](../../topics/generated_files/topic_k-points.html) k-points. 
* [5.](../../topics/generated_files/topic_xc.html) Exchange and correlation functionals. 
* [6.](../../topics/generated_files/topic_convergency.html) Convergency settings. 
* [7.](../../topics/generated_files/topic_PAW.html) PAW special settings. 
* [8.](../../topics/generated_files/topic_spinpolarisation.html) Spin-polarised systems and spin-orbit coupling 
* [9.](../../topics/generated_files/topic_otherGS.html) Other settings. 



* * *



### **3\. Molecular dynamics, geometry optimization, transition paths.**

* [1.](../../topics/generated_files/topic_MolecularDynamics.html) Molecular dynamics calculations. 
* [2.](../../topics/generated_files/topic_GeoOpt.html) Geometry optimization calculations. 
* [3.](../../topics/generated_files/topic_TransPath.html) Transition path calculations: NEB and string method. 
* [4.](../../topics/generated_files/topic_PIMD.html) PIMD calculations. 



* * *



### **4\. Correlated electrons.**

When correlated electrons are to be considered, it is necessary to go beyond
the DFT framework. ABINIT enables the following possibilities:

* [1.](../../topics/generated_files/topic_Hybrids.html) The use of hybrid functionals. 
* [2.](../../topics/generated_files/topic_CRPA.html) Calculation of the effective Coulomb interaction. 
* [3.](../../topics/generated_files/topic_DFT+U.html) The use of the DFT+U approximation. 
* [4.](../../topics/generated_files/topic_DMFT.html) The use of the DMFT framework. 



* * *



### ** 5.Response functions. **

* [1.](../../topics/generated_files/topic_DFPT.html) DFPT: phonon modes, elastic tensors, effective charges, dielectric tensors,... 
* [2.](../../topics/generated_files/topic_nonlinear.html) Raman intensities and electro-optic properties. 
* [3.](../../topics/generated_files/topic_ElPhon.html) Electron-phonon calculations. 
* [4.](../../topics/generated_files/topic_EffMass.html) Effective mass calculations. 



* * *


### ** 6.Excited state calculations. **

* 1. GW calculations. 
* 2. Bethe-Salpeter calculations. 
* [3.](../../topics/generated_files/topic_GWls.html) GW- Lanczos-Sternheimer method. 
* [4.](../../topics/generated_files/topic_TDDFT.html) TDDFT calculations. 



* * *



### ** 7\. Practical settings.**

* [1.](../../topics/generated_files/topic_multidtset.html) Multi-dataset calculations. 
* [2.](../../topics/generated_files/topic_parallelism.html) Parallelism and ABINIT. 
* [3.](../../topics/generated_files/topic_printing.html) Printing options. 

* * *



### ** 8\. Others.**

* [1.](../../topics/generated_files/topic_positron.html) Positron calculations. 
* [2.](../../topics/generated_files/topic_Wavelets.html) Wavelets in ABINIT. 
* [3.](../../topics/generated_files/topic_Wannier.html) Wannier functions in ABINIT. 
* [4.](../../topics/generated_files/topic_recursion.html) Recursion methods and orbital free calculations. 


