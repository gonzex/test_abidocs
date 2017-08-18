## **algalch** 


*Mnemonics:* ALGorithm for generating ALCHemical pseudopotentials  
*Variable type:* integer  
*Dimensions:* ([[ntypalch]])  
*Default value:* *1  



Used for the generation of alchemical pseudopotentials, that is, when
[[ntypalch]] is non-zero.

Give the algorithm to be used to generate the [[ntypalch]] alchemical
potentials from the different [[npspalch]] pseudopotentials dedicated to this
use.

Presently, [[algalch]] can only have the value 1, that is :

  * the local potentials are mixed, thanks to the [[mixalch]] mixing coefficients 
  * the form factors of the non-local projectors are all preserved, and all considered to generate the alchemical potential 
  * the scalar coefficients of the non-local projectors are multiplied by the proportion of the corresponding type of atom that is present in [[mixalch]] 
  * the characteristic radius for the core charge is a linear combination of the characteristic radii of the core charges, build with the [[mixalch]] mixing coefficients 
  * the core charge function f(r/rc) is a linear combination of the core charge functions, build with the [[mixalch]] mixing coefficients 

Later, other algorithms for the mixing might be included.

Note that alchemical mixing cannot be used with PAW.


* * *

## **boxcenter** 


*Mnemonics:* BOX CENTER  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* [0.5, 0.5, 0.5]  



Defines the center of the box, in reduced coordinates. At present, this
information is only used in the case of Time-Dependent DFT computation of the
oscillator strength. One must take boxcenter such as to be roughly the center
of the cluster or molecule. The default is sensible when the vacuum
surrounding the cluster or molecule has xred 0 or 1. On the contrary, when the
cluster or molecule is close to the origin, it is better to take
[[boxcenter]]=(0 0 0).


* * *

## **boxcutmin** 


*Mnemonics:* BOX CUT-off MINimum  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 2.0  



The box cut-off ratio is the ratio between the wavefunction plane wave sphere
radius, and the radius of the sphere that can be inserted in the FFT box, in
reciprocal space. In order for the density to be exact (in the case of plane
wave, not PAW), this ratio should be at least two. If one uses a smaller
ratio, one will gain speed, at the expense of accuracy. In case of pure ground
state calculation (e.g. for the determination of geometries), this is
sensible. However, the wavefunctions that are obtained CANNOT be used for
starting response function calculation.


* * *

## **charge** 


*Mnemonics:* CHARGE  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0  



Used to establish charge balance between the number of electrons filling the
bands and the nominal [[charge]] associated with the atomic cores.  
The code adds up the number of valence electrons provided by the
pseudopotentials of each type (call this "zval"), then add [[charge]], to get
the number of electrons per unit cell, [[nelect]].  
Then, if [[iscf]] is positive, the code adds up the band occupancies (given in
array [[occ]]) for all bands at each k point, then multiplies by the k point
weight [[wtk]] at each k point. Call this sum "nelect_occ" (for the number of
electrons from occupation numbers). It is then required that:  
nelect_occ = nelect  
To treat a neutral system, which is desired in nearly all cases, one must use
[[charge]]=0. To treat a system missing one electron per unit cell, set
[[charge]]=+1.


* * *

## **chkexit** 


*Mnemonics:* CHecK whether the user want to EXIT  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If [[chkexit]] is 1 or 2, ABINIT will check whether the user wants to
interrupt the run (using the keyword "exit" on the top of the input file or
creating a file named "abinit.exit": see the [ end of section 3.2
](../../users/generated_files/help_abinit.html#chkexit) of the
[[help_abinit]]).

If [[chkexit]]=0, the check is not performed at all

If [[chkexit]]=1, the check is not performed frequently (after each SCF step)

If [[chkexit]]=2, the check is performed frequently (after a few bands, at
each k point)

In all cases, the check is performed at most every 2 seconds of CPU time.


* * *

## **chkprim** 


*Mnemonics:* CHecK whether the cell is PRIMitive  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



If the symmetry finder is used (see [[nsym]]), a non-zero value of [[chkprim]]
will make the code stop if a non-primitive cell is used. If [[chkprim]]=0, a
warning is issued, but the run does not stop.

If you are generating the atomic and cell geometry using [[spgroup]], you
might generate a PRIMITIVE cell using [[brvltt]]=-1 .


* * *

## **chksymbreak** 


*Mnemonics:* CHecK SYMmetry BREAKing  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



This variable governs the behaviour of the code when there are potential
source of symmetry breaking, related e.g. to the k point grid or the presence
of non-symmorphic translations which might not be coherent with the exchange-
correlation grid.

When [[chksymbreak]]=1, the code stops (or issue a warning) if :

  * (1) The k point grid is non-symmetric, in case [[kptopt]] =1, 2, or 4 ; 
  * (2) The non-symmorphic translation part of the symmetry operations has components that are not zero, or simple fractions, with 2, 3, 4, 6, 8 or 12 as denominators. 

  
When [[chksymbreak]] is zero, there is no such check.  
When [[chksymbreak]] is minus 1, the code stops if the condition (1) is met,
but in case the condition (2) is met, there will be a trial to shift the
atomic coordinates such as to obtain symmetry operations with the adequate
non-symmorphic part.

Explanation :  
In the ground-state calculation, such breaking of the symmetry is usually
harmless. However, if the user is doing a calculation of phonons using DFPT
([[rfphon]]=1), the convergence with respect to the number of k points will be
much worse with a non-symmetric grid than with a symmetric one. Also, if the
user is doing a [[GW]] calculation, the presence of non-symmorphic
translations that are not coherent with the FFT grid might cause problems. In
the [[GW]] part, indeed, one needs to reconstruct the wavefunctions in the
full Brillouin zone for calculating both the polarizability and the self-
energy. The wavefunctions in the full Brillouin zone are obtained from the
irreducible wedge by applying the symmetry operations of the space group of
the crystal. In the present implementation, the symmetrization of the
wavefunctions is done in real space on the FFT mesh that, therefore, has to be
coherent both with the rotational part as well as with the fractional
translation of each symmetry operation. If the condition (2) is met, the
[[GW]] code will not be able to find a symmetry-preserving FFT mesh.  
So, it was decided to warn the user about these possible problems already at
the level of the ground state calculations, although such warning might be
irrelevant.  
If you encounter a problem outlined above, you have two choices : change your
atomic positions (translate them) such that the origin appears as the most
symmetric point ; or ignore the problem, and set [[chksymbreak]]=0 .


* * *

## **cpuh** 


*Mnemonics:* CPU time limit in Hours  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*The use of this variable forbids the use of:* specified([[cpum]]) or specified([[cpus]])  



Only one of the three real parameters [[cpus]], [[cpum]] and [[cpuh]] can be
defined in the input file to set up a CPU time limit. When the job reaches
that limit, it will try to end smoothly. However, note that this might still
take some time. If the user want a firm CPU time limit, the present parameter
must be reduced sufficiently. Intuition about the actual margin to be taken
into account should come with experience ...  
A zero value has no action of the job.


* * *

## **cpum** 


*Mnemonics:* CPU time limit in Minutes  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*The use of this variable forbids the use of:* specified([[cpum]]) or specified([[cpus]])  



Only one of the three real parameters [[cpus]], [[cpum]] and [[cpuh]] can be
defined in the input file to set up a CPU time limit. When the job reaches
that limit, it will try to end smoothly. However, note that this might still
take some time. If the user want a firm CPU time limit, the present parameter
must be reduced sufficiently. Intuition about the actual margin to be taken
into account should come with experience ...  
A zero value has no action of the job.


* * *

## **cpus** 


*Mnemonics:* CPU time limit in seconds  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*The use of this variable forbids the use of:* specified([[cpum]]) or specified([[cpus]])  



Only one of the three real parameters [[cpus]], [[cpum]] and [[cpuh]] can be
defined in the input file to set up a CPU time limit. When the job reaches
that limit, it will try to end smoothly. However, note that this might still
take some time. If the user want a firm CPU time limit, the present parameter
must be reduced sufficiently. Intuition about the actual margin to be taken
into account should come with experience ...  
A zero value has no action of the job.


* * *

## **diecut** 


*Mnemonics:* DIElectric matrix energy CUToff  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 2.2  



Kinetic energy cutoff that controls the number of planewaves used to represent
the dielectric matrix:  
(1/2)[(2 Pi)*(Gmax)]  2  =[[ecut]] for Gmax.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since [[diecut]] has
the '[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)  
All planewaves inside this "basis sphere" centered at G=0 are included in the
basis. This is useful only when [[iprcel]]&gt;=21, which means that a
preconditioning scheme based on the dielectric matrix is used.  
NOTE : a negative [[diecut]] will define the same dielectric basis sphere as
the corresponding positive value, but the FFT grid will be identical to the
one used for the wavefunctions. The much smaller FFT grid, used when
[[diecut]] is positive, gives exactly the same results.  
No meaning for RF calculations yet.


* * *

## **diegap** 


*Mnemonics:* DIElectric matrix GAP  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.1  



Gives a rough estimation of the dielectric gap between the highest energy
level computed in the run, and the set of bands not represented. Used to
extrapolate dielectric matrix when [[iprcel]] &gt;= 21.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since [[diegap]] has
the '[[ENERGY]]' characteristics. (1 Ha=27.2113845 eV)  
No meaning for RF calculations yet.


* * *

## **dielam** 


*Mnemonics:* DIElectric matrix LAMbda  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.5  
*Only relevant if:* [[iprcel]] >= 21  



Gives the amount of occupied states with mean energy given by the highest
level computed in the run, included in the extrapolation of the dielectric
matrix.  
No meaning for RF calculations yet.


* * *

## **dielng** 


*Mnemonics:* model DIElectric screening LeNGth  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.0774841d0  



Used for screening length (in Bohr) of the model dielectric function, diagonal
in reciprocal space. By default, given in Bohr atomic units (1
Bohr=0.5291772108 Angstrom), although Angstrom can be specified, if preferred,
since [[dielng]] has the '[[LENGTH]]' characteristics.  
This model dielectric function is as follows (K being a wavevector) :

    
    
             (     1        +     [[dielng]]2* K2   )
    diel(K)= ------------------------------------
             ( 1/[[diemac]] + [[dielng]]2 * K2 ) * [[diemix]]
     

The inverse of this model dielectric function will be applied to the residual,
to give the preconditioned change of potential. Right at K=0, diel(K) is
imposed to be 1.

If the preconditioning were perfect, the change of potential would lead to an
exceedingly fast solution of the self-consistency problem (two or three
steps). The present model dielectric function is excellent for rather
homogeneous unit cells.  
When K-&gt;0 , it tends to the macroscopic dielectric constant, eventually
divided by the mixing factor [[diemix]] (or [[diemixmag]]  for magnetization).  
For metals, simply put [[diemac]] to a very large value (10^6 is OK)  
The screening length [[dielng]] governs the length scale to go from the
macroscopic regime to the microscopic regime, where it is known that the
dielectric function should tend to 1. It is on the order of 1 Bohr for metals
with medium density of states at the Fermi level, like Molybdenum, and for
Silicon. For metals with a larger DOS at the Fermi level (like Iron), the
screening will be more effective, so that [[dielng]] has to be decreased by a
factor of 2-4.  
This works for GS and RF calculations.


* * *

## **diemac** 


*Mnemonics:* model DIElectric MACroscopic constant  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1000000.0  



A rough knowledge of the macroscopic dielectric constant [[diemac]] of the
system is a useful help to speed-up the SCF procedure: a model dielectric
function, see the keyword [[dielng]], is used for that purpose. It is
especially useful for speeding up the treatment of rather homogeneous unit
cells.

Some hint :  
The value of [[diemac]] should usually be bigger than 1.0d0, on physical
grounds.  
For metals, simply put [[diemac]] to a very large value (the default 10  6  is
OK)  
For silicon, use 12.0 . A similar value is likely to work well for other
semiconductors  
For wider gap insulators, use 2.0 ... 4.0  
For molecules in an otherwise empty big box, try 1.5 ... 3.0  
Systems that combine a highly polarisable part and some vacuum are rather
badly treated by the model dielectric function. One has to use the
"extrapolar" technique, activated by the input variable [[iprcel]].  
In sufficiently homogeneous systems, you might have to experiment a bit to
find the best [[diemac]]. If you let [[diemac]] to its default value, you
might even never obtain the self-consistent convergence !  
For response function calculations, use the same values as for GS. The
improvement in speed can be considerable for small (but non-zero) values of
the wavevector.


* * *

## **diemix** 


*Mnemonics:* model DIElectric MIXing factor  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.0 if [[usepaw]]==0 or [[iprcel]] !=0,
0.7 if [[usepaw]]==1 or [[iprcel]]==0,
None otherwise.
  
*Only relevant if:* [[diemix]] &gt;= 0.0 and [[diemix]] &lt;=  1.0  



Gives overall factor of the preconditioned residual density/potential to be
transferred in the SCF cycle.  
It should be between 0.0 and 1.0 .  
If the model dielectric function were perfect, [[diemix]] should be 1.0 . By
contrast, if the model dielectric function does nothing (when [[diemac]]=1.0d0
or [[dielng]] is larger than the size of the cell), [[diemix]] can be used to
damp the amplifying factor inherent to the SCF loop.  
For molecules, a value on the order 0.5 or 0.33 is rather usual.  
When mod([[iscf]],10)=3, 4 ,5 or 7, [[diemix]] is only important at the few
first iterations when anharmonic effects are important, since these schemes
compute their own mixing factor for self-consistency.  
Also note that a different value of diemix can be used for the magnetization
(see [[diemixmag]]).


* * *

## **diemixmag** 


*Mnemonics:* model DIElectric MIXing factor for the MAGgnetization  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* [[diemix]] if 70 < [[iprcel]] and [[iprcel]] < 80,
[[diemix]] if [[iprcel]]==0,
[[diemix]] if [[iscf]]<10,
-[[diemix]] otherwise.
  



Gives overall factor of the preconditioned residual magnetization/magnetic
field to be transferred in the SCF cycle (see [[diemix]] for further
information).  
For the time being, apply only when the SCF mixing is done on the density
([[iscf]]&gt;=10).  
  
A negative value of diemixmag means that magnetization is only preconditionned
by ABS(diemixmag), without the use of any preconditionner.  
  
When SCF cycle has some difficulties to converge, changing the value of
[[diemixmag]] can have a positive effect.  
In particular [[diemixmag]]=-4 is a good choice (i.e. diemixmag=4, no other
preconditionner on magnetization).


* * *

## **dosdeltae** 


*Mnemonics:* DOS DELTA in Energy  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



Defines the linear grid resolution (energy increment) to be used for the
computation of the Density-Of-States, when [[prtdos]] is non-zero.  
If [[dosdeltae]] is set to zero (the default value), the actual increment is
0.001 Ha if [[prtdos]]=1, and the much smaller value 0.00005 Ha if
[[prtdos]]=2. This different default value arises because the [[prtdos]]=1
case, based on a smearing technique, gives a quite smooth DOS, while the DOS
from the tetrahedron method, [[prtdos]]=2, is rapidly varying.


* * *

## **enunit** 


*Mnemonics:* ENergy UNITs  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Governs the units to be used for output of eigenvalues (and eventual phonon
frequencies)

  * 0=&gt;print eigenvalues in hartree; 
  * 1=&gt;print eigenvalues in eV; 
  * 2=&gt;print eigenvalues in both hartree and eV. 

If phonon frequencies are to be computed :

  * 0=&gt; phonon frequencies in Hartree and cm-1; 
  * 1=&gt; phonon frequencies in eV and THz; 
  * 2=&gt; phonon frequencies in hartree, eV, cm-1, Thz and Kelvin. 


* * *

## **fband** 


*Mnemonics:* Factor for the number of BANDs  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.125 if [[occopt]]==1,
0.5 if [[occopt]]>2,
0.0 if [[usewvl]]==1,
0.0 otherwise.
  



Governs the number of bands to be used in the code in the case the parameter
[[nband]] is not defined in the input file (which means that [[occopt]] is not
equal to 0 or 2).

In case [[fband]] is 0.0d0, the code computes from the pseudopotential files
and the geometry data contained in the input file, the number of electrons
present in the system. Then, it computes the minimum number of bands that can
accommodate them, and use that value for [[nband]].  
In case [[fband]] differs from zero, other bands will be added, just larger
than [[fband]] times the number of atoms. This parameter is not echoed in the
top of the main output file, but only the parameter [[nband]] that it allowed
to compute. It is also not present in the dtset array (no internal).  
The default values are chosen such as to give naturally some conduction bands.
This improves the robustness of the code, since this allows to identify lack
of convergence coming from (near-)degeneracies at the Fermi level. In the
metallic case, the number of bands generated might be too small if the
smearing factor is large. The occupation numbers of the higher bands should be
small enough such as to neglect higher bands. It is difficult to automate
this, so a fixed default value has been chosen.


* * *

## **iatsph** 


*Mnemonics:* Index for the ATomic SPHeres of the atom-projected density-of-states  
*Variable type:* integer  
*Dimensions:* ([[natsph]])  
*Default value:* [1 .. [[natsph]]]  
*Only relevant if:* [[prtdos]] == 3 or [[pawfatbnd]] in [1,2]  



[[iatsph]] gives the number of the [[natsph]] atoms around which the sphere
for atom-projected density-of-states will be build, in the [[prtdos]]=3 case.
The radius of these spheres is given by [[ratsph]].  
If [[pawfatbnd]]=1 or 2, it gives the number of the [[natsph]] atoms around
which atom-projected band structure will be built.


* * *

## **icoulomb** 


*Mnemonics:* Index for the Coulomb TReaTMenT  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Defines the type of computation used for Hartree potential, local part of
pseudo-potential and ion-ion interaction:

  * [[icoulomb]]=0 : usual reciprocal space computation, using 1 / g^2 for the Hartree potential and using Ewald correction. 
  * [[icoulomb]]=1 : free boundary conditions are used when the Hartree potential is computed, real space expressions of pseudo-potentials are involved (restricted to GTH pseudo-potentials) and simple coulomb interaction gives the ion-ion energy. 


* * *

## **iprcel** 


*Mnemonics:* Integer for PReConditioning of ELectron response  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used when [[iscf]]&gt;0, to define the SCF preconditioning scheme. Potential-
based preconditioning schemes for the SCF loop (electronic part) are still a
subject of active research. The present parameter (electronic part) describes
the way the change of potential is derived from the residual.  
The possible values of [[iprcel]] correspond to :

  * 0 =&gt; model dielectric function described by [[diemac]], [[dielng]] and [[diemix]]. 
  * larger or equal to 21 =&gt; will compute the dielectric matrix according to [[diecut]], [[dielam]], [[diegap]]. This methodology is described in P.-M. Anglade, X. Gonze, Phys. Rev. B 78, 045126 (2008). 
  * Between 21 and 29 =&gt; for the first few steps uses the same as option 0 then compute RPA dielectric function, and use it as such. 
  * Between 31 and 39 =&gt; for the first few steps uses the same as option 0 then compute RPA dielectric function, and use it, with the mixing factor [[diemix]]. 
  * Between 41 and 49 =&gt; compute the RPA dielectric matrix at the first step, and recompute it at a later step, and take into account the mixing factor [[diemix]]. 
  * Between 51 and 59 =&gt; same as between 41 and 49, but compute the RPA dielectric matrix by another mean 
  * Between 61 and 69 =&gt; same as between 41 and 49, but compute the electronic dielectric matrix instead of the RPA one. 
  * Between 71 and 78 =&gt; STILL UNDER DEVELOPMENT -- NOT USABLE ; Use the modified Kerker preconditioner with a real-space formulation (basic formulation is shown at [[dielng]]). The dielectric matrix is approximated thanks to [[diemac]] and [[dielng]]. Note that [[diemix]] is also used. 
  * 79 =&gt; STILL UNDER DEVELOPMENT -- NOT USABLE ; same as previous but with an alternate algorithm. 
  * 141 to 169 =&gt; same as Between 41 and 69 (but, the dielectric matrix is also recomputed every iprcel modulo 10 step). 

  
The computation of the dielectric matrix (for 0 [100]&lt; [[iprcel]] &lt; 70
[100]) is based on the ** extrapolar ** approximation. This approximation can
be tuned with [[diecut]], [[dielam]], and [[diegap]]. Yet its accuracy mainly
depends on the number of conduction bands included in the system. Having 2 to
10 empty bands in the calculation is usually enough (use [[nband]]).  
  
NOTES:

  * The step at which the dielectric matrix is computed or recomputed is determined by modulo([[iprcel]],10). The recomputation happens just once in the calculation for [[iprcel]] &lt; 100\. 
  * For non-homogeneous relatively large cells [[iprcel]]=45 will likely give a large improvement over [[iprcel]]=0. 
  * In case of PAW and [[iprcel]]&gt;0, see [[pawsushat]] input variable. By default, an approximation (which can be suppressed) is done for the computation of susceptibility matrix. 
  * For extremely large inhomogeneous cells where computation of the full dielectric matrix takes too many weeks, 70 &lt; [[iprcel]] &lt; 80 is advised. 
  * For [[nsppol]]=2 or [[nspinor]]=2 with metallic [[occopt]], only ** mod(iprcel,100) ** &lt;50 is allowed. 
  * No meaning for RF calculations yet. 
  * The exchange term in the full dielectric matrix diverges for vanishing densities. Therefore the values of [[iprcel]] beyond 60 must not be used for cells containing vacuum, unless ones computes this matrix for every step ([[iprcel]]=161). 


* * *

## **iqpt** 


*Mnemonics:* Index for QPoinT generation  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Only used if [[nqpt]]=1, and [[qptopt]]=1 to 4.

Defines the index of the Q point to be selected in the list of q points
generated by [[ngqpt]], [[qptrlatt]], [[nshiftq]], and [[shiftq]].

If [[iqpt]]=0, then the q point is Gamma (0 0 0).

The usual working mode is to define a series of values for [[iqpt]], starting
with [[iqpt]]=0 or 1 (so through the definition of ** iqpt: ** ), and
increasing it by one for each dataset (thanks to ** iqpt+ ** ).


* * *

## **ixcpositron** 


*Mnemonics:* Integer for the eXchange-Correlation applied to the electron-POSITRON interaction  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Comment:* (Teter parameterization). However, if all the pseudopotentials have the same value of pspxc, the initial value of ixc will be that common value  



Relevant only when [[positron]]/=0.  
Define the type of electron-positron correlation that is used in case of a
electron-positron two-component DFT calculation.  
Define also the analytical formula of the enhancement factor used to compute
the electron-positron annhilation rate:  
  
Electron-positron correlation functional:  

** ixcpositron=1 ** : LDA zero positron density limit parametrized by Arponen &amp; Pajanne and provided by Boronski &amp; Nieminen [1,2]   
** ixcpositron=11 ** : LDA zero positron density limit parametrized by Arponen &amp; Pajanne and fitted by Sterne &amp; Kaiser [1,3]   
** ixcpositron=2 ** : LDA electron-positron correlation provided by Puska, Seitsonen, and Nieminen [1,4]   
** ixcpositron=3 ** : GGA zero positron density limit parametrized by Arponen &amp; Pajanne and provided by Boronski &amp; Nieminen [1,2,5]   
** ixcpositron=31 ** : GGA zero positron density limit parametrized by Arponen &amp; Pajanne and fitted by Sterne &amp; Kaiser [1,3,5] 
Annihilation rate enhancement factor:  

** ixcpositron=1 ** : Boronski and Nieminen full modelisation and RPA limit [1]   
** ixcpositron=11 ** : Sterne and Kaiser [2]   
** ixcpositron=2 ** : Puska, Seitsonen and Nieminen [3]   
** ixcpositron=3 ** : Boronski and Nieminen full modelisation and RPA limit [1], with GGA corrections   
** ixcpositron=31 ** : Sterne and Kaiser [2], with GGA corrections   

References:  ** [1] ** J. Arponen and E. Pajanne, Ann. Phys. (N.Y.) 121, 343
(1979).  
** [2] ** Boronski and R.M. Nieminen, Phys. Rev. B 34, 3820 (1986).   
** [3] ** P.A. Sterne and J.H. Kaiser, Phys. Rev. B 43, 13892 (1991).   
** [4] ** M.J. Puska, A.P. Seitsonen and R.M. Nieminen, Phys. Rev. B 52, 10947 (1994).   
** [5] ** B. Barbiellini, M.J. Puska, T. Torsti and R.M.Nieminen, Phys. Rev. B 51, 7341 (1994)   


* * *

## **jellslab** 


*Mnemonics:* include a JELLium SLAB in the cell  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1, a slab of uniform positive background charge density, that is, a
jellium slab, is included in the calculation cell. A portion of the unit cell
is filled with such positive charge density distribution which is equal to a
bulk-mean value n  bulk  between two edges and zero in the vacuum region if
present.  
For the sake of convenience the unit cell is supposed to have the third
crystal primitive lattice vector orthogonal to the other ones so that the
portion of the cell filled by the jellium slab can be defined through its
edges along z.  
The bulk-mean positive charge density is fixed by the input variable
[[slabwsrad]], while the position of the slab edges along z is defined through
the input variables [[slabzbeg]] and [[slabzend]].


* * *

## **kptbounds** 


*Mnemonics:* K PoinT BOUNDarieS  
*Variable type:* real  
*Dimensions:* (3,abs([[kptopt]])+1))  
*Default value:* None  



It is used to generate the circuit to be followed by the band structure, when
[[kptopt]] is negative (it is not read if [[kptopt]] is zero or positive).

There are abs([[kptopt]]) segments to be defined, each of which starting from
the end point of the preceeding one. Thus, the number of points to be input is
abs([[kptopt]])+1. They form a circuit starting at
[[kptbounds]](1:3,1)/[[kptnrm]] and ending at
[[kptbounds]](1:3,abs([[kptopt]])+1)/[[kptnrm]]. The number of divisions of
each segment can be defined either using the array [[ndivk]] or the variable
[[ndivsm]] that just defines the number of divisions for the smallest segment

As for [[kpt]], [[kptbounds]] is specified using the primitive vectors in
reciprocal space. If your Bravais lattice is simple, then it should be quite
easy to find the coordinates of the end points. On the other hand, for
centered, body-centered, face-centered, hexagonal, and rhombohedral Bravais
lattice, the conversion might be more difficult. See the description of
[[kpt]] for an explanation of how to convert data from the "conventional"
cartesian coordinates to the primitive vectors in the reciprocal space. In
order to help a bit, we list below a series of typical values, for the FCC,
BCC, hexagonal and rhombohedral Bravais lattices. Note : all the data below
are given in dimensionless units ; they have to be rescaled by the actual
lengths defined by the [[acell]] values. However, [[kptbounds]] values can be
used as such, if the values of [[rprim]] given below are adopted.

A. ** FCC lattice **

Suppose the primitive vectors in real space are given by  

    
    
      rprim   0 1 1    1 0 1    1 1 0
     

or

    
    
      rprim   0 1/2 1/2    1/2 0 1/2    1/2 1/2 0
     

(these two possibilities only differ by a scaling factor, irrelevant for the
definition of the k points in the primitive vectors in reciprocal space).
Then, the reciprocal primitive vectors (in conventional cartesian coordinates)
are

    
    
      (-1/2 1/2 1/2), (1/2 -1/2 1/2), (1/2 1/2 -1/2)
     

or

    
    
      (-1 1 1), (1 -1 1), (1 1 -1)
     

and, in both cases, the coordinates of several special points with respect to
primitive vectors in reciprocal space are

    
    
      X (0   1/2 1/2)   (conventional cartesian coordinate 1/2 0 0)
      X'(1/2 1/2 1  )   (conventional cartesian coordinate 1/2 1/2 0)  (an other instance of X, in another Brillouin zone)
      L (1/2 1/2 1/2)   (conventional cartesian coordinate  1/4 1/4 1/4)
      L'(1/2 0   0  )   (conventional cartesian coordinate -1/4 1/4 1/4) (an other instance of L, on another face of the BZ)
      W (1/4 1/2 3/4)   (conventional cartesian coordinate 1/2 1/4 0)
      U (1/4 5/8 5/8)   (conventional cartesian coordinate 1/2 1/8 1/8)
      K (3/8 3/8 3/4)   (conventional cartesian coordinate 3/8 3/8 0)
     

Note that K is actually equivalent to U, by spatial and translational
symmetry. So, if you want to specify a typical circuit, the following might do
the work : L-Gamma-X-W-K,U-L-W-X-K,U-Gamma with  

    
    
      kptbounds  1/2 0 0  0 0 0  0 1/2 1/2  1/4 1/2 3/4  3/8 3/8 3/4  1/2 1/2 1/2  1/4 1/2 3/4  1/2 1/2 1  3/8 3/8 3/4  0 0 0
     

The lengths of segments (this information is useful to draw the band
structure, with the correct relative scale between special points) can be
found using the conventional cartesian coordinates :
l(L-Gamma)=sqrt(3)/4=0.433... ; l(Gamma-X)=1/2=0.5 ; l(X-W)=1/4=0.25 ;
l(W-K)=sqrt(2)/8=0.177... ; l(K-L)=sqrt(6)/8=0.306... ;
l(L-W)=sqrt(2)/4=0.354... ; l(W-X)=1/4=0.25 ; l(X-K)=sqrt(2)/8=0.177... ;
l(K-Gamma)=sqrt(2).3/8=0.530...

B. ** BCC lattice **

Suppose the primitive vectors in real space are given by  

    
    
      rprim  -1 1 1    1 -1 1    1 1 -1
     

(as for the FCC lattice, there is a scale invariance). Then, the reciprocal
primitive vectors (in conventional cartesian coordinates) are (0 1/2 1/2),
(1/2 0 1/2), and (1/2 1/2 0) and the coordinates of several special points
with respect to primitive vectors in reciprocal space are

    
    
      H (-1/2 1/2 1/2)   (conventional cartesian coordinate 1/2 0 0)
      N ( 0   0   1/2)   (conventional cartesian coordinate 1/4 1/4 0)
      P ( 1/4 1/4 1/4)   (conventional cartesian coordinate 1/4 1/4 1/4)
     

So, if you want to specify a typical circuit, the following might do the work
: Gamma-H-N-Gamma-P-N-P-H  

    
    
      kptbounds  0 0 0  -1/2 1/2 1/2  0 0 1/2  0 0 0   1/4 1/4 1/4  0 0 1/2  1/4 1/4 1/4  -1/2 1/2 1/2
     

The lengths of segments (this information is useful to draw the band
structure, with the correct relative scale between special points) can be
found using the conventional cartesian coordinates : l(Gamma-H)=1/2=0.5 ;
l(H-N)=sqrt(2)/4=0.354... ; l(N-Gamma)=sqrt(2)/4=0.354... ;
l(Gamma-P)=sqrt(3)/4=0.433... ; l(P-N)=1/4=0.25 ; l(N-P)=1/4=0.25 ;
l(P-H)=sqrt(3)/4=0.433...

C. ** Hexagonal lattices **

Suppose the primitive vectors in real space are given by  

    
    
      rprim  1 0 0    -1/2 sqrt(0.75) 0    0 0 1
     

The coordinates of several special points with respect to primitive vectors in
reciprocal space are

    
    
      M (1/2 0 0) or (0 1/2 0) or (-1/2 1/2 0)
      L (1/2 0 1/2) or (0 1/2 1/2) or (-1/2 1/2 1/2)
      K (1/3 1/3 0) or (2/3 -1/3 0) or (-1/3 2/3 0)
      H (1/3 1/3 1/2) or (2/3 -1/3 1/2) or (-1/3 2/3 1/2)
      A (0 0 1/2)
     

So, if you want to specify a typical circuit, the following might do the work
: K-Gamma-M-K-H-A-L-H-L-M-Gamma-A  

    
    
      kptbounds  1/3 1/3 0  0 0 0  1/2 0 0  1/3 1/3 0  1/3 1/3 1/2  0 0 1/2  1/2 0 1/2  1/3 1/3 1/2  1/2 0 1/2  1/2 0 0  0 0 0  0 0 1/2
     

In order to find the lengths of segments (this information is useful to draw
the band structure, with the correct relative scale between special points)
one needs to know the a and c lattice parameters. Also, in what follows, we
omit the 2*pi factor sometimes present in the definition of the reciprocal
space vectors. The reciprocal vectors are (1/a 1/(sqrt(3)*a) 0) , (0
2/(sqrt(3)*a) 0), (0 0 1/c). The lengths of the above-mentioned segments can
be computed as : l(K-Gamma)=2/(3*a)=0.666.../a ;
l(Gamma-M)=1/(sqrt(3)*a)=0.577.../a ; l(M-K)=1/(3*a)=0.333.../a ;
l(K-H)=1/(2*c)=0.5.../c ; l(H-A)=2/(3*a)=0.666.../a ;
l(A-L)=1/(sqrt(3)*a)=0.577.../a ; l(L-H)=1/(3*a)=0.333.../a ;
l(H-L)=1/(3*a)=0.333.../a ; l(L-M)=1/(2*c)=0.5.../c ;
l(M-Gamma)=-1/(sqrt(3)*a)=0.577.../a ; l(Gamma-A)=1/(2*c)=0.5.../c

D. ** Rhombohedral lattices **

Rhombohedral lattices are characterised by two parameters, the length of the
primitive vectors, that we will denote a0, and the angle they form, alpha.
These can be directly input of ABINIT, as [[acell]] and [[angdeg]]

This will generate the primitive vectors in real space , with

    
    
      [[acell]] a0 a0 a0    and      [[rprim]]  a 0 c    -a/2 a*sqrt(0.75) c    -a/2 -a*sqrt(0.75) c
     

with a^2+c^2=1, a^2=(1-cos(alpha))*2/3, c^2=(1+2*cos(alpha))*1/3,
(a/c)^2=2*(1-cos(alpha))/(1+2*cos(alpha)) and also
cos(alpha)=(1-(a/c)^2/2)/(1+(a/c)^2). Alternatively, these values of rprim
might directly be the input of ABINIT (then, the balance of the scaling factor
might be adjusted between [[acell]] and [[rprim]]).

Unlike for the simple cubic, FCC, BCC, hexagonal (and some other) Bravais
lattice, the topology of the Brillouin zone will depend on the alpha (or a/c)
value. We give below information concerning the case when cos(alpha) is
positive, that is, (a/c)^2 lower than 2.

The coordinates of several special points with respect to primitive vectors in
reciprocal space will not depend on the a/c ratio, but some others will depend
on it. So, some care has to be exercised. Notations for the Brillouin Zone
special points are the same as in Phys. Rev. B 41, 11827 (1990).

    
    
      L (1/2 0 0) or (0 1/2 0) or (0 0 1/2) (or with negative signs)
      T (1/2 1/2 1/2)
      X (1/2 1/2 0) or (1/2 0 1/2) or (0 1/2 1/2) (or with separate negative signs)
      W (5/6 - (a/c)^2/6 , 1/2 , 1/6 + (a/c)^2/6 ) = (1 0 -1)*(1-(a/c)^2/2)/3 + (1 1 1)/2
      U ( (1+(a/c)^2)/6 , (8-(a/c)^2)/12 , (8-(a/c)^2)/12 ) = (-1 1/2 1/2)*(1-(a/c)^2/2)/3 + (1 1 1)/2
      K (1 0 -1)*(1+(a/c)^2/4)/3
     

So, if you want to specify a typical circuit, the following might do the work
(the representative points on lines of symmetry are indicated - there are
sometimes more than one way to go from one point to another) : X-V-K-Sigma-
Gamma-Lambda-T-Q-W-Y-L-sigma-Gamma-sigma-X . The suggestion is to sample this
path with the following coordinates for the special points X, Gamma, T, L,
Gamma, X :  

    
    
      kptbounds  1/2 0 -1/2   0 0 0    1/2 1/2 1/2  1 1/2 0   1 0 0  1 1/2 1/2
     

In order to find the lengths of segments (this information is useful to draw
the band structure, with the correct relative scale between special points)
one needs to know the a and c lattice parameters. Also, in what follows, we
omit the 2*pi factor sometimes present in the definition of the reciprocal
space vectors. The reciprocal vectors are (2/(3*a) 0 1/(3*c)) , -(1/(3*a)
1/(sqrt(3)*a) 1/(3*c), -(1/(3*a) -1/(sqrt(3)*a) 1/(3*c) ). The lengths of the
above-mentioned segments can be computed as :
l(X-Gamma)=2/(sqrt(3)*a)=1.155.../a , with
l(K-Gamma)=(1+(a/c)^2/4)*4/(3*sqrt(3)*a); l(Gamma-T)=1/(2*c) ;
l(T-L)=2/(sqrt(3)*a)=1.155.../a , with l(T-W)=(1-(a/c)^2/2)*4/(3*sqrt(3)*a);
l(L-Gamma)=sqrt(4/(a^2)+1/(c^2))/3 l(Gamma-X)=sqrt(1/(a^2)+1/(c^2))*2/3


* * *

## **kptrlatt** 


*Mnemonics:* K - PoinTs grid : Real space LATTice  
*Variable type:* integer  
*Dimensions:* (3,3)  
*Default value:* *0  
*The use of this variable forbids the use of:* specified([[ngkpt]])  



This input variable is used only when [[kptopt]] is positive. It partially
defines the k point grid. The other piece of information is contained in
[[shiftk]]. [[kptrlatt]] cannot be used together with [[ngkpt]].

The values kptrlatt(1:3,1), kptrlatt(1:3,2), kptrlatt(1:3,3) are the
coordinates of three vectors in real space, expressed in the [[rprimd]]
coordinate system (reduced coordinates). They defines a super-lattice in real
space. The k point lattice is the reciprocal of this super-lattice, possibly
shifted (see [[shiftk]]).

If neither [[ngkpt]] nor [[kptrlatt]] are defined, ABINIT will automatically
generate a set of k point grids, and select the best combination of
[[kptrlatt]] and [[shiftk]] that allows to reach a sufficient value of
[[kptrlen]]. See this latter variable for a complete description of this
procedure.


* * *

## **kptrlen** 


*Mnemonics:* K - PoinTs grid : Real space LENgth  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 30.0  



This input variable is used only when [[kptopt]] is positive and non-zero.

Preliminary explanation :  
The k point lattice defined by [[ngkpt]] or [[kptrlatt]] is used to perform
integrations of periodic quantities in the Brillouin Zone, like the density or
the kinetic energy. One can relate the error made by replacing the continuous
integral by a sum over k point lattice to the Fourier transform of the
periodic quantity. Erroneous contributions will appear only for the vectors in
real space that belong to the reciprocal of the k point lattice, except the
origin. Moreover, the expected size of these contributions usually decreases
exponentially with the distance. So, the length of the smallest of these real
space vectors is a measure of the accuracy of the k point grid.

When either [[ngkpt]] or [[kptrlatt]] is defined, [[kptrlen]] is not used as
an input variable, but the length of the smallest vector will be placed in
this variable, and echoed in the output file.

On the other hand, when neither [[ngkpt]] nor [[kptrlatt]] are defined, ABINIT
will automatically generate a large set of possible k point grids, and select
among this set, the grids that give a length of smallest vector LARGER than
[[kptrlen]], and among these grids, the one that, when used with [[kptopt]]=1,
reduces to the smallest number of k points. Note that this procedure can be
time-consuming. It is worth doing it once for a given unit cell and set of
symmetries, but not use this procedure by default. The best is then to set
[[prtkpt]]=1, in order to get a detailed analysis of the set of grids.

If some layer of vacuum is detected in the unit cell (see the input variable
[[vacuum]]), the computation of [[kptrlen]] will ignore the dimension related
to the direction perpendicular to the vacuum layer, and generate a bi-
dimensional k point grid. If the system is confined in a tube, a one-
dimensional k point grid will be generated. For a cluster, this procedure will
only generate the Gamma point.


* * *

## **magcon_lambda** 


*Mnemonics:* MAGnetization CONstraint LAMBDA parameter  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 10.0  



This variable gives the amplitude of the constraint imposed on the
magnetization vectors on each atom (turned on with flag variable
[[magconon]]). Typical values for lambda are 10 to a few hundred. The energy
will vary strongly and convergence will be difficult if lambda is too large.
The constraint will be weak and the magnetization will not be close to
[[spinat]] if lambda is too small. See variable [[magconon]] for more details.


* * *

## **magconon** 


*Mnemonics:* turn MAGnetization CONstraint ON  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Turns on the imposition of a Lagrangian constraint on the magnetization. For
each atom, the magnetization is calculated in a sphere (radius [[ratsph]]) and
a constraint is applied to bring it closer to the input values of [[spinat]].
The constraint can be either on the direction only (magconon 1) or on the full
vector (magconon 2). The Lagrangian constraint has an amplitude
[[magcon_lambda]] which should be neither too big (bad or impossible
convergence) nor too small (no effect).


* * *

## **mixalch** 


*Mnemonics:* MIXing coefficients for ALCHemical potentials  
*Variable type:* real  
*Dimensions:* ([[npspalch]],[[ntypalch]])  
*Default value:* None  



Used for the generation of alchemical pseudoatoms, that is, when [[ntypalch]]
is non-zero.

This array gives, for each type of alchemical pseudatom (there are
[[ntypalch]] such pseudoatoms), the mixing coefficients of the basic
[[npspalch]] pseudopotentials for alchemical use. For each type of alchemical
pseudoatom, the sum of the mixing coefficients must equal 1.

The actual use of the mixing coefficients is defined by the input variable
[[algalch]]. Note that the masses of the atoms, [[amu]] are also mixed
according to the value of [[mixalch]], by default.

Example 1. Suppose that we want to describe Ba(0.25) Sr(0.75) Ti O3.  
The input variables related to the construction of the alchemical Ba(0.25)
Sr(0.75) potential will be :

    
    
      npsp   4                 ! 4 pseudopotentials should be read.
      znucl  8 40 56 38        ! The nuclear charges. Note that the two
                               ! atoms whose pseudopotentials are to be mixed
                               ! are mentioned at the end of the series.
      ntypat  3                ! There will be three types of atoms.
      ntypalch   1             ! One pseudoatom will be alchemical.
                               ! Hence, there will be ntyppure=2 pure pseudoatoms,
                               ! with znucl 8 (O) and 40 (Ti), corresponding to
                               ! the two first pseudopotentials. Out of the
                               ! four pseudopotentials, npspalch=2 are left
                               ! for alchemical purposes, with znucl 56 (Ba)
                               ! and 38 (Sr).
      mixalch    0.25  0.75    ! For that unique pseudoatom to be
                               ! generated, here are the mixing coeeficients,
                               ! to be used to combine the Ba and Sr pseudopotentials.
     

Example 2. More complicated, and illustrate some minor drawback of the design
of input variables. Suppose that one wants to generate Al(0.25)Ga(0.75)
As(0.10)Sb(0.90).  
The input variables will be :

    
    
      npsp  4                  ! 4 pseudopotentials should be read
      znucl  13 31 33 51       ! The atomic numbers. All pseudopotentials
                               ! will be used for some alchemical purpose
      ntypat  2                ! There will be two types of atoms.
      ntypalch   2             ! None of the atoms will be "pure".
                               ! Hence, there will be npspalch=4 pseudopotentials
                               !  to be used for alchemical purposes.
      mixalch    0.25  0.75 0.0  0.0   ! This array is a (4,2) array, arranged in the
                 0.0   0.0  0.1  0.9   ! usual Fortran order.
     

Minor drawback : one should not forget to fill [[mixalch]] with the needed
zero's, in this later case.

In most cases, the use of [[mixalch]] will be as a static (non-evolving)
variable. However, the possibility to have different values of [[mixalch]] for
different images has been coded. A population of cells with different atomic
characteristics can thus be considered, and can be made to evolve, e.g. with a
genetic algorithm (not coded in v7.0.0 though). There is one restriction to
this possibility : the value of [[ziontypat]] for the atoms that are mixed
should be identical.


* * *

## **natsph** 


*Mnemonics:* Number of ATomic SPHeres for the atom-projected density-of-states  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* [[natom]]  
*Only relevant if:* [[prtdos]] == 3 or [[pawfatbnd]] in [1,2]  



[[natsph]] gives the number of atoms around which the sphere for atom-
projected density-of-states will be built, in the [[prtdos]]=3 case. The
indices of these atoms are given by [[iatsph]]. The radius of these spheres is
given by [[ratsph]].  
If [[pawfatbnd]]=1 or 2, it gives the number of atoms around which atom-
projected band structure will be built (the indices of these atoms are given
by [[iatsph]]).


* * *

## **natsph_extra** 


*Mnemonics:* Number of ATomic SPHeres for the l-projected density-of-states in EXTRA set  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[prtdos]] == 3 or [[pawfatbnd]] in [1,2]  



[[natsph_extra]] gives the number of extra spheres for which the angular-
momentum-projected density-of-states will be built, in the [[prtdos]]=3 case.
The radius of these spheres is given by [[ratsph_extra]]. This simulates the
STS signal for an STM tip atom placed at the sphere position, according to the
chemical nature of the tip (s- p- d- wave etc...).  
If [[pawfatbnd]]=1 or 2, it gives the number of spheres in which l-projected
band structure will be built.  
The position of the spheres is given by the [[xredsph_extra]] variable.


* * *

## **nbdbuf** 


*Mnemonics:* Number of BanDs for the BUFfer  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2*[[nspinor]] if [[optdriver]]==0 and [[iscf]]<0,
2*[[nspinor]] if [[optdriver]]==1 and 3<=[[occopt]] and [[occopt]]<= 8,
0 otherwise.
  



[[nbdbuf]] gives the number of bands, the highest in energy, that, among the
[[nband]] bands, are to be considered as part of a buffer. This concept is
useful in three situations: in non-self-consistent calculations, for the
determination of the convergence tolerance ; for response functions of metals,
to avoid instabilities, and also when finite electric fields or non-linear
responses (with electric field perturbations) are considered. For the two
first, the need of a buffer is a natural requirement of the problem, so that
the default value is changed to 2 automatically, as explained in the
following. The third case is only for implementation convenience.

In non-self-consistent GS calculations ([[iscf]]&lt;0), the highest levels
might be difficult to converge, if they are degenerate with another level,
that does not belong to the set of bands treated. Then, it might take
extremely long to reach [[tolwfr]], although the other bands are already
extremely well-converged, and the energy of the highest bands (whose residual
are not yet good enough), is also rather well converged.  
In response to this problem, for non-zero [[nbdbuf]], the largest residual
(residm), to be later compared with [[tolwfr]], will be computed only in the
set of non-buffer bands (this modification applies for non-self-consistent as
well as self-consistent calculation, for GS as well as RF calculations).  
For a GS calculation, with [[iscf]]&lt;0, supposing [[nbdbuf]] is not
initialized in the input file, then ABINIT will overcome the default
[[nbdbuf]] value, and automatically set [[nbdbuf]] to 2.

In metallic RF calculations, in the conjugate gradient optimisation of first-
order wavefunctions, there is an instability situation when the q wavevector
of the perturbation brings the eigenenergy of the highest treated band at some
k point higher than the lowest untreated eigenenergy at some k+q point. If one
accepts a buffer of frozen states, this instability can be made to disappear.
Frozen states receive automatically a residual value of -0.1d0.  
For a RF calculation, with 3&lt;=[[occopt]]&lt;=7, supposing [[nbdbuf]] is not
initialized in the input file, then ABINIT will overcome the default
[[nbdbuf]] value, and automatically set [[nbdbuf]] to 2. This value might be
too low in some cases.

Also, the number of active bands, in all cases, is imposed to be at least 1,
irrespective of the value of [[nbdbuf]].


* * *

## **ndivk** 


*Mnemonics:* Number of DIVisions of K lines  
*Variable type:* integer  
*Dimensions:* (abs([[kptopt]]))  
*Default value:* None  
*Comment:* Will be generated automatically from [[ndivsm]] if the latter is defined.  
*Only relevant if:* [[kptopt]] < 0  
*The use of this variable forbids the use of:* specified([[ndivsm]])  



Gives the number of divisions of each of the segments of the band structure,
whose path is determined by [[kptopt]] and [[kptbounds]]. In this case, the
absolute value of [[kptopt]] is the number of such segments.

For example, suppose that the number of segment is just one ([[kptopt]]=-1), a
value [[ndivk]]=4 will lead to the computation of points with relative
coordinates 0.0, 0.25, 0.5, 0.75 and 1.0 , along the segment in consideration.

Now, suppose that there are two segments ([[kptopt]]=-2), with [[ndivk]](1)=4
and [[ndivk]](2)=2, the computation of the eigenvalues will be done at 7
points, 5 belonging to the first segment, with relative coordinates 0.0, 0.25,
0.5, 0.75 and 1.0, the last one being also the starting point of the next
segment, for which two other points must be computed, with relative
coordinates 0.5 and 1.0 .

It is easy to compute disconnected circuits (non-chained segments), by
separating the circuits with the value [[ndivk]]=1 for the intermediate
segment connecting the end of one circuit with the beginning of the next one
(in which case no intermediate point is computed along this segment).

Alternatively it is possible to generate automatically the array [[ndivk]] by
just specifying the number of divisions for the smallest segment. See the
related input variable [[ndivsm]].


* * *

## **ndivsm** 


*Mnemonics:* Number of DIVisions for the SMallest segment  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* None  



This variable defines the number of divisions used to sample the smallest
segment of the circuit employed in a band structure calculations (see related
input variables [[kptopt]] and [[kptbounds]]). If [[ndivsm]] is given in the
input file, there is no need to specify the number of divisions to be used for
the other segments. Indeed [[ndivk]] is automatically calculated inside the
code in order to generate a path where the number of divisions in each segment
is proportional to the length of the segment itself. This option is activated
only when [[kptopt]] is negative. In this case, the absolute value of
[[kptopt]] is the number of such segments.


* * *

## **ngfft** 


*Mnemonics:* Number of Grid points for Fast Fourier Transform  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Comment:* (automatic selection of optimal values)  



gives the size of fast Fourier transform (fft) grid in three dimensions. Each
number must be composed of the factors 2, 3, and 5 to be consistent with the
radices available in our fft. If no [[ngfft]] is provided or if [[ngfft]] is
set to 0 0 0, the code will automatically provide an optimal set of [[ngfft]]
values, based on [[acell]], [[rprim]] and [[ecut]] (see also [[boxcutmin]] for
speed/accuracy concerns). This is the recommended procedure, of course.  
The total number of FFT points is the product:  
[[ngfft]](1)*[[ngfft]](2)*[[ngfft]](3)=nfft  .  
When [[ngfft]] is made smaller than recommended values (e.g. by setting
[[boxcutmin]] to a value smaller than 2.0 or by setting [[ngfft]] manually),
the code runs faster and the equations in effect are approximated by a low
pass Fourier filter. The code reports to standard output (unit 06) a parameter
"boxcut" which is the smallest ratio of the fft box side to the G vector basis
sphere diameter. When boxcut is less than 2 the Fourier filter approximation
is being used. When boxcut gets less than about 1.5 the approximation may be
too severe for realistic results and should be tested against larger values of
[[ngfft]]. When boxcut is larger than 2, [[ngfft]] could be reduced without
loss of accuracy. In this case, the small variations that are observed are
solely due to the xc quadrature, that may be handled with [[intxc]]=1 to even
reduce this effect.

Internally, [[ngfft]] is an array of size 18. The present components are
stored in [[ngfft]](1:3), while

  * [[ngfft]](4:6) contains slightly different (larger) values, modified for efficiency of the FFT 
  * [[ngfft]](7) is [[fftalg]] 
  * [[ngfft]](8) is [[fftcache]] 
  * [[ngfft]](9) is set to 0 if the parallelization of the FFT is not activated, while it is set to 1 if it is activated. 
  * [[ngfft]](10) is the number of processors of the FFT group 
  * [[ngfft]](11) is the index of the processor in the group of processors 
  * [[ngfft]](12) is n2proc, the number of x-z planes, in reciprocal space, treated by the processor 
  * [[ngfft]](13) is n3proc, the number of x-y planes, in real space, treated by the processor 
  * [[ngfft]](14) is mpi_comm_fft, the handle on the MPI communicator in charge of the FFT parallelisation 
  * [[ngfft]](15:18) are not yet used 

  
The number of points stored by this processor in real space is n1*n2*n3proc,
while in reciprocal space, it is n1*n2proc*n3.


* * *

## **ngqpt** 


*Mnemonics:* Number of Grid pointsfor Q PoinTs generation  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[nqpt]]==1 and [[kptopt]]>=0  
*The use of this variable forbids the use of:* specified([[qptrlatt]])  



At variance with [[ngkpt]], note that only one q point is selected per dataset
(see [[iqpt]]).  
Its three positive components give the number of q points of Monkhorst-Pack
grids (defined with respect to primitive axis in reciprocal space) in each of
the three dimensions. The use of [[nshiftq]] and [[shiftq]], allows to
generate shifted grids, or Monkhorst-Pack grids defined with respect to
conventional unit cells.

For more information on Monkhorst-Pack grids, see [[ngkpt]].


* * *

## **nline** 


*Mnemonics:* Number of LINE minimisations  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 4  



Gives maximum number of line minimizations allowed in preconditioned conjugate
gradient minimization for each band. The Default, 4, is fine.  
Special cases, with degeneracies or near-degeneracies of levels at the Fermi
energy may require a larger value of [[nline]] (5 or 6 ?) Line minimizations
will be stopped anyway when improvement gets small. With the input variable
[[nnsclo]], governs the convergence of the wavefunctions for fixed potential.  
Note that [[nline]]=0 can be used to diagonalize the Hamiltonian matrix in the
subspace spanned by the input wavefunctions.


* * *

## **npsp** 


*Mnemonics:* Number of PSeudoPotentials  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* [[ntypat]]  



Usually, the number of pseudopotentials to be read is equal to the number of
type of atoms. However, in the case an alchemical mixing of pseudopotential is
to be used, often the number of pseudopotentials to be read will not equal the
number of types of atoms.

Alchemical pseudopotentials will be present when [[ntypalch]] is non-zero. See
[[ntypalch]] to understand how to use alchemical potentials in ABINIT. The
input variables ([[ntypalch]], [[algalch]],[[mixalch]]) are active, and
generate alchemical potentials from the available pseudopotentials. Also, the
inner variables ([[ntyppure]],[[npspalch]]) become active. See these input
variables, especially [[mixalch]], to understand how to use alchemical
potentials in ABINIT.


* * *

## **npspalch** 


*Mnemonics:* Number of PSeudoPotentials that are "ALCHemical"  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* [[npsp]]-[[ntyppure]]  
*Only relevant if:* [[ntypalch]]/=0  



Gives the number of pseudopotentials that are used for alchemical mixing (when
[[ntypalch]] is non-zero) :

[[npspalch]]=[[npsp]]-[[ntyppure]]


* * *

## **nqpt** 


*Mnemonics:* Number of Q - POINTs  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Determines whether one q point must be read (See the variable [[qptn]]).  
Can be either 0 or 1.  
If 1 and used in ground-state calculation, a global shift of all the k-points
is applied, to give calculation at k+q. In this case, the output wavefunction
will be appended by _WFQ instead of _WFK (see the [ section 4
](../../users/generated_files/help_abinit.html) of the [[help_abinit]]) Also,
if 1 and a RF calculation is done, defines the wavevector of the perturbation.


* * *

## **nshiftq** 


*Mnemonics:* Number of SHIFTs for Q point grids  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



This parameter gives the number of shifted grids to be used concurrently to
generate the full grid of q points. It can be used with primitive grids
defined either from [[ngqpt]] or [[qptrlatt]]. The maximum allowed value of
[[nshiftq]] is 8. The values of the shifts are given by [[shiftq]].


* * *

## **nspden** 


*Mnemonics:* Number of SPin-DENsity components  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* [[nsppol]]  



If [[nspden]]=1, no spin-magnetization : the density matrix is diagonal, with
same values spin-up and spin-down (compatible with [[nsppol]]=1 only, for both
[[nspinor]]=1 or 2)

If [[nspden]]=2, scalar magnetization (the axis is arbitrarily fixed in the z
direction) : the density matrix is diagonal, with different values for spin-up
and spin-down (compatible with [[nspinor]]=1, either with [[nsppol]]=2
-general collinear magnetization- or [[nsppol]]=1 -antiferromagnetism)

If [[nspden]]=4, vector magnetization : the density matrix is full, with
allowed x, y and z magnetization (useful only with [[nspinor]]=2 and
[[nsppol]]=1, either because there is spin-orbit without time-reversal
symmetry - and thus spontaneous magnetization, or with spin-orbit, if one
allows for spontaneous non-collinear magnetism). Not yet available for
response functions. Also note that, with [[nspden]]=4, time-reversal symmetry
is not taken into account (at present ; this has to be checked) and thus
[[kptopt]] has to be different from 1 or 2.

The default ([[nspden]]=[[nsppol]]) does not suit the case of vector
magnetization.


* * *

## **nspinor** 


*Mnemonics:* Number of SPINORial components of the wavefunctions  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2 if [[pawspnorb]]==1,
1 otherwise.
  



If [[nspinor]]=1, usual case : scalar wavefunction (compatible with
([[nsppol]]=1, [[nspden]]=1) as well as ([[nsppol]]=2, [[nspden]]=2) )

If [[nspinor]]=2, the wavefunction is a spinor (compatible with [[nsppol]]=1,
with [[nspden]]=1 or 4, but not with [[nsppol]]=2)

When [[nspinor]] is 2, the values of [[istwfk]] are automatically set to 1.
Also, the number of bands, for each k-point, should be even.


* * *

## **ntypalch** 


*Mnemonics:* Number of TYPe of atoms that are "ALCHemical"  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used for the generation of alchemical pseudopotentials : when [[ntypalch]] is
non-zero, alchemical mixing will be used.

Among the [[ntypat]] types of atoms, the last [[ntypalch]] will be
"alchemical" pseudoatoms, while only the first ** ntyppure ** will be uniquely
associated with a pseudopotential (the ** ntyppure ** first of these,
actually). The [[ntypalch]] types of alchemical pseudoatoms are to be made
from the remaining [[npspalch]] pseudopotentials.

In this case, the input variables [[algalch]],[[mixalch]] are active, and
generate alchemical potentials from the available pseudopotentials. See these
input variables, especially [[mixalch]], to understand how to use alchemical
potentials in ABINIT.


* * *

## **ntyppure** 


*Mnemonics:* Number of TYPe of atoms that are "PURe"  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* [[ntypat]]-[[ntypalch]]  



Gives the number of type of atoms that are "pure" when alchemical mixing is
used ([[ntypalch]] /= 0) :

[[ntyppure]]=[[ntypat]]-[[ntypalch]]


* * *

## **nucdipmom** 


*Mnemonics:* NUClear DIPole MOMents  
*Variable type:* real  
*Dimensions:* (3,[[natom]])  
*Default value:* 0.0  
*Only relevant if:* [[usepaw]] = 1; [[pawcpxocc]] = 2; [[kptopt]] > 2  



Places an array of nuclear magnetic dipole moments on the atomic positions,
useful for computing the magnetization in the presence of nuclear dipoles and
thus the chemical shielding by the converse method. The presence of these
dipoles breaks time reversal symmetry and lowers the overall spatial symmetry.


* * *

## **nwfshist** 


*Mnemonics:* Number of WaveFunctionS HISTory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



In the wavelet basis set, the ground state is found by direct minimisation.
The algorithm used can be either the steepest descent or the DIIS (Direct
Inversion of Iteration Space). When [[nwfshist]] = 0, the steepest descent is
used ( _ i.e. _ there is no history storage of the previous iterations). If
[[nwfshist]] is strictly positive, a DIIS is used. A typical value is 6. Using
a DIIS increases the memory required by the program since N previous
wavefunctions are stored during the electronic minimisation.


* * *

## **occ** 


*Mnemonics:* OCCupation numbers  
*Variable type:* real  
*Dimensions:* ([[nband]])  
*Default value:* *0  



Gives occupation numbers for all bands in the problem. Needed if [[occopt]]==0
or [[occopt]]==2. Ignored otherwise. Also ignored when [[iscf]]=-2.  
Typical band occupancy is either 2 or 0, but can be 1 for half-occupied band
or other choices in special circumstances.  
If [[occopt]] is not 2, then the occupancies must be the same for each k
point.  
If [[occopt]]=2, then the band occupancies must be provided explicitly for
each band, EACH k POINT, and EACH SPIN-POLARIZATION, in an array which runs
over all bands, k points, and spin-polarizations.  
The order of entries in the array would correspond to all bands at the first k
point (spin up), then all bands at the second k point (spin up), etc, then all
k-points spin down.  
The total number of array elements which must be provided is  
( [[nband]](1)+[[nband]](2)+...+ [[nband]]([[nkpt]]) ) * [[nsppol]] .  
The occupation numbers evolve only for metallic occupations, that is,
[[occopt]] ≥ 3 .


* * *

## **optdriver** 


*Mnemonics:* OPTions for the DRIVER  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



For each dataset, choose the task to be done, at the level of the "driver"
routine.

The choice is among :  
[[optdriver]]=0 : ground-state calculation (GS), routine "gstate"  
[[optdriver]]=1 : response-function calculation (RF), routine "respfn"  
[[optdriver]]=2 : susceptibility calculation (SUS), routine "suscep"  
[[optdriver]]=3 : susceptibility and dielectric matrix calculation (SCR),
routine "screening"  
(see the input variables [[ecutwfn]], [[ecuteps]], [[ppmfrq]], [[getwfk]], as
well as [[nbandkss]] and [[nband]])  
[[optdriver]]=4 : self-energy calculation (SIG), routine "sigma"  
[[optdriver]]=5 : non-linear response functions (NONLINEAR), using the 2n+1
theorem, routine "nonlinear"  
[[optdriver]] =7: electron-phonon coupling (EPH)  
[[optdriver]] =66: GW using Lanczos-Sternheimer, see input variables whose
name start with gwls_* .  
[[optdriver]]=99 : Bethe-Salpeter calculation (BSE), routine "bethe_salpeter"

If one of [[rfphon]], [[rfddk]], [[rfelfd]], or [[rfstrs]] is non-zero, while
[[optdriver]] is not defined in the input file, ABINIT will set [[optdriver]]
to 1 automatically. These input variables ([[rfphon]], [[rfddk]], [[rfelfd]],
and [[rfstrs]]) must be zero if [[optdriver]] is not set to 1.


* * *

## **optstress** 


*Mnemonics:* OPTion for the computation of STRESS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



If set to 1, the computation of stresses is done, in the SCF case (under the
conditions [[iscf]] &gt; 0 , [[prtstm]]==0 , [[positron]]==0, and either
[[nstep]] &gt;0 , or [[usepaw]]==0 or [[irdwfk]]==1).  
Otherwise, to save CPU time, if no optimization of the cell is required, one
can skip the computation of stresses. The CPU time saving might be interesting
for some PAW calculations.


* * *

## **posdoppler** 


*Mnemonics:* POSitron computation of DOPPLER broadening  
*Variable type:* integer  
*Default value:* 0  



Relevant only when [[positron]]&lt;&gt;0.  
This input parameter activates the calculation of the Doppler broadening of
the electron-positron annihilation radiation.  
An output file containing the momentum distributions of annihilating electron-
positron pairs is created.  
Such a computation needs a core wave-function file (per atom type) to be
provided. This core WF file should be named '&lt;psp_file_name&gt;.corewf'
(where &lt;pspfile_name&gt; is the name of the pseudo-potential (or PAW) file)
or 'corewf.abinit&lt;ityp&gt;' (where &lt;ityp&gt; is the index of the atom
type). Core WF files can be obtained with the atompaw tool by the use of
'prtcorewf' keyword.


* * *

## **positron** 


*Mnemonics:* POSITRON calculation  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



This input parameter can be positive or negative.  
Negative values for [[positron]] are only relevant for PAW calculations.  
Electron-positron correlation functional is defined by [[ixcpositron]].  
Other relevant input parameter: [[posocc]] (occupation number for the
positron).  
  
_Positive values for [[positron]]:_  
_For **[[positron]]=1 or 2**, will perform the calculation of positron
lifetime (and annihilation rate)._  

  * [[positron]]=1**:  
Starting from a previous electronic GS density (with **[[positron]]=0**), a
positronic ground-state calculation is performed, considering that the
electrons are not perturbed by the presence of the positron.  
This is almost correct for a positron in a perfect bulk material. But this
approximation fails when defects exist in the material (for instance: the
positron might be trapped by a vacancy).  
The electronic density will be automatically read from a _DEN file (with or
without [[irdden]] keyword).  
At the end of the SCF cycle, the positron lifetime and annihilation rate are
printed out.  
  
_Additional information for the use of pseudopotentials:  

    * PAW datasets: nothing to do; simply use usual electronic PAW datasets 
    * Norm-conserving pseudopotentials: One has to use specific pseudopotentials for the positron calculation. They must be of the FHI type (pspcod=6), and must contain at their end, the all-electrons core density generated with FHI98PP. They must have lmax=lloc=0 (check that this works for the electronic GS !! No ghost, etc ...). Otherwise, their are similar to an usual FHI pseudopotential.  
_  

  * **positron=2**:  
Starting from a previous positronic GS density (with **positron=1**), an
electronic ground-state calculation is performed, keeping the positronic
density constant.  
The positronic density will be automatically read from a _DEN file (with or
without [[getden]]/[[irdden]] keyword).  
At the end of the SCF cycle, the positron lifetime and annihilation rate are
printed out.  
  
_Additional information for the use of pseudopotentials:  

    * PAW datasets: nothing to do; simply use usual electronic PAW datasets 
    * Norm-conserving pseudopotentials: One has to use specific pseudopotentials for the electron calculation. They must be of the FHI type (pspcod=6), and must contain at their end, the all-electrons core density generated with FHI98PP.  
_  

  * **Typical use**:  
The calculation is done in several steps:  
The first one is a normal GS calculation for the electrons, with
**positron**=0. The only specific thing to do is to set [[prtden]]=1 (this is
the defaut for ABINIT v6.x+). This will create the associated _DEN file which
will be used as input file for the positronic GS calculation.  
The second step is the GS calculation of the positron and subsequently its
lifetime, with **positron**=1. One has to define also [[ixcpositron]].  
Then, it is possible to perform an additional step, computing the GS
electronic density in presence of the positron, with **positron**=2.  
and so on...  
This procedure can be automated (for PAW only) by the use of a negative value
for **positron**.  
At the end, a converged value of the positron lifetime (decomposed in several
contributions) is printed.  
See also [[posdoppler]] keyword for the calculation of Doppler broadening.  

  
_Negative values for **positron**:_  
_For **positron&lt;0**, will perform an automatic calculation of electrons and
positron densities in the two-component DFT context; then will compute
positron lifetime (and annihilation rate)._  

  * **positron=-1**:  
Starting from scratch, will first perform an usual electronic ground-state
calculation until convergence (controlled by the use of one of the _tolerance_
keywords).  
Then will perform a positronic ground state calculation in presence of the
electrons and ions; then an electronic ground state calculation in presence of
the positron and the ions...  
and so on... until the total energy is converged.  
The convergence of the total energy of the ions+electrons+positron system is
controlled by the use of the [[postoldfe]], [[postoldff]] and [[posnstep]]
input keywords.  
With **positron=-1**, at the beginning of each new electronic/positronic step,
the wave functions are unknown.

  * **positron=-10**:  
Same as **positron=-1** except that the electronic/positronic wave functions
are stored in memory.  
Consequently, the total number of iterations to reach the convergence
(diff_Etotal<[[postoldfe]] or diff_Forces<[[postoldff]]) is smaller.  
But, this can increase the total amount of memory needed by the code.

  * **positron=-2**:  
Same as **positron=-1** except that the two-component DFT cycle is forced to
stop at the end of an electronic step.

  * **positron=-20**:  
Same as **positron=-10** except that the two-component DFT cycle is forced to
stop at the end of an electronic step.

  
_Advice for use:_  
There are two typical cases which have to be differently treated:

  * **A positron in a perfect _bulk_ system**:  
In that case, the positron is delocalized in the whole crystal. Its density is
almost zero.  
Thus, the "zero density positron limit" has to be used. [[ixcpositron]] has to
be choosen accordingly.  
In order to have the zero density positron limit it is adviced to follow these
points:  
1- Put a small positronic charge (by setting a [[posocc]] to a small value)
**OR** use a big supercell.  
2- Use only k=gamma wave vector for the positronic calculation.  
3- Use the manual procedure in 2 steps: first **positron**=0 and then
**positron**=1; avoid the **positron=2** step and the automatic procedure
(**positron**&lt;0).  
In principle, the positron lifetime should converge with the value of
[[posocc]] or the size of the supercell.  

  * **A positron trapped in a _default_ (vacancy...)**:  
In that case, the positron is localized in the default. Its density can be
localized in the simulation cell (provided that the cell is sufficiently
large) and influences the electronic density.  
So, it is advised to use the automatic procedure (**positron**&lt;0) or the
manual procedure with several **positron**=0,1,2,1,... steps.  
K-points can be used as in usual electronic calculations.  
Also note that it is possible to use forces and stresses to perform structural
minimization.  

References:  

**[1]** J. Arponen and E. Pajanne, Ann. Phys. (N.Y.) 121, 343 (1979).  
**[2]** Boronski and R.M. Nieminen, Phys. Rev. B 34, 3820 (1986).  
**[3]** P.A. Sterne and J.H. Kaiser, Phys. Rev. B 43, 13892 (1991).  
**[4]** M.J. Puska, A.P. Seitsonen and R.M. Nieminen, Phys. Rev. B 52, 10947 (1994).  
**[5]** B. Barbiellini, M.J. Puska, T. Torsti and R.M.Nieminen, Phys. Rev. B 51, 7341 (1994)  


* * *

## **posnstep** 


*Mnemonics:* POSitron calculation: max. Number of STEPs for the two-component DFT  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 50  



Relevant only when [[positron]]&lt;0\.  
Sets the maximum number of electronic/positronic iterations that, when
reached, will cause the two-component DFT SCF cycle to stop.  
The code will first compute the electronic ground-state, then the positronic
ground state in the electronic density, then the electronic ground-state in
the positronic density, ...  
...until diff_Etotal&lt;[[postoldfe]] or diff_Forces&lt;[[postoldff]] or the
number of electronic/positronic steps is [[posnstep]].  


* * *

## **posocc** 


*Mnemonics:* POSitron calculation: OCCupation number for the positron  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1  



Relevant only when [[positron]]/=0.  
Sets the occupation number for the positron. Has to be &lt;=1.  
Changing [[posocc]] is only useful for bulk calculation when one wants to
perform lifetime computations using a small simulation cell (can avoid the use
of a supercell). It simulates the dispersion of the positron in the whole
crystal.  


* * *

## **postoldfe** 


*Mnemonics:* POSitron calculation: TOLerance on the DiFference of total Energy  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1e-06 if [[postoldff]]=0,
0.0 otherwise.
  



Relevant only when [[positron]]&lt;0\.  
Sets a tolerance for absolute difference of total energy (of _
ions+electrons+positron _ system) that, when reached, will cause the SCF cycle
to stop before the number of steps is [[nstep]] or the number of
electronic/positronic steps is [[posnstep]].  
  
Can be specified in Ha (the default), Ry, eV or Kelvin, since ** toldfe ** has
the '[[ENERGY]]' characteristics.  
Only one and only one of [[postoldfe]] or [[postoldff]] can be set.


* * *

## **postoldff** 


*Mnemonics:* POSitron calculation: TOLerance on the DiFference of Forces  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0  



Relevant only when [[positron]]&lt;0\.  
Sets a tolerance for absolute difference of maximum force acting on ions (due
to _ ions+electrons+positron _ system) that, when reached, will cause the SCF
cycle to stop before the number of SCF steps is [[nstep]] or the number of
electronic/positronic steps is [[posnstep]].  
Only one and only one of [[postoldfe]] or [[postoldff]] can be set.  


* * *

## **prtdensph** 


*Mnemonics:* PRinT integral of DENsity inside atomic SPHeres  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 otherwise.
  



When this flag is activated, values of integral(s) of total density inside
sphere(s) around each atom are printed in output file (for each spin
component). Spheres around atoms are defined by a radius given by [[ratsph]]
keyword.  
Note: integral of density inside a sphere around an atom can be used to
determine a rough approximation of the local magnetic moment; this is
particularly useful for antiferromagnetic systems.  
The algorithm to compute this integral is particularly primitive : the points
on the FFT grids, belonging to the interior of the sphere are determined, and
the value of the functions on these points are summed, taking into account a
fixed volume attributed to each point. In particular, the integral as a
function of the radius will be a constant, except when a new point enters the
sphere, in which case a sudden jump occurs. However, since the purpose of this
output is to get a rough idea of the repartition of the density, this is not a
real problem. If you are interested in a more accurate estimation of the
density within a sphere, you should use the cut3d postprocessor.


* * *

## **prtebands** 


*Mnemonics:* PRinT Electron BANDS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0 if [[nimage]] > 1,
1 otherwise.
  



This option activates the output of the electron eigenvalues. Possible values:

  * 0 Disable the output of the band energies.
  * 1 Write eigenvalues in xmgrace format. A file with extension `EBANDS.agr` is produced at the end of the run. Use `xmgrace file_EBANDS.agr` to visualize the band energies
  * 2 Write eigenvalues in gnuplot format. The code produces a `EBANDS.dat` file with the eigenvalues and a `EBANDS.gnuplot` script. Use `gnuplot file_EBANDS.gnuplot` to visualize the band energies.


* * *

## **qpt** 


*Mnemonics:* Q PoinT  
*Variable type:* real  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  



Only used if [[nqpt]]=1.

Combined with [[qptnrm]], define the q vector [[qptn]](1:3) in the case
[[qptopt]]=0.

This input variable is not internal ([[qptn]](1:3) is used instead), but is
used to echo the value of [[qptn]](1:3), with renormalisation factor one.


* * *

## **qptnrm** 


*Mnemonics:* Q PoinTs NoRMalization  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.0  



Only used if [[nqpt]]=1 and [[qptopt]]=0

Provides re-normalization of [[qpt]]. Must be positive, non-zero. The actual q
vector (renormalized) is [[qptn]](1:3)= [[qpt]](1:3)/[[qptnrm]].


* * *

## **qptopt** 


*Mnemonics:* QPoinTs OPTion  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Only used if [[nqpt]]=1.

Controls the set up to generate the Q point [[qptn]](1:3) to be used for the
specific dataset, either as a shift of k-point grid in ground-state
calculations, or as a stand-alone phonon wavevector.

There are two basic techniques to generate the Q point : either by specifying
it directly, possibly with a renormalisation factor ([[qptopt]]=0), or
extracting it from a grid a Q points ([[qptopt]]=1 to 4), using the index
[[iqpt]]. At variance with the similar generation of k points, only ONE q
point can be used per dataset.

With [[qptopt]]=1 to 4, rely on [[ngqpt]] or [[qptrlatt]], as well as on
[[nshiftq]] and [[shiftq]] to set up a q point grid, from which the q point
with number [[iqpt]] will be selected. The values [[qptopt]]=1 to 4 differ by
the treatment of symmetries. Note that the symmetries are recomputed starting
from the values of [[rprimd]] [[xred]] and [[spinat]]. So, the explicit value
of [[symrel]] are not used. This is to allow doing calculations with
[[nsym]]=1, sometimes needed for T-dependent electronic structure, still
decreasing the number of q points in the case [[qptopt]]=1 or [[qptopt]]=3.

  * 0=&gt; read directly [[qpt]], and its (eventual) renormalisation factor [[qptnrm]]. 
  * 1=&gt; Take fully into account the symmetry to generate the grid of q points in the Irreducible Brillouin Zone only.   
(This is the usual mode for RF calculations)

  * 2=&gt; Take into account only the time-reversal symmetry : q points will be generated in half the Brillouin zone.   

  * 3=&gt; Do not take into account any symmetry : q points will be generated in the full Brillouin zone.   

  * 4=&gt; Take into account all the symmetries EXCEPT the time-reversal symmetry to generate the k points in the Irreducible Brillouin Zone.   

In the case of a grid of q points, the auxiliary variables [[kptrlen]],
[[ngkpt]] and [[prtkpt]] might help you to select the optimal grid, similarly
to the case of the K point grid.


* * *

## **qptrlatt** 


*Mnemonics:* Q - PoinTs grid : Real space LATTice  
*Variable type:* integer  
*Dimensions:* (3,3)  
*Default value:* *0  
*The use of this variable forbids the use of:* specified([[ngqpt]])  



This input variable is used only when [[qptopt]] is positive. It partially
defines the q point grid. The other piece of information is contained in
[[shiftq]]. [[qptrlatt]] cannot be used together with [[ngqpt]].

The values [[qptrlatt]](1:3,1), [[qptrlatt]](1:3,2), [[qptrlatt]](1:3,3) are
the coordinates of three vectors in real space, expressed in the [[rprimd]]
coordinate system (reduced coordinates). They defines a super-lattice in real
space. The k point lattice is the reciprocal of this super-lattice, possibly
shifted (see [[shiftq]]).

If neither [[ngqpt]] nor [[qptrlatt]] are defined, ABINIT will automatically
generate a set of k point grids, and select the best combination of
[[qptrlatt]] and [[shiftq]] that allows to reach a sufficient value of
[[kptrlen]]. See this latter variable for a complete description of this
procedure.


* * *

## **ratsph** 


*Mnemonics:* Radii of the ATomic SPHere(s)  
*Variable type:* real  
*Dimensions:* ([[ntypat]])  
*Default value:* [['AUTO_FROM_PSP']] if usepaw==1,
2.0 otherwise.
  



Relevant only when [[prtdos]]=3 or [[prtdensph]]=1.  
  
When [[prtdos]]=3:  
Provides the radius of the spheres around the [[natsph]] atoms of indices
[[iatsph]], in which the local DOS and its angular-momentum projections will
be analysed. The choice of this radius is quite arbitrary. In a plane-wave
basis set, there is no natural definition of an atomic sphere. However, it
might be wise to use the following well-defined and physically motivated
procedure (in version 4.2, this procedure is NOT implemented, unfortunately) :
from the Bader analysis, one can define the radius of the sphere that contains
the same charge as the Bader volume. This "Equivalent Bader charge atomic
radius" might then be used to perform the present analysis. See the
[[help_aim]] for more explanations. Another physically motivated choice would
be to rely on another charge partitioning, like the Hirshfeld one (see the
cut3d utility). The advantage of using charge partitioning schemes comes from
the fact that the sum of atomic DOS, for all angular momenta and atoms,
integrated on the energy range of the occupied states, gives back the total
charge. If this is not an issue, one could rely on the half of the nearest-
neighbour distances, or any scheme that allows to define an atomic radius.
Note that the choice of this radius is however critical for the balance
between the s, p and d components. Indeed, the integrated charge within a
given radius, behave as a different power of the radius, for the different
channels s, p, d. At the limit of very small radii, the s component dominates
the charge contained in the sphere ...  
  
When [[prtdensph]]=1:  
Provides the radius of the spheres around (all) atoms in which the total
charge density will be integrated.  
  
In case of PAW, [[ratsph]] radius has to be greater or equal to PAW radius of
considered atom type (which is read from the PAW dataset file; see rc_sph or
r_paw).


* * *

## **ratsph_extra** 


*Mnemonics:* Radii of the ATomic SPHere(s) in the EXTRA set  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 2.0 Bohr  



Radius for extra spheres the DOS is projected into. See [[natsph_extra]] and
[[xredsph_extra]] for the number and positions of the spheres.


* * *

## **scphon_supercell** 


*Mnemonics:* Self Consistent PHONon SUPERCELL  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [1, 1, 1]  



Give extent, in number of primitive unit cells, of the supercell being used
for a self-consistent phonon calculation. Presumes the phonon frequencies and
eigenvectors have been calculated in the original primitive unit cell, on a
grid of q-points which corresponds to the supercell in the present
calculation. TO BE IMPROVED : should contain a tutorial on how to do self-
consistent phonon calculations, David Waroquiers 090831


* * *

## **scphon_temp** 


*Mnemonics:* Self Consistent PHONon TEMPerature  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



Temperature which is imposed on phonon distribution, in the self-consistent
scheme of Souvatzis et al. PRL ** 100 ** , 095901. Determines the extent of
the finite displacements used, and consequent anharmonic effects.
Experimental.


* * *

## **shiftq** 


*Mnemonics:* SHIFT for Q points  
*Variable type:* real  
*Dimensions:* (3,[[nshiftq]])  
*Default value:* None if [[nshiftq]]>1,
[0.5, 0.5, 0.5] otherwise.
  



It is used only when [[qptopt]]&gt;=0, and must be defined if [[nshiftq]] is
larger than 1.  
[[shiftq]](1:3,1:[[nshiftq]]) defines [[nshiftq]] shifts of the homogeneous
grid of q points based on [[ngqpt]] or [[qptrlatt]].

See [[shiftk]] for more information on the definition, use, and suitable
values for these shifts.


* * *

## **slabwsrad** 


*Mnemonics:* jellium SLAB Wigner-Seitz RADius  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



Fix the bulk-mean positive charge density nbulk of a jellium slab (if the
latter is employed, e.g. [[jellslab]] ≠ 0). Often called "rs" [see for example
N. D. Lang and W. Kohn PRB 1, 4555 (1970)], [[slabwsrad]] is the radius of a
sphere which has the same volume as the average volume per particle in a
homogeneous electron gas with density nbulk, so:

    
    
      1/nbulk = 4/3 Pi * [[slabwsrad]]3
     

For example, the bulk aluminum fcc lattice constant is a=4.0495 Angstroms
(webelements.com), each cubic centered cell includes 4 Al atoms and each atom
has 3 valence electrons, so the average volume per electron is a3/12=37.34
Bohr3 which has to be equal to 4/3 Pi*rs3. Consequently Al has approximately
rs =2.07 Bohr, while for example magnesium has rs =2.65 Bohr, sodium 3.99
Bohr.  
By default, given in Bohr atomic units (1 Bohr=0.5291772108 Angstroms).


* * *

## **slabzbeg** 


*Mnemonics:* jellium SLAB BEGinning edge along the Z direction  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* [0.0, 0.0]  



Define the edges of the jellium slab (if used, so if [[jellslab]] ≠ 0) along
z, namely the slab starts at a point along z which is expressed in Bohr by
**slabzbeg** and it ends at a point expressed in Bohr by [[slabzend]]. The z
direction is parallel to the third crystal primitive lattice vector which has
to be orthogonal to the other ones, so the length of the cell along z is
[[rprimd]](3,3). In addition **slabzbeg** and [[slabzend]] have to be such
that:

    
    
      0 ≤ **slabzbeg** < [[slabzend]] ≤ [[rprimd]](3,3)
     

Together with [[slabwsrad]] they define the jellium positive charge density
distribution n+(x,y,z) in this way:

    
    
      n+(x,y,z) = nbulk     if **slabzbeg** ≤ z ≤ [[slabzend]]
                = 0        otherwise,
     

so the positive charge density is invariant along the xy plane as well as the
electrostatic potential generated by it.


* * *

## **slabzend** 


*Mnemonics:* jellium SLAB ENDing edge along the Z direction  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* [0.0, 0.0]  



Define the edges of the jellium slab (if used, so if [[jellslab]] ≠ 0) along
z, namely the slab starts at a point along z which is expressed in Bohr by
[[slabzbeg]] and it ends at a point expressed in Bohr by **slabzend**. The z
direction is parallel to the third crystal primitive lattice vector which has
to be orthogonal to the other ones, so the length of the cell along z is
[[rprimd]](3,3). In addition [[slabzbeg]] and **slabzend** have to be such
that:

    
    
      0 ≤ [[slabzbeg]] < **slabzend** ≤ [[rprimd]](3,3)
     

Together with [[slabwsrad]] they define the jellium positive charge density
distribution n+(x,y,z) in this way:

    
    
      n+(x,y,z) = nbulk     if [[slabzbeg]] ≤ z ≤ **slabzend**
                = 0        otherwise,
     

so the positive charge density is invariant along the xy plane as well as the
electrostatic potential generated by it.


* * *

## **so_psp** 


*Mnemonics:* Spin-Orbit treatment for each PSeudoPotential  
*Variable type:* integer  
*Dimensions:* ([[npsp]])  
*Default value:* [[npsp]]*1  
*Only relevant if:* [[nspinor]]==2 and [[usepaw]]==0  



For each type of atom (each pseudopotential), specify the treatment of spin-
orbit interaction (if [[nspinor]]==2 and Norm-conserving pseudopotentials
[[usepaw]]==0)  
If 0 : no spin-orbit interaction, even if [[nspinor]]=2  
If 1 : treat spin-orbit as specified in the pseudopotential file.  
If 2 : treat spin-orbit in the HGH form (usual form, although not allowed for
all pseudopotentials)  
If 3 : treat spin-orbit in the HFN form (Hemstreet-Fong-Nelson) (actually, not
implemented ...).

For typical usage, the default value is OK. If the spin-orbit needs to be
turned off for one atom, 0 might be relevant. Note however, that the code will
stop if [[nspinor]]=2 is used and one of the pseudopotential does not contain
the information about the spin-orbit interaction (this is the case for some
old pseudopotentials). Indeed, for spinorial calculations, turning off the
spin-orbit interaction is unphysical, and also does not save CPU time ... It
should only be done for test purposes

Note that if [[nspinor]]==1, the spin-orbit cannot be treated anyhow, so the
value of [[so_psp]] is irrelevant. In case [[usepaw]]=1, please refer to
[[pawspnorb]].

Prior to v5.4, the input variable ** so_typat ** was used, in place of
[[so_psp]]. Because the values 0 and 1 have been switched between [[so_psp]]
and so_typat, it was dangerous to continue to allow the use of so_typat.


* * *

## **spinat** 


*Mnemonics:* SPIN for AToms  
*Variable type:* real  
*Dimensions:* [3, '[[natrd]]'] if [[natrd]]<[[natom]],
[3, '[[natom]]'] otherwise.
  
*Default value:* 0.0  



Gives the initial electronic spin-magnetization for each atom, in unit of
h-bar/2.

Note that if [[nspden]]=2, the z-component must be given for each atom, in
triplets (0 0 z-component).  
For example, the electron of an hydrogen atom can be spin up (0 0 1.0) or spin
down (0 0 -1.0).

This value is only used to create the first exchange and correlation
potential, and is not used anymore afterwards.  
It is not checked against the initial occupation numbers [[occ]] for each spin
channel.  
It is meant to give an easy way to break the spin symmetry, and to allow to
find stable local spin fluctuations, for example : antiferromagnetism, or the
spontaneous spatial spin separation of elongated H2 molecule.  
  

* If the geometry builder is used, [[spinat]] will be related to the preprocessed set of atoms, generated by the geometry builder. The user must thus foresee the effect of this geometry builder (see [[objarf]]). 
  

* If the geometry builder is not used, and the symmetries are not specified by the user ([[nsym]]=0), spinat will be used, if present, to determine the anti-ferromagnetic characteristics of the symmetry operations, see [[symafm]].   
In case of collinear antiferromagnetism ([[nsppol]]=1, [[nspinor]]=1,
[[nspden]]=2), these symmetries are used to symmetrize the density.  
In case of non-collinear magnetism ([[nsppol]]=1, [[nspinor]]=1,
[[nspden]]=4), they are also used to symmetrize the density. In the latter
case, this strongly constrains the magnetization (imposing its direction). If
the user want to let all degrees of freedom of the magnetization evolve, it is
then recommended to put [[nsym]]=1.  

  

* If the symmetries are specified, and the irreducible set of atoms is specified, the anti-ferromagnetic characteristics of the symmetry operations [[symafm]] will be used to generate [[spinat]] for all the non-irreducible atoms. 
  

* In the case of PAW+U calculations using the [[dmatpawu]] initial occupation matrix, and if [[nspden]]=4, [[spinat]] is also used to determine the direction of the integrated magnetization matrix. 


* * *

## **stmbias** 


*Mnemonics:* Scanning Tunneling Microscopy BIAS voltage  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



Gives, in Hartree, the bias of the STM tip, with respect to the sample, in
order to generate the STM density map.  
Used with positive [[iscf]], [[occopt]]=7 (metallic, gaussian), [[nstep]]=1 ,
and positive [[prtstm]], this value is used to generate a charge density map
from electrons close to the Fermi energy, in a (positive or negative) energy
range. Positive [[stmbias]] will lead to the inclusion of occupied (valence)
states only, while negative [[stmbias]] will lead to the inclusion of
unoccupied (conduction) states only.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since [[stmbias]] has
the '[[ENERGY]]' characteristics (0.001 Ha = 27.2113845 meV = 315.773 Kelvin).
With [[occopt]]=7, one has also to specify an independent broadening
[[tsmear]].


* * *

## **symafm** 


*Mnemonics:* SYMmetries, Anti-FerroMagnetic characteristics  
*Variable type:* integer  
*Dimensions:* ([[nsym]])  
*Default value:* [[nsym]]*1  



In case the material is magnetic (well, this is only interesting in the case
of antiferromagnetism, collinear or not), additional symmetries might appear,
that change the sign of the magnetization. They have been introduced by
Shubnikov (1951). They can be used by ABINIT to decrease the CPU time, by
using them to decrease the number of k-points.  
[[symafm]] should be set to +1 for all the usual symmetry operations, that do
not change the sign of the magnetization, while it should be set to -1 for the
magnetization-changing symmetries.  
If the symmetry operations are not specified by the user in the input file,
that is, if [[nsym]]=0, then ABINIT will use the values of [[spinat]] to
determine the content of [[symafm]].  
The symmetries found as "antiferro magnetic" ([[symafm]]=-1) are used to
symmetrize density and magnetization in the following cases:  
\- antiferromagnetism ([[nsppol]]=1, [[nspinor]]=1, [[nspden]]=2)  
\- non-collinear magnetism ([[nsppol]]=1, [[nspinor]]=1, [[nspden]]=4)  
In other cases they are not used.


* * *

## **timopt** 


*Mnemonics:* TIMing OPTion  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[SEQUENTIAL]],
0 otherwise.
  



This input variable allows to modulate the use of the timing routines.

If 0 =&gt; as soon as possible, suppresses all calls to timing routines  
If 1 =&gt; usual timing behaviour, with short analysis, appropriate for
sequential execution  
If 2 =&gt; close to [[timopt]]=1, except that the analysis routine does not
time the timer, appropriate for parallel execution.  
If 3 =&gt; close to [[timopt]]=1, except that the different parts of the
lobpcg routine are timed in detail.  
If 4 =&gt; close to [[timopt]]=1, except that the different parts of the
lobpcg routine are timed in detail. A different splitting of lobpcg than for
[[timopt]]=-3 is provided.  
If -1 =&gt; a full analysis of timings is delivered  
If -2 =&gt; a full analysis of timings is delivered, except timing the timer  
If -3 =&gt; a full analysis of timings is delivered, including the detailed
timing of the different parts of the lobpcg routine. (this takes time, and is
discouraged for too small runs - the timing would take more time than the run
!). The timer is timed.  
If -4 =&gt; a full analysis of timings is delivered, including the detailed
timing of the different parts of the lobpcg routine. A different splitting of
lobpcg than for [[timopt]]=-3 is provided (this takes time, and is discouraged
for too small runs - the timing would take more time than the run !). The
timer is timed. The sum of the independent parts is closer to 100% than for
[[timopt]]=-3.


* * *

## **tl_nprccg** 


*Mnemonics:* TaiL maximum Number of PReConditionner Conjugate Gradient iterations  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 30  



This variable is similar to [[wvl_nprccg]] but for the preconditionner
iterations during the tail corrections (see [[tl_radius]]  ). TO BE IMPROVED :
all tl_* and wvl_* variables should contain a link to a tutorial, David
Waroquiers 090831.


* * *

## **tl_radius** 


*Mnemonics:* TaiL expansion RADIUS  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



In the wavelet computation case, the linkage between the grid and the free
boundary conditions can be smoothed using an exponential decay. This means a
correction on the energy at the end on each wavefunction optimisation run. If
this parameter is set to zero, no tail computation is done. On the contrary,
put it to a positive value makes the tail correction available. The value
correspond to a length in atomic units being the spacial expansion with the
exponential decay around the grid.


* * *

## **tphysel** 


*Mnemonics:* Temperature (PHYSical) of the ELectrons  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  



Gives, in Hartree, the physical temperature of the system, in case
[[occopt]]=4, 5, 6, or 7.  
Can be specified in Ha (the default), Ry, eV or Kelvin, since ** ecut ** has
the '[[ENERGY]]' characteristics (0.001 Ha = 27.2113845 meV = 315.773 Kelvin).
One has to specify an independent broadening [[tsmear]]. The combination of
the two parameters [[tphysel]] and [[tsmear]] is described in a paper by M.
Verstraete and X. Gonze, Phys. Rev. B 65, 035111 (2002). Note that the
signification of the entropy is modified with respect to the usual entropy.
The choice has been made to use [[tsmear]] as a prefactor of the entropy, to
define the entropy contribution to the free energy.


* * *

## **tsmear** 


*Mnemonics:* Temperature of SMEARing  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.01  



Gives the broadening of occupation numbers [[occ]], in the metallic cases
([[occopt]]=3, 4, 5, 6 and 7). Can be specified in Ha (the default), eV, Ry,
or Kelvin, since [[tsmear]] has the '[[ENERGY]]' characteristics (0.001 Ha =
27.2113845 meV = 315.773 Kelvin).  
Default is 0.01 Ha. This should be OK using gaussian like smearings (occopt
4,5,6,7) for a free-electron metal like Al. For d-band metals, you may need to
use less.  
Always check the convergence of the calculation with respect to this
parameter, and simultaneously, with respect to the sampling of k-points (see
[[nkpt]])  
If [[occopt]]=3, [[tsmear]] is the physical temperature, as the broadening is
based on Fermi-Dirac statistics. However, if [[occopt]]=4, 5, 6, or 7, the
broadening is not based on Fermi-Dirac statistics, and [[tsmear]] is only a
convergence parameter. It is still possible to define a physical temperature,
thanks to the input variable [[tphysel]]. See the paper by M. Verstraete and
X. Gonze, Phys. Rev. B (2002).


* * *

## **usekden** 


*Mnemonics:* USE Kinetic energy DENsity  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If [[usekden]]=1 the kinetic energy density will be computed during the self-
consistency loop, in a way similar to the computation of the density. This is
needed if a meta-GGA is to be used as XC functional. Otherwise
([[usekden]]=0), the kinetic energy density is not computed during the self-
consistency loop.


* * *

## **vacuum** 


*Mnemonics:* VACUUM identification  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* None  



Establishes the presence (if 1) or absence (if 0) of a vacuum layer, along the
three possible directions normal to the primitive axes.

This information might be used to generate k-point grids, if [[kptopt]]=0 and
neither [[ngkpt]] nor [[kptrlatt]] are defined (see explanations with the
input variable [[prtkpt]]).  
It will allow to select a zero-, one-, two- or three-dimensional grid of k
points. The coordinate of the k points along vacuum directions is
automatically set to zero.

If [[vacuum]] is not defined, the input variable [[vacwidth]] will be used to
determine automatically whether the distance between atoms is sufficient to
have the presence or absence of vacuum.


* * *

## **vacwidth** 


*Mnemonics:* VACuum WIDTH  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 10.0  



Give a minimum "projected" distance between atoms to be found in order to
declare that there is some [[vacuum]] present for each of the three
directions. By default, given in Bohr atomic units (1 Bohr=0.5291772108
Angstroms), although Angstrom can be specified, if preferred, since
[[vacwidth]] has the '[[LENGTH]]' characteristics.  
The precise requirement is that a slab of width [[vacwidth]], delimited by two
planes of constant reduced coordinates in the investigated direction, must be
empty of atoms.


* * *

## **wtq** 


*Mnemonics:* WeighTs for the current Q-points  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1  
*Comment:* Except when [[qptopt]]/=0  



Gives the current q-point weight.


* * *

## **wvl_bigdft_comp** 


*Mnemonics:* WaVeLet BigDFT Comparison  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



This variable is used for the wavelets capabilities of ABINIT (see [[usewvl]]
). It is used to compare the results obtained with ABINIT with those obtained
with BigDFT stand-alone. When it is set to 1, ABINIT will follow the workflow
as in BigDFT stand-alone. Therefore, the results must be exactly the same with
the two codes.


* * *

## **wvl_crmult** 


*Mnemonics:* WaVeLet Coarse grid Radius MULTiplier  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 6.0  



This factor is used to defined the expansion of the coarse resolution grid in
the case of wavelets (seea [[usewvl]] ). The grid is made of points inside
spheres centered on atoms. The radius of these spheres are the product between
this factor and the covalent radius of element (read from the pseudo-potential
file).  
This factor is responsible for the amount of used memory (see also
[[wvl_hgrid]]).


* * *

## **wvl_frmult** 


*Mnemonics:* WaVeLet Fine grid Radius MULTiplier  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 10.0  



This factor is used to defined the expansion of the fine resolution grid in
the case of wavelets (see [[usewvl]] ). This fine resolution grid has the same
grid step than the coarse one (see [[wvl_crmult]] ), but on each point, 8
coefficients are stored instead of one, increasing the precision of the
calculation in this area. The grid is made of points inside spheres centered
on atoms. The radius of these spheres are the product between this factor and
a value read from the pseudo-potential file.  
This factor is responsible for the amount of used memory (see also
[[wvl_hgrid]]).


* * *

## **wvl_ngauss** 


*Mnemonics:* WaVeLet Number of GAUSSians  
*Variable type:* integer  
*Dimensions:* (2)  
*Default value:* [1, 100]  



In the wavelet-PAW computation case, projectors may be fitted to a sum of
complex Gaussians. The fit is done for wvl_ngauss(1), wvl_ngauss(1)+1 ... up
to wvl_ngauss(2) Gaussians.


* * *

## **wvl_nprccg** 


*Mnemonics:* WaVeLet maximum Number of PReConditionner Conjugate Gradient iterations  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 5  



In the wavelet computation case, the wavefunctions are directly minimised
using a real-space preconditionner. This preconditionner has internally some
conjugate gradient iterations. This value defines a boundary for the number of
conjugate gradient iterations on each wavefunction convergence step.


* * *

## **xredsph_extra** 


*Mnemonics:* X(position) in REDuced coordinates of the SPHeres for dos projection in the EXTRA set  
*Variable type:* real  
*Dimensions:* (3,[[natsph_extra]])  
*Default value:* *0.0  
*Only relevant if:* [[natsph_extra]] > 0  



The positions in reduced coordinates of extra spheres used in the DOS
projection, simulating an STS signal. See [[natsph_extra]] for a more complete
description.


* * *
