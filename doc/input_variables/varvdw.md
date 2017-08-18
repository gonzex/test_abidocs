## **irdvdw** 


*Mnemonics:* Integer that governs the ReaDing of _VDW files  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used when [[vdw_xc]]&gt;0, to read previously calculated vdW-DF variables.  
Supported values:

  * 0 =&gt; do not read vdW-DF variables 
  * 1 =&gt; read vdW-DF variables 


* * *

## **prtvdw** 


*Mnemonics:* PRinT Van Der Waals file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Print out a NetCDF file containing a vdW-DF kernel.


* * *

## **vdw_df_acutmin** 


*Mnemonics:* vdW-DF MINimum Angular CUT-off  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 10  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build angular meshes for the vdW-DF kernel.  


* * *

## **vdw_df_aratio** 


*Mnemonics:* vdW-DF Angle RATIO between the highest and
lowest angles.  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 30  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build angular meshes for the vdW-DF kernel.  


* * *

## **vdw_df_damax** 


*Mnemonics:* vdW-DF Delta for Angles, MAXimum   
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.5  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build angular meshes for the vdW-DF kernel.  


* * *

## **vdw_df_damin** 


*Mnemonics:* vdW-DF Delta for Angles, MINimum  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.01  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build angular meshes for the vdW-DF kernel.  


* * *

## **vdw_df_dcut** 


*Mnemonics:* vdW-DF D-mesh CUT-off  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 30  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_dratio** 


*Mnemonics:* vdW-DF, between the highest and
lowest D, RATIO.  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 20  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_dsoft** 


*Mnemonics:* vdW-DF Distance for SOFTening.  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.0  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_gcut** 


*Mnemonics:* vdW-DF G-space CUT-off  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 5  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to filter the vdW-DF kernel in reciprocal space.  


* * *

## **vdw_df_ndpts** 


*Mnemonics:* vdW-DF Number of D-mesh PoinTS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 20  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_ngpts** 


*Mnemonics:* vdW-DF Number of G-mesh PoinTS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* -1  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_nqpts** 


*Mnemonics:* vdW-DF Number of Q-mesh PoinTS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 30  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_nrpts** 


*Mnemonics:* vdW-DF Number of R-PoinTS  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2048  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to define the sampling of the vdW-DF-kernel in
real-space.  


* * *

## **vdw_df_nsmooth** 


*Mnemonics:* vdW-DF Number of SMOOTHening iterations  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 12  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to exponentially smoothen q near q0.  


* * *

## **vdw_df_phisoft** 


*Mnemonics:* vdW-DF PHI value SOFTening.  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* -1.0  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_qcut** 


*Mnemonics:* vdW-DF Q-mesh CUT-off  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 5  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_qratio** 


*Mnemonics:* vdW-DF, between highest and lowest Q, RATIO .  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 20  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, .  


* * *

## **vdw_df_rcut** 


*Mnemonics:* vdW-DF Real-space CUT-off  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 100  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to define the vdW-DF kernel cut-off radius.  


* * *

## **vdw_df_rsoft** 


*Mnemonics:* vdW-DF radius SOFTening.  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_threshold** 


*Mnemonics:* vdW-DF energy calculation THRESHOLD  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.01  
*Only relevant if:* [[vdw_xc]]>0  



Sets a threshold for the energy gradient that, when reached, will cause the
vdW-DF interactions to be calculated.  
Adjust it to a big value (e.g. 1e12) to enable it all along the SCF
calculation. Too small values, as well as negative values, will result in the
vdW-DF energy contributions never being calculated.


* * *

## **vdw_df_tolerance** 


*Mnemonics:* vdW-DF global TOLERANCE.  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1e-13  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  


* * *

## **vdw_df_tweaks** 


*Mnemonics:* vdW-DF TWEAKS.  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, to build the vdW-DF kernel.  
** _ IMPORTANT NOTE: modifying this variable will likely transform the calculated energies and their gradients into garbage. You have been warned! _ **   


* * *

## **vdw_df_zab** 


*Mnemonics:* vdW-DF ZAB parameter  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* -0.8491  
*Only relevant if:* [[vdw_xc]]>0  



Used when [[vdw_xc]]&gt;0, as introduced in [
doi:10.1103/PhysRevLett.92.246401
](http://dx.doi.org/10.1103/PhysRevLett.92.246401) .  


* * *

## **vdw_nfrag** 


*Mnemonics:* Van Der Waals Number of interacting FRAGments  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[vdw_xc]] in [10,11]  



The absolute value of vdw_nfrag is the number of vdW interacting fragments in
the unit cell. As wannierization takes place in reciprocal space, the MLWF
center positions could be translated by some lattice vector from the cell
where atoms are placed. If [[vdw_nfrag]] &gt;= 1 then MLWFs are translated to
the original unit cell, otherwise the program will keep the positions obtained
by Wannier90. The later is usually correct if some atoms are located at the
corners or at limiting faces of the unit cell.


* * *

## **vdw_supercell** 


*Mnemonics:* Van Der Waals correction from Wannier functions in SUPERCELL  
*Variable type:* integer  
*Dimensions:* (3)  
*Default value:* [0, 0, 0]  
*Only relevant if:* [[vdw_xc]] in [10,11]  



Set of dimensionless positive numbers which define the maximum multiples of
the primitive translations ([[rprimd]]) in the supercell construction. Each
component of vdw_supercell indicates the maximum number of cells along both
positive or negative directions of the corresponding primitive vector i.e. the
components of [[rprimd]]. In the case of layered systems for which vdW
interactions occur between layers made of tightly bound atoms, the evaluation
of vdW corrections coming from MLWFs in the same layer (fragment) must be
avoided. Both a negative or null value for one component of [[vdw_supercell]]
will indicate that the corresponding direction is normal to the layers.


* * *

## **vdw_tol** 


*Mnemonics:* Van Der Waals TOLerance  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1e-10  
*Only relevant if:* [[vdw_xc]]==5  



The DFT-D methods (S. Grimme approach) dispersion potentials, [[vdw_xc]]==5 or
6 or 7, include a pair potential. The number of pairs of atoms contributing to
the potential is necessarily limited. To be included in the potential a pair
of atom must have contribution to the energy larger than [[vdw_tol]].


* * *

## **vdw_tol_3bt** 


*Mnemonics:* Van Der Waals TOLerance for 3-Body Term  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* -1  
*Comment:* Do include the 3-body term in the correction  
*Only relevant if:* [[vdw_xc]] == 6  



Control the computation of the 3-body correction inside DFT-D3 dispersion
correction (Grimme approach) to the total energy:  
-If ** vdw_tol_3bt**&lt;0, no 3-body correction.   
-If ** vdw_tol_3bt**&gt;0, the 3-body term is included with a tolerance = **vdw_tol_3bt**   
  
DFT-D3 as proposed by S. Grimme adds two contributions to the total energy in
order to take into account of the dispersion:  

  * A pair-wise potential for which the tolerance is controlled by [[vdw_tol]] 
  

  * A 3-body term which is obtained by summing over all triplets of atoms. Each individual contribution depends of the distances and angles between the three atoms. As it is impossible to sum over all the triplets in a periodic system, one has to define a stopping criterium which is here that an additional contribution to the energy must be higher than **vdw_tol_3bt**

The last term has been predicted to have an important effect for large
molecules (see for e.g. _ Grimme S., J. Chem. Phys. 132, 154104 (2010) _). It
is however quite costly in computational time for periodic systems and seems
to lead to an overestimation of lattice parameters for weakly bound systems
(see for e.g. _ Reckien W., J. Chem. Phys. 132, 154104(2010) _). Still, its
contribution to energy, to forces and to stress is available (not planned for
elastic constants, dynamical matrix and internal strains)


* * *

## **vdw_typfrag** 


*Mnemonics:* Van Der Waals TYPe of FRAGment  
*Variable type:* integer  
*Dimensions:* ([[natom]])  
*Default value:* 1*[[natom]]  
*Only relevant if:* [[vdw_xc]] in [10,11]  



This array defines the interacting fragments by assigning to each atom an
integer index from 1 to ** vdw_nfrag ** . The ordering of [[vdw_typfrag]] is
the same as [[typat]] or [[xcart]]. Internally each MLWF is assigned to a
given fragment by computing the distance to the atoms. MLWFs belong to the
same fragment as their nearest atom. The resulting set of MLWFs in each
interacting fragment can be found in the output file in xyz format for easy
visualization.


* * *

## **vdw_xc** 


*Mnemonics:* Van Der Waals eXchange-Correlation functional  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Selects a van-der-Waals density functional to apply the corresponding
correction to the exchange-correlation energy. If set to zero, no correction
will be applied.  
Possible values are:

  * 0: no correction. 
  * 1: apply vdW-DF1 (DRSLL) from Dion _ et al. _   
_ doi:10.1103/PhysRevLett.92.246401 _

  * 2: apply vdw-DF2 (LMKLL) from Lee _ et al. _   
_ arXiv:1003.5255v1 _

  * 5: apply vdw-DFT-D2 as proposed by S. Grimme (adding a semi-empirical dispersion potential)   
Available only for ground-state calculations and response functions; see
[[vdw_tol]] variable to control convergency  
_ J. Comp. Chem. 27, 1787 (2006) _

  * 6: apply vdw-DFT-D3 as proposed by S. Grimme (refined version of DFT-D2)   
Available only for ground-state calculations and response functions; see
[[vdw_tol]] variable to control convergency and [[vdw_tol_3bt]] variable to
include 3-body corrections  
_ J. Chem. Phys. 132, 154104 (2010) _

  * 7: apply vdw-DFT-D3(BJ) as proposed by Grimme (based on Becke-Jonhson method J. Chem. Phys. 2004-2006)   
Available only for ground-state calculations and response functions; see
[[vdw_tol]] variable to control convergency  
_ J. Comput. Chem. 32, 1456 (2011) _

  * 10: evaluate the vdW correlation energy from maximally localized Wannier functions, as proposed by P. L. Silvestrelli, also known as vdW-WF1 method.   
_ doi:10.1103/PhysRevLett.100.053002. _ For details on this implementation
please check: _ doi:10.1016/j.cpc.2011.11.003 _  
The improvements introduced by Andrinopoulos _ et al. _ in _ J. Chem. Phys.
135, 154105 (2011) _ namely the amalgamation procedure, splitting of p-like
MLWFs into  
two s-like Wannier functions and fractional occupation of MLWFs are performed
automatically.  

  * 11: evaluate the vdW correlation energy from maximally localized Wannier functions, as proposed by A. Ambrosetti and P. L. Silvestrelli, also known as vdW-WF2 method.   
_ doi:10.1103/PhysRevB.85.073101 _

  * 14: apply DFT/vdW-QHO-WF method as proposed by Silvestrelli, which combines the quantum harmonic oscillator-model with localized Wannier functions.   
_ J. Chem. Phys. 139, 054106 (2013) _  
For periodic systems a supercell approach has to be used since **
vdw_supercell ** is not enabled in this case.

For [[vdw_xc]]=1 and [[vdw_xc]]=2, the implementation follows the strategy
devised in the article of Roman-Perez and Soler
([doi:10.1103/PhysRevLett.103.096102](https://dx.doi.org/10.1103/PhysRevLett.103.096102))


* * *
