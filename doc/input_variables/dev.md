## **builtintest** 


*Mnemonics:* BUIT-IN TEST number  
*Mentioned in topic(s):* [[topic:Control]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



When [[builtintest]] is non-zero, the input file is a special one, that runs
very quickly, and that is accompanied by a specific analysis by ABINIT, at the
end of the run, against a hard-coded value of total energy (and possibly
stresses, forces ...). The echo of the analysis is done in the STATUS file. In
particular, such built-in tests can be used to check quickly whether ABINIT
fallbacks have been connected or not (bigdft, etsf_io, libxc, wannier90). At
present, [[builtintest]]=1 ... 7 are allowed. See more information in
tests/built-in/README .


* * *

## **cgtyphf** 


*Mnemonics:* Conjugate Gradient TYPe used for Hartree Fock exact exchange  
*Mentioned in topic(s):* [[topic:Hybrids]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2 if [[usefock]] == 1,
0 otherwise.
  
Test list:

- v7:  [[tests/v7/Input/t65.in]], [[tests/v7/Input/t66.in]]





Gives how is calculated Fock exact exchange contribution in the conjugate
gradient, in the SCF case.  
The value 2 corresponds to calculate the Fock exact exchange contribution each
time in the conjugate gradient. The value 1 corresponds to calculate the Fock
exact exchange contribution only for the initial guess (not for the gradient
direction) in the conjugate gradient


* * *

## **densfor_pred** 


*Mnemonics:* DENSity and FORces PREDictor  
*Mentioned in topic(s):* [[topic:SCFAlgorithms]], [[topic:MolecularDynamics]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 6 if [[paral_kgb]]==1,
2 otherwise.
  
*Only relevant if:* [[iscf]] >0  



Used when [[iscf]]&gt;0, to define:  
\- the way a change of density is derived from a change of atomic position,  
\- the way forces are corrected when the SCF cycle is not converged.  
  
Supported values :

  * 0 =&gt; density not changed (fixed charge), forces not corrected 
  * 1 =&gt; density not changed, forces corrected with rigid ion hypothesis (atomic charge moved with atom) 
  * 2 =&gt; density changed and forces corrected with rigid ion hypothesis (atomic charge moves with atom) 
  * 3 =&gt; density changed and forces corrected with a different implementation of the rigid ion hypothesis 
  * 4 =&gt; density not changed, forces corrected with the use of Harris functional formula (*) 
  * 5 =&gt; density changed using D. Alfe 2nd-order algorithm (**), forces not corrected 
  * 6 =&gt; density changed using D. Alfe 2nd-order algorithm (**) and forces corrected with the use of Harris functional formula (*) 

Similar negative values are also allowed (see the meaning later), for
development purposes only. No meaning for RF calculations.  
  
For the time being,  
\- [[densfor_pred]]=3 must be used with [[ionmov]]=4 and [[iscf]]=5.  
\- [[densfor_pred]]=4, 5 or 6 must be used when band-FFT parallelism is
selected.  
Otherwise, use [[densfor_pred]]=2  
  
** (*) ** _ Note concerning the correction of forces (use of [[densfor_pred]]=1, 2, 3, 4 or 6) _ :   
The force on the atom located at R is corrected by the addition of the
following term:  
_ F_residual=Int[dr.V_residual.dRho_atomic/dR] _ , where Rho_atomic is an
atomic (spherical) density.  
\- When such an atomic density (Rho_atomic) is found in the pseudopotential or
PAW file, it is used. If not, a gaussian density (defined by [[densty]]
parameter) is used.  
\- When SCF mixing is done on the density ([[iscf]]&gt;=10), the potential
residual (V_residual) is obtained from the density residual with the first
order formula _ V_residual=dV/drho.Rho_residual _ and uses the exchange-
correlation kernel _ dVxc/drho=Kxc _ whose computation is time-consuming for
GGA functionals. By default (positive values of [[densfor_pred]]), the local-
density part of the GGA exchange-correlation kernel is used (even for GGA, for
which it seems to give a reasonable accuracy). Using the full GGA exchange
correlation kernel (so, including derivatives with respect to the gradient of
the density) is always possible by giving a negative value to
[[densfor_pred]]. In case of hybrid functionals, a similar correction term is
added, although in the density mixing scheme, the related GGA kernel is used
instead of the hybrid functional kernel.  
  
** (**) ** _ Note concerning the use of [[densfor_pred]]=5 or 6 (density prediction) _ :   
The algorithm is described in _ Computer Physics Communications ** 118 **
(1999) 31-33 _ . It uses an atomic (spherical) density. When such an atomic
density is found in the pseudopotential or PAW file, it is used. If not, a
gaussian density (defined by [[densty]] parameter) is used.  
Also note that, to be efficient, this algorithm requires a minimum convergence
of the SCF cycle; Typically, vres2 (or nres2) has to be small enough (10  -4
...10  -5  ).


* * *

## **densty** 


*Mnemonics:* initial DENSity for each TYpe of atom  
*Mentioned in topic(s):* [[topic:xc]]  
*Variable type:* real  
*Dimensions:* ([[ntypat]])  
*Default value:* 0.0  



Gives a rough description of the initial GS density, for each type of atom.
This value is only used to create the first exchange and correlation
potential, and is not used anymore afterwards. For the time being, it
corresponds to an average radius (a.u.) of the density, and is used to
generate a gaussian density. If set to 0.0d0, an optimized value is used.  
No meaning for RF calculations.


* * *

## **dmft_read_occnd** 


*Mnemonics:* Dynamical Mean Fied Theory: READ OCCupations (Non Diagonal)  
*Mentioned in topic(s):* [[topic:DMFT]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v6:  [[tests/v6/Input/t45.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Flag to read/write Occupations as computed in DMFT. This flag is useful to
restart a DFT+DMFT calculation with self-consistency over electronic density.
The occupations are written each time a DMFT loop is finished. So if the
calculation stops because the time limit is reached, this option offers the
possibility to restart the self-consistent loop over density at the point
where it stopped (assuming a restart with the wave functions, see [[getwfk]]).

  * 0=&gt; Occupations are written but never read. 
  * 1=&gt; Occupations are read from I_DMFTOCCND, where I is the root for input files. 
  * 2=&gt; Occupations are read from O_DMFTOCCND, where O is the root for output files. 

An alternative and more simple way to restart a DFT+DMFT calculation is to use
the density file (obtained with [[prtden]]=1 or [[prtden]]=-1) and the self-
energy (see [[dmft_rslf]]).


* * *

## **dmftctqmc_basis** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo BASIS  
*Mentioned in topic(s):* [[topic:DMFT]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Choose the basis to perform CTQMC calculation.

  * 0=&gt; Use the local basis in the spherical harmonics basis. Can be useful if the Hamiltonian has weak off diagonal terms and for this reason, one want to keep the original basis for simplicity and for physical insight. 
  * 1=&gt; Default value, diagonalize the local Hamiltonian (but only if it is not diagonal). The best choice in general. 
  * 2=&gt; Diagonalise the local correlated occupation matrix. Can lead to non diagonal Hamiltonian that cannot be handled by CTQMC. This option should be thus avoided. 


* * *

## **effmass_free** 


*Mnemonics:* EFFective MASS for the FREE electron  
*Mentioned in topic(s):* [[topic:Artificial]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1  
Test list:

- v1:  [[tests/v1/Input/t25.in]]
- v6:  [[tests/v6/Input/t31.in]], [[tests/v6/Input/t32.in]]





This parameter allows to change the free electron mass, with respect to its
experimental value.

The electron mass is simply changed in the Schrodinger equation.

Only for testing purposes, of course.


* * *

## **eshift** 


*Mnemonics:* Energy SHIFT  
*Mentioned in topic(s):* [[topic:SCFAlgorithms]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[wfoptalg]]==3  
Test list:

- v3:  [[tests/v3/Input/t45.in]]





[[eshift]] gives the shift of the energy used in the shifted Hamiltonian
squared. The algorithm will determine eigenvalues and eigenvectors centered on
[[eshift]].  
Can be specified in Ha (the default), Ry, eV or Kelvin, since ** ecut ** has
the '[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)


* * *

## **exchmix** 


*Mnemonics:* EXCHange MIXing  
*Mentioned in topic(s):* [[topic:xc]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.25  
*Only relevant if:* [[useexexch]] == 1  
Test list:

- v5:  [[tests/v5/Input/t18.in]]





[[exchmix]] allows to tune the ratio of exact exchange when [[useexexch]] is
used. The default value of 0.25 corresponds to PBE0.


* * *

## **exchn2n3d** 


*Mnemonics:* EXCHange N2 and N3 Dimensions  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v4:  [[tests/v4/Input/t92.in]]





If [[exchn2n3d]] is 1, the internal representation of the FFT arrays in
reciprocal space will be array(n1,n3,n2), where the second and third
dimensions have been switched. This is to allow to be coherent with the
[[exchn2n3d]]=4xx FFT treatment.


* * *

## **extrapwf** 


*Mnemonics:* flag - EXTRAPolation of the Wave-Functions  
*Mentioned in topic(s):* [[topic:TuningSpeed]], [[topic:MolecularDynamics]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[densfor_pred]]==5 or [[densfor_pred]]==6  
Test list:

- v7:  [[tests/v7/Input/t09.in]]





This flag activates the extrapolation of wave-functions from one Molecular
Dynamics (or Structural Relaxation) step to another. The wave functions are
extrapolated using 2nd-order algorithm of Arias, Payne and Joannopoulos (PRB
45, 1538 (1992)).  
Note that, when activated, this extrapolation requires non-negligible
additional memory resources as the wave functions are stored for the two
previous time steps. Also, it can only be activated if a consistent density
extrapolation is activated (see [[densfor_pred]]).  
ABINIT 7.10: this option is **under development** and might give wrong
results.


* * *

## **fermie_nest** 


*Mnemonics:* FERMI Energy for printing the NESTing function  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v6:  [[tests/v6/Input/t72.in]], [[tests/v6/Input/t90.in]]
- v7:  [[tests/v7/Input/t90.in]]





This input variable is only effective when [[prtnest]]=1. The energy is
relative to the calculated fermi energy.


* * *

## **fftalg** 


*Mnemonics:* Fast Fourier Transform ALGorithm  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 312 if [[FFTW3]] and [[usedmft]]==0,
401 if [[paral_kgb]]==1,
112 otherwise.
  



This keyword is ** irrelevant ** when Fast Fourier Transforms are done using
** Graphics Processing Units ** (GPU), i.e. when [[use_gpu_cuda]]=1 (in that
case, it is ignored).  
  
Allows to choose the algorithm for Fast Fourier Transforms. These have to be
used when applied to wavefunctions (routine fourwf.F90), as well as when
applied to densities and potentials (routine fourdp.F90). Presently, it is the
concatenation of three digits, labelled (A), (B) and (C).  
  
The first digit (A) is to be chosen among 1, 2, 3, 4 or 5 :

  * 1=&gt; use FFT routines written by S. Goedecker. 
  * 2=&gt; not available anymore 
  * 3=&gt; use serial or multi-threaded FFTW3 fortran routines ( [ http://www.fftw.org ](http://www.fftw.org) ). Currently implemented with [[fftalg]]=312. 
  * 4=&gt; use FFT routines written by S. Goedecker, 2002 version, that will be suited for MPI and OpenMP parallelism. 
  * 5=&gt; use serial or multi-threaded MKL routines Currently implemented with [[fftalg]]=512. 

The second digit (B) is related to fourdp.f :

  * 0=&gt; only use Complex-to-complex FFT 
  * 1=&gt; real-to-complex is also allowed (only coded for A==1, A==3 and A==5) 

The third digit (C) is related to fourwf.f :

  * 0=&gt; no use of zero padding 
  * 1=&gt; use of zero padding (only coded for A==1, A==4) 
  * 2=&gt; use of zero padding, and also combines actual FFT operations (using 2 routines from S. Goedecker) with important pre- and post-processing operations, in order to maximize cache data reuse. This is very efficient for cache architectures. (coded for A==1 and A==4, but A==4 is not yet sufficiently tested) 

Internal representation as [[ngfft]](7).


* * *

## **fftcache** 


*Mnemonics:* Fast Fourier Transform CACHE size  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 16  
*Comment:* todo: Not yet machine-dependent  
Test list:

- v6:  [[tests/v6/Input/t03.in]]





Gives the cache size of the current machine, in Kbytes.  
Internal representation as [[ngfft]](8).


* * *

## **getgam_eig2nkq** 


*Mnemonics:* GET the GAMma phonon data EIG2NKQ from dataset  
*Mentioned in topic(s):* [[topic:multidtset]], [[topic:TDepES]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[ieig2rf]] != 0 and [[qpt]] != (0.0,0.0,0.0)  
Test list:

- v6:  [[tests/v6/Input/t37.in]], [[tests/v6/Input/t50.in]]





Relevant for second-order eigenvalue calculations using response-functions
([[ieig2rf]] != 0), and only for non-zero wavevectors [[qpt]].  
From the electron-phonon matrix elements at some wavevector only, it is not
possible to determine the Debye-Waller contribution : one has to know also the
q=Gamma electron-phonon matrix elements.  
The variable [[getgam_eig2nkq]] allows to transmit the information about the
second-order derivatives of the eigenvalues for q=Gamma from the dataset where
the calculation at Gamma was done, to the datasets for other wavevectors.


* * *

## **getwfkfine** 


*Mnemonics:* GET the fine grid wavefunctions from _WFK file  
*Mentioned in topic(s):* [[topic:multidtset]], [[topic:DFPT]], [[topic:TDepES]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v67mbpt:  [[tests/v67mbpt/Input/t32.in]], [[tests/v67mbpt/Input/t33.in]], [[tests/v67mbpt/Input/t34.in]], [[tests/v67mbpt/Input/t35.in]]
- v7:  [[tests/v7/Input/t50.in]], [[tests/v7/Input/t51.in]]





Eventually used when [[ndtset]]&gt;0 (in the multi-dataset mode), to indicate
starting wavefunctions, as an alternative to [[irdwfkfine]]. One should first
read the explanations given for these latter variables.  
The [[getwfkfine]] variables is typically used to chain the calculations in
the multi-dataset mode, since they describe from which dataset the OUTPUT
wavefunctions are to be taken, as INPUT wavefunctions of the present dataset.  
If [[getwfkfine]]==0, no use of previously computed output wavefunction file
appended with _DSx_WFK is done.  
If [[getwfkfine]] is positive, its value gives the index of the dataset for
which the output wavefunction file appended with _WFK must be used.  
If [[getwfkfine]] is -1, the output wf file with _WFK of the previous dataset
must be taken, which is a frequently occurring case.  
If [[getwfkfine]] is a negative number, it indicates the number of datasets to
go backward to find the needed wavefunction file. In this case, if one refers
to a non existent data set (prior to the first), the wavefunctions are not
initialised from a disk file, so that it is as if [[getwfkfine]]=0 for that
initialisation. Thanks to this rule, the use of [[getwfkfine]] -1 is rather
straightforward : except for the first wavefunctions, that are not initialized
by reading a disk file, the output wavefunction of one dataset is input of the
next one.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
     ndtset 3   jdtset 1 2 4  getXXX -1
    

refers to dataset 2 when dataset 4 is initialized. Response-function
calculation :

  * one and only one of [[getwfkfine]] or [[irdwfkfine]] MUST be non-zero 
  * if [[getwfkfine]] = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * Reading the fine grid wavefunction will trigger the k-points interpolation technique of the temperature dependent calculations. 

Bethe-Salpeter calculation :

  * one and only one of [[getwfkfine]] or [[irdwfkfine]] MUST be non-zero 
  * if [[getwfkfine]] = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * This variable or [[irdwfkfine]] is mandatory when [[bs_interp_mode]] == 1 

** This variable is experimental. In development. **


* * *

## **intxc** 


*Mnemonics:* INTerpolation for eXchange-Correlation  
*Mentioned in topic(s):* [[topic:xc]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



  * 0=&gt; do "usual" xc quadrature on fft grid 
  * 1=&gt; do higher accuracy xc quadrature using fft grid and additional points at the centers of each cube (doubles number of grid points)--the high accuracy version is only valid for boxcut&gt;=2. If boxcut &lt; 2, the code stops. 

  
For RF calculations only [[intxc]]=0 is allowed yet. Moreover, the GS
preparation runs (giving the density file and zero-order wavefunctions) must
be done with [[intxc]]=0

Prior to ABINITv2.3, the choice [[intxc]]=1 was favoured (it was the default),
but the continuation of the development of the code lead to prefer the default
[[intxc]]=0 . Indeed, the benefit of [[intxc]]=1 is rather small, while making
it available for all cases is a non-negligible development effort. Other
targets are prioritary... You will notice that many automatic tests use
[[intxc]]=1. Please, do not follow this historical choice for your production
runs.


* * *

## **iomode** 


*Mnemonics:* Input-Output MODE  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[MPI_IO]] and [[paral_kgb]]==1,
0 otherwise.
  



This option selects the format used to produce the output wavefunction files
and the files containing densities and potentials. It mainly affects the
creation of the output files since several parts of Abinit are able to read
data from files independently of their format (either binary files or netcdf
files). The possible values are:

  * 0 =&gt; Use standard Fortran IO (ok for sequential runs, not suitable for large parallel runs) 
  * 1 =&gt; Use MPI/IO routines (ok both for sequential and large parallel runs) 
  * 3 =&gt; Use NetCDF library to produce files according to the ETSF specification (ok for sequential, requires netcdf4 + hdf5 + MPI-IO support for large parallel runs) 

  

By default, Abinit produces Fortran files and uses parallel MPI-IO under the
hood when these operations cannot be implemented in terms of simple Fortran
write/read statements. For example, [[paral_kgb]]=1 uses the MPI-IO API
provided by your MPI library.

In a nutshell, use the default value and make sure that your MPI library
supports MPI-IO before embarking yourself in large parallel runs (HAVE_MPI_IO
should be set to 1 in ~abinit/config.h). Many MPI libraries, nowadays, support
the MPI-2 standard so it's very likely that your MPI supports parallel IO. If
you encounter problems, please ask your sysadmin to install a MPI library with
MPI-IO capabilities.

There are cases, however, in which you would like to change the default
behaviour. For example, you may want to generate WFK or DEN files in etsf-io
format because you need data in this format. In this case, you have to use
iomode==3 in the input file to override the default behaviour. Note however
that you still need parallel IO capabilities enabled in the netcdf library if
you want to produce netcdf files in parallel with [[paral_kgb]]=1 (i.e.
netcdf4 + hdf5 + MPI-IO). At present, the internal fallbacks provided by
Abinit do not support netcdf4 so you have to link against an external netcdf
library that supports hdf5+MPI-IO and is compatible with the mpif90 used to
compile Abinit. See ~abinit/doc/build/config-examples/ubu_gnu_4.9_mpich.ac for
a typical configuration file.

References:

  * "Specification of an extensible and portable file format for electronic structure and crystallographic data", X. Gonze, C.-O. Almbladh, A. Cucca, D. Caliste, C. Freysoldt, M. Marques, V. Olevano, Y. Pouillon, M.J. Verstraete, Comput. Mat. Science 43, 1056 (2008) 
  * "Sharing electronic structure and crystallographic data with ETSF_IO", D. Caliste, Y. Pouillon, M.J. Verstraete, V. Olevano, X. Gonze, Comput. Physics Communications 179, 748 (2008) 
  * see also [ http://www.etsf.eu/fileformats ](http://www.etsf.eu/fileformats) . 


* * *

## **iprcfc** 


*Mnemonics:* Integer for PReConditioner of Force Constants  
*Mentioned in topic(s):* [[topic:GeoOpt]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v1:  [[tests/v1/Input/t44.in]], [[tests/v1/Input/t45.in]], [[tests/v1/Input/t48.in]], [[tests/v1/Input/t49.in]]





Used when [[iscf]]&gt;0, to define the SCF preconditioning scheme. Potential-
based preconditioning schemes for the SCF loop are still under development.  
The present parameter (force constant part) describes the way a change of
force is derived from a change of atomic position.  
Supported values :

  * 0 =&gt; hessian is the identity matrix 
  * 1 =&gt; hessian is 0.5 times the identity matrix 
  * 2 =&gt; hessian is 0.25 times the identity matrix 
  * -1=&gt; hessian is twice the identity matrix 
  * ... (simply corresponding power of 2 times the identity matrix) 

No meaning for RF calculations.


* * *

## **irandom** 


*Mnemonics:* Integer for the choice of the RANDOM number generator  
*Mentioned in topic(s):* [[topic:PIMD]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 3  
Test list:

- v6:  [[tests/v6/Input/t26.in]]
- v7:  [[tests/v7/Input/t08.in]]
- v8:  [[tests/v8/Input/t05.in]]





For the time being, only used when [[imgmov]]=9 (Langevin Path-Integral
Molecular Dynamics).  
[[irandom]] defines the random number generator.  
  
Supported values :

  * 1 =&gt; "uniformrandom", delivered with ABINIT package (initially comes from numerical recipes). 
  * 2 =&gt; intrinsic Fortran 90 random number generator. 
  * 3 =&gt; "ZBQ" non-deterministic random number generator by R. Chandler and P. Northrop. (Available at [). 

[[irandom]]=3 is strongly advised when performing Molecular Dynamics restarts
(avoids bias).


* * *

## **irdwfkfine** 


*Mnemonics:* Integer that governs the ReaDing of the grid _WFK file on the FINE grid  
*Mentioned in topic(s):* [[topic:multidtset]], [[topic:TDepES]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t51.in]]





Indicates eventual starting wavefunctions. As alternative, one can use the
input variables [[getwfkfine]].  
  
Ground-state calculation :

  * only [[irdwfkfine]] and [[getwfkfine]] have a meaning 
  * at most one of [[irdwfkfine]] or [[getwfkfine]] can be non-zero 
  * if [[irdwfkfine]] = 1 : read ground state wavefunctions from a disk file appended with _WFK , produced in a previous ground state fine grid calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 

Response-function calculation :

  * one and only one of [[irdwfkfine]] or [[getwfkfine]] MUST be non-zero 
  * if [[irdwfkfine]] = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * Reading the fine grid wavefunction will trigger the k-points interpolation technique of the temperature dependent calculations. 

Bethe-Salpeter calculation :

  * one and only one of [[irdwfkfine]] or [[getwfkfine]] MUST be non-zero 
  * if [[irdwfkfine]] = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * This variable or [[getwfkfine]] is mandatory when [[bs_interp_mode]] = 1 

** This variable is experimental. In development. **


* * *

## **isecur** 


*Mnemonics:* Integer for level of SECURity choice  
*Mentioned in topic(s):* [[topic:SCFAlgorithms]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- fast:  [[tests/fast/Input/t17.in]], [[tests/fast/Input/t19.in]]
- v1:  [[tests/v1/Input/t08.in]], [[tests/v1/Input/t33.in]], [[tests/v1/Input/t85.in]], [[tests/v1/Input/t86.in]], [[tests/v1/Input/t98.in]], [[tests/v1/Input/t99.in]]
- v2:  [[tests/v2/Input/t51.in]]





In the presently used algorithms, there is a compromise between speed and
robustness, that can be tuned by using [[isecur]].  
If [[isecur]] =0, an extrapolation of out-of-line data is allowed, and might
save one non-SCF calculation every two line minimisation when some stability
conditions are fulfilled (since there are 2 non-SCF calculations per line
minimisation, 1 out of 4 is saved)  
Using [[isecur]]=1 or higher integers will raise gradually the threshold to
make extrapolation.  
Using [[isecur]]=-2 will allow to save 2 non-SCF calculations every three line
minimisation, but this can make the algorithm unstable. Lower values of
[[isecur]] allows for more (tentative) savings. In any case, there must be one
non-SCF computation per line minimisation.  
No meaning for RF calculations yet.


* * *

## **istatr** 


*Mnemonics:* Integer for STATus file rate  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Comment:* Values lower than 10 may not work on some machines.  



Govern the rate of output of the status file. This status file is written when
the number of the call to the status subroutine is equal to ' ** istatshft **
' modulo '[[istatr]]', so that it is written once every '[[istatr]]' call.
When '[[istatr]]'=0, there is no writing of a status file (which is the
default).


* * *

## **istatshft** 


*Mnemonics:* Integer for STATus file SHiFT  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
Test list:

- v3:  [[tests/v3/Input/t45.in]]





Govern the rate of output of the status file. This status file is written when
the number of the call to the status subroutine is equal to '[[istatshft]]'
modulo ' ** istatr ** ', so that it is written once every ' ** istatr ** '
call. There is also a writing for each of the 5 first calls, and the 10th
call.


* * *

## **istwfk** 


*Mnemonics:* Integer for choice of STorage of WaveFunction at each k point  
*Mentioned in topic(s):* [[topic:k-points]], [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* ([[nkpt]])  
*Default value:* *0  
*Comment:* For RF calculations, the Default is not used : <b>istwfk</b> is forced to be 1 deep inside the code, for all k points. For spin-orbit calculations ([[nspinor]]=2), <b>istwfk</b> is also forced to be 1, for all k points.  



Control the way the wavefunction for each k-point is stored inside ABINIT, in
reciprocal space.  
For the GS calculations, in the "cg" array containing the wavefunction
coefficients, there is for each k-point and each band, a segment
cg(1:2,1:npw). The 'full' number of plane wave is determined by [[ecut]].
However, if the k-point coordinates are build only from zeroes and halves (see
list below), the use of time-reversal symmetry (that connects coefficients)
has been implemented, in order to use real-to-complex FFTs (see [[fftalg]]),
and to treat explicitly only half of the number of plane waves (this being
used as 'npw').  
For the RF calculations, there is not only the "cg" array, but also the "cgq"
and "cg1" arrays. For the time-reversal symmetry to decrease the number of
plane waves of these arrays, the q vector MUST be (0 0 0). Then, for each k
point, the same rule as for the RF can be applied.  
WARNING (991018) : for the time being, the time-reversal symmetry cannot be
used in the RF calculations.

  * 1=&gt; do NOT take advantage of the time-reversal symmetry 
  * 2=&gt; use time-reversal symmetry for k=( 0 0 0 ) 
  * 3=&gt; use time-reversal symmetry for k=(1/2 0 0 ) 
  * 4=&gt; use time-reversal symmetry for k=( 0 0 1/2) 
  * 5=&gt; use time-reversal symmetry for k=(1/2 0 1/2) 
  * 6=&gt; use time-reversal symmetry for k=( 0 1/2 0 ) 
  * 7=&gt; use time-reversal symmetry for k=(1/2 1/2 0 ) 
  * 8=&gt; use time-reversal symmetry for k=( 0 1/2 1/2) 
  * 9=&gt; use time-reversal symmetry for k=(1/2 1/2 1/2) 
  * 0=&gt; (preprocessed) for each k point, choose automatically the appropriate time-reversal option when it is allowed, and chose [[istwfk]]=1 for all the other k points. 


* * *

## **lotf_classic** 


*Mnemonics:* LOTF CLASSIC model for glue model  
*Mentioned in topic(s):* [[topic:LOTF]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 5  
Test list:

- paral:  [[tests/paral/Input/t41.in]]





Glue model used in LOTF.  
For the moment it is imposed to be 5.


* * *

## **lotf_nitex** 


*Mnemonics:* LOTF Number of ITerations  
*Mentioned in topic(s):* [[topic:LOTF]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 10  
Test list:

- paral:  [[tests/paral/Input/t41.in]]





Set the number of Molecular Dynamics iterations which are computed by LOTF.


* * *

## **lotf_nneigx** 


*Mnemonics:* LOTF max Number of NEIGhbours  
*Mentioned in topic(s):* [[topic:LOTF]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 5  
Test list:

- paral:  [[tests/paral/Input/t41.in]]





Set the max number of Neighbours used in the LOTF method.  
For the moment it is imposed to be 40.


* * *

## **lotf_version** 


*Mnemonics:* LOTF VERSION of MD algorithm  
*Mentioned in topic(s):* [[topic:LOTF]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2  
Test list:

- paral:  [[tests/paral/Input/t41.in]]





Set the MD algorithm in the LOTF method.  
For the moment it is imposed to be 2.


* * *

## **macro_uj** 


*Mnemonics:* MACRO variable that activates the determination of the U and J parameter (for the PAW+U calculations)  
*Mentioned in topic(s):* [[topic:DFT+U]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- tutorial:  [[tests/tutorial/Input/tudet_1.in]], [[tests/tutorial/Input/tudet_2.in]]
- v5:  [[tests/v5/Input/t38.in]], [[tests/v5/Input/t39.in]]





Sets proper input values for the determination of U and J i.e. for [[pawujat]]
(first atom treated with PAW+U), [[irdwfk]] (=1), [[tolvrs]] (=10^(-8)),
[[nstep]] (=255), [[diemix]] (=0.45), [[atvshift]] ([[pawujat]]) [[pawujv]]).
Do not overwrite these variables manually unless you know what you do.

  * [[macro_uj]]=1 (and [[nsppol]]=2) Standard procedure to determine U on atom pawujat through a shift of the potential on both spin channels. 
  * [[macro_uj]]=1 (and [[nsppol]]=1) Non standard procedure to determine U from potential shift on atom pawujat (experimental). 
  * [[macro_uj]]=2 (and [[nsppol]]=2) Non standard procedure to determine U from potential shift on atom pawujat through a shift on spin channel 1 on this atom and the response on this channel (experimental). 
  * [[macro_uj]]=3 (and [[nsppol]]=2) Standard procedure to determine J from potential shift on spin channel 1 on atom pawujat and response on spin channel 2 (experimental). 

Determination of U and J can be done only if the symmetry of the atomic
arrangement is reduced and the atom pawujat is not connected to any other atom
by symmetry relations (either input reduced symmetries manually, define
concerned atom as a separate atomic species or shift concerned atom from ideal
position).


* * *

## **maxnsym** 


*Mnemonics:* MAXimum Number of SYMetries  
*Mentioned in topic(s):* [[topic:crystal]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 384  
Test list:

- v5:  [[tests/v5/Input/t06.in]]





Gives the maximum number of spatial symetries allowed in the memory.  
The default value is sufficient for most applications. It might have to be
increased in the case of the use of a supercell (unit cell identically
repeated).


* * *

## **mem_test** 


*Mnemonics:* MEMory TEST  
*Mentioned in topic(s):* [[topic:Control]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
Test list:

- paral:  [[tests/paral/Input/t29.in]]





This variable controls the memory test done in the memana routine. Possible
values:

  * 0 no test on the available memory is performed 
  * 1 the routine tries to allocate the estimated memory, for testing purposes, and if a failure occurs, the routine stops. 
  * 2 like 1, but before stopping, the routine will provide an estimation of the available memory. 


* * *

## **mqgrid** 


*Mnemonics:* Maximum number of Q-space GRID points for pseudopotentials  
*Mentioned in topic(s):* [[topic:Planewaves]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 3001  
Test list:

- v4:  [[tests/v4/Input/t17.in]], [[tests/v4/Input/t62.in]]
- v7:  [[tests/v7/Input/t23.in]], [[tests/v7/Input/t24.in]], [[tests/v7/Input/t25.in]], [[tests/v7/Input/t78.in]], [[tests/v7/Input/t79.in]]





Govern the size of the one-dimensional information related to
pseudopotentials, in reciprocal space : potentials, or projector functions.


* * *

## **nbdblock** 


*Mnemonics:* Number of BanDs in a BLOCK  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
Test list:

- v4:  [[tests/v4/Input/t93.in]], [[tests/v4/Input/t94.in]]





In case of non-standard, blocked algorithms for the optimization of the
wavefunctions (that is, if [[wfoptalg]]=4):

  * if [[wfoptalg]]=4, [[nbdblock]] defines the number of blocks (the number of bands in the block is then [[nband]]/[[nbdblock]] ). 


* * *

## **nc_xccc_gspace** 


*Mnemonics:* Norm-Conserving pseudopotentials - use XC Core-Correction in G-SPACE  
*Mentioned in topic(s):* [[topic:Planewaves]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0 if [[usepaw]]==0,
1 if [[usepaw]]==1,
0 otherwise.
  
*Comment:* 0 when [[usepaw]]=0, 1 when [[usepaw]]=1  
Test list:

- v7:  [[tests/v7/Input/t10.in]], [[tests/v7/Input/t45.in]]





Historically, Abinit treats the model core charge used for the non-linear core
correction in real space. Alternatively, it is possible to instruct the code
to compute the core charge in G-space following the same approach used in the
PAW code. The G-space formalism is more accurate than the interpolation in
real space, especially when derivatives of the model core charge are needed,
e.g. DFPT. Preliminary tests showed that the violation of the acoustic sum
rule is reduced when [[nc_xccc_gspace]]==1 , especially for LDA. It is worth
stressing, however, that [[nc_xccc_gspace]]==1 should be used only in
conjunction with NC pseudos whose model core charge that decays quickly in
G-space. Several NC pseudos available in the Abinit table are not optimized
for the G-space formalism and users are strongly invited to perform
convergence studies with respect to ecut before using this option.


* * *

## **nctime** 


*Mnemonics:* NetCdf TIME between output of molecular dynamics informations  
*Mentioned in topic(s):* [[topic:MolecularDynamics]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- etsf_io:  [[tests/etsf_io/Input/t21.in]]
- paral:  [[tests/paral/Input/t41.in]]





When [[nctime]] is non-zero, the molecular dynamics information is output in
NetCDF format, every [[nctime]] time step. Here is the content of an example
file :

    
    
    netcdf md32.outH_moldyn1 {
    dimensions:
       time = UNLIMITED ; // (11 currently)
       DimTensor = 6 ;
       DimCoord = 3 ;
       NbAtoms = 32 ;
       DimVector = 3 ;
       DimScalar = 1 ;
    variables:
       double E_pot(time) ;
          E_pot:units = "hartree" ;
       double E_kin(time) ;
          E_kin:units = "hartree" ;
       double Stress(time, DimTensor) ;
          Stress:units = "hartree/Bohr^3" ;
       double Position(time, DimCoord, NbAtoms) ;
          Position:units = "Bohr" ;
       double Celerity(time, DimCoord, NbAtoms) ;
          Celerity:units = "Bohr/(atomic time unit)" ;
       double PrimitiveVector1(DimVector) ;
       double PrimitiveVector2(DimVector) ;
       double PrimitiveVector3(DimVector) ;
       double Cell_Volume(DimScalar) ;
          Cell_Volume:units = "Bohr^3" ;
    }
     


* * *

## **nloc_alg** 


*Mnemonics:* Non LOCal ALGorithm  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 4  
Test list:

- v2:  [[tests/v2/Input/t37.in]], [[tests/v2/Input/t38.in]]
- v4:  [[tests/v4/Input/t20.in]], [[tests/v4/Input/t61.in]], [[tests/v4/Input/t62.in]]





Allows to choose the algorithm for non-local operator application. On super-
scalar architectures, the default [[nloc_alg]]=4 is the best.  
More detailed explanations:  

\- [[nloc_alg]]=2 : Should be efficient on vector machines. It is indeed the
fastest algorithm for the NEC, but actual tests on Fujitsu machine did not
gave better performances than the other options.  
\- [[nloc_alg]]=3 : same as [[nloc_alg]]==2, but the loop order is inverted.  
\- [[nloc_alg]]=4 : same as [[nloc_alg]]==3, but maximal use of registers has
been coded. This should be especially efficient on scalar and super-scalar
machines. This has been confirmed by tests.  

Note: internally, [[nloc_alg]] is stored in _ nloalg(1) _ . See also
[[nloc_mem]] for the tuning of the memory used in the non-local operator
application.


* * *

## **nloc_mem** 


*Mnemonics:* Non LOCal MEMOry  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2 if [[usepaw]]==1,
1 otherwise.
  
Test list:

- paral:  [[tests/paral/Input/t41.in]]





Controls the memory use for the application of the non-local operator.  
More detailed explanations:  

\- [[nloc_mem]]==1 : (k+G) vectors are not precomputed, in order to save
memory space.  
\- [[nloc_mem]]==2 : (k+G) vectors are precomputed, once per k-point.  
\- [[nloc_mem]]==-1 or -2 : Negative values of [[nloc_mem]] correspond
positive ones, where the phase precomputation has been suppressed, in order to
save memory space, as an array _ double precision :: ph3d(2,npw,[[natom]]) _
is saved (typically half the space needed for the wavefunctions at 1 k point -
this corresponds to the silicon case). However, the computation of phases
inside nonlop is somehow time-consuming.  

  
Note: internally, sign([[nloc_mem]]) is stored in _ nloalg(2) _ and
abs([[nloc_mem]])-1 is stored in _ nloalg(3) _ . See also [[nloc_alg]] for the
algorithm for the non-local operator application.


* * *

## **nnsclo** 


*Mnemonics:* Number of Non-Self Consistent LOops  
*Mentioned in topic(s):* [[topic:SCFControl]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Gives the maximum number of non-self-consistent loops of [[nline]] line
minimisations, in the SCF case (when [[iscf]] &gt;0). In the case [[iscf]]
&lt;=0 , the number of non-self-consistent loops is determined by [[nstep]].  
The Default value of 0 -- for standard plane-wave calculations -- corresponds
to make the two first fixed potential determinations of wavefunctions have 2
non-self consistent loops, and the next ones to have only 1 non-self
consistent loop.  
The Default value of 0 -- for wavelets calculations ([[usewvl]]=1) --
corresponds to make 2 steps with 3 non-self consistent loops , 2 steps with 2
non-self consistent loops, then the next ones with 1 non-self consistent loop.


* * *

## **nnsclohf** 


*Mnemonics:* Number of Non-Self Consistent LOops for (Hartree)-Fock exact exchange  
*Mentioned in topic(s):* [[topic:Hybrids]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[usefock]]==1,
0 otherwise.
  
Test list:

- v7:  [[tests/v7/Input/t65.in]], [[tests/v7/Input/t66.in]]





Gives the maximum number of loops with non-self-consistent occupied states
used to calculate Fock exact exchange, in the SCF case.  
The Default value is 0 when [[usefock]] = 0. Default value is 1 when
[[usefock]] = 1 and correspond to update occupied wavefunctions at each self-
consistent loop.


* * *

## **normpawu** 


*Mnemonics:* NORMalize atomic PAW+U projector  
*Mentioned in topic(s):* [[topic:DFT+U]]  
*Variable type:* integer  
*Dimensions:* ([[ntypat]])  
*Default value:* 0  
Test list:






Defines whether the atomic wave function (used as projectors in PAW+U) should
be renormalized to 1 within PAW sphere.

  * [[normpawu]]=0 : leave projector 
  * [[normpawu]]=1 : renormalize 


* * *

## **npulayit** 


*Mnemonics:* Number of PULAY ITerations for SC mixing  
*Mentioned in topic(s):* [[topic:SCFAlgorithms]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 7  
*Only relevant if:* [[iscf]] in [7,17]  



Gives the number of previous iterations involved in Pulay mixing (mixing
during electronic SC iterations).


* * *

## **nscforder** 


*Mnemonics:* Nth - SCaling Function ORDER  
*Mentioned in topic(s):* [[topic:Coulomb]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 16  



This variable controls the order of used scaling functions when the Hartree
potential is computed using the Poisson solver (see [[icoulomb]] imput
variable). This variable is of seldom use since the default value is large
enough. Nonetheless, possible values are 8, 14, 16, 20, 24, 30, 40, 50, 60,
100. Values greater than 20 are included in ABINIT for test purposes only.


* * *

## **optforces** 


*Mnemonics:* OPTions for the calculation of FORCES  
*Mentioned in topic(s):* [[topic:ForcesStresses]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[toldff]] or [[tolrff]] != 0,
2 otherwise.
  



Allows to choose options for the calculation of forces.

  * [[optforces]]=0 : the forces are set to zero, and many steps of the computation of forces are skipped 
  * [[optforces]]=1 : calculation of forces at each SCF iteration, allowing to use forces as criterion to stop the SCF cycles 
  * [[optforces]]=2 : calculation of forces at the end of the SCF iterations (like the stresses) 


* * *

## **optnlxccc** 


*Mnemonics:* OPTion for the calculation of Non-Linear eXchange-Correlation Core Correction  
*Mentioned in topic(s):* [[topic:xc]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
Test list:

- v5:  [[tests/v5/Input/t45.in]]





Allows to choose options for the calculation of non-linear XC correction. At
present, only relevant for the FHI type of pseudopotentials, with pspcod=6 .

  * [[optnlxccc]]=1 : uses the old psp6cc.f routine, with inconsistent treatment of real-space derivatives of the core function (computed in this routine, while splined in the other parts of the code) 
  * [[optnlxccc]]=2 : consistent calculation derivatives, in the psp6cc_dhr.f routine from DHamann. 


* * *

## **ortalg** 


*Mnemonics:* ORThogonalisation ALGorithm  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* -2 if [[wfoptalg]] >= 10 ,
2 otherwise.
  



Allows to choose the algorithm for orthogonalisation.  
Positive or zero values make two projections per line minimisation, one before
the preconditioning, one after. This is the clean application of the band-by-
band CG gradient for finding eigenfunctions.  
Negative values make only one projection per line minimisation.  
The orthogonalisation step is twice faster, but the convergence is less good.
This actually calls to a better understanding of this effect.  
[[ortalg]]=0, 1 or -1 is the conventional coding.  
[[ortalg]]=2 or -2 try to make better use of existing registers on the
particular machine one is running.  
More demanding use of registers is provided by [[ortalg]]=3 or -3, and so on.  
The maximal value is presently 4 and -4.  
Tests have shown that [[ortalg]]=2 or -2 is suitable for use on the available
platforms.


* * *

## **papiopt** 


*Mnemonics:* PAPI OPTion  
*Mentioned in topic(s):* [[topic:Control]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






[ PAPI ](http://icl.cs.utk.edu/papi/index.html) aims to provide the tool
designer and application engineer with a consistent interface and methodology
for use of the performance counter hardware found in most major
microprocessors. PAPI enables software engineers to see, in near real time,
the relation between software performance and processor events.  
This option can be used only when ABINIT has been compiled with the `
--enable-papi ` configure option.  
If [[papiopt]]=1, then PAPI counters are used instead of the usual time()
routine. All the timing output of ABINIT is then done with PAPI values. The
measurements are more accurate and give also access to the flops of the
calculation.


* * *

## **pawprt_b** 


*Mnemonics:* PAW PRinT band  
*Mentioned in topic(s):* [[topic:PAW]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






Forces the output of the all-electron wavefunction for only a single band. To
be used in conjuction with: **  
[[pawprtwf]]=1 ** and [[pawprt_k]]. The indexing of the bands start with one
for the lowest occupied band and goes up from there.


* * *

## **pawprt_k** 


*Mnemonics:* PAW PRinT K-point  
*Mentioned in topic(s):* [[topic:PAW]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






Forces the output of the all-electron wavefunction for only a single k-point.
To be used in conjuction with: **  
[[pawprtwf]]=1 ** and [[pawprt_b]]. The indexing follows the order in ouptput
of the internal variable ** kpt ** in the beginning of the run.


* * *

## **pawujat** 


*Mnemonics:* PAW+macro_UJ, ATom number  
*Mentioned in topic(s):* [[topic:DFT+U]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Comment:*  i.e. the first atom treated with PAW+U.  
Test list:

- tutorial:  [[tests/tutorial/Input/tudet_2.in]]
- v5:  [[tests/v5/Input/t39.in]]





Determines the atom for which U (or J) should be determined. See also
[[macro_uj]].


* * *

## **pawujrad** 


*Mnemonics:* PAW+macro_UJ, sphere RADius  
*Mentioned in topic(s):* [[topic:DFT+U]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 20 a.u.  
Test list:

- tutorial:  [[tests/tutorial/Input/tudet_2.in]]
- v5:  [[tests/v5/Input/t39.in]]





The sphere radius serves to extrapolate the U value calculated at r_paw to a
larger sphere radius. See also [[macro_uj]]. As most projector functions are
localized within r_paw to ≈80%, 20 a.u. contains ≈100% of the wavefunction and
corresponds to r_paw -&gt; ∞.


* * *

## **pawujv** 


*Mnemonics:* PAW+macro_UJ, potential shift (V)  
*Mentioned in topic(s):* [[topic:DFT+U]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.1 eV  
Test list:

- tutorial:  [[tests/tutorial/Input/tudet_2.in]]
- v5:  [[tests/v5/Input/t39.in]]





Amplitude of the potential shift for the determination of U (or J). See also
[[macro_uj]].


* * *

## **plowan_bandf** 


*Mnemonics:* Projected Local Orbital WANnier functions BAND Final  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Gives the upper band to include in the calculation of Wannier functions


* * *

## **plowan_bandi** 


*Mnemonics:* Projected Local Orbital WANnier functions BAND Initial  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Gives the lower band to include in the calculation of Wannier functions


* * *

## **plowan_compute** 


*Mnemonics:* Projected Local Orbital WANnier functions COMPUTATION  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Activate computation of Projected Local Orbital Wannier functions (PLO
Wannier) and corresponding band structure. Variables [[plowan_bandi]],
[[plowan_bandf]], [[plowan_natom]], [[plowan_nbl]], [[plowan_iatom]],
[[plowan_lcalc]], [[plowan_projcalc]] are mandatory to precise the nature of
the projections.

  * 0=&gt; Default value: do not activate calculation of PLO Wannier. 
  * 1=&gt; Compute PLO Wannier and band structure 
  * 2=&gt; Compute PLO Wannier and band structure. In this case, the coupling in k-space between blocks of Wannier functions belonging to different angular momenta or atoms is removed. 

Other related variables are [[plowan_realspace]], [[plowan_nt]],
[[plowan_it]]. The implementation is not symetrized over k-point and not
parallelized. (The calculation of projections is detailed in [ Phys. Rev. B
77, 205112, (2008)
](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.77.205112) )


* * *

## **plowan_iatom** 


*Mnemonics:* Projected Local Orbital WANnier functions, Index of ATOM  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Gives the indices of the [[plowan_natom]] atoms on which the projections will
be done.


* * *

## **plowan_it** 


*Mnemonics:* Projected Local Orbital WANnier functions,  Index of Translation.  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* (3,[[plowan_nt]])  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Requires [[plowan_realspace]] to be greater than 0 and [[plowan_nt]] to be
greater than 0. Precise a given set of selected real space translation by
using the real space vectors basis. These atoms are used to define Wannier
functions in real space. These real space Wannier functions are used as a
basis to compute the Hamiltonian.


* * *

## **plowan_lcalc** 


*Mnemonics:* Projected Local Orbital WANnier functions,  L values to use for CALCulation  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* (sum([[plowan_nbl]]))  
*Default value:* -1  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Gives the [[plowan_nbl]] values of angular momenta for each atom, in the order
of the atoms as given in [[plowan_iatom]].


* * *

## **plowan_natom** 


*Mnemonics:* Projected Local Orbital WANnier functions, Number of ATOMs  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Gives the number of atoms on which the projection will be done


* * *

## **plowan_nbl** 


*Mnemonics:* Projected Local Orbital WANnier functions,  NumBer of L values  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* ([[plowan_natom]])  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Gives the total number of angular momenta (over all atoms) to compute the
projections.


* * *

## **plowan_nt** 


*Mnemonics:* Projected Local Orbital WANnier functions,  Number of Translation on which the real space values of
energy are computed  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Requires [[plowan_realspace]] to be greater than 0. Gives a number of selected
atoms. These atoms are used to define Wannier functions in real space. These
real space Wannier functions are used as a basis to compute the Hamiltonian.


* * *

## **plowan_projcalc** 


*Mnemonics:* Projected Local Orbital WANnier functions,  PROJectors values to use for CALCulation  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* (sum([[plowan_nbl]]))  
*Default value:* -1  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





  
Gives the [[plowan_nbl]] values of projectors for each atom, in the order of
the atoms as given in [[plowan_iatom]]. The index i for the projectors refers
to the ith number on line orbitals of the PAW atomic data file.


* * *

## **plowan_realspace** 


*Mnemonics:* Projected Local Orbital WANnier functions,  activate REAL SPACE calculation.  
*Mentioned in topic(s):* [[topic:Wannier]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t71.in]], [[tests/v7/Input/t72.in]]





Can take the following values:

  * 0=&gt; Default value: do not activate calculation of real space Wannier functions. 
  * 1=&gt; Compute PLO Wannier in real space for analysis. These data can also be used in a following dataset to perform a Wannier interpolation. 
  * 2=&gt; Do simple Wannier Interpolation for a given k points starting from real space Wannier function Hamiltonian computed in a preceding dataset. 


* * *

## **prepscphon** 


*Mnemonics:* PREPare Self-Consistent PHONon calculation  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






Print PCINFO, PHFREQ, and PHVEC files, for use with self-consistent phonon
runs, after a perturbation calculation. Only prints out files for the present
q-point, and there is presently no tool to symmetrize or merge these files, so
use anaddb instead (with prtscphon input variable). The abinit input variable
is destined to someday bypass the use of anaddb for scphon calculations.


* * *

## **prtbltztrp** 


*Mnemonics:* PRinT output for BoLTZTRaP code  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v6:  [[tests/v6/Input/t11.in]]
- v7:  [[tests/v7/Input/t88.in]]





Print out geometry (_BLZTRP_GEOM) and eigenenergy (_BLZTRP_EIGEN) files for
the [ BoltzTraP
code](https://www.imc.tuwien.ac.at/forschungsbereich_theoretische_chemie/forschungsgruppen/prof_dr_gkh_madsen_theoretical_materials_chemistry/boltztrap/)
by Georg Madsen.


* * *

## **prtcif** 


*Mnemonics:* PRinT Crystallographic Information File  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- tutorial:  [[tests/tutorial/Input/tfold2bloch_1.in]]
- v6:  [[tests/v6/Input/t08.in]], [[tests/v6/Input/t09.in]]





If set to 1, a CIF file is output with the crystallographic data for the
present run (cell size shape and atomic positions).


* * *

## **prtdipole** 


*Mnemonics:* PRinT DIPOLE  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v6:  [[tests/v6/Input/t06.in]]





Print out dipole of unit cell, calculated in real space for the primitive cell
only. Under development.


* * *

## **prtnest** 


*Mnemonics:* PRinT NESTing function  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v6:  [[tests/v6/Input/t72.in]], [[tests/v6/Input/t90.in]]
- v7:  [[tests/v7/Input/t88.in]], [[tests/v7/Input/t90.in]]





If set to 1, the nesting function for the k-point grid is printed. For the
moment the path in q space for the nesting function is fixed, but will become
an input as well.


* * *

## **prtposcar** 


*Mnemonics:* PRinT POSCAR file  
*Mentioned in topic(s):* [[topic:printing]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v7:  [[tests/v7/Input/t01.in]]





Print out VASP-style POSCAR and FORCES files, for use with PHON or frophon
codes for frozen phonon calculations. See the associated script in
~abinit/extras/post_processing/phondisp2abi.py for further details on
interfacing with PHON, PHONOPY, etc...


* * *

## **recefermi** 


*Mnemonics:* RECursion - initial guess  of the FERMI Energy  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- mpiio:  [[tests/mpiio/Input/t42.in]]
- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). In the first SCF calculation it
fixes the initial guess for the Fermi energy.


* * *

## **recgratio** 


*Mnemonics:* RECursion - Grid RATIO  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
Test list:

- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). It represents the ratio of the two
grid step: [[recgratio]]=fine_step/coarse_step and it is bigger or equal than
1. It introduces a double-grid system which permits to compute the electronic
density on a coarse grid, using a fine grid (defined by [[ngfft]]) in the
discretisation of the green kernel (see [[recptrott]]). Successively the
density and the recursion coefficients are interpolated on the fine grid by
FFT interpolation. Note that ngfft/recgratio=number of points of the coarse
grid has to be compatible with the parallelization parameters.


* * *

## **recnpath** 


*Mnemonics:* RECursion - Number of point for PATH integral calculations  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 500  
Test list:

- mpiio:  [[tests/mpiio/Input/t42.in]]
- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). Determine the number of
discretisation points to compute some path integral in the recursion method ;
those path integrals are used to compute the entropy and the eigenvalues
energy. during the latest SFC cycles.


* * *

## **recnrec** 


*Mnemonics:* RECursion - Number of RECursions  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 10  
Test list:

- mpiio:  [[tests/mpiio/Input/t42.in]]
- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). Determine the maximum order of
recursion, that is the dimension of the krylov space we use to compute
density. If the precision set by [[rectolden]] is reached before that order,
the recursion method automatically stops.


* * *

## **recptrott** 


*Mnemonics:* RECursion - TROTTer parameter  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- mpiio:  [[tests/mpiio/Input/t42.in]]
- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). Determine the trotter parameter
used to compute the exponential of the hamiltonian in the recursion method:
exp(-beta*(-Delta + V)) ~ (exp(-beta/(4*recptrott) V) exp(-beta/(4*recptrott)
Delta) exp(-beta/(4*recptrott) V))^(2*recptrott). If set to 0, we use
recptrott = 1/2 in the above formula. Increasing [[recptrott]] improve the
accuracy of the trotter formula, but increase the dicretisation error: it may
be necessary to increase [[ngfft]]. The discretisation error is essentially
the discretisation error of the green kernel exp((recptrott/beta*|r|^2)) on
the ngfft grid.


* * *

## **recrcut** 


*Mnemonics:* RECursion - CUTing Radius  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- mpiio:  [[tests/mpiio/Input/t42.in]]
- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). Used to improve the computational
time in the case of the recursion method in a large cell: the density at a
point will be computed with taking account only of a sphere of radius
[[recrcut]].


* * *

## **rectesteg** 


*Mnemonics:* RECursion - TEST on Electron Gas  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- v5:  [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). It is used to test an electron gas
by putting the ion potential equal to zero.


* * *

## **rectolden** 


*Mnemonics:* RECursion - TOLerance on the difference of electronic DENsity  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Comment:* Default value to be changed.  
Test list:

- mpiio:  [[tests/mpiio/Input/t42.in]]
- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]





Used in Recursion method ([[tfkinfunc]]=2). Sets a tolerance for differences
of electronic density that, reached TWICE successively, will cause one SCF
cycle to stop. That electronic density difference is computed in the infinity
norm (that is, it is computed point-by-point, and then the maximum difference
is computed).


* * *

## **symmorphi** 


*Mnemonics:* SYMMORPHIc symmetry operation selection  
*Mentioned in topic(s):* [[topic:crystal]], [[topic:GW]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



With [[symmorphi]]=1, symmetry operations with a non-symmorphic vector are
allowed. With [[symmorphi]]=0, they are not allowed. In the latter case, if
the symmetry operations are specified in the input file, the code will stop
and print an error message if a non-symmorphic vector is encountered. By
contrast, if the symmetry operations are to be determined automatically (if
[[nsym]]=0), then the set of symmetries will not include the non-symmorphic
operations.

Note : this feature exist because in a previous status of the GW calculations,
non-symmorphic symmetry operations could not be exploited. Thus, the k points
were restricted to the IBZ. In order to prepare GW calculations, and to
perform GW calculations, [[symmorphi]]=0 was to be used, together with
[[nsym]]=0.


* * *

## **tfkinfunc** 


*Mnemonics:* Thomas-Fermi KINetic energy FUNCtional  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- mpiio:  [[tests/mpiio/Input/t42.in]]
- v4:  [[tests/v4/Input/t97.in]]
- v5:  [[tests/v5/Input/t75.in]], [[tests/v5/Input/t76.in]]
- v7:  [[tests/v7/Input/t11.in]]





  * [[tfkinfunc]]=1 : Thomas-Fermi kinetic functional (explicit functional of the density) is used instead of Kohn-Sham kinetic energy functional (implicit functional of the density through Kohn-Sham wavefunctions).  
See Perrot F., Phys. Rev. A20,586-594 (1979)).

  * [[tfkinfunc]]=11 : Thomas-Fermi-Weizsacker kinetic functional with Gradient Corrections is used.  
The convergence of a calculation with this functional needs to be initialized
from a calculation without Gradient Correction. This is automatically done
with [[tfkinfunc]]=11. For the initialization steps, the [[tfw_toldfe]]
criterion is used. When it is reached, then the Gradient Correction is added
and the SCF cycle continues.  
Note: to obtain the convergence of a Molecular Dynamics simulation with TFW,
it is necessary to find the best set of preconditionning parameters
([[diemix]], [[diemac]], [[dielng]]) and the best value of [[npulayit]] (if
the default Pulay mixing is used).

  * [[tfkinfunc]]=12 : same as **tfkinfunc**=11, but without the initialization steps. Gradient correction is directly added. 
  * [[tfkinfunc]]=2 : the Recursion Method is used in order to compute electronic density, entropy, Fermi energy and eigenvalues energy. This method computes the density without computing any orbital, is efficient at high temperature, with a efficient parallelization (almost perfect scalability). When that option is in use, the [[ecut]] input variable is no longer a convergence parameter ; [[ngfft]] becomes the main convergence parameter: you should adapt ecut for the ngfft grid you need (it is not yet automatically computed). Other convergence parameter are for the energetic values: [[recnrec]], [[recptrott]], [[recnpath]].  
Since the convergence of the self-consistent cycle is determined directly by
the convergence of the density: [[toldfe]], [[toldff]], [[tolrff]],
[[tolvrs]], [[tolwfr]] are not used, and are replaced by [[rectolden]]; the
energetic values, except for the fermi energy, are only computed during the
latest SFC cycle : the output file will show a jump of the total energy at the
end, but it is not because of a bad convergence behavior. Computational speed
can be improved by the use of [[recrcut]] and [[recgratio]]. The recursion
method has not be tested in the case of non cubic cell or with the use of
symmetries.  
In the recursion method the following variables are set to: [[useylm]]=1,
[[userec]]=1.


* * *

## **tfw_toldfe** 


*Mnemonics:* Thomas-Fermi-Weizsacker: TOLerance on the DiFference of total Energy, for initialization steps  
*Mentioned in topic(s):* [[topic:Recursion]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.0E-6 or [[toldfe]] is present  
*Only relevant if:* [[tfkinfunc]]=11  
Test list:

- v7:  [[tests/v7/Input/t11.in]]





This input variable has the same definition as [[toldfe]] and is only relevant
when [[tfkinfunc]]=11.  
It sets a tolerance for absolute differences of total energy that, reached
TWICE successively, will cause the initialization steps (without gradient
correction) to stop and the gradient correction to be added.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since it has the
'ENERGY' characteristics.


* * *

## **tolrde** 


*Mnemonics:* TOLerance on the Relative Difference of Eigenenergies  
*Mentioned in topic(s):* [[topic:SCFControl]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.005  
Test list:

- atompaw:  [[tests/atompaw/Input/t04.in]]
- tutoparal:  [[tests/tutoparal/Input/tdfpt_04.in]]





Sets a tolerance for the ratio of differences of eigenenergies in the line
minimisation conjugate-gradient algorithm. It compares the decrease of the
eigenenergy due to the last line minimisation, with the one observed for the
first line minimisation. When the ratio is lower than [[tolrde]], the next
line minimisations are skipped.  
The number of line minimisations is limited by [[nline]] anyhow.  
This stopping criterion is present for both GS and RF calculations. In RF
calculations, [[tolrde]] is actually doubled before comparing with the above-
mentioned ratio, for historical reasons.


* * *

## **use_gemm_nonlop** 


*Mnemonics:* USE the GEMM routine for the application of the NON-Local OPerator  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Comment:* because it is not usually worth using it unless bandpp is large and it requires additional memory  
Test list:

- paral:  [[tests/paral/Input/t25.in]], [[tests/paral/Input/t30.in]]





This keyword tells abinit to use a BLAS routine to speed up the computation of
the non-local operator. This requires the precomputation of a large matrix,
and has a significant memory overhead. In exchange, it provides improved
performance when used on several bands at once (Chebyshev or LOBPCG algorithm
with [[bandpp]]

The memory overhead is proportional to the number of atoms, the number of
plane waves, and the number of projectors per atom. It can be mitigated by
distributing the array with [[npfft]]

The performance depends crucially on having a good BLAS installed. Provided
the BLAS supports OpenMP, this option also yields very good scaling for the
nonlocal operator.


* * *

## **use_nonscf_gkk** 


*Mnemonics:* USE NON-SCF calculation of GKK matrix elements (electron phonon)  
*Mentioned in topic(s):* [[topic:ElPhonInt]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Comment:* Default is 0 for the moment. Do not use non-scf method.  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/teph_1.in]]
- v5:  [[tests/v5/Input/t85.in]]
- v6:  [[tests/v6/Input/t72.in]], [[tests/v6/Input/t90.in]]
- v7:  [[tests/v7/Input/t90.in]]





When this flag is activated during a phonon calculation with abinit, all of
the perturbations are cycled through, but only the symmetry-irreducible ones
are calculated self-consistently. For the others the perturbed density is
rotated by the appropriate symop and the gkk matrix elements are calculated
non-self-consistently. As they do not depend on the perturbed wave functions,
they are correct from the first iteration, and nstep is set to 1 for those
perturbations. Note that the resulting 1DEN files are simply the
rotate/symmetric ones and that the resulting 1WF files are garbage (completely
unconverged) except the matrix elements in the header (equivalent to GKK
files, but please use the latter much smaller files for el-ph calculations).
The new default behavior with [[use_nonscf_gkk]] = 1 should be transparent for
the user, with the same output files but a much quicker execution.

Caveat: Note that very tight convergence of ground state and phonon
calculations is necessary to get good GKK matrix elements! [[tolwfr]] = 1.e-24
or so is recommended everywhere. There may be problems using use_nonscf_gkk =
1 with non-symmorphic symmetries - please check (at least) that lifetimes for
phonons go to 0 for acoustic modes at Gamma.


* * *

## **usedmft** 


*Mnemonics:* USE Dynamical Mean Field Theory  
*Mentioned in topic(s):* [[topic:DMFT]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1, enable the use of DFT+DMFT, see in particular the important
variables [[dmft_solv]], [[dmftbandi]], [[dmftbandf]], [[dmft_nwli]],
[[dmft_nwlo]], [[dmft_tollc]], [[dmft_tolfreq]], and [[dmft_iter]].

The current implementation uses Wannier functions obtained from [ projected
local orbitals
](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.77.205112) as
correlated orbitals (see [[dmftbandi]] and [[dmftbandf]] input variables to
define them).

The Green functions are computed on a mesh of linear Matsubara frequencies.
However, most of the code uses logarithmic Matsubara grid to lower the
computational cost. Both [[dmft_nwli]] and [[dmft_nwlo]] are thus convergence
parameters.

DMFT is currently available for collinear ([[nspinor]]=1) polarized or
unpolarized calculations ([[nspden]]=[[nsppol]]=2 or [[nspden]]=[[nsppol]]=1)
and for non collinear calculations ([[nspinor]]=2,[[nspden]]=4,[[nsppol]]=1).
However it is not yet available for collinear antiferromagnetic calculations
([[nspden]]=2,[[nsppol]]=1) and non collinear non magnetic calculations
([[nspden]]=1, [[nsppol]]=1,[[nspinor]]=2). CTQMC calculations
([[dmft_solv]]=5) are not yet possible if [[nspinor]]=2.

Only static calculations without relaxation or dynamics are possible (forces
and stress are not computed in the scheme: so the computed values should NOT
be trusted).

When correlated density matrices are diagonal, all values of [[upawu]] and
[[jpawu]] are possible. If the correlated density matrices are non diagonal,
only [[jpawu]] = 0 is implemented.

Relevant direct output quantities from converged DMFT calculations are total
energy and occupation of correlated orbitals. For Hubbard I calculation
([[dmft_solv]]=2), total and partial spectral functions can be obtained with
prtdos=1 and can be found in files OUTSpFunc* (where OUT is the root for
output files). For CTQMC calculations ([[dmft_solv]]=5), imaginary time
impurity Green function are output of the calculations and can be used to
produce spectral function using an external Maximum Entropy Code.

A typical DFT+DMFT calculation involves two runs. First, a DFT calculation is
fully converged (even unoccupied wavefunctions have to be converged). Then,
the DFT+DMFT calculation is started using DFT wavefunctions or density files.
As DFT+DMFT calculations (with CTQMC) are computationnally expensive, it is
convenient to use prtden=-1, to write DEN file at each DFT iteration, in order
to be able to restart the calculation easily.

For details of the implementation see, [ B. Amadon, F. Lechermann, A. Georges,
F. Jollet, T. O. Wehling, and A. I. Lichtenstein, Phys. Rev. B 77(20), (2008)
](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.77.205112) , for
Wannier functions and B. Amadon, J. Phys.: Condens. Matter 24 075604 (2012)
(doi:10.1088/0953-8984/24/7/075604), for self-consistency and Hubbard I
implementation. If [[usedmft]]=1 and [[nbandkss]]/=0, then, the DFT+DMFT
calculation is not done and only projections are computed at the end of the
calculation. They can be used by an external code or used to compute the
screened interaction (see variable [[ucrpa]]).


* * *

## **useria** 


*Mnemonics:* USER Integer variable A  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






These are user-definable integers which the user may input and then utilize in
subroutines of his/her own design. They are not used in the official versions
of the ABINIT code, and should ease independent developments (hopefully
integrated in the official version afterwards).  
Internally, they are available in the dtset structured datatype, e.g.
dtset%useria .


* * *

## **userib** 


*Mnemonics:* USER Integer variable B  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






These are user-definable integers which the user may input and then utilize in
subroutines of his/her own design. They are not used in the official versions
of the ABINIT code, and should ease independent developments (hopefully
integrated in the official version afterwards).  
Internally, they are available in the dtset structured datatype, e.g.
dtset%useria .


* * *

## **useric** 


*Mnemonics:* USER Integer variable C  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






These are user-definable integers which the user may input and then utilize in
subroutines of his/her own design. They are not used in the official versions
of the ABINIT code, and should ease independent developments (hopefully
integrated in the official version afterwards).  
Internally, they are available in the dtset structured datatype, e.g.
dtset%useria .


* * *

## **userid** 


*Mnemonics:* USER Integer variable D  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






These are user-definable integers which the user may input and then utilize in
subroutines of his/her own design. They are not used in the official versions
of the ABINIT code, and should ease independent developments (hopefully
integrated in the official version afterwards).  
Internally, they are available in the dtset structured datatype, e.g.
dtset%useria .


* * *

## **userie** 


*Mnemonics:* USER Integer variable E  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:






These are user-definable integers which the user may input and then utilize in
subroutines of his/her own design. They are not used in the official versions
of the ABINIT code, and should ease independent developments (hopefully
integrated in the official version afterwards).  
Internally, they are available in the dtset structured datatype, e.g.
dtset%useria .


* * *

## **userra** 


*Mnemonics:* USER Real variable A  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
Test list:






These are user-definable with the same purpose as [[useria]] and cie.


* * *

## **userrb** 


*Mnemonics:* USER Real variable B  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
Test list:






These are user-definable with the same purpose as [[useria]] and cie.


* * *

## **userrc** 


*Mnemonics:* USER Real variable C  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
Test list:






These are user-definable with the same purpose as [[useria]] and cie.


* * *

## **userrd** 


*Mnemonics:* USER Real variable D  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
Test list:






These are user-definable with the same purpose as [[useria]] and cie.


* * *

## **userre** 


*Mnemonics:* USER Real variable E  
*Mentioned in topic(s):* [[topic:Dev]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
Test list:






These are user-definable with the same purpose as [[useria]] and cie.


* * *

## **useylm** 


*Mnemonics:* USE YLM (the spherical harmonics)  
*Mentioned in topic(s):* [[topic:TuningSpeed]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[tfkinfunc]]==1,
1 if [[usepaw]]==1,
0 otherwise.
  
Test list:

- built-in:  [[tests/built-in/Input/testin_wannier90.in]]
- v4:  [[tests/v4/Input/t01.in]], [[tests/v4/Input/t02.in]], [[tests/v4/Input/t03.in]]
- wannier90:  [[tests/wannier90/Input/t00.in]], [[tests/wannier90/Input/t01.in]], [[tests/wannier90/Input/t02.in]]





When this flag is activated, the non-local operator is applied using an
algorithm based on spherical harmonics. Non-local projectors are used with
their usual form:  

P  lmn  (r)=Y  lm  (r)*p  ln  (r)

  
  
When [[useylm]]=0, the sum over Y_lm can be reduced to a Legendre polynomial
form.


* * *

## **wfoptalg** 


*Mnemonics:* WaveFunction OPTimisation ALGorithm  
*Mentioned in topic(s):* [[topic:SCFAlgorithms]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* [[AUTO_FROM_PSP]]  
*Comment:* 0 when [[usepaw]]=0 (norm-conserving pseudopotentials), 10 when [[usepaw]]=1 (PAW) ; 114 if [[paral_kgb]]=1.  



Allows one to choose the algorithm for the optimisation of the wavefunctions.  
The different possibilities are :

  * [[wfoptalg]]=0 : standard state-by-state conjugate gradient algorithm, with no possibility to parallelize over the states; 
  * [[wfoptalg]]=2 : minimisation of the residual with respect to different shifts, in order to cover the whole set of occupied bands, with possibility to parallelize over blocks of states (or bands). The number of states in a block is defined in [[nbdblock]]. THIS IS STILL IN DEVELOPMENT. 
  * [[wfoptalg]]=3 : minimisation of the residual with respect to a shift. Available only in the non-self-consistent case [[iscf]]=-2, in order to find eigenvalues and wavefunctions close to a prescribed value. 
  * [[wfoptalg]]=4 : (see also [[wfoptalg]]=14), a parallel code based on the Locally Optimal Block Preconditioned Conjugate Gradient (LOBPCG) method of Knyazev. [ Reference : A.V. Knyazev, "Toward the Optimal Preconditioned Eigensolver : Locally Optimal Block Preconditioned Conjugate Gradient Method". SIAM Journal on Scientific Computing 23, pp517-541 (2001) ](http://dx.doi.org/10.1137/S1064827500366124) . The implementation rests on the [ matlab program by Knyazev ](http://www.mathworks.com/matlabcentral/fileexchange/48-lobpcg-m) . [ Reference A. V. Knyazev, I. Lashuk, M. E. Argentati, and E. Ovchinnikov, Block Locally Optimal Preconditioned Eigenvalue Xolvers (BLOPEX) in hypre and PETSc (2007). SIAM Journal on Scientific Computing (SISC). 25(5): 2224-2239 ](http://dx.doi.org/10.1137/060661624) . For more information see [ F. Bottin, S. Leroux, A. Knyazev, G. Zerah, Large scale ab initio calculations based on three levels of parallelization. (2008). Computational Material Science, 42(2), 329-336. ](http://dx.doi.org/10.1016/j.commatsci.2007.07.019)
  * [[wfoptalg]]=10 : (for PAW) standard state-by-state conjugate gradient algorithm, with no possibility to parallelize over the states, but modified scheme described in Kresse, Furthmuller, PRB 54, 11169 (1996) (modified kinetic energy, modified preconditionning, minimal orthogonalization, ...) ; 
  * [[wfoptalg]]=14 : the recommended for parallel code, the same as [[wfoptalg]]=4 except that the preconditioning of the block vectors does not depend on the kinetic energy of each band, and the orthogonalization after the LOBPCG algorithm is no longer performed. The first modification increases the convergence and the second one the efficiency. 
  * [[wfoptalg]]=114 : A new version of [[wfoptalg]]=14 which is more efficient for few blocks and can take advantage of OpenMP if abinit is compiled with a multithreaded linear algebra library. With more than 1 thread [[npfft]] shoud NOT be used for the time being. 
  * [[wfoptalg]]=1 : new algorithm based on Chebyshev filtering, designed for very large number of processors, in the regime where LOBPCG does not scale anymore. It is not able to use preconditionning and therefore might converge slower than other algorithms. By design, it will ** not ** converge the last bands: it is recommended to use slightly more bands than necessary. For usage with [[tolwfr]], it is imperative to use [[nbdbuf]]. For more performance, try [[use_gemm_nonlop]]. For more information, see the [ performance guide ](../../theory/howto_chebfi.pdf) and the [ paper ](https://arxiv.org/abs/1406.4350) by A. Levitt and M. Torrent. Status: experimental but usable. Questions and bug reports should be sent to antoine (dot) levitt (at) gmail.com. 


* * *

## **xc_denpos** 


*Mnemonics:* eXchange-Correlation - DENsity POSitivity value  
*Mentioned in topic(s):* [[topic:xc]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1e-14  
Test list:

- libxc:  [[tests/libxc/Input/t13.in]]





For the evaluation of the exchange-correlation functionals, the density cannot
be negative, or even too small (e.g. the LDA exchange kernel behaves like the
density at power -(2/3), and the density is used at the denominator of
different factors in GGAs and metaGGAs. [[xc_denpos]] is the smallest value
that the density can assume at the time of the evaluation of a XC functional,
in ABINIT. When then computed density drops below [[xc_denpos]] before
attacking the evaluation of the XC functional, then it will be (only for that
purpose) replaced by [[xc_denpos]]. Note that the evaluation of the gradients
or other quantities that are density-dependent is performed before this
replacement.

It has been observed that the SCF cycle of the Tran-Blaha mGGA can be quite
hard to make converge, for systems for which there is some vacuum. In this
case, setting [[xc_denpos]] to 1.0e-7 ... 1.0e-6 has been seen to allow good
convergence. Of course, this will affect the numerical results somehow, and
one should play a bit with this value to avoid incorrect calculations.


* * *

## **xc_tb09_c** 


*Mnemonics:* Value of the c parameter in the eXchange-Correlation TB09 functional  
*Mentioned in topic(s):* [[topic:xc]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 99.99  
Test list:

- libxc:  [[tests/libxc/Input/t13.in]]





The modified Becke-Johnson exchange-correlation functional by Tran and Blaha
(Phys. Rev. Lett. 102, 226401 (2009)) reads :

V_x(r) = c * V_x^{BR}(r) + (3*c - 2) * 1/pi * sqrt(5/12) *
sqrt(2*kden(r)/den(r))

in which V_x^{BR}(r) is the Becke-Roussel potential.

In this equation the parameter c can be evaluated at each SCF step according
to the following equation :

c = alpha + beta * sqrt(1/V_{cell} * \int_{V_{cell}} |grad(den(r))|/den(r)
d3r)

The c parameter is evaluated thanks to the previous equation when xc_tb09_c is
equal to the "magic" default value 99.99. The c parameter can also be fixed to
some (property-optimized or material-optimized) value by using this variable.


* * *

