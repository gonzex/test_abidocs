## **asr** 


*Mnemonics:* Acoustic Sum Rule  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Govern the imposition of the Acoustic Sum Rule (ASR) in phonon calculations.
Same meaning as the corresponding anaddb variable.


* * *

## **chneut** 


*Mnemonics:* CHarge NEUTrality treatment   
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Set the treatment of the Charge Neutrality requirement for the effective
charges. Same meaning as the corresponding anaddb variable.


* * *

## **ddb_ngqpt** 


*Mnemonics:* Derivative DatabBase: Number of Grid points for Q-PoinTs  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  



This variable is mandatory when [[optdriver]]==7. It defines the number of
divisions in the (homogeneous) q-mesh used to generate the DDB file. See also
the description of the [[getddb]] input variable.


* * *

## **ddb_shiftq** 


*Mnemonics:* Derivative DataBase: SHIFT of the Q-points   
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* [0.0, 0.0, 0.0]  



Only relevant when [[optdriver]]==7. It defines the shift in the q-mesh used
to generate the DDB file, which is defined by the [[ddb_ngqpt]] input
variable. See [[shiftk]] for more information on the definition.


* * *

## **dipdip** 


*Mnemonics:* DIPole-DIPole interaction   
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



This variable defines the treatment of the dipole-dipole interaction. Same
meaning as the corresponding anaddb variable


* * *

## **eph_extrael** 


*Mnemonics:* Electron-PHonon: EXTRA ELectrons  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
* * *

## **eph_fermie** 


*Mnemonics:* Electron-PHonon: FERMI Energy  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



This variable can be used to change the value of the Fermi level when
performing electron-phonon calculations with [[optdriver]]==7. This variable
has effect only if set to a non-zero value. See also [[eph_extrael]].


* * *

## **eph_fsewin** 


*Mnemonics:* Electron-Phonon: Fermi Surface Energy WINdow  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.01 Hartree  



This variable defines the energy window around the Fermi level used for e-ph
calculations ([[optdriver]] = 7). Only the states located in the energy range
[efermi - eph_fsewin, efermi + eph_fsewin] are included in the e-ph
calculation.

Related input variables: [[eph_intmeth]], [[eph_fsmear]], [[eph_extrael]] and
[[eph_fermie]].


* * *

## **eph_fsmear** 


*Mnemonics:* Electron-PHonon: Fermi surface SMEARing  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.01 Hartree  
*Only relevant if:* [[eph_intmeth]] == 1  



This variable defines the gaussian broadening used for the integration over
the Fermi surface when [[eph_intmeth]] == 1.


* * *

## **eph_intmeth** 


*Mnemonics:* Electron-Phonon: INTegration METHod  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2  



This variable defines the technique for the integration on the Fermi surface
of electron-phonon quantities.

1 for Gaussian technique with broadening factor [[eph_fsmear]]. 2 for
tetrahedron method.

See also [[eph_fsewin]], [[eph_extrael]] and [[eph_fermie]].


* * *

## **eph_mustar** 


*Mnemonics:* Electron-PHonon : MU STAR (electron-electron interaction strength)  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.1  



Average electron-electron interaction strength, for the computation of the
superconducting Tc using Mc-Millan's formula.


* * *

## **eph_ngqpt_fine** 


*Mnemonics:* Electron-PHonon : Number of Grid Q-PoinTs in FINE grid.  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  



This variable activates the interpolation of the first-order variation of the
self-consistent potential in the electron-phonon code. If eph_nqgpt_fine
differs from [0, 0, 0], the code will use the Fourier transform to interpolate
the DFPT potentials on this fine q-mesh starting from the irreducible set of
q-points read from the DDB file. This approach is similar to the one used to
interpolate the interatomic force constants in q-space. If eph_ngqpt_fine is
not given, the EPH code uses the list of irreducible q-points reported in the
DDB file (default behavior).


* * *

## **eph_transport** 


*Mnemonics:* Electron-PHonon: TRANSPORT flag  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



NB - this does not work yet. This variable can be used to turn on the
calculation of transport quantities in the eph module of abinit. Value of 1
corresponds to elastic LOVA as in the PRB by Savrasov and Savrasov


* * *

## **ph_intmeth** 


*Mnemonics:* PHonons: INTegration METHod  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2  



Select the integration technique for computing the phonon DOS and the
Eliashberg function a2fF(w).

  
1 for Gaussian scheme (see also [[ph_smear]]).  
  
2 for tetrahedron method (no other input is needed but requires at least 4
q-points in the BZ)


* * *

## **ph_ndivsm** 


*Mnemonics:* PHonons: Number of DIVisions for sampling the SMallest segment  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 20  



This variable is used in conjunction with [[ph_nqpath]] and [[ph_qpath]] to
define the q-path used for phonon band structures and phonon linewidths. It
gives the number of points used to sample the smallest segment in the q-path
specified by [[ph_qpath]].


* * *

## **ph_nqpath** 


*Mnemonics:* PHonons: Number of Q-points defining the PATH  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



This integer defines the number of points in the [[ph_qpath]] array.


* * *

## **ph_nqshift** 


*Mnemonics:* PHonons: Number of Q-SHIFTs  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



This variable defines the number of shifts in the q-mesh used for the phonon
DOS and for the Eliashberg functions (see [[ph_ngqpt]]). If not given, the
code assumes a Gamma-centered mesh. The shifts are specified by [[ph_qshift]].


* * *

## **ph_qshift** 


*Mnemonics:* PHonons: Q-SHIFTs for mesh.  
*Variable type:* real  
*Dimensions:* (3,ph_nqshift)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[ph_nqshift]]  



This array gives the shifts to be used to construct the q-mesh for computing
the phonon DOS and the Eliashberg functions (see also [[ph_nqshift]]. If not
given, a Gamma-centered mesh is used.


* * *

## **ph_smear** 


*Mnemonics:* PHonons: SMEARing factor  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.00002 Hartree  
*Only relevant if:* [[ph_intmeth]]==1  



The gaussian broadening used for the integration of the phonon DOS and the
Eliashberg function. See also [[ph_intmeth]] and [[ph_ngqpt]].


* * *

## **ph_wstep** 


*Mnemonics:* PHonons: frequency(W)  STEP.  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.1 meV  



The step used to generate the (linear) frequency mesh for the phonon DOS and
the Eliashberg function. The extrema of the mesh are automatically computed by
the code.


* * *

## **prtphbands** 


*Mnemonics:* PRinT PHonon BANDS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



This option activates the output of the phonon frequencies in the EPH code.
Possible values:

  * 0 Disable the output of the phonon frequencies.
  * 1 Write frequencies in xmgrace format. A file with extension `PHBANDS.agr` is produced. Use `xmgrace file_PHBANDS.agr` to visualize the data
  * 2 Write frequencies in gnuplot format. The code produces a `PHBANDS.dat` file with the eigenvalues and a `PHBANDS.gnuplot` script. Use `gnuplot file_PHBANDS.gnuplot` to visualize the phonon band structure.


* * *

## **prtphdos** 


*Mnemonics:* PRinT the PHonon Density Of States  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Print the phonon density of states. It is activated by default when
[[optdriver]]==7.


* * *

## **prtphsurf** 


*Mnemonics:* PRinT PHonon iso-SURFace  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Print a bxsf file (Xcrysden format) with the (interpolated) phonon frequencies
computed of the q-mesh determined by [[ph_ngqpt]]. The file can be use to
visualize isosurfaces with Xcrysden or other similar tools supporting the bxsf
format. Note that the (dense) q-mesh must be Gamma-centered, shifted meshs are
not supported by Xcrysden. This variable requires [[optdriver]]==7.


* * *

## **symdynmat** 


*Mnemonics:* SYMmetrize the DYNamical MATrix  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



If symdynmat is equal to 1, the dynamical matrix is symmetrized before the
diagonalization (same meaning as the corresponding anaddb variable). Note that
symdynmat==1 will automatically enable the symmetrization of the electron-
phonon linewidths.


* * *
