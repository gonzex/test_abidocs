## **accuracy** 


*Mnemonics:* ACCURACY  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Allows to tune the accuracy of a calculation by setting automatically the
variables [[ecut]], [[boxcutmin]], [[fband]], [[tolvrs]], [[tolmxf]],
[[optforces]], [[timopt]], [[npulayit]], [[nstep]], [[prteig]], [[prtden]],
and if [[usepaw]]=1, [[pawecutdg]], [[bxctmindg]], [[pawxcdev]], [[pawmixdg]],
[[pawovlp]], [[pawnhatxc]], according to the following table:

accuracy

|

1

|

2

|

3

|

4

|

5

|

6  
  
---|---|---|---|---|---|---  
  
ecut

|

E_min

|

E_med

|

E_med

|

**E_max**

|

**E_max**

|

**E_max**  
  
pawecutdg

|

ecut

|

ecut

|

1.2*ecut

|

**1.5*ecut**

|

2*ecut

|

2*ecut  
  
fband

|

**0.5**

|

**0.5**

|

**0.5**

|

**0.5**

|

0.75

|

0.75  
  
boxcutmin

|

1.5

|

1.8

|

1.8

|

**2.0**

|

**2.0**

|

**2.0**  
  
bxctmindg

|

1.5

|

1.8

|

1.8

|

**2.0**

|

**2.0**

|

**2.0**  
  
pawxcdev

|

**1**

|

**1**

|

**1**

|

**1**

|

2

|

2  
  
pawmixdg

|

**0**

|

**0**

|

**0**

|

**0**

|

1

|

1  
  
pawovlp

|

10

|

7

|

7

|

**5**

|

**5**

|

**5**  
  
pawnhatxc

|

0

|

**1**

|

**1**

|

**1**

|

**1**

|

**1**  
  
tolvrs

|

1.0d-3

|

1.0d-5

|

1.0d-7

|

1.0d-9

|

1.0d-10

|

1.0d-12  
  
tolmxf

|

1.0d-3

|

5.0d-4

|

1.0d-4

|

**5.0d-5**

|

1.0d-6

|

1.0d-6  
  
optforces

|

1

|

1

|

**2**

|

**2**

|

**2**

|

**2**  
  
timopt

|

0

|

0

|

**1**

|

**1**

|

**1**

|

**1**  
  
npulayit

|

4

|

**7**

|

**7**

|

**7**

|

15

|

15  
  
nstep

|

**30**

|

**30**

|

**30**

|

**30**

|

50

|

50  
  
prteig

|

0

|

0

|

**1**

|

**1**

|

**1**

|

**1**  
  
prtden

|

0

|

0

|

**1**

|

**1**

|

**1**

|

**1**  
  
  
For a parallel calculation, [[timopt]] is enforced to be 0.  
E_min, E_med and E_max may be read from the pseudopotential file (available
only for XML PAW atomic data files). If E_min, E_med and E_max are not given
in the pseudopotential file, [[ecut]] must be given in the input file and
E_max=E_med=E_max=ecut.  
The values in bold font are the default values of ABINIT. [[accuracy]]=4
corresponds to the default tuning of ABINIT. It is already a very accurate
tuning.  
If the user wants to modify one of the input variable automatically tuned by
[[accuracy]], he must put it in the input file. The other input variables
automatically tuned by [[accuracy]] will not be affected.  
[[accuracy]]=0 means that this input variable is desactivated.


* * *

## **acell** 


*Mnemonics:* CELL lattice vector scaling  
*Variable type:* real  
*Dimensions:* (3)  
*commentdims:* represented internally as acell(3,[[nimage]])  
*Default value:* 3*1  



Gives the length scales by which dimensionless primitive translations (in
[[rprim]]) are to be multiplied. By default, given in Bohr atomic units (1
Bohr=0.5291772108 Angstroms), although Angstrom can be specified, if
preferred, since [[acell]] has the '[[LENGTH]]' characteristics. See further
description of [[acell]] related to the [[rprim]] input variable, the
[[scalecart]] input variable, and the associated internal [[rprimd]] input
variable.

Note that [[acell]] is NOT the length of the conventional orthogonal basis
vectors, but the scaling factors of the primitive vectors. Use [[scalecart]]
to scale the cartesian coordinates.


* * *

## **angdeg** 


*Mnemonics:* ANGles in DEGrees  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* None  
*Comment:* deduced from '[[rprim]]'  



Gives the angles between directions of primitive vectors of the unit cell (in
degrees), as an alternative to the input array [[rprim]] . Will be used to set
up [[rprim]], that, together with the array [[acell]], will be used to define
the primitive vectors.

  * [[angdeg]](1) is the angle between the 2nd and 3rd vectors, 
  * [[angdeg]](2) is the angle between the 1st and 3rd vectors, 
  * [[angdeg]](3) is the angle between the 1st and 2nd vectors, 

If the three angles are equal within 1.0d-12 (except if they are exactly 90
degrees), the three primitive vectors are chosen so that the trigonal symmetry
that exchange them is along the z cartesian axis :

    
    
    R1=( a , 0,c)
    R2=(-a/2, sqrt(3)/2*a,c)
    R3=(-a/2,-sqrt(3)/2*a,c)
     

where a  2  +c  2  =1.0d0  
If the angles are not all equal (or if they are all 90 degrees), one will have
the following generic form :

  * R1=(1,0,0) 
  * R2=(a,b,0) 
  * R3=(c,d,e) 

where each of the vectors is normalized, and form the desired angles with the
others.


* * *

## **ecut** 


*Mnemonics:* Energy CUToff  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* None  



Used for kinetic energy cutoff which controls number of planewaves at given k
point by:  
(1/2)[(2 Pi)*(k+Gmax)]  2  =[[ecut]] for Gmax.  
All planewaves inside this "basis sphere" centered at k are included in the
basis (except if [[dilatmx]] is defined).  
Can be specified in Ha (the default), Ry, eV or Kelvin, since [[ecut]] has the
'[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)  
This is the single parameter which can have an enormous effect on the quality
of a calculation; basically the larger [[ecut]] is, the better converged the
calculation is. For fixed geometry, the total energy MUST always decrease as
[[ecut]] is raised because of the variational nature of the problem.

_ Usually one runs at least several calculations at various [[ecut]] to
investigate the convergence needed for reliable results. _

For k-points whose coordinates are build from 0 or 1/2, the implementation of
time-reversal symmetry that links coefficients of the wavefunctions in
reciprocal space has been realized. See the input variable [[istwfk]]. If
activated (which corresponds to the Default mode), this input variable
[[istwfk]] will allow to divide the number of plane wave (npw) treated
explicitly by a factor of two. Still, the final result should be identical
with the 'full' set of plane waves.

See the input variable [[ecutsm]], for the smoothing of the kinetic energy,
needed to optimize unit cell parameters.


* * *

## **einterp** 


*Mnemonics:* Electron bands INTERPolation  
*Variable type:* real  
*Dimensions:* (4)  
*Default value:* [0, 0, 0, 0]  



This variable activates the interpolation of the electronic eigenvalues. It
can be used to interpolate KS eigenvalues at the end of the GS run or to
interpolate GW energies in sigma calculations ([[optdriver]] = 4). The k-path
can be specified with [[kptbounds]] and [[nkpath]]. einterp consists of 4
entries. The first element specificies the interpolation method.

  * 0 --> No interpolation (default) 
  * 1 --> Star-function interpolation (Shankland-Koelling-Wood Fourier interpolation scheme, see [[Pickett1988]] 
  * 2 --> B-spline interpolation. 

The meaning of the other entries depend on the interpolation technique
selected.  
In the case of star-function interpolation:

  * einterp(2): Number of star-functions per ab-initio k-point 
  * einterp(3): If non-zero, activate Fourier filtering according to Eq 9 of [[Uehara2000]]. In this case, rcut is given by einterp(2) * Rmax where Rmax is the maximum length of the lattice vectors included in the star expansion 
  * einterp(4): Used if einterp(2) /= 0. It defines rsigma in Eq 9

  
For B-spline interpolation: einterp(2:4): Order of B-spline for the three
reduced directions. Cubic spline (3) is the recomended value.


* * *

## **iscf** 


*Mnemonics:* Integer for Self-Consistent-Field cycles  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 17 if [[usepaw]]==1,
0 if [[usewvl]]==1,
7 otherwise.
  



Controls the self-consistency.  
Positive values =&gt; this is the usual choice for doing the usual ground
state (GS) calculations or for structural relaxation, where the potential has
to be determined self-consistently. The choice between different algorithms
for SCF is possible :

  * =0 =&gt; SCF cycle, direct minimization scheme on the gradient of the wavefunctions. This algorithm is faster than diagonalisation and mixing but is working only for systems with a gap. It is implemented only on the wavelet basis set, when [[usewvl]]=1. 
  * =1 =&gt; get the largest eigenvalue of the SCF cycle   
([[DEVELOP]] option, used with [[irdwfk]]=1 or [[irdwfq]]=1)

  * =2 =&gt; SCF cycle, simple mixing of the potential 
  * =3 =&gt; SCF cycle, Anderson mixing of the potential 
  * =4 =&gt; SCF cycle, Anderson mixing of the potential based on the two previous iterations 
  * =5 =&gt; SCF cycle, CG based on the minim. of the energy with respect to the potential 
  * =7 =&gt; SCF cycle, Pulay mixing of the potential based on the [[npulayit]] previous iterations 
  * =12 =&gt; SCF cycle, simple mixing of the density 
  * =13 =&gt; SCF cycle, Anderson mixing of the density 
  * =14 =&gt; SCF cycle, Anderson mixing of the density based on the two previous iterations 
  * =15 =&gt; SCF cycle, CG based on the minim. of the energy with respect to the density 
  * =17 =&gt; SCF cycle, Pulay mixing of the density based on the [[npulayit]] previous iterations 
  * Other positive values, including zero ones, are not allowed. 

Such algorithms for treating the "SCF iteration history" should be coupled
with accompanying algorithms for the SCF "preconditioning". See the input
variable [[iprcel]]. The default value [[iprcel]]=0 is often a good choice,
but for inhomogeneous systems, you might gain a lot with [[iprcel]]=45.

(Warning : if [[iscf]]&gt;10, at present (v4.6), the energy printed at each
SCF cycle is not variational - this should not affect the other properties,
and at convergence, all values are OK)

\- In the norm-conserving case, the default option is [[iscf]]=7, which is a
compromise between speed and reliability. The value [[iscf]]= 2 is safer but
slower.  
\- In the PAW case, default option is [[iscf]]=17. In PAW you have the
possibility to mix density/potential on the fine or coarse FFT grid (see
[[pawmixdg]]).  
\- Note that a Pulay mixing ([[iscf]]=7 or 17) with [[npulayit]] =1 (resp. 2)
is equivalent to an Anderson mixing with [[iscf]]=3 or 13 (resp. 4 or 14).  
\- Also note that:  
* when mixing is done on potential (iscf &lt;10), total energy is computed by "direct" decomposition.   
* when mixing is done on density (iscf &gt;=10), total energy is computed by "double counting" decomposition.   
"Direct" and "double counting" decomposition of energy are equal when SCF
cycle is converged. Note that, when using GGA XC functionals, these
decompositions of energy can be slightly different due to imprecise
computation of density gradients on FFT grid (difference decreases as size of
FFT grid increases - see [[ecut]] for NC pseudopotentials, [[pawecutdg]] for
PAW).  
  
Other (negative) options:

  * = -2 =&gt; a non-self-consistent calculation is to be done; in this case an electron density rho(r) on a real space grid (produced in a previous calculation) will be read from a disk file (automatically if [[ndtset]]=0, or according to the value of [[getden]] if [[ndtset]]/=0).   
The name of the density file must be given as indicated in the [ section 4
](../../users/generated_files/help_abinit.html#4) of [[help_abinit]].
[[iscf]]=-2 would be used for band structure calculations, to permit
computation of the eigenvalues of occupied and unoccupied states at arbitrary
k points in the fixed self consistent potential produced by some integration
grid of k points. Due to this typical use, ABINIT insist that either
[[prtvol]]&gt;2 or [[prteig]] does not vanish when there are more than 50 k
points.  
To compute the eigenvalues (and wavefunctions) of unoccupied states in a
separate (non-selfconsistent) run, the user should save the self-consistent
rho(r) and then run [[iscf]]=-2 for the intended set of k-points and bands.  
To prepare a run with [[iscf]]=-2, a density file can be produced using the
parameter [[prtden]] (see its description). When a self-consistent set of
wavefunctions is already available, abinit can be used with [[nstep]]=0 (see
Test_v2/t47.in), and the adequate value of [[prtden]].

  * = -3 =&gt; like -2, but initialize [[occ]] and [[wtk]], directly or indirectly (using [[ngkpt]] or [[kptrlatt]]) depending on the value of [[occopt]].   
For GS, this option might be used to generate Density-of-states (thanks to
[[prtdos]]), or to produce STM charge density map (thanks to [[prtstm]]).  
For RF, this option is needed to compute the response to ddk perturbation.

  * = -1 =&gt; like -2, but the non-self-consistent calculation is followed by the determination of excited states within [[TDDFT]]. This is only possible for [[nkpt]]=1, with [[kpt]]=0 0 0. Note that the oscillator strength needs to be defined with respect to an origin of coordinate, thanks to the input variable [[boxcenter]]. The maximal number of Kohn-Sham excitations to be used to build the excited state [[TDDFT]] matrix can be defined by [[td_mexcit]], or indirectly by the maximum Kohn-Sham excitation energy [[td_maxene]]. 


* * *

## **ixc** 


*Mnemonics:* Integer for eXchange-Correlation choice  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Comment:* Default corresponds to Teter parametrization. However, if all the pseudopotentials have the same value of pspxc, the initial value of ixc will be that common value  



Controls the choice of exchange and correlation (xc). The list of XC
functionals is given below. Positive values are for ABINIT native library of
XC functionals, while negative values are for calling the much wider set of
functionals from the ETSF LibXC library (by M. Marques), also available at the
[ ETSF library Web page
](http://www.etsf.eu/resources/software/libraries_and_tools)  
Note that the choice made here should agree with the choice made in generating
the original pseudopotential, except for [[ixc]]=0 (usually only used for
debugging). A warning is issued if this is not the case. However, the choices
[[ixc]]=1, 2, 3 and 7 are fits to the same data, from Ceperley-Alder, and are
rather similar, at least for spin-unpolarized systems.  
The choice between the non-spin-polarized and spin-polarized case is governed
by the value of [[nsppol]] (see below).

** Native ABINIT XC functionals **

  
NOTE : in the implementation of the spin-dependence of these functionals, and
in order to avoid divergences in their derivatives, the interpolating function
between spin-unpolarized and fully-spin-polarized function has been slightly
modified, by including a zeta rescaled by 1.d0-1.d-6. This should affect total
energy at the level of 1.d-6Ha, and should have an even smaller effect on
differences of energies, or derivatives.  
The value [[ixc]]=10 is used internally : gives the difference between
[[ixc]]=7 and [[ixc]]=9, for use with an accurate RPA correlation energy.

  * 0=&gt; NO xc; 

  * 1=&gt; LDA or LSD, Teter Pade parametrization (4/93, published in [[Goedecker1996]], which reproduces Perdew-Wang (which reproduces Ceperley-Alder!). 
  * 2=&gt; LDA, Perdew-Zunger-Ceperley-Alder (no spin-polarization) [[Perdew1981]] 
  * 3=&gt; LDA, old Teter rational polynomial parametrization (4/91) fit to Ceperley-Alder data (no spin-polarization) 
  * 4=&gt; LDA, Wigner functional (no spin-polarization) 
  * 5=&gt; LDA, Hedin-Lundqvist functional (no spin-polarization) 
  * 6=&gt; LDA, "X-alpha" functional (no spin-polarization) 
  * 7=&gt; LDA or LSD, Perdew-Wang 92 functional 
  * 8=&gt; LDA or LSD, x-only part of the Perdew-Wang 92 functional 
  * 9=&gt; LDA or LSD, x- and RPA correlation part of the Perdew-Wang 92 functional 

  * 11=&gt; GGA, Perdew-Burke-Ernzerhof GGA functional 
  * 12=&gt; GGA, x-only part of Perdew-Burke-Ernzerhof GGA functional 
  * 13=&gt; GGA potential of van Leeuwen-Baerends, while for energy, Perdew-Wang 92 functional 
  * 14=&gt; GGA, revPBE of Y. Zhang and W. Yang, Phys. Rev. Lett. 80, 890 (1998) 
  * 15=&gt; GGA, RPBE of B. Hammer, L.B. Hansen and J.K. Norskov, Phys. Rev. B 59, 7413 (1999) 
  * 16=&gt; GGA, HTCH93 of F.A. Hamprecht, A.J. Cohen, D.J. Tozer, N.C. Handy, J. Chem. Phys. 109, 6264 (1998) 
  * 17=&gt; GGA, HTCH120 of A.D. Boese, N.L. Doltsinis, N.C. Handy, and M. Sprik, J. Chem. Phys 112, 1670 (1998) - The usual HCTH functional. 
  * 18=&gt; (NOT AVAILABLE : used internally for GGA BLYP pseudopotentials from M. Krack, see Theor. Chem. Acc. 114, 145 (2005), available from the [ CP2K repository ](https://github.com/cp2k/cp2k/tree/master/potentials/Goedecker/abinit/blyp) \- use the LibXC instead, with [[ixc]]=-106131. 
  * 19=&gt; (NOT AVAILABLE : used internally for GGA BP86 pseudopotentials from M. Krack, see Theor. Chem. Acc. 114, 145 (2005), available from the [ CP2K repository ](https://github.com/cp2k/cp2k/tree/master/potentials/Goedecker/abinit/bp) \- use the LibXC instead, with [[ixc]]=-106132. 

  * 20=&gt; Fermi-Amaldi xc ( -1/N Hartree energy, where N is the number of electrons per cell ; G=0 is not taken into account however), for [[TDDFT]] tests. No spin-pol. Does not work for RF. 
  * 21=&gt; same as 20, except that the xc-kernel is the LDA ([[ixc]]=1) one, for [[TDDFT]] tests. 
  * 22=&gt; same as 20, except that the xc-kernel is the Burke-Petersilka-Gross hybrid, for [[TDDFT]] tests. 
  * 23=&gt; GGA of Z. Wu and R.E. Cohen, Phys. Rev. 73, 235116 (2006). 
  * 24=&gt; GGA, C09x exchange of V. R. Cooper, PRB 81, 161104(R) (2010). 
  * 26=&gt; GGA, HTCH147 of A.D. Boese, N.L. Doltsinis, N.C. Handy, and M. Sprik, J. Chem. Phys 112, 1670 (1998). 
  * 27=&gt; GGA, HTCH407 of A.D. Boese, and N.C. Handy, J. Chem. Phys 114, 5497 (2001). 
  * 28=&gt; (NOT AVAILABLE : used internally for GGA OLYP pseudopotentials from M. Krack, see Theor. Chem. Acc. 114, 145 (2005), available from the [ CP2K repository ](https://github.com/cp2k/cp2k/tree/master/potentials/Goedecker/abinit/olyp) \- use the LibXC instead, with [[ixc]]=-110131. 

  * 40=&gt; Hartree-Fock 
  * 41=&gt; PBE0, J.P. Perdew, M. Ernzerhof and K. Burke, J. Chem. Phys. 105, 9982 (1996) 
  * 42=&gt; PBE0-1/3, C.A. Guido, E. Bremond, C. Adamo and P. Cortona, J. Chem. Phys. 138, 021104 (2013) 

** ETSF Lib XC functionals **

Note that you must compile ABINIT with the LibXC plug-in in order to be able
to access these functionals.  
The LibXC functionals are accessed by ** negative values ** of [[ixc]]. The
LibXC contains functional forms for either exchange-only functionals,
correlation-only functionals, or combined exchange and correlation
functionals. Each of them is to be specified by a three-digit number. In case
of a combined exchange and correlation functional, only one such three-digit
number has to be specified as value of [[ixc]], with a minus sign (to indicate
that it comes from the LibXC). In the case of separate exchange functional
(let us represent its identifier by XXX) and correlation functional (let us
represent its identified by CCC), a six-digit number will have to be specified
for [[ixc]], by concatenation, be it XXXCCC or CCCXXX. As an example,
[[ixc]]=-020 gives access to the Teter93 LDA, while [[ixc]]=-101130 gives
access to the PBE GGA. In version 0.9 of LibXC (December 2008), there are 16
three-dimensional (S)LDA functionals (1 for X, 14 for C, 1 for combined XC),
and there are 41 three-dimensional GGA (23 for X, 8 for C, 10 for combined
XC). Note that for a meta-GGA, the kinetic energy density is needed. This
means having [[usekden]]=1 .

(S)LDA functionals (do not forget to add a minus sign, as discussed above)

  * 001=&gt; XC_LDA_X [PAM Dirac, Proceedings of the Cambridge Philosophical Society 26, 376 (1930); F Bloch, Zeitschrift fuer Physik 57, 545 (1929) ] 
  * 002=&gt; XC_LDA_C_WIGNER Wigner parametrization [EP Wigner, Trans. Faraday Soc. 34, 678 (1938) ] 
  * 003=&gt; XC_LDA_C_RPA Random Phase Approximation [M Gell-Mann and KA Brueckner, Phys. Rev. 106, 364 (1957) ] 
  * 004=&gt; XC_LDA_C_HL Hedin &amp; Lundqvist [L Hedin and BI Lundqvist, J. Phys. C 4, 2064 (1971) ] 
  * 005=&gt; XC_LDA_C_GL ! Gunnarson &amp; Lundqvist [O Gunnarsson and BI Lundqvist, PRB 13, 4274 (1976) ] 
  * 006=&gt; XC_LDA_C_XALPHA ! Slater's Xalpha ] 
  * 007=&gt; XC_LDA_C_VWN ! Vosko, Wilk, &amp; Nussair [SH Vosko, L Wilk, and M Nusair, Can. J. Phys. 58, 1200 (1980) ] 
  * 008=&gt; XC_LDA_C_VWN_RPA ! Vosko, Wilk, &amp; Nussair (RPA) [SH Vosko, L Wilk, and M Nusair, Can. J. Phys. 58, 1200 (1980) ] 
  * 009=&gt; XC_LDA_C_PZ ! Perdew &amp; Zunger [[Perdew1981]] 
  * 010=&gt; XC_LDA_C_PZ_MOD ! Perdew &amp; Zunger (Modified) [[Perdew1981]] Modified to improve the matching between the low and high rs part ] 
  * 011=&gt; XC_LDA_C_OB_PZ ! Ortiz &amp; Ballone (PZ) [G Ortiz and P Ballone, Phys. Rev. B 50, 1391 (1994) ; G Ortiz and P Ballone, Phys. Rev. B 56, 9970(E) (1997) ; [[Perdew1981]] ] 
  * 012=&gt; XC_LDA_C_PW ! Perdew &amp; Wang [JP Perdew and Y Wang, Phys. Rev. B 45, 13244 (1992) ] 
  * 013=&gt; XC_LDA_C_PW_MOD ! Perdew &amp; Wang (Modified) [JP Perdew and Y Wang, Phys. Rev. B 45, 13244 (1992) ; Added extra digits to some constants as in the PBE routine see [ https://www.chem.uci.edu/~kieron/dftold2/pbe.php ](https://www.chem.uci.edu/~kieron/dftold2/pbe.php) (at some point it was available at http://dft.uci.edu/pbe.php) ] 
  * 014=&gt; XC_LDA_C_OB_PW ! Ortiz &amp; Ballone (PW) [G Ortiz and P Ballone, Phys. Rev. B 50, 1391 (1994) ; G Ortiz and P Ballone, Phys. Rev. B 56, 9970(E) (1997) ; JP Perdew and Y Wang, Phys. Rev. B 45, 13244 (1992) ] 
  * 017=&gt; XC_LDA_C_vBH ! von Barth &amp; Hedin [U von Barth and L Hedin, J. Phys. C: Solid State Phys. 5, 1629 (1972) ] 
  * 020=&gt; XC_LDA_XC_TETER93 ! Teter 93 parametrization [S Goedecker, M Teter, J Hutter, PRB 54, 1703 (1996) ] 
  * 022=&gt; XC_LDA_C_ML1 ! Modified LSD (version 1) of Proynov and Salahub [EI Proynov and D Salahub, Phys. Rev. B 49, 7874 (1994) ] 
  * 023=&gt; XC_LDA_C_ML2 ! Modified LSD (version 2) of Proynov and Salahub [EI Proynov and D Salahub, Phys. Rev. B 49, 7874 (1994) ] 
  * 024=&gt; XC_LDA_C_GOMBAS ! Gombas parametrization [P. Gombas, Pseudopotentials (Springer-Verlag, New York, 1967) ] 
  * 025=&gt; XC_LDA_C_PW_RPA ! Perdew &amp; Wang fit of the RPA [JP Perdew and Y Wang, Phys. Rev. B 45, 13244 (1992) ] 
  * 027=&gt; XC_LDA_C_RC04 ! Ragot-Cortona [S Ragot and P Cortona, J. Chem. Phys. 121, 7671 (2004) ] 
  * 028=&gt; XC_LDA_C_VWN_1 ! Vosko, Wilk, &amp; Nussair (1) [SH Vosko, L Wilk, and M Nusair, Can. J. Phys. 58, 1200 (1980) ] 
  * 029=&gt; XC_LDA_C_VWN_2 ! Vosko, Wilk, &amp; Nussair (2) [SH Vosko, L Wilk, and M Nusair, Can. J. Phys. 58, 1200 (1980) ] 
  * 030=&gt; XC_LDA_C_VWN_3 ! Vosko, Wilk, &amp; Nussair (3) [SH Vosko, L Wilk, and M Nusair, Can. J. Phys. 58, 1200 (1980) ] 
  * 031=&gt; XC_LDA_C_VWN_4 ! Vosko, Wilk, &amp; Nussair (4) [SH Vosko, L Wilk, and M Nusair, Can. J. Phys. 58, 1200 (1980) ] 

GGA functionals (do not forget to add a minus sign, as discussed above)

  * 84=&gt; XC_GGA_C_OP_XALPHA ! one-parameter progressive functional (G96 version) [T Tsuneda, T Suzumura, and K Hirao, J. Chem. Phys. 111, 5656 (1999) ] 
  * 85=&gt; XC_GGA_C_OP_G96 ! one-parameter progressive functional (G96 version) [T Tsuneda, T Suzumura, and K Hirao, J. Chem. Phys. 111, 5656 (1999) ] 
  * 86=&gt; XC_GGA_C_OP_PBE ! one-parameter progressive functional (PBE version) [T Tsuneda, T Suzumura, and K Hirao, J. Chem. Phys. 111, 5656 (1999) ] 
  * 87=&gt; XC_GGA_C_OP_B88 ! one-parameter progressive functional (B88 version) [T Tsuneda, T Suzumura, and K Hirao, J. Chem. Phys. 111, 5656 (1999) ] 
  * 88=&gt; XC_GGA_C_FT97 ! Filatov &amp; Thiel correlation [M Filatov &amp; W Thiel, Int. J. Quant. Chem. 62, 603-616 (1997) ; M Filatov &amp; W Thiel, Mol Phys 91, 847 (1997) ] WARNING : this functional is not tested. Use at your own risks. 
  * 89=&gt; XC_GGA_C_SPBE ! PBE correlation to be used with the SSB exchange [M Swart, M Sola, and FM Bickelhaupt, J. Chem. Phys. 131, 094103 (2009) ] 
  * 90=&gt; XC_GGA_X_SSB_SW ! Swarta, Sola and Bickelhaupt correction to PBE [M Swart, M Sola, and FM Bickelhaupt, J. Comp. Meth. Sci. Engin. 9, 69 (2009) ] 
  * 91=&gt; XC_GGA_X_SSB ! WARNING : This functional gives NaN on IBM (XG20130608). Swarta, Sola and Bickelhaupt [M Swart, M Sola, and FM Bickelhaupt, J. Chem. Phys. 131, 094103 (2009) ] 
  * 92=&gt; XC_GGA_X_SSB_D ! WARNING : This functional gives NaN on IBM (XG20130608). Swarta, Sola and Bickelhaupt dispersion [M Swart, M Sola, and FM Bickelhaupt, J. Chem. Phys. 131, 094103 (2009) ] 
  * 93=&gt; XC_GGA_XC_HCTH_407P ! HCTH/407+ [AD Boese, A Chandra, JML Martin, and Dominik Marx, J. Chem. Phys. 119, 5965 (2003) ] 
  * 94=&gt; XC_GGA_XC_HCTH_P76 ! HCTH p=7/6 [G Menconi, PJ Wilson, and DJ Tozer, J. Chem. Phys. 114, 3958 (2001) ] 
  * 95=&gt; XC_GGA_XC_HCTH_P14 ! HCTH p=1/4 [G Menconi, PJ Wilson, and DJ Tozer, J. Chem. Phys. 114, 3958 (2001) ] 
  * 96=&gt; XC_GGA_XC_B97_GGA1 ! Becke 97 GGA-1 [AJ Cohen and NC Handy, Chem. Phys. Lett. 316, 160-166 (2000) ] 
  * 97=&gt; XC_GGA_XC_HCTH_A ! HCTH-A [FA Hamprecht, AJ Cohen, DJ Tozer, and NC Handy, J. Chem. Phys. 109, 6264 (1998) ] 
  * 98=&gt; XC_GGA_X_BPCCAC ! BPCCAC (GRAC for the energy) [E Bremond, D Pilard, I Ciofini, H Chermette, C Adamo, and P Cortona, Theor Chem Acc 131, 1184 (2012) ] 
  * 99=&gt; XC_GGA_C_REVTCA ! Tognetti, Cortona, Adamo (revised) [V Tognetti, P Cortona, and C Adamo, Chem. Phys. Lett. 460, 536-539 (2008) ] 
  * 100=&gt; XC_GGA_C_TCA ! Tognetti, Cortona, Adamo [V Tognetti, P Cortona, and C Adamo, J. Chem. Phys. 128, 034101 (2008) ] 
  * 101=&gt; XC_GGA_X_PBE ! Perdew, Burke &amp; Ernzerhof exchange [JP Perdew, K Burke, and M Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996) ; JP Perdew, K Burke, and M Ernzerhof, Phys. Rev. Lett. 78, 1396(E) (1997) ] 
  * 102=&gt; XC_GGA_X_PBE_R ! Perdew, Burke &amp; Ernzerhof exchange (revised) [Y Zhang and W Yang, Phys. Rev. Lett 80, 890 (1998) ] 
  * 103=&gt; XC_GGA_X_B86 ! Becke 86 Xalfa,beta,gamma [AD Becke, J. Chem. Phys 84, 4524 (1986) ] 
  * 104=&gt; XC_GGA_X_HERMAN ! Herman Xalphabeta GGA [F Herman, JP Van Dyke, and IB Ortenburger, Phys. Rev. Lett. 22, 807 (1969) ; F Herman, IB Ortenburger, and JP Van Dyke, Int. J. Quantum Chem. Symp. 3, 827 (1970) ] 
  * 105=&gt; XC_GGA_X_B86_MGC ! Becke 86 Xalfa,beta,gamma (with mod. grad. correction) [AD Becke, J. Chem. Phys 84, 4524 (1986) ; AD Becke, J. Chem. Phys 85, 7184 (1986) ] 
  * 106=&gt; XC_GGA_X_B88 ! Becke 88 [AD Becke, Phys. Rev. A 38, 3098 (1988) ] 
  * 107=&gt; XC_GGA_X_G96 ! Gill 96 [PMW Gill, Mol. Phys. 89, 433 (1996) ] 
  * 108=&gt; XC_GGA_X_PW86 ! Perdew &amp; Wang 86 [JP Perdew and Y Wang, Phys. Rev. B 33, 8800 (1986) ] 
  * 109=&gt; XC_GGA_X_PW91 ! Perdew &amp; Wang 91 [JP Perdew, in Proceedings of the 21st Annual International Symposium on the Electronic Structure of Solids, ed. by P Ziesche and H Eschrig (Akademie Verlag, Berlin, 1991), p. 11. ; JP Perdew, JA Chevary, SH Vosko, KA Jackson, MR Pederson, DJ Singh, and C Fiolhais, Phys. Rev. B 46, 6671 (1992) ; JP Perdew, JA Chevary, SH Vosko, KA Jackson, MR Pederson, DJ Singh, and C Fiolhais, Phys. Rev. B 48, 4978(E) (1993) ] 
  * 110=&gt; XC_GGA_X_OPTX ! Handy &amp; Cohen OPTX 01 [NC Handy and AJ Cohen, Mol. Phys. 99, 403 (2001) ] 
  * 111=&gt; XC_GGA_X_DK87_R1 ! dePristo &amp; Kress 87 (version R1) [AE DePristo and JD Kress, J. Chem. Phys. 86, 1425 (1987) ] 
  * 112=&gt; XC_GGA_X_DK87_R2 ! dePristo &amp; Kress 87 (version R2) [AE DePristo and JD Kress, J. Chem. Phys. 86, 1425 (1987) ] 
  * 113=&gt; XC_GGA_X_LG93 ! Lacks &amp; Gordon 93 [DJ Lacks and RG Gordon, Phys. Rev. A 47, 4681 (1993) ] 
  * 114=&gt; XC_GGA_X_FT97_A ! Filatov &amp; Thiel 97 (version A) [M Filatov and W Thiel, Mol. Phys 91, 847 (1997) ] 
  * 115=&gt; XC_GGA_X_FT97_B ! Filatov &amp; Thiel 97 (version B) [M Filatov and W Thiel, Mol. Phys 91, 847 (1997) ] 
  * 116=&gt; XC_GGA_X_PBE_SOL ! Perdew, Burke &amp; Ernzerhof exchange (solids) [JP Perdew, et al, Phys. Rev. Lett. 100, 136406 (2008) ] 
  * 117=&gt; XC_GGA_X_RPBE ! Hammer, Hansen &amp; Norskov (PBE-like) [B Hammer, LB Hansen and JK Norskov, Phys. Rev. B 59, 7413 (1999) ] 
  * 118=&gt; XC_GGA_X_WC ! Wu &amp; Cohen [Z Wu and RE Cohen, Phys. Rev. B 73, 235116 (2006) ] 
  * 119=&gt; XC_GGA_X_mPW91 ! Modified form of PW91 by Adamo &amp; Barone [C Adamo and V Barone, J. Chem. Phys. 108, 664 (1998) ] 
  * 120=&gt; XC_GGA_X_AM05 ! Armiento &amp; Mattsson 05 exchange [R Armiento and AE Mattsson, Phys. Rev. B 72, 085108 (2005) ; AE Mattsson, R Armiento, J Paier, G Kresse, JM Wills, and TR Mattsson, J. Chem. Phys. 128, 084714 (2008) ] 
  * 121=&gt; XC_GGA_X_PBEA ! Madsen (PBE-like) [G Madsen, Phys. Rev. B 75, 195108 (2007) ] 
  * 122=&gt; XC_GGA_X_MPBE ! Adamo &amp; Barone modification to PBE [C Adamo and V Barone, J. Chem. Phys. 116, 5933 (2002) ] 
  * 123=&gt; XC_GGA_X_XPBE ! xPBE reparametrization by Xu &amp; Goddard [X Xu and WA Goddard III, J. Chem. Phys. 121, 4068 (2004) ] 
  * 125=&gt; XC_GGA_X_BAYESIAN ! Bayesian best fit for the enhancement factor [JJ Mortensen, K Kaasbjerg, SL Frederiksen, JK Norskov, JP Sethna, and KW Jacobsen, Phys. Rev. Lett. 95, 216401 (2005) ] 
  * 126=&gt; XC_GGA_X_PBE_JSJR ! PBE JSJR reparametrization by Pedroza, Silva &amp; Capelle [LS Pedroza, AJR da Silva, and K. Capelle, Phys. Rev. B 79, 201106(R) (2009) ] 
  * 130=&gt; XC_GGA_C_PBE ! Perdew, Burke &amp; Ernzerhof correlation [JP Perdew, K Burke, and M Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996) ; JP Perdew, K Burke, and M Ernzerhof, Phys. Rev. Lett. 78, 1396(E) (1997) ] 
  * 131=&gt; XC_GGA_C_LYP ! Lee, Yang &amp; Parr [C Lee, W Yang and RG Parr, Phys. Rev. B 37, 785 (1988) B Miehlich, A Savin, H Stoll and H Preuss, Chem. Phys. Lett. 157, 200 (1989) ] 
  * 132=&gt; XC_GGA_C_P86 ! Perdew 86 [JP Perdew, Phys. Rev. B 33, 8822 (1986) ] 
  * 133=&gt; XC_GGA_C_PBE_SOL ! Perdew, Burke &amp; Ernzerhof correlation SOL [JP Perdew, et al, Phys. Rev. Lett. 100, 136406 (2008) ] 
  * 134=&gt; XC_GGA_C_PW91 ! Perdew &amp; Wang 91 [JP Perdew, JA Chevary, SH Vosko, KA Jackson, MR Pederson, DJ Singh, and C Fiolhais, Phys. Rev. B 46, 6671 (1992) ] 
  * 135=&gt; XC_GGA_C_AM05 ! Armiento &amp; Mattsson 05 correlation [ R Armiento and AE Mattsson, Phys. Rev. B 72, 085108 (2005) ; AE Mattsson, R Armiento, J Paier, G Kresse, JM Wills, and TR Mattsson, J. Chem. Phys. 128, 084714 (2008) ] 
  * 136=&gt; XC_GGA_C_XPBE ! xPBE reparametrization by Xu &amp; Goddard [X Xu and WA Goddard III, J. Chem. Phys. 121, 4068 (2004) ] 
  * 137=&gt; XC_GGA_C_LM ! Langreth and Mehl correlation [DC Langreth and MJ Mehl, Phys. Rev. Lett. 47, 446 (1981) ] 
  * 138=&gt; XC_GGA_C_PBE_JRGX ! JRGX reparametrization by Pedroza, Silva &amp; Capelle [LS Pedroza, AJR da Silva, and K. Capelle, Phys. Rev. B 79, 201106(R) (2009) ] 
  * 139=&gt; XC_GGA_X_OPTB88_VDW ! Becke 88 reoptimized to be used with vdW functional of Dion et al [J Klimes, DR Bowler, and A Michaelides, J. Phys.: Condens. Matter 22, 022201 (2010) ] 
  * 140=&gt; XC_GGA_X_PBEK1_VDW ! PBE reparametrization for vdW [J Klimes, DR Bowler, and A Michaelides, J. Phys.: Condens. Matter 22, 022201 (2010) ] 
  * 141=&gt; XC_GGA_X_OPTPBE_VDW ! PBE reparametrization for vdW [J Klimes, DR Bowler, and A Michaelides, J. Phys.: Condens. Matter 22, 022201 (2010) ] 
  * 142=&gt; XC_GGA_X_RGE2 ! Regularized PBE [A Ruzsinszky, GI Csonka, and G Scuseria, J. Chem. Theory Comput. 5, 763 (2009) ] 
  * 143=&gt; XC_GGA_C_RGE2 ! Regularized PBE [A Ruzsinszky, GI Csonka, and G Scuseria, J. Chem. Theory Comput. 5, 763 (2009) ] 
  * 144=&gt; XC_GGA_X_RPW86 ! refitted Perdew &amp; Wang 86 [ED Murray, K Lee and DC Langreth, J. Chem. Theory Comput. 5, 2754-2762 (2009) ] 
  * 145=&gt; XC_GGA_X_KT1 ! Keal and Tozer version 1 [TW Keal and DJ Tozer, J. Chem. Phys. 119, 3015 (2003) ] 
  * 146=&gt; XC_GGA_XC_KT2 ! WARNING : This functional gives NaN on IBM (XG20130608). Keal and Tozer version 2 [TW Keal and DJ Tozer, J. Chem. Phys. 119, 3015 (2003) ] 
  * 147=&gt; XC_GGA_C_WL ! Wilson &amp; Levy [LC Wilson and M Levy, Phys. Rev. B 41, 12930 (1990) ] 
  * 148=&gt; XC_GGA_C_WI ! Wilson &amp; Ivanov [LC Wilson &amp; S Ivanov, Int. J. Quantum Chem. 69, 523-532 (1998) ] 
  * 149=&gt; XC_GGA_X_MB88 ! Modified Becke 88 for proton transfer [V Tognetti and C Adamo, J. Phys. Chem. A 113, 14415-14419 (2009) ] 
  * 150=&gt; XC_GGA_X_SOGGA ! Second-order generalized gradient approximation [Y Zhao and DG Truhlar, J. Chem. Phys. 128, 184109 (2008) ; http://comp.chem.umn.edu/mfm/index.html ] 
  * 151=&gt; XC_GGA_X_SOGGA11 ! Second-order generalized gradient approximation 2011 [R Peverati, Y Zhao, and DG Truhlar, J. Phys. Chem. Lett. 2, 1911-1997 (2011); http://comp.chem.umn.edu/mfm/index.html ] 
  * 152=&gt; XC_GGA_C_SOGGA11 ! Second-order generalized gradient approximation 2011 [R Peverati, Y Zhao, and DG Truhlar, J. Phys. Chem. Lett. 2, 1911-1997 (2011); http://comp.chem.umn.edu/mfm/index.html ] 
  * 153=&gt; XC_GGA_C_WI0 ! Wilson &amp; Ivanov initial version [LC Wilson &amp; S Ivanov, Int. J. Quantum Chem. 69, 523-532 (1998) ] 
  * 154=&gt; XC_GGA_XC_TH1 ! Tozer and Handy v. 1 [DJ Tozer and NC Handy, J. Chem. Phys. 108, 2545 (1998) ] WARNING : this functional is not tested. Use at your own risks. 
  * 155=&gt; XC_GGA_XC_TH2 ! Tozer and Handy v. 2 [DJ Tozer and NC Handy, J. Phys. Chem. A 102, 3162 (1998) ] 
  * 156=&gt; XC_GGA_XC_TH3 ! Tozer and Handy v. 3 [DJ Tozer and NC Handy, Mol. Phys. 94, 707 (1998) ] 
  * 157=&gt; XC_GGA_XC_TH4 ! Tozer and Handy v. 4 [DJ Tozer and NC Handy, Mol. Phys. 94, 707 (1998) ] 
  * 158=&gt; XC_GGA_X_C09X ! C09x to be used with the VdW of Rutgers-Chalmers [VR Cooper, PRB 81, 161104(R) (2010) ] 
  * 159=&gt; XC_GGA_C_SOGGA11_X ! To be used with hyb_gga_x_SOGGA11-X [R Peverati and DG Truhlar, J. Chem. Phys. 135, 191102 (2011); http://comp.chem.umn.edu/mfm/index.html ] 
  * 161=&gt; XC_GGA_XC_HCTH_93 ! HCTH functional fitted to 93 molecules [FA Hamprecht, AJ Cohen, DJ Tozer, and NC Handy, J. Chem. Phys. 109, 6264 (1998) ] 
  * 162=&gt; XC_GGA_XC_HCTH_120 ! HCTH functional fitted to 120 molecules [AD Boese, NL Doltsinis, NC Handy, and M Sprik, J. Chem. Phys. 112, 1670 (2000) ] 
  * 163=&gt; XC_GGA_XC_HCTH_147 ! HCTH functional fitted to 147 molecules [AD Boese, NL Doltsinis, NC Handy, and M Sprik, J. Chem. Phys. 112, 1670 (2000) ] 
  * 164=&gt; XC_GGA_XC_HCTH_407 ! HCTH functional fitted to 407 molecules [AD Boese, and NC Handy, J. Chem. Phys. 114, 5497 (2001) ] 
  * 165=&gt; XC_GGA_XC_EDF1 ! Empirical functionals from Adamson, Gill, and Pople [RD Adamson, PMW Gill, and JA Pople, Chem. Phys. Lett. 284 6 (1998) ] 
  * 166=&gt; XC_GGA_XC_XLYP ! XLYP functional [X Xu and WA Goddard, III, PNAS 101, 2673 (2004) ] 
  * 167=&gt; XC_GGA_XC_B97 ! Becke 97 [AD Becke, J. Chem. Phys. 107, 8554-8560 (1997) ] 
  * 168=&gt; XC_GGA_XC_B97_1 ! Becke 97-1 [FA Hamprecht, AJ Cohen, DJ Tozer, and NC Handy, J. Chem. Phys. 109, 6264 (1998); AD Becke, J. Chem. Phys. 107, 8554-8560 (1997) ] 
  * 169=&gt; XC_GGA_XC_B97_2 ! Becke 97-2 [AD Becke, J. Chem. Phys. 107, 8554-8560 (1997) ] 
  * 170=&gt; XC_GGA_XC_B97_D ! Grimme functional to be used with C6 vdW term [S Grimme, J. Comput. Chem. 27, 1787 (2006) ] 
  * 171=&gt; XC_GGA_XC_B97_K ! Boese-Martin for Kinetics [AD Boese and JML Martin, J. Chem. Phys., Vol. 121, 3405 (2004) ] 
  * 172=&gt; XC_GGA_XC_B97_3 ! Becke 97-3 [TW Keal and DJ Tozer, J. Chem. Phys. 123, 121103 (2005) ] 
  * 173=&gt; XC_GGA_XC_PBE1W ! Functionals fitted for water [EE Dahlke and DG Truhlar, J. Phys. Chem. B 109, 15677 (2005) ] 
  * 174=&gt; XC_GGA_XC_MPWLYP1W ! Functionals fitted for water [EE Dahlke and DG Truhlar, J. Phys. Chem. B 109, 15677 (2005) ] 
  * 175=&gt; XC_GGA_XC_PBELYP1W ! Functionals fitted for water [EE Dahlke and DG Truhlar, J. Phys. Chem. B 109, 15677 (2005) ] 
  * 176=&gt; XC_GGA_XC_SB98_1a ! Schmider-Becke 98 parameterization 1a [HL Schmider and AD Becke, J. Chem. Phys. 108, 9624 (1998) ] 
  * 177=&gt; XC_GGA_XC_SB98_1b ! Schmider-Becke 98 parameterization 1b [HL Schmider and AD Becke, J. Chem. Phys. 108, 9624 (1998) ] 
  * 178=&gt; XC_GGA_XC_SB98_1c ! Schmider-Becke 98 parameterization 1c [HL Schmider and AD Becke, J. Chem. Phys. 108, 9624 (1998) ] 
  * 179=&gt; XC_GGA_XC_SB98_2a ! Schmider-Becke 98 parameterization 2a [HL Schmider and AD Becke, J. Chem. Phys. 108, 9624 (1998) ] 
  * 180=&gt; XC_GGA_XC_SB98_2b ! Schmider-Becke 98 parameterization 2b [HL Schmider and AD Becke, J. Chem. Phys. 108, 9624 (1998) ] 
  * 181=&gt; XC_GGA_XC_SB98_2c ! Schmider-Becke 98 parameterization 2c [HL Schmider and AD Becke, J. Chem. Phys. 108, 9624 (1998) ] 
  * 183=&gt; XC_GGA_X_OL2 ! Exchange form based on Ou-Yang and Levy v.2 [P Fuentealba and O Reyes, Chem. Phys. Lett. 232, 31-34 (1995) ; H Ou-Yang, M Levy, Int. J. of Quant. Chem. 40, 379-388 (1991) ] 
  * 184=&gt; XC_GGA_X_APBE ! mu fixed from the semiclassical neutral atom [LA Constantin, E Fabiano, S Laricchia, and F Della Sala, Phys. Rev. Lett. 106, 186406 (2011) ] 
  * 186=&gt; XC_GGA_C_APBE ! mu fixed from the semiclassical neutral atom [LA Constantin, E Fabiano, S Laricchia, and F Della Sala, Phys. Rev. Lett. 106, 186406 (2011) ] 
  * 191=&gt; XC_GGA_X_HTBS! Haas, Tran, Blaha, and Schwarz [P Haas, F Tran, P Blaha, and K Schwarz, Phys. Rev. B 83, 205117 (2011) ] 
  * 192=&gt; XC_GGA_X_AIRY ! Constantin et al based on the Airy gas [LA Constantin, A Ruzsinszky, and JP Perdew, Phys. Rev. B 80, 035125 (2009) ] 
  * 193=&gt; XC_GGA_X_LAG ! Local Airy Gas [L Vitos, B Johansson, J Kollar, and HL Skriver, Phys. Rev. B 62, 10046-10050 (2000) ] 
  * 194=&gt; XC_GGA_XC_MOHLYP ! Functional for organometallic chemistry [NE Schultz, Y Zhao, DGJ Truhlar, Phys. Chem. A, 109, 11127 (2005) ] 
  * 195=&gt; XC_GGA_XC_MOHLYP2 ! Functional for barrier heights [J Zheng, Y Zhao, DGJ Truhlar, Chem. Theory. Comput. 5, 808 (2009) ] 
  * 196=&gt; XC_GGA_XC_TH_FL ! Tozer and Handy v. FL [DJ Tozer, NC Handy, amd WH Green, Chem. Phys. Lett. 273, 183-194 (1997) ] 
  * 197=&gt; XC_GGA_XC_TH_FC ! Tozer and Handy v. FC [DJ Tozer, NC Handy, amd WH Green, Chem. Phys. Lett. 273, 183-194 (1997) ] 
  * 198=&gt; XC_GGA_XC_TH_FCFO ! Tozer and Handy v. FCFO [DJ Tozer, NC Handy, amd WH Green, Chem. Phys. Lett. 273, 183-194 (1997) ] 
  * 199=&gt; XC_GGA_XC_TH_FCO ! Tozer and Handy v. FCO [DJ Tozer, NC Handy, amd WH Green, Chem. Phys. Lett. 273, 183-194 (1997) ] 
  * 200=&gt; XC_GGA_C_OPTC ! Optimized correlation functional of Cohen and Handy [AJ Cohen and NC Handy, Mol. Phys. 99, 607-615 (2001) ] 
  * 524=&gt; XC_GGA_X_WPBEH ! short-range version of the PBE [J Heyd, GE Scuseria, and M Ernzerhof, J. Chem. Phys. 118, 8207 (2003) ] 
  * 525=&gt; XC_GGA_X_HJS_PBE ! HJS screened exchange PBE version [TM Henderson, BG Janesko, and GE Scuseria, J. Chem. Phys. 128, 194105 (2008) ] 
  * 526=&gt; XC_GGA_X_HJS_PBE_SOL ! HJS screened exchange PBE_SOL version [TM Henderson, BG Janesko, and GE Scuseria, J. Chem. Phys. 128, 194105 (2008) ] 
  * 527=&gt; XC_GGA_X_HJS_B88 ! HJS screened exchange B88 version [TM Henderson, BG Janesko, and GE Scuseria, J. Chem. Phys. 128, 194105 (2008) ] WARNING : this functional is not tested. Use at your own risks. 
  * 528=&gt; XC_GGA_X_HJS_B97X ! HJS screened exchange B97x version [TM Henderson, BG Janesko, and GE Scuseria, J. Chem. Phys. 128, 194105 (2008) ] 
  * 529=&gt; XC_GGA_X_ITYH ! short-range recipe for exchange GGA functionals [H Iikura, T Tsuneda, T Yanai, and K Hirao, J. Chem. Phys. 115, 3540 (2001) ] WARNING : this functional is not tested. Use at your own risks. 

MetaGGA functionals (do not forget to add a minus sign, as discussed above).
See Sun et al, PRB 84, 035117 (2011) for the formulas.

  * 202=&gt; XC_MGGA_X_TPSS ! Tao, Perdew, Staroverov &amp; Scuseria [J Tao, JP Perdew, VN Staroverov, and G Scuseria, Phys. Rev. Lett. 91, 146401 (2003) ; JP Perdew, J Tao, VN Staroverov, and G Scuseria, J. Chem. Phys. 120, 6898 (2004) ] 
  * 203=&gt; XC_MGGA_X_M06L ! Zhao, Truhlar exchange [Y Zhao and DG Truhlar, JCP 125, 194101 (2006); Y Zhao and DG Truhlar, Theor. Chem. Account 120, 215 (2008) ] 
  * 204=&gt; XC_MGGA_X_GVT4 ! GVT4 (X part of VSXC) from van Voorhis and Scuseria [T Van Voorhis and GE Scuseria, JCP 109, 400 (1998) ] 
  * 205=&gt; XC_MGGA_X_TAU_HCTH ! tau-HCTH from Boese and Handy [AD Boese and NC Handy, JCP 116, 9559 (2002) ] 
  * 207=&gt; XC_MGGA_X_BJ06 ! Becke &amp; Johnson correction to Becke-Roussel 89 [AD Becke and ER Johnson, J. Chem. Phys. 124, 221101 (2006) ] WARNING : this Vxc-only mGGA can only be used with a LDA correlation, typically Perdew-Wang 92. 
  * 208=&gt; XC_MGGA_X_TB09 ! Tran-blaha - correction to Becke &amp; Johnson correction to Becke-Roussel 89 [F Tran and P Blaha, Phys. Rev. Lett. 102, 226401 (2009) ] WARNING : this Vxc-only mGGA can only be used with a LDA correlation, typically Perdew-Wang 92. 
  * 209=&gt; XC_MGGA_X_RPP09 ! Rasanen, Pittalis, and Proetto correction to Becke &amp; Johnson [E Rasanen, S Pittalis &amp; C Proetto, arXiv:0909.1477 (2009) ] WARNING : this Vxc-only mGGA can only be used with a LDA correlation, typically Perdew-Wang 92. 
  * 232=&gt; XC_MGGA_C_VSXC ! VSxc from Van Voorhis and Scuseria (correlation part) [T Van Voorhis and GE Scuseria, JCP 109, 400 (1998) ] 

Hybrid functionals (do not forget to add a minus sign, as discussed above).

  * 402=&gt; XC_HYB_GGA_XC_B3LYP ! The (in)famous B3LYP [PJ Stephens, FJ Devlin, CF Chabalowski, MJ Frisch, J. Phys. Chem. 98 11623 (1994) ] 
  * 406=&gt; XC_HYB_GGA_XC_PBEH ! PBEH (PBE0) [C Adamo and V Barone, J. Chem. Phys. 110, 6158 (1999); M. Ernzerhof, G. E. Scuseria, J. Chem. Phys. 110, 5029 (1999) ] 
  * 427=&gt; XC_HYB_GGA_XC_HSE03 ! The 2003 version of the screened hybrid HSE (in this case one should use omega^HF = 0.15/sqrt(2) and omega^PBE = 0.15*(2.0)**1/3)   
428=&gt; XC_HYB_GGA_XC_HSE06 ! The 2006 version of the screened hybrid HSE (in
this case one should use omega^HF = omega^PBE = 0.11)  
(The following section is taken from the LibXC sources. In ABINIT, we stick to
the LibXC choice.) Note that there is an enormous mess in the literature
concerning the values of omega in HSE. This is due to an error in the original
paper that stated that they had used omega=0.15. This was in fact not true,
and the real value used was omega^HF = 0.15/sqrt(2) ~ 0.1061 and omega^PBE =
0.15*(2.0)**1/3 ~ 0.1890. In 2006 Krukau et al [JCP 125, 224106 (2006)] tried
to clarify the situation, and called HSE03 to the above choice of parameters,
and called HSE06 to the functional where omega^HF=omega^PBE. By testing
several properties for atoms they reached the conclusion that the best value
for omega=0.11. Of course, codes are just as messy as the papers. In espresso
HSE06 has the value omega=0.106. VASP, on the other hand, uses for HSE03 the
same value omega^HF = omega^PBE = 0.3 (A^-1) ~ 0.1587 and for HSE06 omega^HF =
omega^PBE = 0.2 (A^-1) ~ 0.1058. [J Heyd, GE Scuseria, and M Ernzerhof, J.
Chem. Phys. 118, 8207 (2003); J Heyd, GE Scuseria, and M Ernzerhof, J. Chem.
Phys. 124, 219906 (2006); AV Krukau, OA Vydrov, AF Izmaylov, and GE Scuseria,
J. Chem. Phys. 125, 224106 (2006) ]

  * 456=&gt; XC_HYB_GGA_XC_PBE0_13 ! PBE0-1/3 [P Cortona, J. Chem. Phys. 136, 086101 (2012) ] 


* * *

## **jdtset** 


*Mnemonics:* index -J- for DaTaSETs  
*Variable type:* integer  
*Dimensions:* ([[ndtset]])  
*Default value:* [1 .. [[ndtset]]]  



Gives the dataset index of each of the datasets. This index will be used :

  * to determine which input variables are specific to each dataset, since the variable names for this dataset will be made from the bare variable name concatenated with this index, and only if such a composite variable name does not exist, the code will consider the bare variable name, or even, the Default; 
  * to characterize output variable names, if their content differs from dataset to dataset; 
  * to characterize output files ( root names appended with _DSx where 'x' is the dataset index ). 

The allowed index values are between 1 and 9999.  
An input variable name appended with 0 is not allowed.  
When [[ndtset]]==0, this array is not used, and moreover, no input variable
name appended with a digit is allowed. This array might be initialized thanks
to the use of the input variable [[udtset]]. In this case, [[jdtset]] cannot
be used.


* * *

## **kpt** 


*Mnemonics:* K - PoinTs  
*Variable type:* real  
*Dimensions:* (3,[[nkpt]])  
*Default value:* [0, 0, 0]  
*Comment:* Adequate for one molecule in a supercell  



Contains the k points in terms of reciprocal space primitive translations (NOT
in cartesian coordinates!).  
Needed ONLY if [[kptopt]]=0, otherwise deduced from other input variables.

It contains dimensionless numbers in terms of which the cartesian coordinates
would be:  
k_cartesian = k1*G1+k2*G2+k3*G3  
where  (k1,k2,k3)  represent the dimensionless "reduced coordinates" and  G1,
G2, G3  are the cartesian coordinates of the primitive translation vectors.
G1,G2,G3 are related to the choice of direct space primitive translation
vectors made in [[rprim]]. Note that an overall norm for the k points is
supplied by [[kptnrm]]. This allows one to avoid supplying many digits for the
k points to represent such points as (1,1,1)/3.  
Note: one of the algorithms used to set up the sphere of G vectors for the
basis needs components of k-points in the range [-1,1], so the remapping is
easily done by adding or subtracting 1 from each component until it is in the
range [-1,1]. That is, given the k point normalization [[kptnrm]] described
below, each component must lie in [-[[kptnrm]],[[kptnrm]]].  
Note: a global shift can be provided by [[qptn]]  
Not read if [[kptopt]]/=0 .


* * *

## **kptnrm** 


*Mnemonics:* K - PoinTs NoRMalization  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1  



Establishes a normalizing denominator for each k point. Needed only if
[[kptopt]]&lt;=0, otherwise deduced from other input variables.  
The k point coordinates as fractions of reciprocal lattice translations are
therefore [[kpt]](mu,ikpt)/[[kptnrm]]. [[kptnrm]] defaults to 1 and can be
ignored by the user. It is introduced to avoid the need for many digits in
representing numbers such as 1/3.  
It cannot be smaller than 1.0d0


* * *

## **kptopt** 


*Mnemonics:* KPoinTs OPTion  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 4 if [[nspden]]==4,
1 otherwise.
  



Controls the set up of the k-points list. The aim will be to initialize, by
straight reading or by a preprocessing approach based on other input
variables, the following input variables, giving the k points, their number,
and their weight: [[kpt]], [[kptnrm]], [[nkpt]], and, for [[iscf]]/=-2,
[[wtk]].

Often, the k points will form a lattice in reciprocal space. In this case, one
will also aim at initializing input variables that give the reciprocal of this
k-point lattice, as well as its shift with respect to the origin: [[ngkpt]] or
[[kptrlatt]], as well as on [[nshiftk]] and [[shiftk]].

A global additional shift can be provided by [[qptn]]

  * 0=&gt; read directly [[nkpt]], [[kpt]], [[kptnrm]] and [[wtk]]. 
  * 1=&gt; rely on [[ngkpt]] or [[kptrlatt]], as well as on [[nshiftk]] and [[shiftk]] to set up the k points. Take fully into account the symmetry to generate the k points in the Irreducible Brillouin Zone only, with the appropriate weights.   
(This is the usual mode for GS calculations)

  * 2=&gt; rely on [[ngkpt]] or [[kptrlatt]], as well as on [[nshiftk]] and [[shiftk]] to set up the k points. Take into account only the time-reversal symmetry : k points will be generated in half the Brillouin zone, with the appropriate weights.   
(This is to be used when preparing or executing a RF calculation at q=(0 0 0)
)

  * 3=&gt; rely on [[ngkpt]] or [[kptrlatt]], as well as on [[nshiftk]] and [[shiftk]] to set up the k points. Do not take into account any symmetry : k points will be generated in the full Brillouin zone, with the appropriate weights.   
(This is to be used when preparing or executing a RF calculation at non-zero q
)

  * 4=&gt; rely on [[ngkpt]] or [[kptrlatt]], as well as on [[nshiftk]] and [[shiftk]] to set up the k points. Take into account all the symmetries EXCEPT the time-reversal symmetry to generate the k points in the Irreducible Brillouin Zone, with the appropriate weights.   
This has to be used when performing calculations with non-collinear magnetism
allowed ([[nspden]]=4)

  * A negative value =&gt; rely on [[kptbounds]], and [[ndivk]] to set up a band structure calculation along different lines (allowed only for [[iscf]]==-2). The absolute value of [[kptopt]] gives the number of segments of the band structure. Weights are usually irrelevant with this option, and will be left to their default value. 

In the case of a grid of k points, the auxiliary variables [[kptrlen]],
[[ngkpt]] and [[prtkpt]] might help you to select the optimal grid.


* * *

## **natom** 


*Mnemonics:* Number of ATOMs  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Gives the total number of atoms in the unit cell. Default is 1 but you will
obviously want to input this value explicitly.  
Note that [[natom]] refers to all atoms in the unit cell, not only to the
irreducible set of atoms in the unit cell (using symmetry operations, this set
allows to recover all atoms). If you want to specify only the irreducible set
of atoms, use the symmetriser, see the input variable [[natrd]].


* * *

## **nband** 


*Mnemonics:* Number of BANDs  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* None  
*Comment:*  the estimated number of occupied bands +1 (TODO provide the mathematical formulation)  



Gives number of bands, occupied plus possibly unoccupied, for which
wavefunctions are being computed along with eigenvalues.  
Note : if the parameter [[occopt]] (see below) is not set to 2, [[nband]] is a
scalar integer, but if the parameter [[occopt]] is set to 2, then [[nband]]
must be an array [[nband]]([[nkpt]]* [[nsppol]]) giving the number of bands
explicitly for each k point. This option is provided in order to allow the
number of bands treated to vary from k point to k point.  
For the values of [[occopt]] not equal to 0 or 2, [[nband]] can be omitted.
The number of bands will be set up thanks to the use of the variable
[[fband]]. The present Default will not be used.

If [[nspinor]] is 2, nband must be even for each k point.

In the case of a [[GW]] calculation ([[optdriver]]=3 or 4), [[nband]] gives
the number of bands to be treated to generate the screening (susceptibility
and dielectric matrix), as well as the self-energy. However, to generate the
_KSS file (see [[kssform]]) the relevant number of bands is given by
[[nbandkss]].


* * *

## **nbandhf** 


*Mnemonics:* Number of BANDs for (Hartree)-Fock exact exchange  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* None  
*Comment:* the estimated number of occupied bands (TODO : provide the mathematical formulation)  



Gives the maximum number of occupied bands with which Fock exact exchange is
being computed for the wavefunctions.


* * *

## **ndtset** 


*Mnemonics:* Number of DaTaSETs  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Gives the number of data sets to be treated.  
If 0, means that the multi-data set treatment is not used, so that the root
filenames will not be appended with _DSx, where 'x' is the dataset index
defined by the input variable [[jdtset]], and also that input names with a
dataset index are not allowed. Otherwise, [[ndtset]]=0 is equivalent to
[[ndtset]]=1.


* * *

## **ngkpt** 


*Mnemonics:* Number of Grid points for K PoinTs generation  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[kptopt]] >=0,   
*The use of this variable forbids the use of:* specified([[kptrlatt]])  



Used when [[kptopt]]&gt;=0, if [[kptrlatt]] has not been defined ([[kptrlatt]]
and [[ngkpt]] are exclusive of each other).  
Its three positive components give the number of k points of Monkhorst-Pack
grids (defined with respect to primitive axis in reciprocal space) in each of
the three dimensions. [[ngkpt]] will be used to generate the corresponding
[[kptrlatt]] input variable. The use of [[nshiftk]] and [[shiftk]], allows to
generate shifted grids, or Monkhorst-Pack grids defined with respect to
conventional unit cells.

When [[nshiftk]]=1, [[kptrlatt]] is initialized as a diagonal (3x3) matrix,
whose diagonal elements are the three values [[ngkpt]](1:3). When [[nshiftk]]
is greater than 1, ABINIT will try to generate [[kptrlatt]] on the basis of
the primitive vectors of the k-lattice: the number of shifts might be reduced,
in which case [[kptrlatt]] will not be diagonal anymore.

Monkhorst-Pack grids are usually the most efficient when their defining
integer numbers are even. For a measure of the efficiency, see the input
variable [[kptrlen]].


* * *

## **nkpath** 


*Mnemonics:* Number of K-points defining the PATH  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



This variable is used to define the number of high-symmetry k-points in the
[[kptbounds]] array when [[kptopt]] > 0. Historically, [[kptbounds]] is used
in conjuction with a negative value of [[kptopt]] when performing a NSCF band
structure calculation. In this case, the number of k-points in kptbounds is
given by abs(kptopt) + 1. There are, however, other cases in which one has to
specify a k-path in the input file in order to activate some kind of post-
processing tool. Typical examples are the interpolation of the GW corrections
at the end of the sigma run or the interpolation of the KS eigenvalues along a
path at the end of the SCF run (see also [[einterp]]) In a nutshell, nkpath
replaces [[kptopt]] when we are not performing a NSCF calculation. Note that,
unlike [[kptopt]], nkpath represents the total number of points in the
[[kptbounds]] array.


* * *

## **nkpt** 


*Mnemonics:* Number of K - Points  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[kptopt]]==0,
0 otherwise.
  



If non-zero, [[nkpt]] gives the number of k points in the k point array
[[kpt]]. These points are used either to sample the Brillouin zone, or to
build a band structure along specified lines.

If [[nkpt]] is zero, the code deduces from other input variables (see the list
in the description of [[kptopt]]) the number of k points, which is possible
only when [[kptopt]]/=0. If [[kptopt]]/=0 and the input value of [[nkpt]]/=0,
then ABINIT will check that the number of k points generated from the other
input variables is exactly the same than [[nkpt]].

If [[kptopt]] is positive, [[nkpt]] must be coherent with the values of
[[kptrlatt]], [[nshiftk]] and [[shiftk]].  
For ground state calculations, one should select the k point in the
irreducible Brillouin Zone (obtained by taking into account point symmetries
and the time-reversal symmetry).  
For response function calculations, one should select k points in the full
Brillouin zone, if the wavevector of the perturbation does not vanish, or in a
half of the Brillouin Zone if q=0. The code will automatically decrease the
number of k points to the minimal set needed for each particular perturbation.

If [[kptopt]] is negative, [[nkpt]] will be the sum of the number of points on
the different lines of the band structure. For example, if [[kptopt]]=-3, one
will have three segments; supposing [[ndivk]] is 10 12 17, the total number of
k points of the circuit will be 10+12+17+1(for the final point)=40.


* * *

## **nkpthf** 


*Mnemonics:* Number of K - Points for (Hartree) Fock exact exchange  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* None  
*Comment:*  the total number of k-point in the full Brillouin zone (TODO : provide the mathematical formulation)  



[[nkpthf]] gives the number of k points used to sample the full Brillouin zone
for the Fock exact exchange contribution.


* * *

## **nshiftk** 


*Mnemonics:* Number of SHIFTs for K point grids  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



This parameter gives the number of shifted grids to be used concurrently to
generate the full grid of k points. It can be used with primitive grids
defined either from [[ngkpt]] or [[kptrlatt]]. The maximum allowed value of
[[nshiftk]] is 8. The values of the shifts are given by [[shiftk]].


* * *

## **nsppol** 


*Mnemonics:* Number of SPin POLarization  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Give the number of INDEPENDENT spin polarisations, for which there are non-
related wavefunctions. Can take the values 1 or 2.

If [[nsppol]]=1, one has an unpolarized calculation ([[nspinor]]=1,
[[nspden]]=1) or an antiferromagnetic system ([[nspinor]]=1, [[nspden]]=2), or
a calculation in which spin up and spin down cannot be disentangled
([[nspinor]]=2), that is, either non-collinear magnetism or presence of spin-
orbit coupling, for which one needs spinor wavefunctions.

If [[nsppol]]=2, one has a spin-polarized (collinear) calculation with
separate and different wavefunctions for up and down spin electrons for each
band and k point. Compatible only with [[nspinor]]=1, [[nspden]]=2. If
[[nsppol]]=2, one usually uses a metallic value for [[occopt]], in order to
let ABINIT find the magnetization. On the contrary, if [[occopt]]==1 is used,
the user has to impose the magnetization, using [[spinmagntarget]], except for
the case of a single isolated Hydrogen atom.

In the present status of development, with [[nsppol]]=1, all values of [[ixc]]
are allowed, while with [[nsppol]]=2, some values of [[ixc]] might not be
allowed (e.g. 2, 3, 4, 5, 6, 20, 21, 22 are not allowed).

See also the input variable [[nspden]] for the components of the density
matrix with respect to the spin-polarization.


* * *

## **nstep** 


*Mnemonics:* Number of (non-)self-consistent field STEPS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 30  



Gives the maximum number of cycles (or "iterations") in a SCF or non-SCF run.  
Full convergence from random numbers is usually achieved in 12-20 SCF
iterations. Each can take from minutes to hours. In certain difficult cases,
usually related to a small or zero bandgap or magnetism, convergence
performance may be much worse. When the convergence tolerance [[tolwfr]] on
the wavefunctions is satisfied, iterations will stop, so for well converged
calculations you should set [[nstep]] to a value larger than you think will be
needed for full convergence, e.g. if using 20 steps usually converges the
system, set [[nstep]] to 30.  
For non-self-consistent runs ( [[iscf]] &lt; 0) nstep governs the number of
cycles of convergence for the wavefunctions for a fixed density and
Hamiltonian.

NOTE that a choice of [[nstep]]=0 is permitted; this will either read
wavefunctions from disk (with [[irdwfk]]=1 or [[irdwfq]]=1, or non-zero
[[getwfk]] or [[getwfq]] in the case of multi-dataset) and compute the
density, the total energy and stop, or else (with all of the above vanishing)
will initialize randomly the wavefunctions and compute the resulting density
and total energy. This is provided for testing purposes.  
Also NOTE that [[nstep]]=0 with [[irdwfk]]=1 will exactly give the same result
as the previous run only if the latter is done with [[iscf]]&lt;10 (potential
mixing).  
One can output the density by using [[prtden]].  
The forces and stress tensor are computed with [[nstep]]=0.


* * *

## **nsym** 


*Mnemonics:* Number of SYMmetry operations  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Gives number of space group symmetries to be applied in this problem.
Symmetries will be input in array "[[symrel]]" and (nonsymmorphic)
translations vectors will be input in array "[[tnons]]". If there is no
symmetry in the problem then set [[nsym]] to 1, because the identity is still
a symmetry.  
In case of a RF calculation, the code is able to use the symmetries of the
system to decrease the number of perturbations to be calculated, and to
decrease of the number of special k points to be used for the sampling of the
Brillouin zone. After the response to the perturbations have been calculated,
the symmetries are used to generate as many as possible elements of the 2DTE
from those already computed.

[[SYMMETRY_FINDER]] mode (Default mode). If [[nsym]] is 0, all the atomic
coordinates must be explicitely given (one cannot use the geometry builder and
the symmetrizer): the code will then find automatically the symmetry
operations that leave the lattice and each atomic sublattice invariant. It
also checks whether the cell is primitive (see [[chkprim]]).  
Note that the tolerance on symmetric atomic positions and lattice is rather
stringent : for a symmetry operation to be admitted, the lattice and atomic
positions must map on themselves within 1.0e-8 .

The user is allowed to set up systems with non-primitive unit cells (i.e.
conventional FCC or BCC cells, or supercells without any distortion). In this
case, pure translations will be identified as symmetries of the system by the
symmetry finder. Then, the combined "pure translation + usual rotation and
inversion" symmetry operations can be very numerous. For example, a
conventional FCC cell has 192 symmetry operations, instead of the 48 ones of
the primitive cell. A maximum limit of 384 symmetry operations is hard-coded.
This corresponds to the maximum number of symmetry operations of a 2x2x2
undistorted supercell. Going beyond that number will make the code stop very
rapidly. If you want nevertheless, for testing purposes, to treat a larger
number of symmetries, change the initialization of "msym" in the abinit.F90
main routine, then recompile the code.

For [[GW]] calculation, the user might want to select only the symmetry
operations whose non-symmorphic translation vector [[tnons]] is zero. This can
be done with the help of the input variable [[symmorphi]]


* * *

## **ntypat** 


*Mnemonics:* Number of TYPes of AToms  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Gives the number of types of atoms. E.g. for a homopolar system (e.g. pure Si)
[[ntypat]] is 1.  
The code tries to read the same number of pseudopotential files.  
The first pseudopotential is assigned type number 1, and so on ...


* * *

## **occopt** 


*Mnemonics:* OCCupation OPTion  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Controls how input parameters [[nband]], [[occ]], and [[wtk]] are handled.

  * [[occopt]]=0:   
All k points have the same number of bands and the same occupancies of bands.
[[nband]] is given as a single number, and [[occ]]([[nband]]) is an array of
[[nband]] elements, read in by the code.  
The k point weights in array [[wtk]]([[nkpt]]) are automatically normalized by
the code to add to 1.

  * [[occopt]]=1:   
Same as [[occopt]]=0, except that the array [[occ]] is automatically generated
by the code, to give a semiconductor.  
An error occurs when filling cannot be done with occupation numbers equal to 2
or 0 in each k-point (non-spin-polarized case), or with occupation numbers
equal to 1 or 0 in each k-point (spin-polarized case). If [[nsppol]]=2 and
[[occopt]]==1 is used, the user has to impose the magnetization, using
[[spinmagntarget]], except for the case of a single isolated Hydrogen atom.

  * [[occopt]]=2:   
k points may optionally have different numbers of bands and different
occupancies. [[nband]]([[nkpt]]*[[nsppol]]) is given explicitly as an array of
[[nkpt]]*[[nsppol]] elements. [[occ]]() is given explicitly for all bands at
each k point, and eventually for each spin -- the total number of elements is
the sum of [[nband]](ikpt) over all k points and spins. The k point weights
[[wtk]] ([[nkpt]]) are NOT automatically normalized under this option.

  * [[occopt]]=3, 4, 5, 6 and 7   
Metallic occupation of levels, using different occupation schemes (see below).
The corresponding thermal broadening, or cold smearing, is defined by the
input variable [[tsmear]] (see below : the variable xx is the energy in Ha,
divided by [[tsmear]])  
Like for [[occopt]]=1, the variable [[occ]] is not read  
All k points have the same number of bands, [[nband]] is given as a single
number, read by the code.  
The k point weights in array [[wtk]]([[nkpt]]) are automatically normalized by
the code to add to 1.

    * [[occopt]]=3:   
Fermi-Dirac smearing (finite-temperature metal) Smeared delta function :
0.25d0/(cosh(xx/2.0d0)**2)

    * [[occopt]]=4:   
"Cold smearing" of N. Marzari (see his thesis work), with a=-.5634
(minimization of the bump)  
Smeared delta function :  
exp(-xx  2  )/sqrt(pi) * (1.5d0+xx*(-a*1.5d0+xx*(-1.0d0+a*xx)))

    * [[occopt]]=5:   
"Cold smearing" of N. Marzari (see his thesis work), with a=-.8165 (monotonic
function in the tail)  
Same smeared delta function as [[occopt]]=4, with different a.

    * [[occopt]]=6:   
Smearing of Methfessel and Paxton [[Methfessel1989]] with Hermite polynomial
of degree 2, corresponding to "Cold smearing" of N. Marzari with a=0 (so, same
smeared delta function as [[occopt]]=4, with different a).

    * [[occopt]]=7:   
Gaussian smearing, corresponding to the 0 order Hermite polynomial of
Methfessel and Paxton.  
Smeared delta function : 1.0d0*exp(-xx**2)/sqrt(pi)

    * [[occopt]]=8:   
Uniform smearing (the delta function is replaced by a constant function of
value one over ]-1/2,1/2[ (with one-half value at the boundaries). Used for
testing purposes only.

WARNING : one can use metallic occupation of levels in the case of a molecule,
in order to avoid any problem with degenerate levels. However, it is advised
NOT to use [[occopt]]=6 (and to a lesser extent [[occopt]]=4 and 5), since the
associated number of electron versus the Fermi energy is NOT guaranteed to be
a monotonic function. For true metals, AND a sufficiently dense sampling of
the Brillouin zone, this should not happen, but be cautious ! As an indication
of this problem, a small variation of input parameters might lead to a jump of
total energy, because there might be two or even three possible values of the
Fermi energy, and the bissection algorithm find one or the other.


* * *

## **rprim** 


*Mnemonics:* Real space PRIMitive translations  
*Variable type:* real  
*Dimensions:* (3,3)  
*commentdims:* Internally, it is represented as rprim(3,3,[[nimage]])  
*Default value:* [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  



Give, in columnwise entry, the three dimensionless primitive translations in
real space, to be rescaled by [[acell]] and [[scalecart]].  
It is [[EVOLVING]] only if [[ionmov]]==2 and [[optcell]]/=0, otherwise it is
fixed.  
If the Default is used, that is, [[rprim]] is the unity matrix, the three
dimensionless primitive vectors are three unit vectors in cartesian
coordinates. Each will be (possibly) multiplied by the corresponding [[acell]]
value, then (possibly) stretched along the cartesian coordinates by the
corresponding [[scalecart]] value, to give the dimensional primitive vectors,
called [[rprimd]].  
In the general case, the dimensional cartesian coordinates of the crystal
primitive translations R1p, R2p and R3p, see [[rprimd]], are

  * R1p(i)=[[scalecart]](i)[[rprim]](i,1)*[[acell]](1) 
  * R2p(i)=[[scalecart]](i)[[rprim]](i,2)*[[acell]](2) 
  * R3p(i)=[[scalecart]](i)[[rprim]](i,3)*[[acell]](3) 

where i=1,2,3 is the component of the primitive translation (i.e. x, y, and
z).  
  
The [[rprim]] variable, scaled by [[scalecart]], is thus used to define
directions of the primitive vectors, that will be multiplied (so keeping the
direction unchanged) by the appropriate length scale [[acell]](1),
[[acell]](2), or [[acell]](3), respectively to give the dimensional primitive
translations in real space in cartesian coordinates.  
Presently, it is requested that the mixed product (R1xR2).R3 is positive. If
this is not the case, simply exchange a pair of vectors.  
To be more specific, keeping the default value of [[scalecart]]=1 to simplify
the matter, [[rprim]] 1 2 3 4 5 6 7 8 9 corresponds to input of the three
primitive translations R1=(1,2,3) (to be multiplied by [[acell]](1)),
R2=(4,5,6) (to be multiplied by [[acell]](2)), and R3=(7,8,9) (to be
multiplied by [[acell](3)).  
Note carefully that the first three numbers input are the first column of
[[rprim]], the next three are the second, and the final three are the third.
This corresponds with the usual Fortran order for arrays. The matrix whose
columns are the reciprocal space primitive translations is the inverse
transpose of the matrix whose columns are the direct space primitive
translations.

Alternatively to [[rprim]], directions of dimensionless primitive vectors can
be specified by using the input variable [[angdeg]]. This is especially useful
for hexagonal lattices (with 120 or 60 degrees angles). Indeed, in order for
symmetries to be recognized, rprim must be symmetric up to [[tolsym]] (10
digits by default), inducing a specification such as

    
    
      rprim  0.86602540378  0.5  0.0
            -0.86602540378  0.5  0.0
             0.0            0.0  1.0
     

that can be avoided thanks to [[angdeg]]:

    
    
      angdeg 90 90 120
     

  
Although the use of [[scalecart]] or [[acell]] is rather equivalent when the
primitive vectors are aligned with the cartesian directions, it is not the
case for non-orthogonal primitive vectors. In particular, beginners often make
the error of trying to use [[acell]] to define primitive vectors in face-
centered tetragonal lattice, or body-centered tetragonal lattice, or similarly
in face or body-centered orthorhombic lattices. Let us take the example of a
body-centered tetragonal lattice, that might be defined using the following
("a" and "c" have to be replaced by the appropriate conventional cell vector
length):

    
    
      rprim  "a"      0        0
              0      "a"       0
             "a/2"   "a/2"    "c/2"
    acell 3*1     scalecart 3*1    !  ( These are default values)
     

The following is a valid, alternative way to define the same primitive vectors
:

    
    
      rprim   1        0       0
              0        1       0
              1/2      1/2     1/2
    scalecart  "a"  "a"  "c"
    acell 3*1    !  ( These are default values)
     

Indeed, the cell has been stretched along the cartesian coordinates, by "a",
"a" and "c" factors.

At variance, the following is WRONG :

    
    
      rprim   1       0       0
              0       1       0
              1/2     1/2     1/2
    acell  "a"  "a"  "c"    !   THIS IS WRONG
    scalecart 3*1    !  ( These are default values)
     

Indeed, the latter would correspond to :

    
    
      rprim  "a"      0       0
              0      "a"      0
             "c/2"   "c/2"   "c/2"
    acell 3*1     scalecart 3*1    !  ( These are default values)
     

Namely, the third vector has been rescaled by "c". It is not at all in the
center of the tetragonal cell whose basis vectors are defined by the scaling
factor "a".  
As another difference between [[scalecart]] or [[acell]], note that
[[scalecart]] is [[INPUT_ONLY]] : its content will be immediately applied to
rprim, at parsing time, and then scalecart will be set to the default values
(3*1). So, in case [[scalecart]] is used, the echo of [[rprim]] in the output
file is not the value contained in the input file, but the value rescaled by
[[scalecart]].


* * *

## **rprimd** 


*Mnemonics:* Real space PRIMitive translations, Dimensional  
*Variable type:* real  
*Dimensions:* (3,3)  
*commentdims:* Internally, it is represented as rprimd(3,3,[[nimage]]).  
*Default value:* None  



This internal variable gives the dimensional real space primitive vectors,
computed from [[acell]], [[scalecart]], and [[rprim]].

  * R1p(i)=[[rprimd]](i,1)=[[scalecart]](i)*[[rprim]](i,1)*[[acell]](1) for i=1,2,3 (x,y,and z) 
  * R2p(i)=[[rprimd]](i,2)=[[scalecart]](i)*[[rprim]](i,2)*[[acell]](2) for i=1,2,3 
  * R3p(i)=[[rprimd]](i,3)=[[scalecart]](i)*[[rprim]](i,3)*[[acell]](3) for i=1,2,3 

It is [[EVOLVING]] only if [[ionmov]]==2 and [[optcell]]/=0, otherwise it is
fixed.  


* * *

## **scalecart** 


*Mnemonics:* SCALE CARTesian coordinates  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* 3*1  



Gives the scaling factors of cartesian coordinates by which dimensionless
primitive translations (in "[[rprim]]") are to be multiplied. [[rprim]] input
variable, the [[acell]] input variable, and the associated internal [[rprimd]]
internal variable.  
Especially useful for body-centered and face-centered tetragonal lattices, as
well as body-centered and face-centered orthorhombic lattices, see [[rprimd]].  
Note that this input variable is [[INPUT_ONLY]] : its content will be
immediately applied to rprim, at parsing time, and then scalecart will be set
to the default values. So, it will not be echoed.


* * *

## **shiftk** 


*Mnemonics:* SHIFT for K points  
*Variable type:* real  
*Dimensions:* (3,[[nshiftk]])  
*Default value:* None if [[nshiftk]]>1,
[0.5, 0.5, 0.5] otherwise.
  



It is used only when [[kptopt]]&gt;=0, and must be defined if [[nshiftk]] is
larger than 1.  
[[shiftk]](1:3,1:[[nshiftk]]) defines [[nshiftk]] shifts of the homogeneous
grid of k points based on [[ngkpt]] or [[kptrlatt]].  
The shifts induced by [[shiftk]] corresponds to the reduced coordinates in the
coordinate system defining the k-point lattice. For example, if the k point
lattice is defined using [[ngkpt]], the point whose reciprocal space reduced
coordinates are ( [[shiftk]](1,ii)/[[ngkpt]](1) [[shiftk]](2,ii)/[[ngkpt]](2)
[[shiftk]](3,ii)/[[ngkpt]](3) ) belongs to the shifted grid number ii.

The user might rely on ABINIT to suggest suitable and efficient combinations
of [[kptrlatt]] and [[shiftk]]. The procedure to be followed is described with
the input variables [[kptrlen]]. In what follows, we suggest some interesting
values of the shifts, to be used with even values of [[ngkpt]]. This list is
much less exhaustive than the above-mentioned automatic procedure.

1) When the primitive vectors of the lattice do NOT form a FCC or a BCC
lattice, the default (shifted) Monkhorst-Pack grids are formed by using
[[nshiftk]]=1 and [[shiftk]] 0.5 0.5 0.5 . This is often the preferred k point
sampling, as the shift improves the sampling efficiency. However, it can also
break symmetry, if the 111 direction is not an axis of rotation, e.g. in
tetragonal or hexagonal systems. Abinit will complain about this breaking, and
you should adapt [[shiftk]]. For a non-shifted Monkhorst-Pack grid, use
[[nshiftk]]=1 and [[shiftk]] 0.0 0.0 0.0 , which will be compatible with all
symmetries, and is necessary for some features such as k-point interpolation.

2) When the primitive vectors of the lattice form a FCC lattice, with
[[rprim]]

    
    
      0.0 0.5 0.5
      0.5 0.0 0.5
      0.5 0.5 0.0
     

the (very efficient) usual Monkhorst-Pack sampling will be generated by using
[[nshiftk]]= 4 and [[shiftk]]

    
    
      0.5 0.5 0.5
      0.5 0.0 0.0
      0.0 0.5 0.0
      0.0 0.0 0.5
     

3) When the primitive vectors of the lattice form a BCC lattice, with
[[rprim]]

    
    
      -0.5  0.5  0.5
       0.5 -0.5  0.5
       0.5  0.5 -0.5
     

the usual Monkhorst-Pack sampling will be generated by using [[nshiftk]]= 2
and [[shiftk]]

    
    
      0.25  0.25  0.25
     -0.25 -0.25 -0.25
     

However, the simple sampling [[nshiftk]]=1 and [[shiftk]] 0.5 0.5 0.5 is
excellent.

4) For hexagonal lattices with hexagonal axes, e.g. [[rprim]]

    
    
      1.0  0.0       0.0
     -0.5  sqrt(3)/2 0.0
      0.0  0.0       1.0
     

one can use [[nshiftk]]= 1 and [[shiftk]] 0.0 0.0 0.5

In rhombohedral axes, e.g. using [[angdeg]] 3*60., this corresponds to
[[shiftk]] 0.5 0.5 0.5, to keep the shift along the symmetry axis.


* * *

## **symrel** 


*Mnemonics:* SYMmetry in REaL space  
*Variable type:* integer  
*Dimensions:* (3,3,[[nsym]])  
*Default value:* [[1, 0, 0], [0, 1, 0], [0, 0, 1]] if [[nsym]]==1,
None otherwise.
  



Gives "[[nsym]]" 3x3 matrices expressing space group symmetries in terms of
their action on the direct (or real) space primitive translations.  
It turns out that these can always be expressed as integers.  
Always give the identity matrix even if no other symmetries hold, e.g.
[[symrel]] 1 0 0 0 1 0 0 0 1  
Also note that for this array as for all others the array elements are filled
in a columnwise order as is usual for Fortran.  
The relation between the above symmetry matrices [[symrel]], expressed in the
basis of primitive translations, and the same symmetry matrices expressed in
cartesian coordinates, is as follows. Denote the matrix whose columns are the
primitive translations as R, and denote the cartesian symmetry matrix as S.
Then  
[[symrel]] = R(inverse) * S * R  
where matrix multiplication is implied.  
When the symmetry finder is used (see [[nsym]]), [[symrel]] will be computed
automatically.


* * *

## **tnons** 


*Mnemonics:* Translation NON-Symmorphic vectors  
*Variable type:* real  
*Dimensions:* (3,[[nsym]])  
*Default value:* None  



Gives the (nonsymmorphic) translation vectors associated with the symmetries
expressed in "[[symrel]]".  
These may all be 0, or may be fractional (nonprimitive) translations expressed
relative to the real space primitive translations (so, using the "reduced"
system of coordinates, see "[[xred]]"). If all elements of the space group
leave 0 0 0 invariant, then these are all 0.  
When the symmetry finder is used (see [[nsym]]), [[tnons]] is computed
automatically.


* * *

## **toldfe** 


*Mnemonics:* TOLerance on the DiFference of total Energy  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Comment:* The default value implies that this stopping condition is ignored. For the SCF case, one and only one of the input tolerance criteria [[tolwfr]], [[toldff]], [[tolrff]], [[toldfe]] or [[tolvrs]] must differ from zero.  
*The use of this variable forbids the use of:* specified([[tolwfr]]) or specified([[toldff]]) or specified([[tolrff]]) or specified([[tolvrs]])  



Sets a tolerance for absolute differences of total energy that, reached TWICE
successively, will cause one SCF cycle to stop (and ions to be moved).  
Can be specified in Ha (the default), Ry, eV or Kelvin, since [[toldfe]] has
the '[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)  
If set to zero, this stopping condition is ignored.  
Effective only when SCF cycles are done ([[iscf]]&gt;0).  
Because of machine precision, it is not worth to try to obtain differences in
energy that are smaller than about 1.0d-12 of the total energy. To get
accurate stresses may be quite demanding.  
When the geometry is optimized (relaxation of atomic positions or primitive
vectors), the use of [[toldfe]] is to be avoided. The use of [[toldff]] or
[[tolrff]] is by far preferable, in order to have a handle on the geometry
characteristics. When all forces vanish by symmetry (e.g. optimization of the
lattice parameters of a high-symmetry crystal), then place [[toldfe]] to
1.0d-12, or use (better) [[tolvrs]].  
Since [[toldfe]], [[toldff]], [[tolrff]], [[tolvrs]] and [[tolwfr]] are aimed
at the same goal (causing the SCF cycle to stop), they are seen as a unique
input variable at reading. Hence, it is forbidden that two of these input
variables have non-zero values for the same dataset, or generically (for all
datasets). However, a non-zero value for one such variable for one dataset
will have precedence on the non-zero value for another input variable defined
generically.


* * *

## **toldff** 


*Mnemonics:* TOLerance on the DiFference of Forces  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Comment:* The default value implies that this stopping condition is ignored. For the SCF case, one and only one of the input tolerance criteria [[tolwfr]], [[toldff]], [[tolrff]], [[toldfe]] or [[tolvrs]] must differ from zero.  
*The use of this variable forbids the use of:* specified([[tolwfr]]) or specified([[toldfe]]) or specified([[tolrff]]) or specified([[tolvrs]])  



Sets a tolerance for differences of forces (in hartree/Bohr) that, reached
TWICE successively, will cause one SCF cycle to stop (and ions to be moved).  
If set to zero, this stopping condition is ignored.  
Effective only when SCF cycles are done ([[iscf]]&gt;0). This tolerance
applies to any particular cartesian component of any atom, INCLUDING fixed
ones. This is to be used when trying to equilibrate a structure to its lowest
energy configuration ([[ionmov]]=2), or in case of molecular dynamics
([[ionmov]]=1)  
A value ten times smaller than [[tolmxf]] is suggested (for example 5.0d-6
hartree/Bohr).  
This stopping criterion is not allowed for RF calculations.  
Since ** toldfe ** , [[toldff]], [[tolrff]], [[tolvrs]] and [[tolwfr]] are
aimed at the same goal (causing the SCF cycle to stop), they are seen as a
unique input variable at reading. Hence, it is forbidden that two of these
input variables have non-zero values for the same dataset, or generically (for
all datasets). However, a non-zero value for one such variable for one dataset
will have precedence on the non-zero value for another input variable defined
generically.


* * *

## **tolrff** 


*Mnemonics:* TOLerance on the Relative diFference of Forces  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Comment:* The default value implies that this stopping condition is ignored. For the SCF case, one and only one of the input tolerance criteria [[tolwfr]], [[toldff]], [[tolrff]], [[toldfe]] or [[tolvrs]] must differ from zero.  
*The use of this variable forbids the use of:* specified([[tolwfr]]) or specified([[toldfe]]) or specified([[toldff]]) or specified([[tolvrs]])'  



Sets a tolerance for the ratio of differences of forces (in hartree/Bohr) to
maximum force, that, reached TWICE successively, will cause one SCF cycle to
stop (and ions to be moved) : diffor &lt; tolrff * maxfor.  
If set to zero, this stopping condition is ignored.  
Effective only when SCF cycles are done ([[iscf]]&gt;0). This tolerance
applies to any particular cartesian component of any atom, INCLUDING fixed
ones. This is to be used when trying to equilibrate a structure to its lowest
energy configuration ([[ionmov]]=2), or in case of molecular dynamics
([[ionmov]]=1)  
A value of 0.02 is suggested.  
This stopping criterion is not allowed for RF calculations.  
Since ** toldfe ** , [[toldff]], [[tolrff]], [[tolvrs]] and [[tolwfr]] are
aimed at the same goal (causing the SCF cycle to stop), they are seen as a
unique input variable at reading. Hence, it is forbidden that two of these
input variables have non-zero values for the same dataset, or generically (for
all datasets). However, a non-zero value for one such variable for one dataset
will have precedence on the non-zero value for another input variable defined
generically.


* * *

## **tolvrs** 


*Mnemonics:* TOLerance on the potential V(r) ReSidual  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Comment:* The default value implies that this stopping condition is ignored. For the SCF case, one and only one of the input tolerance criteria [[tolwfr]], [[toldff]], [[tolrff]], [[toldfe]] or [[tolvrs]] must differ from zero.  
*The use of this variable forbids the use of:* specified([[tolwfr]]) or specified([[toldfe]]) or specified([[toldff]]) or specified([[tolrff]])'  



Sets a tolerance for potential residual that, when reached, will cause one SCF
cycle to stop (and ions to be moved).  
If set to zero, this stopping condition is ignored.  
Effective only when SCF cycles are done ([[iscf]]&gt;0).  
To get accurate stresses may be quite demanding. For simple materials with
internal positions determined by symmetries, a value of [[tolvrs]]=10^-12
empirically leads to a very approximate 10^-6 atomic unit accuracy for the
optimized lattice parameter.

Additional explanation : the residual of the potential is the difference
between the input potential and the output potential, when the latter is
obtained from the density determined from the eigenfunctions of the input
potential. When the self-consistency loop is achieved, both input and output
potentials must be equal, and the residual of the potential must be zero. The
tolerance on the potential residual is imposed by first subtracting the mean
of the residual of the potential (or the trace of the potential matrix, if the
system is spin-polarized), then summing the square of this function over all
FFT grid points. The result should be lower than [[tolvrs]].  
Since ** toldfe ** , [[toldff]], [[tolrff]], [[tolvrs]] and [[tolwfr]] are
aimed at the same goal (causing the SCF cycle to stop), they are seen as a
unique input variable at reading. Hence, it is forbidden that two of these
input variables have non-zero values for the same dataset, or generically (for
all datasets). However, a non-zero value for one such variable for one dataset
will have precedence on the non-zero value for another input variable defined
generically.


* * *

## **tolwfr** 


*Mnemonics:* TOLerance on WaveFunction squared Residual  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Comment:* The default value implies that this stopping condition is ignored. For the SCF case, one and only one of the input tolerance criteria [[tolwfr]], [[toldff]], [[tolrff]], [[toldfe]] or [[tolvrs]] must differ from zero.  
*The use of this variable forbids the use of:* specified([[toldfe]]) or specified([[toldff]]) or specified([[tolrff]]) or specified([[tolvrs]])  



The signification of this tolerance depends on the basis set. In plane waves,
it gives a convergence tolerance for the largest squared "residual" (defined
below) for any given band. The squared residual is:  

    
    
      < nk|(H-E)2|nk >,    E = < nk|H|nk >
     

  
which clearly is nonnegative and goes to 0 as the iterations converge to an
eigenstate. With the squared residual expressed in Hartrees  2  (Hartrees
squared), the largest squared residual (called residm) encountered over all
bands and k points must be less than [[tolwfr]] for iterations to halt due to
successful convergence.  
Note that if [[iscf]]&gt;0, this criterion should be replaced by those based
on [[toldfe]] (preferred for [[ionmov]]==0), [[toldff]] [[tolrff]] (preferred
for [[ionmov]]/=0), or [[tolvrs]] (preferred for theoretical reasons!).  
When [[tolwfr]] is 0.0, this criterion is ignored, and a finite value of
[[toldfe]], [[toldff]] or [[tolvrs]] must be specified. This also imposes a
restriction on taking an ion step; ion steps are not permitted unless the
largest squared residual is less than [[tolwfr]], ensuring accurate forces.  
To get accurate stresses may be quite demanding.  
Note that the preparatory GS calculations before a RF calculations must be
highly converged.  
Typical values for these preparatory runs are [[tolwfr]] between 1.0d-16 and
1.0d-22.

Note that [[tolwfr]] is often used in the test cases, but this is _ tolwfr _
purely for historical reasons : except when [[iscf]]&lt;0, other critera
should be used.

In the wavelet case (see [[usewvl]] = 1), this criterion is the favoured one.
It is based on the norm 2 of the gradient of the wavefunctions. Typical values
range from 5*10  -4  to 5*10  -5  .

  
Since ** toldfe ** , [[toldff]], [[tolrff]], [[tolvrs]] and [[tolwfr]] are
aimed at the same goal (causing the SCF cycle to stop), they are seen as a
unique input variable at reading. Hence, it is forbidden that two of these
input variables have non-zero values for the same dataset, or generically (for
all datasets). However, a non-zero value for one such variable for one dataset
will have precedence on the non-zero value for another input variable defined
generically.


* * *

## **typat** 


*Mnemonics:* TYPe of AToms  
*Variable type:* integer  
*Dimensions:* [3, '[[natrd]]'] if [[natrd]]<[[natom]],
[3, '[[natom]]'] otherwise.
  
*Default value:* 1 if [[natom]]==1,
None otherwise.
  



Array giving an integer label to every atom in the unit cell to denote its
type.  
The different types of atoms are constructed from the pseudopotential files.
There are at most [[ntypat]] types of atoms.  
As an example, for BaTiO3, where the pseudopotential for Ba is number 1, the
one of Ti is number 2, and the one of O is number 3, the actual value of the
[[typat]] array might be :

    
    
      typat 1 2 3 3 3
     

  
The array [[typat]] has to agree with the actual locations of atoms given in
[[xred]] , [[xcart]] or [[xangst]], and the input of pseudopotentials has to
be ordered to agree with the atoms identified in [[typat]].  
The nuclear charge of the elements, given by the array [[znucl]], also must
agree with the type of atoms designated in "[[typat]]".  
The array [[typat]] is not constrained to be increasing. An internal
representation of the list of atoms, deep in the code (array atindx), groups
the atoms of same type together. This should be transparent to the user, while
keeping efficiency.


* * *

## **udtset** 


*Mnemonics:* Upper limit on DaTa SETs  
*Variable type:* integer  
*Dimensions:* (2)  
*Default value:* None  
*Comment:* It is not used when it is not defined  



Used to define the set of indices in the multi-data set mode, when a double
loop is needed (see later).  
The values of [[udtset]](1) must be between 1 and 999, the values of
[[udtset]](2) must be between 1 and 9, and their product must be equal to
[[ndtset]].  
The values of [[jdtset]] are obtained by looping on the two indices defined by
[[udtset]](1) and [[udtset]](2) as follows :

    
    
      do i1=1,intarr(1)
       do i2=1,intarr(2)
        idtset=idtset+1
        dtsets(idtset)%jdtset=i1*10+i2
       end do
      end do
     

So, [[udtset]](2) sets the largest value for the unity digit, that varies
between 1 and [[udtset]](2).  
If [[udtset]] is used, the input variable [[jdtset]] cannot be used.


* * *

## **usewvl** 


*Mnemonics:* Use WaVeLet basis set  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Comment:* use plane-wave basis set  



Used to define if the calculation is done on a wavelet basis set or not.  
The values of [[usewvl]] must be 0 or 1. Putting [[usewvl]] to 1, makes
[[icoulomb]] mandatory to 1. The number of band ([[nband]]) must be set
manually to the strict number need for an isolator system ( _ i.e. _ number of
electron over two). The cut-off is not relevant in the wavelet case, use
[[wvl_hgrid]] instead.  
In wavelet case, the system must be isolated systems (molecules or clusters).
All geometry optimization are available (see [[ionmov]], especially the
geometry optimisation and the molecular dynamics).  
The spin computation is not currently possible with wavelets and metalic
systems may be slow to converge.


* * *

## **wtk** 


*Mnemonics:* WeighTs for K points  
*Variable type:* real  
*Dimensions:* ([[nkpt]])  
*Default value:* [[nkpt]]*1.0  
*Comment:* Except when [[kptopt]]/=0  



Gives the k point weights.  
The k point weights will have their sum (re)normalized to 1 (unless
[[occopt]]=2 and [[kptopt]]=0; see description of [[occopt]]) within the
program and therefore may be input with any arbitrary normalization. This
feature helps avoid the need for many digits in representing fractional
weights such as 1/3.  
[[wtk]] is ignored if [[iscf]] is not positive, except if [[iscf]]=-3.


* * *

## **wvl_hgrid** 


*Mnemonics:* WaVeLet H step GRID  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.5  



It gives the step size in real space for the grid resolution in the wavelet
basis set. This value is highly responsible for the memory occupation in the
wavelet computation. The value is a length in atomic units.


* * *

## **xangst** 


*Mnemonics:* vectors (X) of atom positions in cartesian coordinates -length in ANGSTrom-  
*Variable type:* real  
*Dimensions:* (3,min([[natom]],[[natrd]]))  
*Default value:* None  



Gives the cartesian coordinates of atoms within unit cell, in angstrom. This
information is redundant with that supplied by array [[xred]] or [[xcart]].  
If [[xred]] and [[xangst]] are ABSENT from the input file and [[xcart]] is
provided, then the values of [[xred]] will be computed from the provided
[[xcart]] (i.e. the user may use xangst instead of [[xred]] or [[xcart]] to
provide starting coordinates).  
One and only one of [[xred]], [[xcart]] and [[xangst]] must be provided.  
The conversion factor between Bohr and Angstrom is 1 Bohr=0.5291772108
Angstrom, see the [ NIST site
](http://physics.nist.gov/cuu/Constants/index.html) .  
Atomic positions evolve if [[ionmov]]/=0 . In constrast with [[xred]] and
[[xcart]], [[xangst]] is not internal.


* * *

## **xcart** 


*Mnemonics:* vectors (X) of atom positions in CARTesian coordinates  
*Variable type:* real  
*Dimensions:* (3,min([[natom]],[[natrd]]))  
*Default value:* None  



Gives the cartesian coordinates of atoms within unit cell. This information is
redundant with that supplied by array [[xred]] or [[xangst]]. By default,
[[xcart]] is given in Bohr atomic units (1 Bohr=0.5291772108 Angstroms),
although Angstrom can be specified, if preferred, since [[xcart]] has the
'[[LENGTH]]' characteristics.  
If [[xred]] and [[xangst]] are ABSENT from the input file and [[xcart]] is
provided, then the values of [[xred]] will be computed from the provided
[[xcart]] (i.e. the user may use [[xcart]] instead of [[xred]] or [[xangst]]
to provide starting coordinates).  
One and only one of [[xred]], [[xcart]] and ** xangst ** must be provided.  
Atomic positions evolve if [[ionmov]]/=0 .


* * *

## **xred** 


*Mnemonics:* vectors (X) of atom positions in REDuced coordinates  
*Variable type:* real  
*Dimensions:* (3,min([[natom]],[[natrd]]))  
*commentdims:* represented internally as xred(3,[[natom]],[[nimage]])  
*Default value:* *0.0  



Gives the atomic locations within unit cell in coordinates relative to real
space primitive translations (NOT in cartesian coordinates). Thus these are
fractional numbers typically between 0 and 1 and are dimensionless. The
cartesian coordinates of atoms (in Bohr) are given by:  
R_cartesian = xred1*rprimd1+xred2*rprimd2+xred3*rprimd3  
where (xred1,xred2,xred3) are the "reduced coordinates" given in columns of
"[[xred]]", (rprimd1,rprimd2,rprimd3) are the columns of primitive vectors
array "[[rprimd]]" in Bohr.  
If you prefer to work only with cartesian coordinates, you may work entirely
with "[[xcart]]" or "[[xangst]]" and ignore [[xred]], in which case [[xred]]
must be absent from the input file.  
One and only one of [[xred]], [[xcart]] and [[xangst]] must be provided.  
Atomic positions evolve if [[ionmov]]/=0 .


* * *

## **znucl** 


*Mnemonics:* charge -Z- of the NUCLeus  
*Variable type:* real  
*Dimensions:* ([[npsp]])  
*Default value:* None  



Gives nuclear charge for each type of pseudopotential, in order.  
If [[znucl]] does not agree with nuclear charge, as given in pseudopotential
files, the program writes an error message and stops.

N.B. : In the pseudopotential files, [[znucl]] is called "zatom".

For a "dummy" atom, with [[znucl]]=0 , as used in the case of calculations
with only a jellium surface, ABINIT sets arbitrarily the covalent radius to
one.


* * *
