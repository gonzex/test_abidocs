---
description: ffield input variables
rpath: /variables/ffield.md
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->
# ffield input variables

This document lists and provides the description of the name (keywords) of the
ffield input variables to be used in the input file for the abinit executable.

## **atvshift** 


*Mnemonics:* ATomic potential (V) energy SHIFTs  
*Characteristics:* [[DEVELOP]]  
*Mentioned in topic(s):* [[topic:DFT+U]]  
*Variable type:* real  
*Dimensions:* ([[natvshift]],[[nsppol]],[[natom]])  
*Default value:* *0.0d0  
*Only relevant if:* [[usepawu]] /= 0 and [[natvshift]] in [5,7]  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - v5:  [[tests/v5/Input/t14.in|t14.in]], [[tests/v5/Input/t15.in|t15.in]]






Defines for each atom and each spin channel (at present, can only be used with
[[nsppol]]=1 or 2, like the +U scheme), a possible potential shift, for the d
(with [[lpawu]]=2, [[natvshift]]=5), or f states (with [[lpawu]]=3,
[[natvshift]]=7). In the case of d states, and 2 spin channels, a set of 10
numbers for each atom must be defined. The first set of 5 numbers corresponds
to real spherical harmonics m=-2 to m=+2 for the spin-up channel, the second
set of 5 numbers corresponds to real spherical harmonics m=-2 to m=+2 for the
spin-down channel. In the case of f states, the same ordering applies, for
sets of 7 numbers, corresponding to m=-3 to m=+3.  
[[usepawu]] should be non-zero, [[lpawu]] should be 2 or 3.

## **bdberry** 


*Mnemonics:* BanD limits for BERRY phase  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* integer  
*Dimensions:* (4)  
*Default value:* 4*0  
*Only relevant if:* [[berryopt]] in [1, 2, 3] and [[nberry]] > 0  

??? note "Test list (click to open). Rarely used, [7/920] in all abinit tests, [1/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv2_81.in|tsv2_81.in]], [[tests/seq/Input/tsv2_82.in|tsv2_82.in]], [[tests/seq/Input/tsv3_03.in|tsv3_03.in]], [[tests/seq/Input/tsv3_04.in|tsv3_04.in]], [[tests/seq/Input/tsv3_05.in|tsv3_05.in]]
    - tutorespfn:  [[tests/tutorespfn/Input/telast_5.in|telast_5.in]]
    - v4:  [[tests/v4/Input/t66.in|t66.in]]






Give the lower band and the upper band of the set of bands for which the Berry
phase must be computed. Irrelevant if [[nberry]] is not positive. When
[[nsppol]] is 1 (no spin-polarisation), only the two first numbers, giving the
lower and highest bands, are significant. Their occupation number is assumed
to be 2. When [[nsppol]] is 2 (spin-polarized calculation), the two first
numbers give the lowest and highest bands for spin up, and the third and
fourth numbers give the lowest and highest bands for spin down. Their
occupation number is assumed to be 1 .

Presently, [[bdberry]] MUST be initialized by the user in case of a Berry
phase calculation with [[berryopt]] = 1, 2, or 3: the above-mentioned default
will cause an early exit.

## **berryopt** 


*Mnemonics:* BERRY phase OPTions  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  

??? note "Test list (click to open). Moderately used, [40/920] in all abinit tests, [7/116] in abinit tutorials"
    - paral:  [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]]
    - seq:  [[tests/seq/Input/tsv2_81.in|tsv2_81.in]], [[tests/seq/Input/tsv2_82.in|tsv2_82.in]], [[tests/seq/Input/tsv3_03.in|tsv3_03.in]], [[tests/seq/Input/tsv3_04.in|tsv3_04.in]], [[tests/seq/Input/tsv3_05.in|tsv3_05.in]], [[tests/seq/Input/tsv4_55.in|tsv4_55.in]], [[tests/seq/Input/tsv4_78.in|tsv4_78.in]], [[tests/seq/Input/tsv4_80.in|tsv4_80.in]], [[tests/seq/Input/tsv5_112.in|tsv5_112.in]], [[tests/seq/Input/tsv5_113.in|tsv5_113.in]], [[tests/seq/Input/tsv6_121.in|tsv6_121.in]], [[tests/seq/Input/tsv6_122.in|tsv6_122.in]], [[tests/seq/Input/tsv6_123.in|tsv6_123.in]], [[tests/seq/Input/tsv6_124.in|tsv6_124.in]], [[tests/seq/Input/tsv6_125.in|tsv6_125.in]], [[tests/seq/Input/tsv6_126.in|tsv6_126.in]], [[tests/seq/Input/tsv7_70.in|tsv7_70.in]]
    - tutorespfn:  [[tests/tutorespfn/Input/telast_4.in|telast_4.in]], [[tests/tutorespfn/Input/telast_5.in|telast_5.in]], [[tests/tutorespfn/Input/tffield_1.in|tffield_1.in]], [[tests/tutorespfn/Input/tffield_2.in|tffield_2.in]], [[tests/tutorespfn/Input/tffield_4.in|tffield_4.in]], [[tests/tutorespfn/Input/tffield_5.in|tffield_5.in]], [[tests/tutorespfn/Input/tffield_6.in|tffield_6.in]]
    - v4:  [[tests/v4/Input/t66.in|t66.in]], [[tests/v4/Input/t72.in|t72.in]], [[tests/v4/Input/t75.in|t75.in]]
    - v5:  [[tests/v5/Input/t23.in|t23.in]]
    - v6:  [[tests/v6/Input/t06.in|t06.in]], [[tests/v6/Input/t20.in|t20.in]], [[tests/v6/Input/t42.in|t42.in]], [[tests/v6/Input/t43.in|t43.in]]
    - v7:  [[tests/v7/Input/t03.in|t03.in]]






Specifies the use of Berry phase for the computation of either the
polarization, the derivatives with respect to the wavevector, or finite
electric field calculations.

  * 0 =&gt; no computation of expressions relying on a Berry phase (default) 
  * 1 =&gt; the computation of Berry phases is activated (berryphase routine) 
  * 2 =&gt; the computation of derivatives with respect to the wavevector, thanks to the Berry phase finite-difference formula, is activated (uderiv routine) 
  * 3 =&gt; same as option 1 and 2 together 
**Note that options 1 to 3 require the use of a serial build of Abinit.**
  * -1 =&gt; alternative computation of Berry phases (berryphase_new routine) 
  * -2 =&gt; alternative computation of derivatives with respect to the wavevector, thanks to the Berry phase finite-difference formula (berryphase_new routine) 
  * -3 =&gt; same as option -1 and -2 together 
**Options -1 to -3 permit use of a parallel build and will be preferred by most users.**
  * 4 =&gt; finite electric field calculation (unreduced E-field) 
  * 6 =&gt; finite electric displacement field calculation (unreduced D-field) 
  * 14 =&gt; finite reduced electric field calculation 
  * 16 =&gt; finite electric displacement field calculation 
  * 17 =&gt; mixed electric boundary condition: finite reduced electric field in some directions, finite reduced electric displacement field along other directions. See variable [[jfielddir]] for more details. 

Other related input variables are :

  * in case of [[berryopt]]=1,2, or 3 : [[bdberry]] and [[kberry]]; also, [[nberry]] must be larger than 0; 
  * in case of [[berryopt]]=-1,-2, or -3 : the variable [[rfdir]] must be used to specify the primitive vector along which the projection of the polarization or the ddk will be computed. For example if [[berryopt]]=-1 and [[rfdir]]=1 0 0, the projection of the polarization along the reciprocal lattice vector G_1 is computed. In case [[rfdir]]=1 1 1, ABINIT computes the projection of P along G_1, G_2 and G_3 and transforms the results to cartesian coordinates; 
  * in cases where [[berryopt]] is negative, [[berrystep]] allow a computation of multiple-step Berry phase in order to accelerate the convergence. 
  * [[efield]] and [[rfdir]] in case of [[berryopt]]=4 ; 

The cases [[berryopt]]=-1,-2,-3, 4, 6, 7, 14, 16, and 17 have to be used with
[[occopt]]=1.

The cases [[berryopt]]=-1 and 4, 6, 7, 14, 16, 17 are compatible with PAW,
howevever, if in these cases one uses [[kptopt]]/=3, one must also use only
symmorphic symmetries (either because the space group is symmorphic or the
variable [[symmorphi]] is set to zero).

For a phonon calculation under a finite electric field, respect the following
procedure.

  * 1\. Run a scf ground-state calculation at zero electric field to get wavefunctions to initialize the ground-state calculation in finite electric fields. 
  * 2\. Run a scf ground-state calculation in finite electric field. The electric field is controlled by the input variable [[efield]]. [[berryopt]] should be 4. The input variable [[kptopt]] should be set to be 2. 
  * 3\. Based on the wave functions obtained in step (2), perform phonon calculation by setting [[berryopt]]=4, [[kptopt]]=3 and The same value of [[efield]] than in step 2. [[nsym]] should be set to 1 currently but this restriction may be removed later . The other parameters are the same as phonon calculation at zero electric field. 
  * Note : the choice of k-point sampling N x N x N should be the same in the three runs and N should be an even number. 

In case of finite electric and displacement field calculations
([[berryopt]]=4,6,7,14,16,17), see also the input variables [[berrysav]],
[[dfield]], [[red_dfield]], [[red_efield]], [[ddamp]]

## **berrysav** 


*Mnemonics:* BERRY SAVe  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  

??? note "Test list (click to open). Rarely used, [1/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_124.in|tsv6_124.in]]






  * 0 =&gt; for finite electric field calculation ([[berryopt]]=4/14), the polarization branch will be chosen on each iteration from (-pi, pi); for finite electric displacement field calculation([[berryopt]]=6/7/16/17), the polarization will be chosen to minimize the internal energy. 
  * 1 =&gt; the polarization will be kept in the same branch on each iteration. At the end of the run, a file "POLSAVE" will be saved containing the reduced polarization in atomic units. Note: Make sure that "POLSAVE" is empty or it does not exist before the calculation, or else that it specifies the desired polarization branch. 

## **berrystep** 


*Mnemonics:* BERRY phase : multiple STEP  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* 0 > [[berryopt]]  

??? note "Test list (click to open). Rarely used, [1/920] in all abinit tests, [0/116] in abinit tutorials"
    - v6:  [[tests/v6/Input/t20.in|t20.in]]






If [[berryopt]] is negative, this variable is used to compute berry phases
using multiple discrete steps, in order to accelerate convergence. The single-
step berry phase is the standard calculation using strings of k-points based
on overlap of Bloch function separated by dk, while the two-step berry phase
use strings use overlaps based on dk and 2*dk, the three-step use overlaps
based on dk, 2*dk and 3*dk...

The default value of this variable is 1, meaning that only the single-step
berry phase calculation is done. If a larger value is set, ABINIT will compute
all the multiple-step berry phase from the single-step to the
[[berrystep]]-step, and use the large-step values of berry phase to correct
the single-step berry phase. Use with care: while experience is still to be
gained with this procedure, the outlook is promising.

## **bfield** 


*Mnemonics:* finite B FIELD calculation  
*Mentioned in topic(s):* [[topic:MagField]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*0.0  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - paral:  [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]]
    - v6:  [[tests/v6/Input/t43.in|t43.in]]






Perform finite magnetic field calculation.  
**THIS CODE IS UNDER DEVELOPMENT AND IS NOT READY FOR USE.**

## **ddamp** 


*Mnemonics:* electric Displacement field DAMPing parameter  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.1  
*Only relevant if:* [[berryopt]] = 6 or 16  

??? note "Test list (click to open). Rarely used, [5/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_121.in|tsv6_121.in]], [[tests/seq/Input/tsv6_122.in|tsv6_122.in]], [[tests/seq/Input/tsv6_124.in|tsv6_124.in]], [[tests/seq/Input/tsv6_125.in|tsv6_125.in]], [[tests/seq/Input/tsv6_126.in|tsv6_126.in]]






In case [[berryopt]]=6, the electric field is updated after each SCF iteration
according to E_{n+1}= [[ddamp]]*(D - 4*pi*P_{n}) + (1-[[ddamp]])*E_{n} where
P_{n} and E_{n} are the polarization and electric field after nth SCF
iteration. [[ddamp]] is a damping parameter used to control the convergence
speed.  
In case [[berryopt]]=16, the electric field is updated after each SCF
iteration according to e_{n+1}= [[ddamp]]*(d - p_{n}) + (1-[[ddamp]])*e_{n}  
If you have difficulty getting convergence, try to reduce this value or reduce
maxestep. This parameter is used in finite electric displacement field
calculations (berryopt=6,16,17).

## **dfield** 


*Mnemonics:* Displacement FIELD  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*0.0  
*Only relevant if:* [[berryopt]] = 6, [[efield]]  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_122.in|tsv6_122.in]], [[tests/seq/Input/tsv6_124.in|tsv6_124.in]], [[tests/seq/Input/tsv6_125.in|tsv6_125.in]], [[tests/seq/Input/tsv6_126.in|tsv6_126.in]]






In case [[berryopt]]=6, [[dfield]] specifies the (unreduced) finite electric
displacement field vector, in atomic units, that is to be imposed as a
constraint during the calculation.

## **efield** 


*Mnemonics:* Electric FIELD  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*0.0  
*Only relevant if:* [[berryopt]] = 4 or 6  

??? note "Test list (click to open). Moderately used, [22/920] in all abinit tests, [1/116] in abinit tutorials"
    - paral:  [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]]
    - seq:  [[tests/seq/Input/tsv4_55.in|tsv4_55.in]], [[tests/seq/Input/tsv4_78.in|tsv4_78.in]], [[tests/seq/Input/tsv4_80.in|tsv4_80.in]], [[tests/seq/Input/tsv6_121.in|tsv6_121.in]], [[tests/seq/Input/tsv6_122.in|tsv6_122.in]], [[tests/seq/Input/tsv6_123.in|tsv6_123.in]], [[tests/seq/Input/tsv6_124.in|tsv6_124.in]], [[tests/seq/Input/tsv6_125.in|tsv6_125.in]], [[tests/seq/Input/tsv6_126.in|tsv6_126.in]], [[tests/seq/Input/tsv7_70.in|tsv7_70.in]]
    - tutorespfn:  [[tests/tutorespfn/Input/tffield_6.in|tffield_6.in]]
    - v5:  [[tests/v5/Input/t23.in|t23.in]]
    - v6:  [[tests/v6/Input/t42.in|t42.in]], [[tests/v6/Input/t43.in|t43.in]]
    - v7:  [[tests/v7/Input/t03.in|t03.in]]






In case [[berryopt]]=4, a finite electric field calculation is performed. The
value of this electric field, and its direction is determined by [[efield]].
It must be given in atomic units (1 a.u. of electric field= 514220624373.482
V/m, see note below), in cartesian coordinates.

References for the calculation under electric field (based on multi k point
Berry phase) :

  * Nunes and Vanderbilt, PRL 73, 712 (1994) : real-space version of the finite-field Hamiltonian 
  * Nunes and Gonze, PRB 63, 155107 (2001) : reciprocal-space version of the finite-field Hamiltonian (the one presently implemented), and extensive theoretical analysis 
  * Souza, Iniguez and Vanderbilt, PRL 89, 117602 (2003) : implementation of the finite-field Hamiltonian (reciprocal-space version) 
  * Zwanziger, Galbraith, Kipouros, Torrent, Giantomassi and Gonze, Comp. Mater. Sci. 58, 113 (2012) : extension to PAW formalism 

See also Umari, Gonze, Pasquarello, PRL 90, 027401 (2003).

The atomic unit of electric field strength is : e_Cb/(4 pi eps0 a0**2), where
e_Cb is the electronic charge in Coulomb (1.60217653e-19), eps0 is the
electric constant (8.854187817d-12 F/m), and a0 is the Bohr radius in meter
(0.5291772108e-10).

## **jfielddir** 


*Mnemonics:* electric/displacement FIELD DIRection  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* 3*0  
*Only relevant if:* [[berryopt]] = 17  

??? note "Test list (click to open). Rarely used, [1/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_125.in|tsv6_125.in]]






When specifying mixed electric field boundary conditions ( [[berryopt]]=17),
jfielddir controls whether reduced electric field ([[jfielddir]]=1) or reduced
electric displacement field ([[jfielddir]]=2) is chosen to be fixed, in each
of the three lattice directions (i.e., in the reduced, not the Cartesian,
frame). For example, [[jfielddir]]=(1 1 2) tells the code to use fixed ebar_1
and ebar_2 along the first two lattice directions and fixed d_3 along the
third.  
For the case of mixed electric field boundary conditions, [[red_efieldbar]]
and [[red_dfield]] are used to control ebar and d, respectively. For example,
for electric boundary conditions corresponding to a material in a parallel-
plate capacitor, if you want to control d_3=d0, while fixing ebar_1=ebar_2=0,
then the input files should have [[berryopt]]=17, [[jfielddir]]=(1 1 2),
[[red_efieldbar]]=(0.0 0.0 a), and [[red_dfield]]=(b c d0). Here a, b, and c
are the starting values. They can be chosen in this way: do a single run for
fixed d calculation ([[red_dfield]]=0,0,d0), from the final results you will
have ebar_3, which is a good guess for a. Then do another single run for fixed
ebar calculation ([[red_efieldbar]]=(0 0 0)), from the final results you will
have d_1,d_2, these are good guesses for b, c.

## **kberry** 


*Mnemonics:* K wavevectors for BERRY phase computation  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* integer  
*Dimensions:* (3,[[nberry]])  
*Default value:* *0  
*Only relevant if:* [[berryopt]] = 1, 2, or 3  

??? note "Test list (click to open). Rarely used, [5/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv2_81.in|tsv2_81.in]], [[tests/seq/Input/tsv2_82.in|tsv2_82.in]], [[tests/seq/Input/tsv3_03.in|tsv3_03.in]], [[tests/seq/Input/tsv3_04.in|tsv3_04.in]], [[tests/seq/Input/tsv3_05.in|tsv3_05.in]]






Used for values of [[berryopt]] = 1, 2, or 3.

This array defines, for each Berry phase calculation (the number of such
calculations is defined by [[nberry]]), the difference of wavevector between k
points for which the overlap matrix must be computed. The polarisation vector
will be projected on the direction of that wavevector, and the result of the
computation will be the magnitude of this projection. Doing more than one
wavevector, with different independent direction, allows to find the full
polarisation vector. However, note that converged results need oriented grids,
denser along the difference wavevector than usual Monkhorst-Pack grids.

The difference of wavevector is computed in the coordinate system defined by
the k-points grid (see [[ngkpt]] and [[kptrlatt]]), so that the values of
[[kberry]] are integers. Of course, such a k point grid must exist, and all
the corresponding wavefunctions must be available, so that the computation is
allowed only when [[kptopt]] is equal to 3. In order to save computing time,
it is suggested to make a preliminary calculation of the wavefunctions on the
irreducible part of the grid, with [[kptopt]] equal to 1, and then use these
converged wavefunctions in the entire Brillouin zone, by reading them to
initialize the [[kptopt]]=3 computation.

## **maxestep** 


*Mnemonics:* MAXimum Electric field STEP  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.005  
*Only relevant if:* [[berryopt]] = 6, 16, or 17  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_122.in|tsv6_122.in]], [[tests/seq/Input/tsv6_126.in|tsv6_126.in]]






This variable controls the maximum change of electric field when updating the
electric field after each SCF iteration. When the calculation is difficult to
converge, try reducing this value or reducing [[ddamp]]. This variable is used
in finite electric displacement field calculations ([[berryopt]]=6,16,17).

## **natvshift** 


*Mnemonics:* Number of ATomic potential (V) energy SHIFTs (per atom)  
*Mentioned in topic(s):* [[topic:DFT+U]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[usepawu]] /= 0, [[atvshift]]  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - v5:  [[tests/v5/Input/t14.in|t14.in]], [[tests/v5/Input/t15.in|t15.in]]






Number of atomic potential energy shifts (per atom), to be used to define the
array [[atvshift]]. If non-zero, only two possibilities exist : 5 for d states
(with [[lpawu]]=2), and 7 for f states (with [[lpawu]]=3). If non-zero, one
should define [[usepawu]], [[lpawu]] and [[atvshift]].

## **nberry** 


*Mnemonics:* Number of BERRY phase computations  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[berryopt]] = 1, 2, or 3  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv2_81.in|tsv2_81.in]], [[tests/seq/Input/tsv2_82.in|tsv2_82.in]], [[tests/seq/Input/tsv3_03.in|tsv3_03.in]], [[tests/seq/Input/tsv3_04.in|tsv3_04.in]]






Gives the number of Berry phase computations of polarisation, or finite-
difference estimations of the derivative of wavefunctions with respect to the
wavevector, each of which might be characterized by a different change of
wavevector [[kberry]].

When equal to 0, no Berry phase calculation of polarisation is performed. The
maximal value of [[nberry]] is 20.

Note that the computation of the polarisation for a set of bands having
different occupation numbers is meaningless (although in the case of spin-
polarized calculations, the spin up bands might have an identical occupation
number, that might differ from the identical occupation number of spin down
bands). Although meaningless, ABINIT will perform such computation, if
required by the user. The input variable [[bdberry]] governs the set of bands
for which a Berry phase is computed.

For the [[berryopt]] = 1, 2, and 3 cases, spinor wavefunctions are not
allowed, nor are parallel computations.

## **polcen** 


*Mnemonics:* POLarization for CENtrosymmetric geometry  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*0  

??? note "Test list (click to open). Rarely used, [1/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_126.in|tsv6_126.in]]






When doing a finite electric displacement field calculation, if the structure
is centrosymmetric but the polarization is non-zero (such as for AlAs), this
non-zero polarization should be specified as [[polcen]] (in REDUCED
coordinates, in atomic units) in the input file. See Eq.(24) in the Suppl. of
Nat. Phys. (M. Stengel, N.A. Spaldin and D. Vanderbilt, Nat. Phys. 5,304
(2009))

## **qprtrb** 


*Mnemonics:* Q-wavevector of the PERTurbation  
*Characteristics:* [[DEVELOP]]  
*Mentioned in topic(s):* [[topic:Artificial]]  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[vprtrb]]  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - v6:  [[tests/v6/Input/t01.in|t01.in]], [[tests/v6/Input/t02.in|t02.in]]






Gives the wavevector, in units of reciprocal lattice primitive translations,
of a perturbing potential of strength [[vprtrb]]. See [[vprtrb]] for more
explanation.

## **red_dfield** 


*Mnemonics:* REDuced Displacement FIELD  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*0.0  
*Only relevant if:* [[berryopt]] = 16, [[red_efield]]  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_122.in|tsv6_122.in]], [[tests/seq/Input/tsv6_125.in|tsv6_125.in]]






In case [[berryopt]]=16, a reduced finite electric displacement field
calculation is performed. The value of this displacement field, and its
direction is determined by [[red_dfield]]. It must be given in atomic units.

[[red_dfield]] is defined via Eq.(26) in the Supplement of M. Stengel, N.A.
Spaldin and D. Vanderbilt, Nat. Phys. 5,304 (2009).

## **red_efield** 


*Mnemonics:* REDuced Electric FIELD  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*0.0  
*Only relevant if:* [[berryopt]] = 16  

??? note "Test list (click to open). Rarely used, [3/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_121.in|tsv6_121.in]], [[tests/seq/Input/tsv6_122.in|tsv6_122.in]], [[tests/seq/Input/tsv6_125.in|tsv6_125.in]]






In case [[berryopt]]=16, a reduced finite electric displacement field
calculation is performed. In this case, the parameter red_efield specifies the
initial electric field used on the first iteration, in atomic units.

[[red_efield]] is defined via Eq.(25) in the Supplement of M. Stengel, N.A.
Spaldin and D. Vanderbilt, Nat. Phys. 5,304 (2009).

## **red_efieldbar** 


*Mnemonics:* REDuced Electric FIELD BAR  
*Mentioned in topic(s):* [[topic:Berry]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*0.0  
*Only relevant if:* [[berryopt]] = 14  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - seq:  [[tests/seq/Input/tsv6_121.in|tsv6_121.in]], [[tests/seq/Input/tsv6_125.in|tsv6_125.in]]






In case [[berryopt]]=14, a reduced finite electric field calculation is
performed. The magnitude and direction of this electric field are determined
by red_efieldbar. It must be given in atomic units.

[[red_efieldbar]] is defined via Eq.(28) in the Supplement of M. Stengel, N.A.
Spaldin and D. Vanderbilt, Nat. Phys. 5,304 (2009).

## **spinmagntarget** 


*Mnemonics:* SPIN-MAGNetization TARGET  
*Mentioned in topic(s):* [[topic:spinpolarisation]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* -99.99  

??? note "Test list (click to open). Moderately used, [33/920] in all abinit tests, [0/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t22.in|t22.in]], [[tests/mpiio/Input/t25.in|t25.in]]
    - paral:  [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t22.in|t22.in]], [[tests/paral/Input/t25.in|t25.in]], [[tests/paral/Input/t26.in|t26.in]], [[tests/paral/Input/t30.in|t30.in]], [[tests/paral/Input/t62.in|t62.in]], [[tests/paral/Input/t62.in|t62.in]], [[tests/paral/Input/t94.in|t94.in]]
    - seq:  [[tests/seq/Input/tsv2_81.in|tsv2_81.in]], [[tests/seq/Input/tsv3_03.in|tsv3_03.in]], [[tests/seq/Input/tsv4_90.in|tsv4_90.in]]
    - v1:  [[tests/v1/Input/t39.in|t39.in]]
    - v2:  [[tests/v2/Input/t76.in|t76.in]]
    - v3:  [[tests/v3/Input/t12.in|t12.in]], [[tests/v3/Input/t20.in|t20.in]], [[tests/v3/Input/t51.in|t51.in]], [[tests/v3/Input/t58.in|t58.in]], [[tests/v3/Input/t86.in|t86.in]]
    - v5:  [[tests/v5/Input/t33.in|t33.in]], [[tests/v5/Input/t61.in|t61.in]], [[tests/v5/Input/t62.in|t62.in]], [[tests/v5/Input/t63.in|t63.in]]
    - v6:  [[tests/v6/Input/t31.in|t31.in]], [[tests/v6/Input/t32.in|t32.in]], [[tests/v6/Input/t63.in|t63.in]]
    - v67mbpt:  [[tests/v67mbpt/Input/t29.in|t29.in]]
    - v7:  [[tests/v7/Input/t22.in|t22.in]], [[tests/v7/Input/t66.in|t66.in]]






This input variable is active only in the [[nsppol]]=2 case. If
[[spinmagntarget]] is not the "magic" value of -99.99d0, the spin-
magnetization of the primitive cell will be fixed (or optimized, if it is not
possible to impose it) to the value of [[spinmagntarget]], in Bohr magneton
units, e.g. for an Hydrogen atom, it is 1.  
If [[occopt]] is a metallic one, the Fermi energies for spin up and spin down
are adjusted to give the target spin-polarisation (this is equivalent to an
exchange splitting). If [[occopt]]=1 and [[nsppol]]=2, the occupation numbers
for spin up and spin down will be adjusted to give the required spin-
magnetization (occupation numbers are identical for all k-points, with
[[occopt]]=1). The definition of [[spinmagntarget]] is actually requested in
this case, except for the single isolated Hydrogen atom.  
If [[spinmagntarget]] is the default one, the spin-magnetization will not be
constrained, and will be determined self-consistently, by having the same spin
up and spin down Fermi energy in the metallic case, while for the other cases,
there will be no spin-magnetization, except for an odd number of electrons if
[[occopt]]=1 and [[nsppol]]=2.

Note : for the time being, only the spin down Fermi energy is written out in
the main output file. In the fixed magnetic moment case, it differs from the
spin up Fermi energy.

## **vprtrb** 


*Mnemonics:* potential -V- for the PeRTuRBation  
*Characteristics:* [[DEVELOP]], [[ENERGY]]  
*Mentioned in topic(s):* [[topic:Artificial]]  
*Variable type:* real  
*Dimensions:* (2)  
*Default value:* [0.0, 0.0]  
*Only relevant if:* [[qprtrb]]  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - v6:  [[tests/v6/Input/t01.in|t01.in]], [[tests/v6/Input/t02.in|t02.in]]






Gives the real and imaginary parts of a scalar potential perturbation. Can be
specified in Ha (the default), Ry, eV or Kelvin, since [[vprtrb]] has the
'[[ENERGY]]' characteristics.  
This is made available for testing responses to such perturbations. The form
of the perturbation, which is added to the local potential, is:

  * ([[vprtrb]](1)+I*[[vprtrb]](2))/2 at G=[[qprtrb]] and 
  * ([[vprtrb]](1)-I*[[vprtrb]](2))/2 at G=-[[qprtrb]] (see [[qprtrb]] also). 

## **zeemanfield** 


*Mnemonics:* ZEEMAN FIELD  
*Characteristics:* [[MAGNETIC_FIELD]]  
*Mentioned in topic(s):* [[topic:MagField]]  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 0  

??? note "Test list (click to open). Rarely used, [1/920] in all abinit tests, [0/116] in abinit tutorials"
    - v6:  [[tests/v6/Input/t17.in|t17.in]]






Give the value of the Zeeman field, H, acting on the spinorial wavefunctions.
Note that Tesla are admitted. This sets the magnitude of mu_0*H, in Tesla,
with H in Amperes/metre.
