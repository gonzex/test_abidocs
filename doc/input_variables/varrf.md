## **bdeigrf** 


*Mnemonics:* BanD for second-order EIGenvalues from Response-Function  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* -1  
*Only relevant if:* [[ieig2rf]] in [1,2,3,4,5]  



that is, if the user is performing second-order eigenvalue calculations using
response-functions.  
  
The variable [[bdeigrf]] is the maximum number of bands for which the second-
order eigenvalues must be calculated: the full number of bands is still used
during the computation of these corrections.  
  
If [[bdeigrf]] is set to -1, the code will automatically set [[bdeigrf]] equal
to nband.


* * *

## **d3e_pert1_atpol** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 1: limits of ATomic POLarisations  
*Variable type:* integer  
*Dimensions:* (2)  
*Default value:* [1, 1]  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Controls the range of atoms for which displacements will be considered in non-
linear computations (using the 2n+1 theorem), for the 1st perturbation.  
May take values from 1 to [[natom]], with
**d3e_pert1_atpol**(1)&lt;=**d3e_pert1_atpol**(2).  
See [[rfatpol]] for additional details.


* * *

## **d3e_pert1_dir** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 1: DIRections  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Gives the directions to be considered in non-linear computations (using the
2n+1 theorem), for the 1st perturbation.  
The three elements corresponds to the three primitive vectors, either in real
space (atomic displacement), or in reciprocal space (electric field
perturbation).  
See [[rfdir]] for additional details.


* * *

## **d3e_pert1_elfd** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 1: ELectric FielD  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Turns on electric field perturbation in non-linear computation, as 1st
perturbation. Actually, such calculations requires first the non-self-
consistent calculation of derivatives with respect to k, independently of the
electric field perturbation itself.  
See [[rfelfd]] for additional details.


* * *

## **d3e_pert1_phon** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 1: PHONons  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Turns on atomic displacement perturbation in non-linear computation, as 1st
perturbation.  
See [[rfphon]] for additional details.


* * *

## **d3e_pert2_atpol** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 2: limits of ATomic POLarisations  
*Variable type:* integer  
*Dimensions:* (2)  
*Default value:* [1, 1]  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Controls the range of atoms for which displacements will be considered in non-
linear computations (using the 2n+1 theorem), for the 2nd perturbation.  
May take values from 1 to [[natom]], with
**d3e_pert2_atpol**(1)&lt;=**d3e_pert2_atpol**(2).  
See [[rfatpol]] for additional details.


* * *

## **d3e_pert2_dir** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 2: DIRections  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Gives the directions to be considered in non-linear computations (using the
2n+1 theorem), for the 2nd perturbation.  
The three elements corresponds to the three primitive vectors, either in real
space (atomic displacement), or in reciprocal space (electric field
perturbation).  
See [[rfdir]] for additional details.


* * *

## **d3e_pert2_elfd** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 2: ELectric FielD  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Turns on electric field perturbation in non-linear computation, as 2nd
perturbation. Actually, such calculations requires first the non-self-
consistent calculation of derivatives with respect to k, independently of the
electric field perturbation itself.  
See [[rfelfd]] for additional details.


* * *

## **d3e_pert2_phon** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 2: PHONons  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Turns on atomic displacement perturbation in non-linear computation, as 2nd
perturbation.  
See [[rfphon]] for additional details.


* * *

## **d3e_pert3_atpol** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 3: limits of ATomic POLarisations  
*Variable type:* integer  
*Dimensions:* (2)  
*Default value:* [1, 1]  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Controls the range of atoms for which displacements will be considered in non-
linear computations (using the 2n+1 theorem), for the 3rd perturbation.  
May take values from 1 to [[natom]], with
**d3e_pert3_atpol**(1)&lt;=**d3e_pert3_atpol**(2).  
See [[rfatpol]] for additional details.


* * *

## **d3e_pert3_dir** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 3: DIRections  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Gives the directions to be considered in non-linear computations (using the
2n+1 theorem), for the 3rd perturbation.  
The three elements corresponds to the three primitive vectors, either in real
space (atomic displacement), or in reciprocal space (electric field
perturbation).  
See [[rfdir]] for additional details.


* * *

## **d3e_pert3_elfd** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 3: ELectric FielD  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Turns on electric field perturbation in non-linear computation, as 3rd
perturbation. Actually, such calculations requires first the non-self-
consistent calculation of derivatives with respect to k, independently of the
electric field perturbation itself.  
See [[rfelfd]] for additional details.


* * *

## **d3e_pert3_phon** 


*Mnemonics:* 3rd Derivative of Energy, mixed PERTurbation 3: PHONons  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[optdriver]]==5 (non-linear response computations)  



Turns on atomic displacement perturbation in non-linear computation, as 3rd
perturbation.  
See [[rfphon]] for additional details.


* * *

## **dfpt_sciss** 


*Mnemonics:* DFPT SCISSor operator  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0  



It is the value of the "scissors operator", the shift of conduction band
eigenvalues, used in response function calculations.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since ** ecut ** has
the '[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)  
Typical use is for response to electric field ([[rfelfd]]=3), but NOT for d/dk
([[rfelfd]]=2) and phonon responses.


* * *

## **efmas** 


*Mnemonics:* EFfective MASs  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Turns on effective mass tensor calculations. Such calculations requires the
non-self-consistent calculation of derivatives with respect to k, in the same
dataset. It must therefore be used with [[rfelfd]]=2.  

  * 0=&gt;no effective mass tensor calculation 
  * 1=&gt;effective mass tensor calculation 

At the present time, both norm-conserving (NC) and PAW calculations are
supported. Also, for PAW calculations only, [[nspinor]]==2 and
[[pawspnorb]]==1 (i.e. spin-orbit (SO) calculations) is supported. NC SO
calculations are NOT currently supported. Also, for both NC and PAW,
[[nspden]]/=1 and [[nsppol]]/=1 are NOT supported.


* * *

## **efmas_bands** 


*Mnemonics:* EFfective MASs, BANDS to be treated.  
*Variable type:* integer  
*Dimensions:* (2,[[nkpt]])  
*Default value:* The full range of band available in the calculation for each k-point.  
*Only relevant if:* [[efmas]]==1  



This variable controls the range of bands for which the effective mass is to
be calculated. If a band is degenerate, all other bands of the degenerate
group will automatically be treated, even if they were not part of the user
specified range.


* * *

## **efmas_calc_dirs** 


*Mnemonics:* EFfective MASs, CALCulate along DIRectionS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[efmas]]==1  



Allows the user to calculate the scalar effective mass of all bands specified
by [[efmas_bands]] along specific directions in reciprocal space. This is
particularly useful when considering degenerate bands, which are usually
warped, and thus cannot have their dispersion (hessian) and effective mass
expressed as a tensor. This allows the user to see the more complex angular
behavior of effective masses in these cases, for instance.

When [[efmas_calc_dirs]]==0, no directions are read from the input file (using
[[efmas_dirs]]) and the effective masses along the 3 cartesian directions are
output by default.

When [[efmas_calc_dirs]]==1, 2 or 3, [[efmas_n_dirs]] directions are read from
[[efmas_dirs]], assuming cartesian, reduced or angular (theta,phi)
coordinates, respectively. In the case [[efmas_calc_dirs]]==3, 2 real values
per directions are read, whereas 3 real values are read in the two other
cases.


* * *

## **efmas_deg** 


*Mnemonics:* EFfective MASs, activate DEGenerate formalism  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[efmas]]>0  



Activate (==1) or not (==0) the treatment of degenerate bands (within a
criterion [[efmas_deg_tol]]) using the transport equivalent effective mass
idea (see [PRB 89 155131 (2014)](https://doi.org/10.1103/PhysRevB.89.155131)).


* * *

## **efmas_deg_tol** 


*Mnemonics:* EFfective MASs, DEGeneracy TOLerance  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1e-05  
*Only relevant if:* [[efmas_deg]]==1  



Energy difference below which 2 bands are considered degenerate (and treated
using the formalism activated with [[efmas_deg]]==1). [[efmas_deg_tol]] has
the '[[ENERGY]]' characteristics.


* * *

## **efmas_dim** 


*Mnemonics:* EFfective MASs, DIMension of the effective mass tensor  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 3  
*Only relevant if:* [[efmas]]==1  



For 2D or 1D systems, the band dispersion goes to 0 perpendicular to the
system, which causes the inverse effective mass to be singular, i.e. the
effective mass to be NaN. This keyword circumvents the problem by eliminating
the troublesome dimensions from the inverse effective mass.

In 2D, the Z axis is ignored and, in 1D, the Z and Y axis are ignored.

Also, note that in the 2D degenerate case, a subtlety arises: the 'transport
equivalent' effective mass does not determine the scale of the transport
tensors (conductivity and others). Therefore, for this specific case, the
factor by which these transport tensors should be scaled once determined from
the 'transport equivatlent' effective mass tensor is output separately on the
line immediately after the effective mass.


* * *

## **efmas_dirs** 


*Mnemonics:* EFfective MASs, DIRectionS to be calculated  
*Variable type:* real  
*Dimensions:* (3 or 2,[[efmas_n_dirs]])  
*Default value:* 0  
*Only relevant if:* [[efmas_calc_dirs]]>0  



List of [[efmas_n_dirs]] directions to be considered according to the value of
[[efmas_calc_dirs]]. The directions are specified by 3 real values if
[[efmas_calc_dirs]]==1 or 2 and by 2 real values if [[efmas_calc_dirs]]==3.


* * *

## **efmas_n_dirs** 


*Mnemonics:* EFfective MASs, Number of DIRectionS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[efmas_calc_dirs]]>0  



Number of directions in [[efmas_dirs]], to be considered according to
[[efmas_calc_dirs]].


* * *

## **efmas_ntheta** 


*Mnemonics:* EFfective MASs, Number of points for integration w/r to THETA  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1000  
*Only relevant if:* [[efmas]]==1 and [[efmas_bands]]==(degenerate band index)  



When a band is degenerate, the usual definition of effective mass becomes
invalid. However, it is still possible to define a 'transport equivalent mass
tensor' that reproduces the contribution of the band to the conductivity
tensor. To obtain this tensor, an integration over the solid sphere is
required. The default value gives a tensor accurate to the 4th decimal in Ge.


* * *

## **elph2_imagden** 


*Mnemonics:* ELectron-PHonon interaction at 2nd order : IMAGinary shift of the DENominator  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Only relevant if:* [[ieig2rf]] != 0  



that is, if the user is performing performing second-order eigenvalue
calculations using response-functions.  
  
The variable [[elph2_imagden]] determines the imaginary shift of the
denominator of the sum-over-states in the perturbation denominator,
(e_{nk}-e_{n'k'}+i [[elph2_imagden]]). One should use a width comparable with
the Debye frequency or the maximum phonon frequency.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since ** ecut ** has
the '[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)


* * *

## **eph_task** 


*Mnemonics:* Electron-PHonon: Task  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



When [[optdriver]]==7, select the task to be performed. The choice is among :  
[[eph_task]]=1 : phonon linewidth  
[[eph_task]]=2 : electron-phonon coupling elements


* * *

## **esmear** 


*Mnemonics:* Eigenvalue SMEARing  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.01  
*Only relevant if:* [[smdelta]] != 0  



that is, if the user is performing simulations of the electronic lifetimes
induced by the electron-phonon coupling.  
  
The variable [[esmear]] determines the width of the functions approximating
the delta function, \delta(e_{nk}-e_{n'k'}), present in the expression of the
lifetimes. One should use a width comparable with the Debye frequency or the
maximum phonon frequency.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since ** ecut ** has
the '[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)


* * *

## **frzfermi** 


*Mnemonics:* FReeZe FERMI energy  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Can be used to suppress artificially the first-order change of Fermi energy,
in case of Response Function calculation for metals at Q=0. The input variable
[[frzfermi]], if set to 1, allows to suppress this contribution, but this is
incorrect.


* * *

## **ieig2rf** 


*Mnemonics:* Integer for second-order EIGenvalues from Response-Function  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If [[ieig2rf]] is greater then 0, the code will produce a file, named with the
trailing suffix _EIGR2D, containing the second-order electronic eigenvalues
for the perturbation. These files are used in the calculation of the thermal
correction to the electronic eigenvalues.  
  
If [[ieig2rf]] is set to 1, the second-order electronic eigenvalues will be
calculated from the DFPT method (Sternheimer).  
If [[ieig2rf]] is set to 2, the second-order electronic eigenvalues will be
calculated from the Allen-Cardona method. (sum over states)  
If [[ieig2rf]] is set to 3, the second-order electronic eigenvalues will be
calculated from the DFPT method (sum over states) but using a different part
of the code. This is equivalent to [[ieig2rf]] = 1 [debuging]  
If [[ieig2rf]] is set to 4, the second-order electronic eigenvalues will be
calculated from the dynamical DFPT method (Sternheimer). The code will
generate _EIGR2D.nc files that contain the electron-phonon matrix element
squared on the space orthogonal to the active space. The code will also
produce _FAN.nc files that contain the electron-phonon matrix elements
squared. Note that [[ieig2rf]]=4 can only be used if Abinit is compiled with
NETCDF support.  
If [[ieig2rf]] is set to 5, the second-order electronic eigenvalues will be
calculated from the dynamical DFPT method (Sternheimer). The code will
generate _EIGR2D.nc files that contain the electron-phonon matrix element
square on the space orthogonal to the active space. The code will also produce
_GKK.nc files that contain electron-phonon matrix elements. This option is
preferable for large system to [[ieig2rf]]=4 as the GKK files take less much
less disk space and memory (but run a little bit slower). Note that
[[ieig2rf]]=5 can only be used if Abinit is compiled with NETCDF support.  
Related variables :
[[bdeigrf]],[[elph2_imagden]],[[getgam_eig2nkq]],[[smdelta]] Related variables
: [[bdeigrf]],[[elph2_imagden]],[[getgam_eig2nkq]],[[smdelta]]


* * *

## **ph_ngqpt** 


*Mnemonics:* PHonons: Number of Grid points for Q-PoinT mesh.  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [20, 20, 20]  



This variable defines the q-mesh used to compute the phonon DOS and the
Eliashberg function via Fourier interpolation. Related input variables:
[[ph_qshift]] and [[ph_nqshift]].


* * *

## **ph_qpath** 


*Mnemonics:* Phonons: Q-PATH  
*Variable type:* real  
*Dimensions:* (3,ph_nqpath)  
*Default value:* None  
*Only relevant if:* specified([[ph_nqpath]])  



This array contains the list of special q-points used to construct the q-path
for phonon band structures and phonon linewidths. See also [[ph_nqpath]] and
[[[ph_ndivsm]].


* * *

## **prepanl** 


*Mnemonics:* PREPAre Non-Linear response calculation  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



The computation of third-order derivatives from the 2n+1 theorem requires the
first-order wavefunctions and densities obtained from a linear response
calculation. The standard approach in a linear response calculation is (i) to
compute only the irreducible perturbations, and (ii) to use symmetries to
reduce the number of k-points for the k-point integration.  
This approach cannot be applied, presently (v4.1), if the first-order
wavefunctions are to be used to compute third-order derivatives. First, for
electric fields, the code needs the derivatives along the three directions.
Still, in case of phonons, only the irreducible perturbations are required.
Second, for both electric fields and phonons, the wavefunctions must be
available in half the BZ (kptopt=2), or the full BZ (kptopt=3).  
During the linear response calculation, in order to prepare a non-linear
calculation, one should put [[prepanl]] to 1 in order to force ABINIT (i) to
compute the electric field perturbation along the three directions explicitly,
and (ii) to keep the full number of k-points.


* * *

## **prepgkk** 


*Mnemonics:* PREPAre GKK calculation  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



The calculation of electron-phonon coupling quantities requires the presence
of all the perturbations (all atoms in all directions) for the chosen set of
(irreducible) q-points. To impose this and prevent ABINIT from using symmetry
to reduce the number of perturbations, set [[prepgkk]] to 1. Use in
conjunction with [[prtgkk]].


* * *

## **prtbbb** 


*Mnemonics:* PRinT Band-By-Band decomposition  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If [[prtbbb]] is 1, print the band-by-band decomposition of Born effective
charges and localization tensor, in case they are computed. See Ph. Ghosez and
X. Gonze, J. Phys.: Condens. Matter 12, 9179 (2000).


* * *

## **rf2_dkdk** 


*Mnemonics:* Response Function : 2nd Derivative of wavefunctions with respect to K  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



UNUSABLE (in development)

Activates computation of second derivatives of wavefunctions with respect to
wavevectors. This is not strictly a response function but is a needed
auxiliary quantity in the calculations of 3rd-order derivatives of the energy
(non-linear response). The directions for the derivatives are determined by
[[rfdir]] (TO BE CORRECTED!).

  * 0=&gt;no derivative calculation 
  * 1=&gt;calculation along diagonal directions (d2/(dk_i dk_i), natom+10 is activated) 
  * 2=&gt;calculation along off-diagonal directions (d2/(dk_i dk_j), natom+11 is activated) 
  * 3=&gt;calculation along all directions (both natom+10 and natom+11 are activated) 


* * *

## **rfasr** 


*Mnemonics:* Response Function : Acoustic Sum Rule  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Control the evaluation of the acoustic sum rule in effective charges and
dynamical matrix at Gamma within a response function calculation (not active
at the level of producing the DDB, but at the level of the phonon
eigenfrequencies output).

  * 0 =&gt; no acoustic sum rule imposed 
  * 1 =&gt; acoustic sum rule imposed for dynamical matrix at Gamma, and charge neutrality imposed with extra charge evenly distributed among atoms 
  * 2 =&gt; acoustic sum rule imposed for dynamical matrix at Gamma, and charge neutrality imposed with extra charge given proportionally to those atoms with the largest effective charge. 

The treatment of the acoustic sum rule and charge neutrality sum rule is finer
at the level of the ANADDB utility, with the two independent input variables [
asr ](../../users/generated_files/help_anaddb.html#asr) and [ chneut
](../../users/generated_files/help_anaddb.html#chneut) .


* * *

## **rfatpol** 


*Mnemonics:* Response Function : ATomic POLarisation  
*Variable type:* integer  
*Dimensions:* (2)  
*Default value:* [1, 1]  



Control the range of atoms for which displacements will be considered in
phonon calculations (atomic polarizations), using the 2n+1 theorem.  
These values are only relevant to phonon response function calculations.  
May take values from 1 to [[natom]], with [[rfatpol]](1)&lt;=[[rfatpol]](2).  
The atoms to be moved will be defined by the  
do-loop variable iatpol :  
do iatpol=[[rfatpol]](1),[[rfatpol]](2)  
For the calculation of a full dynamical matrix, use [[rfatpol]](1)=1 and
[[rfatpol]](2)=[[natom]], together with [[rfdir]] 1 1 1 . For selected
elements of the dynamical matrix, use different values of [[rfatpol]] and/or
[[rfdir]]. The name 'iatpol' is used for the part of the internal variable
ipert when it runs from 1 to [[natom]]. The internal variable ipert can also
assume values larger than [[natom]], denoting perturbations of electric field
or stress type (see [ the response function help file
](../../users/generated_files/help_respfn.html) ).


* * *

## **rfddk** 


*Mnemonics:* Response Function with respect to Derivative with respect to K  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Activates computation of derivatives of ground state wavefunctions with
respect to wavevectors. This is not strictly a response function but is a
needed auxiliary quantity in the electric field calculations (see [[rfelfd]])
The directions for the derivatives are determined by [[rfdir]].

  * 0=&gt;no derivative calculation 
  * 1=&gt;calculation of first derivatives of wavefunctions with respect to k points (d/dk calculation). The exact same functionality is provided by [[rfelfd]] = 2. 


* * *

## **rfdir** 


*Mnemonics:* Response Function : DIRections  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  



Gives the directions to be considered for response function calculations (also
for the Berry phase computation of the polarization, see the [[berryopt]]
input variable).  
The three elements corresponds to the three primitive vectors, either in real
space (phonon calculations), or in reciprocal space (d/dk, homogeneous
electric field, homogeneous magnetic field calculations). So, they generate a
basis for the generation of the dynamical matrix or the macroscopic dielectric
tensor or magnetic susceptibility and magnetic shielding, or the effective
charge tensors.  
If equal to 1, response functions, as defined by [[rfddk]], [[rfelfd]],
[[rfphon]], [[rfdir]] and [[rfatpol]], are to be computed for the
corresponding direction. If 0, this direction should not be considered.


* * *

## **rfelfd** 


*Mnemonics:* Response Function with respect to the ELectric FielD  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Turns on electric field response function calculations. Actually, such
calculations requires first the non-self-consistent calculation of derivatives
with respect to k, independently of the electric field perturbation itself.

  * 0=&gt;no electric field perturbation 
  * 1=&gt;full calculation, with first the derivative of ground-state wavefunction with respect to k (d/dk calculation), by a non-self-consistent calculation, then the generation of the first-order response to an homogeneous electric field 
  * 2=&gt;only the derivative of ground-state wavefunctions with respect to k 
  * 3=&gt;only the generation of the first-order response to the electric field, assuming that the data on derivative of ground-state wavefunction with respect to k is available on disk. 

(Note : because the tolerances to be used for derivatives or homogeneous
electric field are different, one often does the calculation of derivatives in
a separate dataset, followed by calculation of electric field response as well
as phonon.  
The options 2 and 3 proves useful in that context ; also, in case a scissor
shift is to be used, it is usually not applied for the d/dk response).


* * *

## **rfmagn** 


*Mnemonics:* Response Function with respect to MAGNetic B-field perturbation  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



It must be equal to 1 to run response function calculations with respect to
external magnetic field. Currently, orbital magnetism is not taken into
account and the perturbing potential has Zeeman form.


* * *

## **rfmeth** 


*Mnemonics:* Response Function METHod  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Selects method used in response function calculations. Presently, only 1 is
allowed.


* * *

## **rfphon** 


*Mnemonics:* Response Function with respect to PHONons  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



It must be equal to 1 to run phonon response function calculations.


* * *

## **rfstrs** 


*Mnemonics:* Response Function with respect to STRainS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used to run strain response-function calculations (e.g. needed to get elastic
constants). Define, with [[rfdir]], the set of perturbations.

  * 0=&gt;no strain perturbation 
  * 1=&gt;only uniaxial strain(s) (ipert=natom+3 is activated) 
  * 2=&gt;only shear strain(s) (ipert=natom+4 is activated) 
  * 3=&gt;both uniaxial and shear strain(s) (both ipert=natom+3 and ipert=natom+4 are activated) 

See the possible restrictions on the use of strain perturbations, in the [
respfn help file ](../../users/generated_files/help_respfn.html#1) .


* * *

## **rfuser** 


*Mnemonics:* Response Function, USER-defined  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Available to the developpers, to activate the use of ipert=natom+6 and
ipert=natom+7, two sets of perturbations that the developpers can define.  

  * 0=&gt;no computations for ipert=natom+6 or ipert=natom+7 
  * 1=&gt;response with respect to perturbation natom+6 will be computed 
  * 2=&gt;response with respect to perturbation natom+7 will be computed 
  * 3=&gt;responses with respect to perturbations natom+6 and natom+7 will be computed 

In order to define and use correctly the new perturbations, the developper
might have to include code lines or additional routines at the level of the
following routines : dfpt_cgwf.F90, dfpt_dyout.F90, dfpt_symph.F90,
dfpt_dyout.F90, dfpt_etot.F90, littlegroup_pert.F90, dfpt_looppert.F90,
dfpt_mkcor.F90, dfpt_nstdy.F90, dfpt_nstwf.F90, respfn.F90, dfpt_scfcv.F90,
irreducible_set_pert.F90, dfpt_vloca.F90, dfpt_vtorho.F90, dfpt_vtowfk.F90. In
these routines, the developper should pay a particular attention to the rfpert
array, defined in the routine respfn.F90 , as well as to the ipert local
variable.


* * *

## **smdelta** 


*Mnemonics:* SMeared DELTA function  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



When [[smdelta]] in non-zero, it will trigger the calculation of the imaginary
part of the second-order electronic eigenvalues, which can be related to the
electronic lifetimes. The delta function is evaluated using:  

  * when [[smdelta]] == 1, Fermi-Dirac smearing : 0.25_dp/(cosh(xx/2.0_dp)**2 
  * when [[smdelta]] == 2, Cold smearing by Marzari using the parameter a=-.5634 (minimization of the bump): exp(-xx2)/sqrt(pi) * (1.5d0+xx*(-a*1.5d0+xx*(-1.0d0+a*xx))) 
  * when [[smdelta]] == 3, Cold smearing by Marzari using the parameter a=-.8165 (monotonic function in the tail): as 2 but different a 
  * when [[smdelta]] == 4, Smearing of Methfessel and Paxton (PRB40,3616(1989)) with Hermite polynomial of degree 2, corresponding to "Cold smearing" of N. Marzari with a=0 (so, same smeared delta function as smdelta=2, with different a). 
  * when [[smdelta]] == 5, Gaussian smearing : 1.0d0*exp(-xx**2)/sqrt(pi) 


* * *

## **td_maxene** 


*Mnemonics:* Time-Dependent dft : MAXimal kohn-sham ENErgy difference  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



The Matrix to be diagonalized in the Casida framework (see "Time-Dependent
Density Functional Response Theory of Molecular systems: Theory, Computational
Methods, and Functionals", by M.E. Casida, in Recent Developments and
Applications of Modern Density Functional Theory, edited by J.M. Seminario
(Elsevier, Amsterdam, 1996).) is a NxN matrix, where, by default, N is the
product of the number of occupied states by the number of unoccupied states.  
The input variable [[td_maxene]] allows to diminish N : it selects only the
pairs of occupied and unoccupied states for which the Kohn-Sham energy
difference is less than [[td_maxene]]. The default value 0.0 means that all
pairs are taken into account.  
See [[td_mexcit]] for an alternative way to decrease N.


* * *

## **td_mexcit** 


*Mnemonics:* Time-Dependent dft : Maximal number of EXCITations  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0  



The Matrix to be diagonalized in the Casida framework (see "Time-Dependent
Density Functional Response Theory of Molecular systems: Theory, Computational
Methods, and Functionals", by M.E. Casida, in Recent Developments and
Applications of Modern Density Functional Theory, edited by J.M. Seminario
(Elsevier, Amsterdam, 1996).) is a NxN matrix, where, by default, N is the
product of the number of occupied states by the number of unoccupied states.  
The input variable [[td_mexcit]] allows to diminish N : it selects the first
[[td_mexcit]] pairs of occupied and unoccupied states, ordered with respect to
increasing Kohn-Sham energy difference. However, when [[td_mexcit]] is zero,
all pairs are allowed.  
See [[td_maxene]] for an alternative way to decrease N.


* * *
