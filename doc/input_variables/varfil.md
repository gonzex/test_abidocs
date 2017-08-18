## **get1den** 


*Mnemonics:* GET the first-order density from _1DEN file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Relevant only for non self consistent RF calculations (e.g. to get electron
phonon matrix elements) or for non linear RF calculations (to get mixed higher
order derivatives you need several perturbed densities and wave functions).
Indicate the files from which first-order densities must be obtained, in
multi-dataset mode (in single dataset mode, use [[ird1den]]).  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **get1wf** 


*Mnemonics:* GET the first-order wavefunctions from _1WF file   
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (in the multi-dataset mode), to indicate
starting wavefunctions, as an alternative to [[irdwfk]], [[irdwfq]],
[[ird1wf]], [[irdddk]]. One should first read the explanations given for these
latter variables.  
The ** getwfk ** , ** getwfq ** , [[get1wf]] and ** getddk ** variables are
typically used to chain the calculations in the multi-dataset mode, since they
describe from which dataset the OUTPUT wavefunctions are to be taken, as INPUT
wavefunctions of the present dataset.  
  
We now focus on the ** getwfk ** input variable (the only one used in ground-
state calculations), but the rules for ** getwfq ** and [[get1wf]] are
similar, with _WFK replaced by _WFQ or _1WF.  
If ** getwfk ** ==0, no use of previously computed output wavefunction file
appended with _DSx_WFK is done.  
If ** getwfk ** is positive, its value gives the index of the dataset for
which the output wavefunction file appended with _WFK must be used.  
If ** getwfk ** is -1, the output wf file with _WFK of the previous dataset
must be taken, which is a frequently occurring case.  
If ** getwfk ** is a negative number, it indicates the number of datasets to
go backward to find the needed wavefunction file. In this case, if one refers
to a non existent data set (prior to the first), the wavefunctions are not
initialised from a disk file, so that it is as if ** getwfk ** =0 for that
initialisation. Thanks to this rule, the use of ** getwfk ** -1 is rather
straightforward : except for the first wavefunctions, that are not initialized
by reading a disk file, the output wavefunction of one dataset is input of the
next one.  
In the case of a ddk calculation in a multi dataset run, in order to compute
correctly the localisation tensor, it is mandatory to declare give getddk the
value of the current dataset (i.e. getddk3 3 ) - this is a bit strange and
should be changed in the future.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getbscoup** 


*Mnemonics:* GET the Bethe-Salpeter COUPling block from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (multi-dataset mode) and, in the case of
a Bethe-Salpeter calculation to indicate that the starting coupling block of
the excitonic Hamiltonian will be taken from the output of a previous dataset.
It is used to chain the calculations, since it describes from which dataset
the OUTPUT coupling block is to be taken, as INPUT of the present dataset.  
If [[getbscoup]]==0, no such use of previously computed coupling block file is
done.  
If [[getbscoup]] is positive, its value gives the index of the dataset to be
used as input.  
If [[getbscoup]] is -1, the output of the previous dataset must be taken,
which is a frequently occuring case.  
If [[getbscoup]] is a negative number, it indicates the number of datasets to
go backward to find the needed file. In this case, if one refers to a non
existent data set (prior to the first), the coupling block is not initialised
from a disk file, so that it is as if [[getbscoup]]=0 for that initialisation.


* * *

## **getbseig** 


*Mnemonics:* GET the Bethe-Salpeter EIGenstates from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (multi-dataset mode) and, in the case of
a Bethe-Salpeter calculation to indicate that the starting excitonic
eigenstates are to be taken from the output of a previous dataset. It is used
to chain the calculations, since it describes from which dataset the OUTPUT
eigenstates are to be taken, as INPUT eigenstates of the present dataset.  
If [[getbseig]]==0, no such use of previously computed output eigenstates file
is done.  
If [[getbseig]] is positive, its value gives the index of the dataset from
which the output states is to be used as input.  
If [[getbseig]] is -1, the output eigenstates of the previous dataset must be
taken, which is a frequently occurring case.  
If [[getbseig]] is a negative number, it indicates the number of datasets to
go backward to find the needed file. In this case, if one refers to a non
existent data set (prior to the first), the eigenstates are not initialised
from a disk file, so that it is as if [[getbseig]]=0 for that initialisation.


* * *

## **getbsreso** 


*Mnemonics:* GET the Bethe-Salpeter RESOnant block from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (multi-dataset mode) and, in the case of
a Bethe-Salpeter calculation to indicate that the starting resonant block of
the excitonic Hamiltonian will be taken from the output of a previous dataset.
It is used to chain the calculations, since it describes from which dataset
the OUTPUT resonant block is to be taken, as INPUT of the present dataset.  
If [[getbsreso]]==0, no such use of previously computed resonant block file is
done.  
If [[getbsreso]] is positive, its value gives the index of the dataset to be
used as input.  
If [[getbsreso]] is -1, the output of the previous dataset must be taken,
which is a frequently occurring case.  
If [[getbsreso]] is a negative number, it indicates the number of datasets to
go backward to find the needed file. In this case, if one refers to a non
existent data set (prior to the first), the resonant block is not initialised
from a disk file, so that it is as if [[getbsreso]]=0 for that initialisation.


* * *

## **getddb** 


*Mnemonics:* GET the DDB from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



This variable should be used when performing electron-phonon or temperature-
dependence calculations. The Born effective charge as well as the dielectric
tensor will be read from a previous DFPT calculations of the electric field at
q=Gamma. The use of this variable will trigger the cancellation of a residual
dipole that leads to an unphysical divergence of the GKK with vanishing
q-points. The use of this variable greatly improves the k-point convergence
speed as the density of the k-point grid required to obtain the fulfillment of
the charge neutrality sum rule is usually prohibitively large.  
If [[getddb]]==0, no such use of previously computed Born effective charge and
dielectric tensor is done.  
If [[getddb]] is positive, its value gives the index of the dataset from which
the output density is to be used as input.  
If [[getddb]] is -1, the output density of the previous dataset must be taken,
which is a frequently occurring case.  
If [[getddb]] is a negative number, it indicates the number of datasets to go
backward to find the needed file.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getddk** 


*Mnemonics:* GET the DDK wavefunctions from _1WF file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (in the multi-dataset mode), to indicate
starting wavefunctions, as an alternative to
[[irdwfk]],[[irdwfq]],[[ird1wf]],[[irdddk]]. One should first read the
explanations given for these latter variables.  
The ** getwfk ** , ** getwfq ** , ** get1wf ** and [[getddk]] variables are
typically used to chain the calculations in the multi-dataset mode, since they
describe from which dataset the OUTPUT wavefunctions are to be taken, as INPUT
wavefunctions of the present dataset.  
  
We now focus on the ** getwfk ** input variable (the only one used in ground-
state calculations), but the rules for ** getwfq ** and ** get1wf ** are
similar, with _WFK replaced by _WFQ or _1WF.  
If ** getwfk ** ==0, no use of previously computed output wavefunction file
appended with _DSx_WFK is done.  
If ** getwfk ** is positive, its value gives the index of the dataset for
which the output wavefunction file appended with _WFK must be used.  
If ** getwfk ** is -1, the output wf file with _WFK of the previous dataset
must be taken, which is a frequently occurring case.  
If ** getwfk ** is a negative number, it indicates the number of datasets to
go backward to find the needed wavefunction file. In this case, if one refers
to a non existent data set (prior to the first), the wavefunctions are not
initialised from a disk file, so that it is as if ** getwfk ** =0 for that
initialisation. Thanks to this rule, the use of ** getwfk ** -1 is rather
straightforward : except for the first wavefunctions, that are not initialized
by reading a disk file, the output wavefunction of one dataset is input of the
next one.  
In the case of a ddk calculation in a multi dataset run, in order to compute
correctly the localisation tensor, it is mandatory to declare give getddk the
value of the current dataset (i.e. getddk3 3 ) - this is a bit strange and
should be changed in the future.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getden** 


*Mnemonics:* GET the DENsity from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (multi-dataset mode) and, in the case of
a ground-state calculation, if [[iscf]]&lt;0 (non-SCF calculation), to
indicate that the starting density is to be taken from the output of a
previous dataset. It is used to chain the calculations, since it describes
from which dataset the OUTPUT density are to be taken, as INPUT density of the
present dataset.  
If [[getden]]==0, no such use of previously computed output density file is
done.  
If [[getden]] is positive, its value gives the index of the dataset from which
the output density is to be used as input.  
If [[getden]] is -1, the output density of the previous dataset must be taken,
which is a frequently occurring case.  
If [[getden]] is a negative number, it indicates the number of datasets to go
backward to find the needed file. In this case, if one refers to a non
existent data set (prior to the first), the density is not initialised from a
disk file, so that it is as if [[getden]]=0 for that initialisation. Thanks to
this rule, the use of [[getden]] -1 is rather straightforward : except for the
first density, that is not initialized by reading a disk file, the output
density of one dataset is input of the next one.  
Be careful : the output density file of a run with non-zero [[ionmov]] does
not have the proper name (it has a "TIM" indication) for use as an input of an
[[iscf]]&lt;0 calculation.  
One should use the output density of a [[ionmov]]==0 run.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **gethaydock** 


*Mnemonics:* GET the HAYDOCK restart file from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (multi-dataset mode) and, in the case of
a Bethe-Salpeter calculation to indicate that the Haydock iterative technique
will be restarted from the output of a previous dataset.  
If [[gethaydock]]==0, no such use of previously computed coupling block file
is done.  
If [[gethaydock]] is positive, its value gives the index of the dataset to be
used as input.  
If [[gethaydock]] is -1, the output of the previous dataset must be taken,
which is a frequently occuring case.  
If [[gethaydock]] is a negative number, it indicates the number of datasets to
go backward to find the needed file. In this case, if one refers to a non
existent data set (prior to the first), the coupling block is not initialised
from a disk file, so that it is as if [[gethaydock]]=0 for that
initialisation.


* * *

## **getocc** 


*Mnemonics:* GET OCC parameters from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



This variable is typically used to chain the calculations, in the multi-
dataset mode ([[ndtset]]&gt;0), since it describes from which dataset the
array [[occ]] is to be taken, as input of the present dataset. The occupation
numbers are [[EVOLVING]] variables, for which such a chain of calculations is
useful.  
If [[getocc]]==0, no such use of previously computed output occupations is
done.  
If [[getocc]] is positive, its value gives the index of the dataset from which
the data are to be used as input data. It must be the index of a dataset
already computed in the SAME run.  
If [[getocc]] is -1, the output data of the previous dataset must be taken,
which is a frequently occurring case.  
If [[getocc]] is a negative number, it indicates the number of datasets to go
backward to find the needed data. In this case, if one refers to a non
existent data set (prior to the first), the date is not initialised from a
disk file, so that it is as if [[getocc]]==0 for that initialisation.  
NOTE that a non-zero [[getocc]] MUST be used with [[occopt]]==2, so that the
number of bands has to be initialized for each k point. Of course, these
numbers of bands must be identical to the numbers of bands of the dataset from
which [[occ]] will be copied. The same is true for the number of k points.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getqps** 


*Mnemonics:* GET QuasiParticle Structure  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used when [[ndtset]]&gt;0 (multi-dataset mode) and [[optdriver]]=3, or 4
(screening or sigma step of a [[GW]] calculation), to indicate that the
eigenvalues and possibly the wavefunctions have to be taken from a previous
quasiparticle calculation (instead of the usual LDA starting point). This is
to achieve quasiparticle self-consistency. See also [[irdqps]]  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getscr** 


*Mnemonics:* GET SCReening (the inverse dielectric matrix) from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used when [[ndtset]]&gt;0 (multi-dataset mode) and [[optdriver]]=4 (sigma step
of a [[GW]] calculation), to indicate that the dielectric matrix (_SCR file)
is to be taken from the output of a previous dataset. It is used to chain the
calculations, since it describes from which dataset the OUTPUT dielectric
matrix is to be taken, as INPUT of the present dataset.  
If [[getscr]]==0, no such use of previously computed output _SCR file is done.  
If [[getscr]] is positive, its value gives the index of the dataset from which
the output _SCR file is to be used as input.  
If [[getscr]] is -1, the output _SCR file of the previous dataset must be
taken, which is a frequently occurring case.  
If [[getscr]] is a negative number, it indicates the number of datasets to go
backward to find the needed file. In this case, if one refers to a non
existent data set (prior to the first), the _SCR file is not initialised from
a disk file, so that it is as if [[getscr]]=0 for that initialisation.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getsuscep** 


*Mnemonics:* GET SUSCEPtibility (the irreducible polarizability) from ...  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used when [[ndtset]]&gt;0 (multi-dataset mode) and [[optdriver]]=4 (sigma step
of a [[GW]] calculation), to indicate that the irreducible polarizability
(_SUSC file) is to be taken from the output of a previous dataset. It is used
to chain the calculations, since it describes from which dataset the OUTPUT
susceptibility is to be taken, as INPUT of the present dataset. Performing a
[[GW]] calculations starting from the _SUSC file instead of the _SCR file
presents the advantage that starting from the irreducible polarizability, one
can calculate the screened interaction using different expressions without
having to perform a screening calculation from scratch. For example, it is
possible to apply a cutoff to the Coulomb interaction in order to facilitate
the convergence of the [[GW]] correction with respect to the size of the
supercell (see [[vcutgeo]] and [[icutcoul]])  
If [[getsuscep]]==0, no such use of previously computed output _SUSC file is
done.  
If [[getsuscep]] is positive, its value gives the index of the dataset from
which the output _SUSC file is to be used as input.  
If [[getsuscep]] is -1, the output _SUSC file of the previous dataset must be
taken, which is a frequently occurring case.  
If [[getsuscep]] is a negative number, it indicates the number of datasets to
go backward to find the needed file. In this case, if one refers to a non
existent data set (prior to the first), the _SUSC file is not initialised from
a disk file, so that it is as if [[getsuscep]]=0 for that initialisation.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getwfk** 


*Mnemonics:* GET the wavefunctions from _WFK file   
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (in the multi-dataset mode), to indicate
starting wavefunctions, as an alternative to [[irdwfk]],[[irdwfq]],[[ird1wf]],
or [[irdddk]]. One should first read the explanations given for these latter
variables.  
The [[getwfk]], ** getwfq ** , ** get1wf ** and ** getddk ** variables are
typically used to chain the calculations in the multi-dataset mode, since they
describe from which dataset the OUTPUT wavefunctions are to be taken, as INPUT
wavefunctions of the present dataset.  
  
We now focus on the [[getwfk]] input variable (the only one used in ground-
state calculations), but the rules for ** getwfq ** and ** get1wf ** are
similar, with _WFK replaced by _WFQ or _1WF.  
If [[getwfk]]==0, no use of previously computed output wavefunction file
appended with _DSx_WFK is done.  
If [[getwfk]] is positive, its value gives the index of the dataset for which
the output wavefunction file appended with _WFK must be used.  
If [[getwfk]] is -1, the output wf file with _WFK of the previous dataset must
be taken, which is a frequently occurring case.  
If [[getwfk]] is a negative number, it indicates the number of datasets to go
backward to find the needed wavefunction file. In this case, if one refers to
a non existent data set (prior to the first), the wavefunctions are not
initialised from a disk file, so that it is as if [[getwfk]]=0 for that
initialisation. Thanks to this rule, the use of [[getwfk]] -1 is rather
straightforward : except for the first wavefunctions, that are not initialized
by reading a disk file, the output wavefunction of one dataset is input of the
next one.  
In the case of a ddk calculation in a multi dataset run, in order to compute
correctly the localisation tensor, it is mandatory to declare give getddk the
value of the current dataset (i.e. getddk3 3 ) - this is a bit strange and
should be changed in the future.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **getwfq** 


*Mnemonics:* GET the wavefunctions from _WFQ file   
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Eventually used when [[ndtset]]&gt;0 (in the multi-dataset mode), to indicate
starting wavefunctions, as an alternative to [[irdwfk]],[[irdwfq]],[[ird1wf]]
or [[irdddk]]. One should first read the explanations given for these latter
variables.  
The ** getwfk ** , [[getwfq]], ** get1wf ** and ** getddk ** variables are
typically used to chain the calculations in the multi-dataset mode, since they
describe from which dataset the OUTPUT wavefunctions are to be taken, as INPUT
wavefunctions of the present dataset.  
  
We now focus on the ** getwfk ** input variable (the only one used in ground-
state calculations), but the rules for [[getwfq]] and ** get1wf ** are
similar, with _WFK replaced by _WFQ or _1WF.  
If ** getwfk ** ==0, no use of previously computed output wavefunction file
appended with _DSx_WFK is done.  
If ** getwfk ** is positive, its value gives the index of the dataset for
which the output wavefunction file appended with _WFK must be used.  
If ** getwfk ** is -1, the output wf file with _WFK of the previous dataset
must be taken, which is a frequently occurring case.  
If ** getwfk ** is a negative number, it indicates the number of datasets to
go backward to find the needed wavefunction file. In this case, if one refers
to a non existent data set (prior to the first), the wavefunctions are not
initialised from a disk file, so that it is as if ** getwfk ** =0 for that
initialisation. Thanks to this rule, the use of ** getwfk ** -1 is rather
straightforward : except for the first wavefunctions, that are not initialized
by reading a disk file, the output wavefunction of one dataset is input of the
next one.  
In the case of a ddk calculation in a multi dataset run, in order to compute
correctly the localisation tensor, it is mandatory to declare give getddk the
value of the current dataset (i.e. getddk3 3 ) - this is a bit strange and
should be changed in the future.  
NOTE : a negative value of a "get" variable indicates the number of datasets
to go backwards; it is not the number to be subtracted from the current
dataset to find the proper dataset. As an example :

    
    
      ndtset 3   jdtset 1 2 4  getXXX -1
     

refers to dataset 2 when dataset 4 is initialized.


* * *

## **ird1den** 


*Mnemonics:* Integer that governs the ReaDing of 1st-order DEN file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[iscf]] < 0,
0 otherwise.
  



If first order density is needed in single dataset mode (for example in
nonlinear optical response), use [[ird1den]]=1 to read first-order densities
from _DENx files produced in other calculations. In multi-dataset mode use
[[get1den]].

When iscf &lt; 0, the reading of a DEN file is always enforced.

A non-zero value of ** ird1den ** is treated in the same way as other "ird"
variables, see the [ section 4
](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]].  


* * *

## **ird1wf** 


*Mnemonics:* Integer that governs the ReaDing of _1WF files   
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Indicates eventual starting wavefunctions. As alternative, one can use the
input variables [[getwfk]], [[getwfq]], [[get1wf]] or [[getddk]].  
  
Ground-state calculation :

  * only ** irdwfk ** and [[getwfk]] have a meaning 
  * at most one of ** irdwfk ** or [[getwfk]] can be non-zero 
  * if ** irdwfk ** and [[getwfk]] are both zero, initialize wavefunctions with random numbers for ground state calculation. 
  * if ** irdwfk ** = 1 : read ground state wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 

Response-function calculation :

  * one and only one of ** irdwfk ** or [[getwfk]] MUST be non-zero 
  * if ** irdwfk ** = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * only one of ** irdwfq ** or [[getwfq]] can be non-zero, if both of them are non-zero, use as k + q file the one defined by ** irdwfk ** and/or [[getwfk]] 
  * if ** irdwfq ** = 1 : read ground state k+q -wavefunctions from a disk file appended with _WFQ , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of [[ird1wf]] or [[get1wf]] can be non-zero 
  * if both are zero, initialize first order wavefunctions to zeroes 
  * if [[ird1wf]] = 1 : read first-order wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of ** irdddk ** or [[getddk]] can be non-zero 
  * one of them must be non-zero if an homogeneous electric field calculation is done (presently, a ddk calculation in the same dataset is not allowed) 
  * if ** irdddk ** = 1 : read first-order ddk wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 


* * *

## **irdbscoup** 


*Mnemonics:* Integer that governs the ReaDing of COUPling block  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Start the Bethe-Salpeter calculation from the BSC file containing the coupling
block produced in a previous run.


* * *

## **irdbseig** 


*Mnemonics:* Integer that governs the ReaDing of BS_EIG file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Start the Bethe-Salpeter calculation from the BS_EIG contining the exciton
eigenvectors produced in a previous run.


* * *

## **irdbsreso** 


*Mnemonics:* Integer that governs the ReaDing of RESOnant block  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Start the Bethe-Salpeter calculation from the BSR file containing the resonat
block produced in a previous run.


* * *

## **irdddb** 


*Mnemonics:* Integer that governs the ReaDing of DDB file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[iscf]] < 0,
0 otherwise.
  



This variable should be used when performing electron-phonon or temperature-
dependence calculations. The Born effective charge as well as the dielectric
tensor will be read from a previous DFPT calculations of the electric field at
q=Gamma. The use of this variable will trigger the cancellation of a residual
dipole that leads to an unphysical divergence of the GKK with vanishing
q-points. The use of this variable greatly improves the k-point convergence
speed as the density of the k-point grid required to obtain the fulfillment of
the charge neutrality sum rule is usually prohibitively large.

A non-zero value of [[irdddb]] is treated in the same way as other "ird"
variables, see the [ section 4
](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]].  
  


* * *

## **irdddk** 


*Mnemonics:* Integer that governs the ReaDing of DDK wavefunctions, in _1WF files  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Indicates eventual starting wavefunctions. As alternative, one can use the
input variables [[getwfk]], [[getwfq]], [[get1wf]] or [[getddk]].  
  
Ground-state calculation :

  * only ** irdwfk ** and [[getwfk]] have a meaning 
  * at most one of ** irdwfk ** or [[getwfk]] can be non-zero 
  * if ** irdwfk ** and [[getwfk]] are both zero, initialize wavefunctions with random numbers for ground state calculation. 
  * if ** irdwfk ** = 1 : read ground state wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 

Response-function calculation :

  * one and only one of ** irdwfk ** or [[getwfk]] MUST be non-zero 
  * if ** irdwfk ** = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * only one of ** irdwfq ** or [[getwfq]] can be non-zero, if both of them are non-zero, use as k + q file the one defined by ** irdwfk ** and/or [[getwfk]] 
  * if ** irdwfq ** = 1 : read ground state k+q -wavefunctions from a disk file appended with _WFQ , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of ** ird1wf ** or [[get1wf]] can be non-zero 
  * if both are zero, initialize first order wavefunctions to zeroes 
  * if ** ird1wf ** = 1 : read first-order wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of [[irdddk]] or [[getddk]] can be non-zero 
  * one of them must be non-zero if an homogeneous electric field calculation is done (presently, a ddk calculation in the same dataset is not allowed) 
  * if [[irdddk]] = 1 : read first-order ddk wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 


* * *

## **irdden** 


*Mnemonics:* Integer that governs the ReaDing of DEN file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[iscf]] < 0,
0 otherwise.
  



Start the ground-state calculation from the density file of a previous run.
When iscf &lt; 0, the reading of a DEN file is always enforced.

A non-zero value of [[irdden]] is treated in the same way as other "ird"
variables, see the [ section 4
](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]].  
  


* * *

## **irdhaydock** 


*Mnemonics:* Integer that governs the ReaDing of the HAYDOCK restart file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Used to re-start the Haydock iterative technique from the HAYDR_SAVE file
produced in a previous run.


* * *

## **irdqps** 


*Mnemonics:* Integer that governs the ReaDing of QuasiParticle Structure  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Relevant only when [[optdriver]]=3 or 4. Indicate the file from which the
eigenvalues and possibly the wavefunctions must be obtained, in order to
achieve a self-consistent quasiparticle calculations. See also [[getqps]]


* * *

## **irdscr** 


*Mnemonics:* Integer that governs the ReaDing of the SCReening  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Relevant only when [[optdriver]]=4. Indicate the file from which the
dielectric matrix must be obtained. As alternative, one can use the input
variable [[getscr]].  
When [[optdriver]]=4, at least one of [[irdscr]] or [[getscr]] (alternatively,
[[irdsuscep]] or [[getsuscep]]) must be non-zero.

A non-zero value of [[irdscr]] is treated in the same way as other "ird"
variables, see the [ section 4
](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]].


* * *

## **irdsuscep** 


*Mnemonics:* Integer that governs the ReaDing of the SUSCEPtibility  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Relevant only when [[optdriver]]=4. Indicate the file from which the
irreducible polarizability must be obtained. As alternative, one can use the
input variable [[getsuscep]].  
When [[optdriver]]=4, at least one of [[irdsuscep]] or [[getsuscep]]
(alternatively, [[irdscr]] or [[getscr]]) must be non-zero.

A non-zero value of [[irdsuscep]] is treated in the same way as other "ird"
variables, see the [ section 4
](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]].


* * *

## **irdwfk** 


*Mnemonics:* Integer that governs the ReaDing of _WFK files  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Indicates eventual starting wavefunctions. As alternative, one can use the
input variables [[getwfk]], [[getwfq]], [[get1wf]] or [[getddk]].  
  
Ground-state calculation :

  * only [[irdwfk]] and [[getwfk]] have a meaning 
  * at most one of [[irdwfk]] or [[getwfk]] can be non-zero 
  * if [[irdwfk]] and [[getwfk]] are both zero, initialize wavefunctions with random numbers for ground state calculation. 
  * if [[irdwfk]] = 1 : read ground state wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 

Response-function calculation :

  * one and only one of [[irdwfk]] or [[getwfk]] MUST be non-zero 
  * if [[irdwfk]] = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * only one of ** irdwfq ** or [[getwfq]] can be non-zero, if both of them are non-zero, use as k + q file the one defined by [[irdwfk]] and/or [[getwfk]] 
  * if ** irdwfq ** = 1 : read ground state k+q -wavefunctions from a disk file appended with _WFQ , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of ** ird1wf ** or [[get1wf]] can be non-zero 
  * if both are zero, initialize first order wavefunctions to 0's. 
  * if ** ird1wf ** = 1 : read first-order wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of ** irdddk ** or [[getddk]] can be non-zero 
  * one of them must be non-zero if an homogeneous electric field calculation is done (presently, a ddk calculation in the same dataset is not allowed) 
  * if ** irdddk ** = 1 : read first-order ddk wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 


* * *

## **irdwfq** 


*Mnemonics:* Integer that governs the ReaDing of _WFQ files  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Indicates eventual starting wavefunctions. As alternative, one can use the
input variables [[getwfk]], [[getwfq]], [[get1wf]] or [[getddk]].  
  
Ground-state calculation :

  * only ** irdwfk ** and [[getwfk]] have a meaning 
  * at most one of ** irdwfk ** or [[getwfk]] can be non-zero 
  * if ** irdwfk ** and [[getwfk]] are both zero, initialize wavefunctions with random numbers for ground state calculation. 
  * if ** irdwfk ** = 1 : read ground state wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 

Response-function calculation :

  * one and only one of ** irdwfk ** or [[getwfk]] MUST be non-zero 
  * if ** irdwfk ** = 1 : read ground state k -wavefunctions from a disk file appended with _WFK , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * only one of [[irdwfq]] or [[getwfq]] can be non-zero, if both of them are non-zero, use as k + q file the one defined by ** irdwfk ** and/or [[getwfk]] 
  * if [[irdwfq]] = 1 : read ground state k+q -wavefunctions from a disk file appended with _WFQ , produced in a previous ground state calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of ** ird1wf ** or [[get1wf]] can be non-zero 
  * if both are zero, initialize first order wavefunctions to 0's. 
  * if ** ird1wf ** = 1 : read first-order wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 
  * at most one of ** irdddk ** or [[getddk]] can be non-zero 
  * one of them must be non-zero if an homogeneous electric field calculation is done (presently, a ddk calculation in the same dataset is not allowed) 
  * if ** irdddk ** = 1 : read first-order ddk wavefunctions from a disk file appended with _1WFx , produced in a previous response function calculation (see the [ section 4 ](../../users/generated_files/help_abinit.html#4) of the [[help_abinit]]). 


* * *

## **kssform** 


*Mnemonics:* Kohn Sham Structure file FORMat  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  



Governs the choice of the format for the file that contains the Kohn-Sham
electronic structure information, for use in [[GW]] calculations, see the
input variables [[optdriver]] and [[nbandkss]].

  * [[kssform]]=1, a single file .kss (double precision) containing complete information on the Kohn Sham Structure (eigenstates and the pseudopotentials used) will be generated through full diagonalization of the complete Hamiltonian matrix. The file has at the beginning the standard abinit header. 
  * [[kssform]]=3, a single file .kss (double precision) containing complete information on the Kohn Sham Structure (eigenstates and the pseudopotentials used) will be generated through the usual conjugate gradient algorithm (so, a restricted number of states). The file has at the beginning the standard abinit header. 

Very important : for the time being, [[istwfk]] must be 1 for all the
k-points.


* * *

## **prt1dm** 


*Mnemonics:* PRinT 1-DiMensional potential and density  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set &gt;= 1, provide one-dimensional projection of potential and density,
for each of the three axis. This corresponds to averaging the potential or the
density on bi-dimensional slices of the FFT grid.


* * *

## **prtden** 


*Mnemonics:* PRinT the DENsity  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0 if [[nimage]]>1,
1 otherwise.
  



If set to 1 or a larger value , provide output of electron density in real
space rho(r), in units of electrons/Bohr^3.  
If [[ionmov]]==0, the name of the density file will be the root output name,
followed by _DEN .  
If [[ionmov]]==1 or 2, density files will be output at each time step, with
the name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _DEN 

The file structure of the unformatted output file is described below, see
section 6).  
If [[prtden]] is lower than 0, two files will be printed for restart every
[[prtden]] step, with the names being made of

  * the root temporary name, 
  * followed by _DEN_x , where x is 0000 or 0001 alternatively. 
  * The most recent of the two files should be used for restart, and copied to root input name_DS2_DEN 
  * To perform a restart, in a multidataset mode, use ndtset 2 and jdtset 2 3 (that is 2 datasets, numbered 2 and 3) 
  * In the dataset 2, get the density you just copied (getden2 -1), perform a non selfconsistent calculation and print the wave function (prtwf2 1) 
  * In the dataset 3, get the previous wf(getwfk3 -1), and continue the calculation 
  * This complicated procedure is due to the fact that reading the density is only allowed for a non sc calculation, and also for a dataset different of 0 or the previous one, the option we choose here. 

Please note that in the case of PAW ([[usepaw]]=1) calculations, the _DEN
density output is not the full physical electron density. If what is wanted is
the full physical electron density, say for post-processing with [ AIM
](../../users/generated_files/help_aim.html) or visualization, prtden &gt; 1
will produce physical electron density or other interesting quantities (see
below). Nevertheless, even in the PAW case, when chaining together
calculations where the density from one calculation is to be used in a
subsequent calculation, it is necessary to use the _DEN files and ** not **
one of the other files produced with prtden &gt; 1, i.e. _PAWDEN, ATMDEN_xxx
or else. Note that the usual _DEN file is always generated as soon as prtden
&gt;= 1. Options 2 to 6 for prtden are relevant only for [[usepaw]]=1 and
control the output of the full electron density in the PAW case :  
  

** prtden=2 ** causes generation of a file _PAWDEN that contains the bulk ** valence ** charge density together with the PAW on-site contributions, and has the same format as the other density files.   
** prtden=3 ** causes generation of a file _PAWDEN that contains the bulk ** full ** charge density (valence+core)   
** prtden=4 ** causes generation of three files _ATMDEN_CORE, _ATMDEN_VAL and _ATMDEN_FULL which respectively contain the core, valence and full atomic protodensity (the density of the individual component atoms in vacuum superposed at the bulk atomic positions). This can be used to generate various visualizations of the bonding density.   
** prtden=5 ** options 2 and 4 taken together.   
** prtden=6 ** options 3 and 4 taken together.   
** prtden=7 ** causes the generation of all the individual contributions to the bulk ** valence ** charge density : n_tilde-n_hat (_N_TILDE), n_onsite (_N_ONE) and n_tilde_onsite (_NT_ONE). This is for diagnosis purposes only.   

  
Options 3 to 6 currently require the user to supply the atomic core and
valence density in external files in the working directory. The files must be
named properly; for example, the files for an atom of type 1 should be named:
"core_density_atom_type1.dat" and "valence_density_atom_type1.dat". The file
should be a text file, where the first line is assumed to be a comment, and
the subsequent lines contain two values each, where the first one is a radial
coordinate and the second the value of the density n(r). Please note that it
is n(r) which should be supplied, ** not ** n(r)/r^2. The first coordinate
point must be the origin, i.e. ** _ r = 0 _ ** . The atomic densities are
spherically averaged, so assumed to be completely spherically symmetric, even
for open shells.  
  
NOTE: in the PAW case, ** DO NOT ** use _PAWDEN or _ATMDEN_xxx files produced
by prtden &gt; 1 to chain the density output from one calculation as the input
to another, use the _DEN file for that.


* * *

## **prtdos** 


*Mnemonics:* PRinT the Density Of States  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Provide output of Density of States if set to 1, 2 or 3. Can either use a
smearing technique ([[prtdos]]=1), or the tetrahedron method ([[prtdos]]=2).
If [[prtdos]]=3, provide output of Local Density of States inside a sphere
centered on an atom, as well as the angular-momentum projected DOS, in the
same sphere. The resolution of the linear grid of energies for which the DOS
is computed can be tuned thanks to [[dosdeltae]].

If [[prtdos]]=1, the smeared density of states is obtained from the
eigenvalues, properly weighted at each k point using [[wtk]], and smeared
according to [[occopt]] and [[tsmear]]. All levels that are present in the
calculation are taken into account (occupied and unoccupied). Note that
[[occopt]] must be between 3 and 7 . Also note that the sampling of the
Brillouin Zone that is needed to get a converged DOS is usually much finer
than the sampling needed to converge the total energy or the geometry of the
system, unless [[tsmear]] is very large (hence the DOS is not obtained
properly).. A separate convergence study is needed.  
In order to compute the DOS of an insulator with [[prtdos]]=1, compute its
density thanks to a self-consistent calculation (with a non-metallic
[[occopt]] value, 0, 1 or 2), then use [[prtdos]]=1, together with
[[iscf]]=-3, and a metallic [[occopt]], between 3 and 7, providing the needed
smearing. If [[prtdos]]=1, the name of the DOS file is the root name for the
output files, followed by "_DOS" .

If [[prtdos]]=2, the DOS is computed using the tetrahedron method. As in the
case of [[prtdos]]=1, all levels that are present in the calculation are taken
into account (occupied and unoccupied). In this case, the k-points must have
been defined using the input variable [[ngkpt]] or the input variable
[[kptrlatt]]. There must be at least two non-equivalent points in the
Irreducible Brillouin Zone to use [[prtdos]]=2. It is strongly advised to use
a non-shifted k-point grid ([[shiftk]] 0 0 0): such grids contain naturally
more extremal points (band minima and maxima at Gamma or at the zone-
boundaries) than shifted grids, and lead to more non-equivalent points than
shifted grids, for the same grid spacing. There is no need to take care of the
[[occopt]] or [[tsmear]] input variables, and there is no subtlety to be taken
into account for insulators. The computation can be done in the self-
consistent case as well as in the non-self-consistent case, using [[iscf]]=-3.
This allows to refine the DOS at fixed starting density.  
In that case, if [[ionmov]]==0, the name of the potential file will be the
root output name, followed by _DOS (like in the [[prtdos]]=1 case).  
However, if [[ionmov]]==1 or 2, potential files will be output at each time
step, with the name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _DOS. 

If [[prtdos]]=3, the same tetrahedron method as for [[prtdos]]=2 is used, but
the DOS inside a sphere centered on some atom is delivered, as well as the
angular-momentum projected (l=0,1,2,3,4) DOS in the same sphere. The
preparation of this case, the parameters under which the computation is to be
done, and the file denomination is similar to the [[prtdos]]=2 case. However,
three additional input variables might be provided, describing the atoms that
are the center of the sphere (input variables [[natsph]] and [[iatsph]]), as
well as the radius of this sphere (input variable [[ratsph]]).  
In case of PAW, [[ratsph]] radius has to be greater or equal to largest PAW
radius of the atom types considered (which is read from the PAW atomic data
file; see rc_sph or r_paw). Additional printing and/or approximations in PAW
mode can be controlled with [[pawprtdos]] keyword (in
particular,[[pawprtdos]]=2 can be used to compute quickly a very good
approximation of the DOS).  
  
Note 1: when [[prtdos]]=3, it is possible to output m-decomposed LDOS in _DOS
file; simply use [[prtdosm]] keyword.  
Note 2: the integrated total DOS in spheres around atoms can be obtained when
[[prtdensph]] flag is activated. It can be compared to the integrated DOS
provided in _DOS file when [[prtdos]]=3.

[[prtdos]]=4 delivers the sphere-projected DOS (like [[prtdos]]=3), on the
basis of a smearing approach (like [[prtdos]]=1)

[[prtdos]]=5 delivers the spin-spin DOS in the [[nspinor]]==2 case, using the
tetrahedron method (as [[prtdos]]=2).


* * *

## **prtdosm** 


*Mnemonics:* PRinT the Density Of States with M decomposition  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Relevant only when [[prtdos]]=3.  
If set to 1, the m-decomposed LDOS is delivered in DOS file.  
Note that [[prtdosm]] computes the M-resolved partial dos for complex
spherical harmonics,giving e.g. DOS(L,M) == DOS(L,-M) (without spin-orbit). In
the contrary, the LDA+U occupation matrix, see [[dmatpawu]] is in the real
spherical harmonics basis.  
If set to 2, the m-decomposed LDOS is delivered in DOS file.  
In this case, [[prtdosm]] computes the M-resolved partial dos for real
spherical harmonics in the same basis as the LDA+U occupation matrix.


* * *

## **prteig** 


*Mnemonics:* PRinT EIGenenergies  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0 if [[nimage]] > 1,
1 otherwise.
  



If set to 1, a file *_EIG, containing the k-points and one-electron
eigenvalues is printed.


* * *

## **prtelf** 


*Mnemonics:* PRinT Electron Localization Function (ELF)  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1 or a larger value, provide output of ELF in real space elf(r).
This is a dimensionless quantity bounded between 0 and 1.  
The name of the ELF file will be the root output name, followed by _ELF.  
Like a _DEN file, it can be analyzed by cut3d. However unlike densities, in
case of spin polarized calculations, the spin down component can not be
obtained by subtracting the spin up component to the total ELF. Hence when
spin polarized calculations are performed the code produces also output files
with _ELF_UP and _ELF_DOWN extensions. (For technical reasons these files
contain also two components but the second is zero. So to perform analysis of
_ELF_UP and _ELF_DOWN files with cut3d you have to answer "ispden= 0 ==&gt;
Total density" when cut3d ask you which ispden to choose. Also remember that
spin down component can not be obtained by using cut3d on the _ELF file. Sorry
for the inconvenience, this will be fixed in the next release.)  
ELF is not yet implemented in non collinear spin case.  
If prtelf is set to 2, in the case of spin polarized calculation, the total
ELF is computed from an alternative approach which should better take into
account the existence of spin dependent densities (see the documentation in
/doc/theory/ELF of your ABINIT repository)  
  
Please note that ELF is ** not ** yet implemented in the case of PAW
([[usepaw]]=1) calculations.


* * *

## **prtfsurf** 


*Mnemonics:* PRinT Fermi SURFace file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1, provide Fermi surface file in the BXSF format (Xcrysden) If
[[prtfsurf]]=1, a _BXSF file readable by [ XCrySDen ](http://www.xcrysden.org)
will be produced at the end of the calculation. The file contains information
on the band structure of the system and can be used to visualize the Fermi
surface or any other energy isosurface. [[prtfsurf]]=1 is compatible only with
SCF calculations ([[iscf]] &gt; 1) or NSCF runs in which the occupation
factors and Fermi level are recalculated once convergence is achieved
([[iscf]] = -3). The two methods should produce the same Fermi surface
provided that the k-meshes are sufficiently dense. The k-mesh used for the
sampling of the Fermi surface can be specified using the standard variables
[[ngkpt]], ([[shiftk]], and [[nshiftk]]. Note, however, that the mesh must be
homogeneous and centered on gamma (multiple shifts are not supported by
Xcrysden)


* * *

## **prtgden** 


*Mnemonics:* PRinT the Gradient of electron DENsity  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1 or a larger value, provide output of gradient of electron density
in real space grho(r), in units of Bohr^-(5/2).  
The names of the gradient of electron density files will be the root output
name, followed by _GDEN1, _GDEN2, GDEN3 for each principal direction (indeed
it is a vector).  
Like a _DEN file, it can be analyzed by cut3d. The file structure of the
unformatted output file is described below, see section 6).


* * *

## **prtgeo** 


*Mnemonics:* PRinT the GEOmetry analysis  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1 or a larger value, provide output of geometrical analysis (bond
lengths and bond angles). The value of [[prtgeo]] is taken by the code to be
the maximum coordination number of atoms in the system.  
It will deduce a maximum number of "nearest" and "next-nearest" neighbors
accordingly , and compute corresponding bond lengths.  
It will compute bond angles for the "nearest" neighbours only.  
If [[ionmov]]==0, the name of the file will be the root output name, followed
by _GEO .  
If [[ionmov]]==1 or 2, one file will be output at each time step, with the
name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _GEO 

The content of the file should be rather self-explanatory.  
No output is provided by [[prtgeo]] is lower than or equal to 0.  
If [[prtgeo]]&gt;0, the maximum number of atoms ([[natom]]) is 9999.


* * *

## **prtgkk** 


*Mnemonics:* PRinT the GKK matrix elements file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1, provide output of electron-phonon "gkk" matrix elements, for
further treatment by mrggkk utility or anaddb utility. Note that symmetry will
be disabled for the calculation of the perturbation, forcing the inclusion of
all k-points and all perturbation directions. Additional information on
electron-phonon treatment in ABINIT is given in the tutorial
~abinit/doc/tutorial/lesson_eph.html and in ~abinit/doc/users/elphon_manual.ps


* * *

## **prtgsr** 


*Mnemonics:* PRinT the GSR file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* prtgsr = 0  



If set to 1, ABINIT will produce a GSR file at the end of the GS calculation.
The GSR file contains the most important GS results (band structure, forces,
stresses, electronic density). The GSR file can be read by AbiPy and used for
futher postprocessing.  
Note that, by default, the GSR file contains the electronic density unless
[[prtden]] is set to 0.


* * *

## **prtkden** 


*Mnemonics:* PRinT the Kinetic energy DENsity  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1 or a larger value , provide output of kinetic energy density in
real space tau(r), in units of Bohr^-5.  
The name of the kinetic energy density file will be the root output name,
followed by _KDEN.  
Like a _DEN file, it can be analyzed by cut3d. The file structure of the
unformatted output file is described below (see [ section 6
](../../users/generated_files/help_abinit.html#6)).  
Note that the computation of the kinetic energy density must be activate,
thanks to the input variable [[usekden]].  
Please note that kinetic energy density is ** not ** yet implemented in the
case of PAW ([[usepaw]]=1) calculations.


* * *

## **prtkpt** 


*Mnemonics:* PRinT the K-PoinTs sets  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set /= 0 , proceeds to a detailed analysis of different k point grids.
Works only if [[kptopt]] is positive, and neither [[kptrlatt]] nor [[ngkpt]]
are defined. ABINIT will stop after this analysis.

Different sets of k point grids are defined, with common values of [[shiftk]].
In each set, ABINIT increases the length of vectors of the supercell (see
[[kptrlatt]]) by integer steps. The different sets are labelled by "iset". For
each k point grid, [[kptrlen]] and [[nkpt]] are computed (the latter always
invoking [[kptopt]]=1, that is, full use of symmetries). A series is finished
when the computed [[kptrlen]] is twice larger than the input variable
[[kptrlen]]. After the examination of the different sets, ABINIT summarizes,
for each [[nkpt]], the best possible grid, that is, the one with the largest
computed [[kptrlen]].

Note that this analysis is also performed when [[prtkpt]]=0, as soon as
neither [[kptrlatt]] nor [[ngkpt]] are defined. But, in this case, no analysis
report is given, and the code selects the grid with the smaller [[ngkpt]] for
the desired [[kptrlen]]. However, this analysis takes some times (well
sometimes, it is only a few seconds - it depends on the value of the input
[[kptrlen]]), and it is better to examine the full analysis for a given cell
and set of symmetries, [[shiftk]] for all the production runs.

if set to -2, the code stops in invars1 after the computation of the
irreducible set and a file named kpts.nc with the list of the k-points and the
corresponding weights is produced


* * *

## **prtlden** 


*Mnemonics:* PRinT the Laplacian of electron DENsity  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1 or a larger value, provide output of Laplacian of electron density
in real space grho(r), in units of Bohr^-(7/2).  
The name of the Laplacian of electron density file will be the root output
name, followed by _LDEN.  
Like a _DEN file, it can be analyzed by cut3d. The file structure of the
unformatted output file is described below (see [ section 6
](../../users/generated_files/help_abinit.html#6)).


* * *

## **prtpot** 


*Mnemonics:* PRinT total POTential  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set &gt;=1 , provide output of the total (Kohn-Sham) potential (sum of
local pseudo-potential, Hartree potential, and xc potential).

If [[ionmov]]==0, the name of the potential file will be the root output name,
followed by _POT.  
If [[ionmov]]==1 or 2, potential file will be output at each time step, with
the name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _POT. 

The file structure of this unformatted output file is described in [ section
6.6 ](../../users/generated_files/help_abinit.html#localpotfile) of the
[[help_abinit]]. No output is provided by a negative value of this variable.


* * *

## **prtpsps** 


*Mnemonics:* PRint the PSPS file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1, the code produces a netcdf file (PSPS.nc) with the internal
tables used by Abinit to apply the pseudopotential part of the KS Hamiltonian.
The data can be visualized with AbiPy. if prtpsps is set to -1, the code will
exit after the output of the PSPS.nc file.


* * *

## **prtspcur** 


*Mnemonics:* PRinT the SPin CURrent density  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1 or a larger value, provide output of the current density of
different direction spins (x,y,z) in the whole unit cell. Should require
spinorial wave functions [[nspinor]] = 2. Experimental: this does not work
yet.


* * *

## **prtstm** 


*Mnemonics:* PRinT the STM density  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 1 or a larger value, provide output of the electron density in real
space rho(r), made only from the electrons close to the Fermi energy, in a
range of energy (positive or negative), determined by the (positive or
negative, but non-zero) value of the STM bias [[stmbias]].  
This is a very approximate way to obtain STM profiles : one can choose an
equidensity surface, and consider that the STM tip will follow this surface.
Such equidensity surface might be determined with the help of Cut3D, and
further post-processing of it (to be implemented). The big approximations of
this technique are : neglect of the finite size of the tip, and position-
independent transfer matrix elements between the tip and the surface.  
The charge density is provided in units of electrons/Bohr^3. The name of the
STM density file will be the root output name, followed by _STM . Like a _DEN
file, it can be analyzed by cut3d. The file structure of this unformatted
output file is described in [ section 6.5
](../../users/generated_files/help_abinit.html#densoutputfile) of the
[[help_abinit]].  
For the STM charge density to be generated, one must give, as an input file,
the converged wavefunctions obtained from a previous run, at exactly the same
k-points and cut-off energy, self-consistently determined, using the
occupation numbers from [[occopt]]=7.  
In the run with positive [[prtstm]], one has to use :

  * positive [[iscf]] 
  * [[occopt]]=7, with specification of [[tsmear]] 
  * [[nstep]]=1 
  * the [[tolwfr]] convergence criterion 
  * [[ionmov]]=0 (this is the default value) 
  * [[optdriver]]=0 (this is the default value) 

  
Note that you might have to adjust the value of [[nband]] as well, for the
treatment of unoccupied states, because the automatic determination of
[[nband]] will often not include enough unoccupied states.  
When [[prtstm]] is non-zero, the stress tensor is set to zero.  
No output of _STM file is provided by [[prtstm]] lower or equal to 0.  
No other printing variables for density or potentials should be activated
(e.g. [[prtden]] has to be set to zero).


* * *

## **prtsuscep** 


*Mnemonics:* PRinT the SUSCEPtibility file (the irreducible polarizability)  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set to 0, no _SUSC file will be produced after the screening calculation,
only the _SCR file will be output.


* * *

## **prtvclmb** 


*Mnemonics:* PRinT V CouLoMB  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set >= 0 outputs a file with the Coulomb potential, defined as Hartree +
local Pseudopotential.

If **prtvclmb=1** and in case of PAW ([[usepaw]] > 0), the full core potential
is added for the Hartree part, with the on-site corrections vh1 - vht1.

If **prtvclmb=2**, only the smooth part of the Coulomb potential is output.


* * *

## **prtvha** 


*Mnemonics:* PRinT V_HArtree  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set &gt;=1 , provide output of the Hartree potential.  

If [[ionmov]]==0, the name of the potential file will be the root output name,
followed by _VHA.  
If [[ionmov]]==1 or 2, potential files will be output at each time step, with
the name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _VHA. 

The file structure of this unformatted output file is described in [ section
6.6 ](../../users/generated_files/help_abinit.html#localpotfile) of the
[[help_abinit]]. No output is provided by a negative value of this variable.


* * *

## **prtvhxc** 


*Mnemonics:* PRinT V_HXC  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set &gt;=1 , provide output of the sum of the Hartree potential and xc
potential.

If [[ionmov]]==0, the name of the potential file will be the root output name,
followed by _VHXC.  
If [[ionmov]]==1 or 2, potential files will be output at each time step, with
the name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _VHXC. 

The file structure of this unformatted output file is described in [ section
6.6 ](../../users/generated_files/help_abinit.html#localpotfile) of the
[[help_abinit]]. No output is provided by a negative value of this variable.


* * *

## **prtvol** 


*Mnemonics:* PRinT VOLume  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Control the volume of printed output. In particular, this concerns the
explicit echo of eigenenergies and residuals for all bands and k points in the
main output file. Also, the analysis of the value and location of the maximal
density (and magnetization).  
Standard choice is 0. Positive values print more in the output and log files,
while negative values are for debugging (or preprocessing only), and cause the
code to stop at some point.

  * 0 =&gt; The eigenenergies and residuals for all bands and k points are not echoed in the main output file. There are exceptions: the eigenvalues of the first k point are printed at the end of the SCF loop, and also, if [[iscf]]=-2 and [[kptopt]]&lt;=0, the eigenvalues for all the k points are printed anyway, for a maximum of 50 k-points. Due to some subtlety, if for **some** dataset [[prtvol]] is non-zero, the limit for input and output echoes cannot be enforced, so it is like if [[prtvol]]=1 for **all** the datasets for which [[prtvol]] was set to 0.
  * 1 =&gt; the eigenvalues for the first 50 k-points are printed in all cases, at the end of the SCF loop.
  * 2 =&gt; all the eigenvalues and the residuals are printed at the end of the SCF loop. Also, the analysis of the value and location of the maximal density (and magnetization) is printed.
  * 3 =&gt; Print memory information for lobpcg 
  * 4 =&gt; Like 3 and prints information of lobpcg algorithm convergence
  * 10 =&gt; the eigenvalues are printed for every SCF iteration, as well as other additions (to be specified in the future...) 

Debugging options :

  * = -1 =&gt; stop in abinit (main program), before call driver. Useful to see the effect of the preprocessing of input variables (memory needed, effect of symmetries, k points ...) without going further. Run very fast, on the order of the second.
  * =-2 =&gt; same as -1, except that print only the first dataset. All the non default input variables associated to all datasets are printed in the output file, but only for the first dataset. Also all the input variables are written in the NetCDF file \"OUT.nc\", even if the value is the default.
  * = -3 =&gt; stop in gstate, before call scfcv, move or brdmin. Useful to debug pseudopotentials
  * = -4 =&gt; stop in move, after completion of all loops
  * = -5 =&gt; stop in brdmin, after completion of all loops
  * = -6 =&gt; stop in scfcv, after completion of all loops 
  * = -7 =&gt; stop in vtorho, after the first rho is obtained
  * = -8 =&gt; stop in vtowfk, after the first k point is treated
  * = -9 =&gt; stop in cgwf, after the first wf is optimized
  * = -10 =&gt; stop in getghc, after the Hamiltonian is applied once

This debugging feature is not yet activated in the RF routines. Note that
[[fftalg]] offers another option for debugging.


* * *

## **prtvolimg** 


*Mnemonics:* PRinT VOLume for IMaGes  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Control the volume of printed output when an algorithm using images of the
cell is used ([[nimage]]&gt;1).  
When such an algorithm is activated, the printing volume (in output file) can
be large and difficult to read.  
Using ** prtvolimg=1 ** , the printing volume, for each image, is reduced to
unit cell, atomic positions, total energy, forces, stresses, velocities and
convergence residuals.  
Using ** prtvolimg=2 ** , the printing volume, for each image, is reduced to
total energy and convergence residuals only.


* * *

## **prtvpsp** 


*Mnemonics:* PRinT V_PSeudoPotential  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set &gt;=1 , provide output of the local pseudo potential.  

If [[ionmov]]==0, the name of the potential file will be the root output name,
followed by _VPSP.  
If [[ionmov]]==1 or 2, potential files will be output at each time step, with
the name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _VPSP. 

The file structure of this unformatted output file is described in [ section
6.6 ](../../users/generated_files/help_abinit.html#localpotfile) of the
[[help_abinit]]. No output is provided by a negative value of this variable.


* * *

## **prtvxc** 


*Mnemonics:* PRinT V_XC  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



If set &gt;=1 , provide output of the exchange-correlation potential.

If [[ionmov]]==0, the name of the potential file will be the root output name,
followed by _VXC.  
If [[ionmov]]==1 or 2, potential files will be output at each time step, with
the name being made of

  * the root output name, 
  * followed by _TIMx , where x is related to the timestep (see later) 
  * then followed by _VXC. 

The file structure of this unformatted output file is described in [ section
6.6 ](../../users/generated_files/help_abinit.html#localpotfile) of the
[[help_abinit]]. No output is provided by a negative value of this variable.


* * *

## **prtwant** 


*Mnemonics:* PRinT WANT file  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Flag used to indicate that either the Wannier90 or the WanT interfaces will be
used.

  * [[prtwant]]=1 =&gt; Use the ** ABINIT- WanT ** interface. 

Provide an output file that can be used by the WanT postprocessing program
(see http://www.wannier-transport.org). The value of the prtwant indicates the
version of the WanT code that can read it. Currently only the value
[[prtwant]]=1 is implemented, corresponding to WanT version 1.0.1, available
since Oct. 22, 2004.

Notes : Several requirements must be fulfilled by the wavefunction. Among
them, two are mandatory:  

    * 1\. An uniform grid of k-points, including the GAMMA point must be used. 
    * 2\. The use of time reversal symmetry is not allowed (istwfk=1) 
    * 3\. The list of k-points must be ordered, such that the coordinates, namely three-components vectors has the third index varying the most rapidly, then the second index, then the first index 
If these requirement are not fulfilled, the program will stop and an error
message is returned.

As an example of k-point grid in case of systems that have some 3D character
(1D systems are easy) :

    
             nkpt 8
    kpt  0   0   0
    0   0   1/2
    0   1/2 0
    0   1/2 1/2
    1/2 0   0
    1/2 0   1/2
    1/2 1/2 0
    1/2 1/2 1/2
    istwfk 8*1
        

Also, in order to use WanT as a postprocessing program for ABINIT you might
have to recompile it with the appropriate flags (see ABINIT makefile). Up to
now only the -convert big-endian was found to be mandatory, for machines with
little-endian default choice.

  * [[prtwant]]=2 =&gt; Use the ** ABINIT- Wannier90 ** interface. 

ABINIT will produce the input files required by Wannier90 and it will run
Wannier90 to produce the Maximally-locallized Wannier functions (see [
http://www.wannier.org ](http://www.wannier.org) ).

Notes:

    * The files that are created can also be used by Wannier90 in stand-alone mode. 
    * In order to use Wannier90 as a postprocessing program for ABINIT you might have to recompile it with the appropriate flags (see ABINIT makefile). You might use ./configure --enable-wannier90 
    * There are some other variables related to the interface of Wannier90 and ABINIT. See, [ VARW90 ](varw90.html) . 

  * [[prtwant]]=3 =&gt; Use the ** ABINIT- Wannier90 ** interface after converting the input wavefunctions to ** [[GW]] quasiparticle ** wavefunctions. 

ABINIT will produce the input files required by Wannier90 and it will run
Wannier90 to produce the Maximally-localized Wannier functions (see [
http://www.wannier.org ](http://www.wannier.org) ).

Additional Notes:

    * An input file of LDA wave functions is required which is completely consistent with the _KSS file used in the self-consistent [[GW]] calculation. This means that [[kssform]] 3 must be used to create the _KSS file and the output _WFK file from the same run must be used as input here. 
    * Wannier90 requires [[nshiftk]]=1, and [[shiftk]]= 0 0 0 is recommended. The k-point set used for the [[GW]] calculation, typically the irreducible BZ set created using [[kptopt]]=1, and that for the Abinit- Wannier90 interface must be consistent. 
    * Full-BZ wavefunctions should be generated in the run calling the interface by setting [[kptopt]]=3, [[iscf]]=-2, and [[nstep]]=3. This will simply use symmetry to transform the input IBZ wavefunctions to the full BZ set, still consistent with the [[GW]] _KSS input. 
    * The final _QPS file created by the self-consistent [[GW]] run is required as input. 
    * Any value of [[gwcalctyp]] between between 20 and 29 should be suitable, so, for example, Hartree-Fock maximally-localized Wannier functions could be generated setting [[gwcalctyp]]=25. 


* * *

## **prtwf** 


*Mnemonics:* PRinT the WaveFunction  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0 if [[nimage]] > 1,
1 otherwise.
  



If [[prtwf]]=1 , provide output of wavefunction and eigenvalue file, as
described in [ section 6.7
](../../users/generated_files/help_abinit.html#wavefctfile) of the main
[[help_abinit]].  
For a standard ground-state calculation, the name of the wavefunction file
will be the root output name, followed by _WFK. If [[nqpt]]=1, the root name
will be followed by _WFQ. For response-function calculations, the root name
will be followed by _1WFx, where x is the number of the perturbation. The
dataset information will be added as well, if relevant.  
No wavefunction output is provided by [[prtwf]]=0.  
If [[prtwf]]=-1, the code writes the wavefunction file only if convergence is
not achieved in the self-consistent cycle.

  
If [[prtwf]]=2, a file pwfn.data is produced, to be used as input for the
CASINO QMC code. See more explanation at the end of this section.  
If [[prtwf]]=3, the file that is created is nearly the same as with
[[prtwf]]=1, except that the records that should contain the wavefunction is
empty (so, such records exist, but store nothing). This is useful to generate
size-reduced DDK files, to perform an optic run. Indeed, in the latter case,
only matrix elements are needed [so, no wavefunction], but possibly a large
number of conduction bands, so that the DDK file might be huge if it contains
the wavefunctions.

Further explanation for the [[prtwf]]=2 case. To produce a wave function
suitable for use as a CASINO trial wave function, certain ABINIT parameters
must be set correctly. Primarily, CASINO (and QMC methods generally) can only
take advantage of time-reversal symmetry, and not the full set of symmetries
of the crystal structure. Therefore, ABINIT must be instructed to generate
k-points not just in the Irreducible Brillouin Zone, but in a full half of the
Brillouin Zone (using time-reversal symmetry to generate the other half).
Additionally, unless instructed otherwise, Abinit avoids the need for internal
storage of many of the coefficients of its wave functions for k-points that
have the property 2k=G_latt, where G_latt is a reciprocal lattice vector, by
making use of the property that c_k(G)=c^*_k(-G-G_latt). Abinit must be
instructed not to do this in order to output the full set of coefficients for
use in CASINO. See the ABINIT theoretical background documents
ABINIT/Infos/Theory/geometry.pdf and ABINIT/Infos/Theory/1WF.pdf for more
information.  
The first of these requirements is met by setting the ABINIT input variable
kptopt to 2 (see ABINIT/Infos/varbas.html#kptopt) and the second by setting
istwfk to 1 for all the k points (see ABINIT/Infos/vardev.html#istwfk). Since
CASINO is typically run with relatively small numbers of k-points, this is
easily done by defining an array of "1" in the input file.  
For example, for the 8 k-points generated with ngkpt 2 2 2, we add the
following lines to the input file:

    
    
      # Turn off special storage mode for time-reversal k-points
    istwfk 1 1 1 1 1 1 1 1
    # Use only time reversal symmetry, not full set of symmetries.
    kptopt 2
     

Other useful input variables of relevance to the plane waves ABINIT will
produce include ecut, nshiftk, shiftk, nband, occopt, occ, spinat and nsppol
(see relevant input variable documents in ABINIT/Infos/). If ABINIT is run in
multiple dataset mode, the different wave functions for the various datasets
are exported as pwfn1.data, pwfn2.data, ..., pwfnn.data where the numbers are
the contents of the contents of the input array jdtset (defaults to
1,2,...,ndtset).  
Once the routine is incorporated into the ABINIT package it is anticipated
that there will be an input variable to control whether or not a CASINO
pwfn.data file is written.

Other issues related to [[prtwf]]=2.  
The exporter does not currently work when ABINIT is used in parallel mode on
multiple processors if k-point parallelism is chosen. ABINIT does not store
the full wave function on each processor but rather splits the k-points
between the processors, so no one processor could write out the whole file.
Clearly this could be fixed but we have not done it yet. The sort of plane
wave DFT calculations usually required to generate QMC trial wave functions
execute very rapidly anyway and will generally not require a parallel
machines. The outqmc routine currently bails out with an error if this
combination of modes is selected - this will hopefully be fixed later.  
There has not been very extensive testing of less common situations such as
different numbers of bands for different k-points, and more complicated spin
polarized systems, so care should be taken when using the output in these
circumstances.  
If there is any doubt about the output of this routine, the first place to
look is the log file produced by ABINIT: if there are any warnings about
incorrectly normalized orbitals or non-integer occupation numbers there is
probably something set wrong in the input file.


* * *

## **prtwf_full** 


*Mnemonics:* PRinT Wavefunction file on the FULL mesh  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[prtwf]] == 1  



If set to 1 in a ground-state calculation, the code will output another WFK
file (with extension FULL_WFK) containing the wavefunctions in the full BZ as
well as a text file with the tables used for the tetrahedron method. Note that
prtwf_full requires [[prtwf]] == 1 and a ground-state calculation done on a
homogeneous k-mesh (see [[ngkpt]] and [[shiftk]]). The tetrahedron table is
produced only if the number of k-points in the irreducible zone ([[nkpt]]) is
greater than 3.


* * *

## **prtxml** 


*Mnemonics:* PRinT an XML output  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Create an XML output with common values. The corresponding DTD is distributed
in sources as extras/post_processing/abinitRun.dtd. All the DTD is not yet
implemented and this one is currently restricted to ground-state computations
(and derivative such as geometry optimisation).


* * *

