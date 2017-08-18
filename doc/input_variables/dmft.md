## **dmft_dc** 


*Mnemonics:* Dynamical Mean Fied Theory: Double Counting  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]], [[tests/paral/Input/t99.in]]
- v6:  [[tests/v6/Input/t45.in]]
- v7:  [[tests/v7/Input/t27.in]], [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]], [[tests/v7/Input/t30.in]], [[tests/v7/Input/t31.in]]
- v8:  [[tests/v8/Input/t01.in]]





  
Value of double counting used for DMFT. Only value 1 is activated for the
moment and is the FLL double counting.


* * *

## **dmft_entropy** 


*Mnemonics:* Dynamical Mean Fied Theory: ENTROPY  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[usedmft]]==1 and [[dmft_solv]]==5  
Test list:

- v7:  [[tests/v7/Input/t29.in]], [[tests/v7/Input/t30.in]], [[tests/v7/Input/t31.in]]





If 1, enable the calculation of the entropy within the DMFT framework and so
allows the calculation of the total energy (free energy). In the current
implementation, this is only possible with [[dmft_solv]]=5 (Continuous Time
Quantum Monte Carlo). See also the input variable [[dmft_nlambda]].


* * *

## **dmft_iter** 


*Mnemonics:* Dynamical Mean Fied Theory: number of ITERation  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



  
Number of iterations for the DMFT inner loop.


* * *

## **dmft_mxsf** 


*Mnemonics:* Dynamical Mean Fied Theory: MiXing parameter for the SelF energy  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.3  



  
Mixing parameter for the simple mixing of the self-energy.


* * *

## **dmft_nlambda** 


*Mnemonics:* Dynamical Mean Fied Theory: Number of LAMBDA points  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 6  
*Only relevant if:* [[usedmft]]==1 and [[dmft_entropy]]==1  
Test list:

- v7:  [[tests/v7/Input/t29.in]], [[tests/v7/Input/t30.in]], [[tests/v7/Input/t31.in]]





[[dmft_nlambda]] gives the number of integration points for the
thermodynamical integration in case of free energy calculation within DMFT.
Its value must be greater or equal to 3.


* * *

## **dmft_nwli** 


*Mnemonics:* Dynamical Mean Fied Theory: Number of frequency omega (W) in the LInear mesh  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



  
Number of Matsubara frequencies (linear mesh)


* * *

## **dmft_nwlo** 


*Mnemonics:* Dynamical Mean Fied Theory: Number of frequency omega (W) in the LOg mesh  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



  
Number of frequencies in the log mesh.


* * *

## **dmft_rslf** 


*Mnemonics:* Dynamical Mean Fied Theory: Read SeLF energy  
*Mentioned in topic(s):* DMFT_basic  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



Flag to read/write Self-Energy. If put to one, self-energy is written and read
at each DFT iteration.


* * *

## **dmft_solv** 


*Mnemonics:* Dynamical Mean Fied Theory: choice of SOLVer  
*Mentioned in topic(s):* DMFT_basic  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 5  



  
Choice of solver for the Impurity model.

  * 0=&gt; No solver and U=0, J=0 (see [[upawu]] and [[jpawu]]). 
  * 1=&gt; LDA+U self-energy is used (for testing purpose) 
  * 2=&gt; Hubbard one solver. The Hubbard one solver is an approximation which gives a rough description of correlated Mott insulators. It should not be used for metals. 
  * 5=&gt; Use the Continuous Time Quantum Monte Carlo (CTQMC) solver CT-Hyb of ABINIT in the density density representation, CTQMC calculations are much more time consuming that Hubbard I calculations. Nevertheless, the calculation is fully parallelised. 
  * 6=&gt; Continuous Time Quantum Monte Carlo (CTQMC) solver CT-Hyb of TRIQS in the density density representation. 
  * 7=&gt; Continuous Time Quantum Monte Carlo (CTQMC) solver CT-Hyb of TRIQS with the rotationally invariant formulation. 

  
The CT Hyb algorithm is described in [ Phys. Rev. Lett 97, 076405, (2006)
](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.076405). For a
discussion of density-density approximation with respect with the
rotationnally invariant formulation, see e.g. [ Phys. Rev. B 86, 155107 (2012)
](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.86.155107).  
The ABINIT/CT Hyb implementation is discussed in [
http://dx.doi.org/10.1016/j.cpc.2016.04.003
](http://dx.doi.org/10.1016/j.cpc.2016.04.003).  
The TRIQS/CT Hyb implementation is described in [ Comp. Phys. Comm. 200, 274
(2016) ](http://dx.doi.org/10.1016/j.cpc.2015.10.023). Before using it, it has
to be installed following instructions at
https://triqs.ipht.cnrs.fr/1.3/applications/cthyb/install.html. The current
interface is valid for TRIQS 1.3 and TRIQS/CTHYB 1.3.  
See the useful variables for CT-QMC solver : [[dmftctqmc_basis]],
[[dmftctqmc_check]], [[dmftctqmc_correl]], [[dmftctqmc_gmove]],
[[dmftctqmc_grnns]], [[dmftctqmc_meas]], [[dmftctqmc_mrka]],
[[dmftctqmc_mov]], [[dmftctqmc_order]], [[dmftctqmc_triqs_nleg]],
[[dmftqmc_l]], [[dmftqmc_n]], [[dmftqmc_seed]], [[dmftqmc_therm]]


* * *

## **dmft_t2g** 


*Mnemonics:* Dynamical Mean Fied Theory: t2g orbitals  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- paral:  [[tests/paral/Input/t99.in]]
- v7:  [[tests/v7/Input/t27.in]], [[tests/v7/Input/t30.in]], [[tests/v7/Input/t31.in]]
- v8:  [[tests/v8/Input/t01.in]]





  
Can be set to 1 only if in cubic symmetry. It enables one to carry a DFT+DMFT
calculations only on t2g orbitals.


* * *

## **dmft_tolfreq** 


*Mnemonics:* Dynamical Mean Fied Theory: TOLerance on DFT correlated electron occupation matrix for the definition of the FREQuency grid  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0001  
Test list:

- paral:  [[tests/paral/Input/t99.in]]
- v8:  [[tests/v8/Input/t01.in]]





  
The LDA occupation matrix for correlated electrons can be computed directly.
It can be compared to the calculation of the same quantity using LDA Green's
function, a sum over Matsubara frequencies and a projection over correlated
orbitals. Because the Matsubara grid is finite, the two quantities differ. If
this difference is larger than dmft_tolfreq, then the code stops and an error
message is given.


* * *

## **dmft_tollc** 


*Mnemonics:* Dynamical Mean Fied Theory: TOLerance on Local Charge for convergence of the DMFT loop  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1e-05  
Test list:

- v6:  [[tests/v6/Input/t45.in]]





  
Tolerance for the variation of Local Charge during iterations of the DMFT
Loop.  
The default value is good for fast calculations. However, to obtain good
convergence of the DFT Loop, the DMFT Loop needs a better convergence
criterion.


* * *

## **dmftbandf** 


*Mnemonics:* Dynamical Mean Field Theory: BAND: Final  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



[[dmftbandf]] is the last band taken into account in the Projected Local
Orbitals scheme of DFT+DMFT. With [[dmftbandi]], they define the energy window
used to define Wannier Functions. (see Amadon, B., Lechermann, F., Georges,
A., Jollet, F., Wehling, T. O., and Lichtenstein, A. I. Phys. Rev. B 77(20),
(2008).)


* * *

## **dmftbandi** 


*Mnemonics:* Dynamical Mean Field Theory: BAND: Initial  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



[[dmftbandi]] is the first band taken into account in the Projected Local
Orbitals scheme of LDA+DMFT. With [[dmftbandf]], they define the energy window
used to define Wannier Functions. (see Amadon, B., Lechermann, F., Georges,
A., Jollet, F., Wehling, T. O., and Lichtenstein, A. I. Phys. Rev. B 77(20),
(2008).)


* * *

## **dmftcheck** 


*Mnemonics:* Dynamical Mean Fied Theory: CHECKs  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  



  
Only for developer purposes. (Introduced by B. Amadon, v6.1.0)


* * *

## **dmftctqmc_check** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo CHECK  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Check the fast calculations during the Monte Carlo simulation with very slow
but robust methods. Should only be used for debugging.

  * 0=&gt; No check. 
  * 1=&gt; Check the overlap calculations (Impurity operator). 
  * 2=&gt; Check the update of M matrix calculation (Bath operator). 
  * 3=&gt; Check both. 


* * *

## **dmftctqmc_correl** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo CORRELations  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Flag to compute statistics about segments and anti-segments during the
simulation. Slow down the simulation.

  * 0=&gt; Nothing done 
  * 1=&gt; Calculations performed and written in "Correlation.dat" file 


* * *

## **dmftctqmc_gmove** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo Global MOVEs  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Default is no global moves. The value of this variable is the modulo used to
try a global move. A value of 5000 means that a global move is tried every
5000 Monte Carlo sweep.


* * *

## **dmftctqmc_grnns** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo GReeNs NoiSe  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Compute the statistical noise for each time slice of each green function. This
is a good approximation only if there is enough Monte Carlo sweeps per cpu.

  * 0=&gt; Nothing 
  * 1=&gt; Do it and write the noise in the "Gtau.dat" file. 


* * *

## **dmftctqmc_meas** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo MEASurements  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
The modulo used to measure the interaction energy and the number of electrons.
Example : 2 means the measure is perform every two sweeps.


* * *

## **dmftctqmc_mov** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo MOVie  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Print a latex file per cpu displaying the full simulation. This option should
only be use with very small number (&lt;1000) of Monte Carlo sweeps since it
requires a lot of I/O band width.

  * 0=&gt; Nothing 
  * 1=&gt; Write the "Movie_id.dat" file where id is the MPI rank of each process 


* * *

## **dmftctqmc_mrka** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo MARKov Analysis  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Measure the time evolution of the number of electrons for each orbital and
perform a fourier transform. The result can be plotted using the
"Markov_id.dat" file

  * 0=&gt; Nothing 
  * 1=&gt; Do it and write the noise in the "Markov_id.dat" file where id is the rank of each MPI process. 


* * *

## **dmftctqmc_order** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo perturbation ORDER  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]]
- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Print a file containing the statistic distribution of the number of segments
per orbital. The maximal order taken into account [[dmftctqmc_order]] : 50
means that we have the statistic distribution from 0 to 50 segments. The
result is written in the "Perturbation.dat" file.


* * *

## **dmftctqmc_triqs_nleg** 


*Mnemonics:* Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo perturbation of TRIQS, Number of LEGendre polynomials  
*Mentioned in topic(s):* DMFT_expert  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 30  
*Only relevant if:* [[dmft_solv]]==6 or 7  
Test list:

- paral:  [[tests/paral/Input/t99.in]]
- v8:  [[tests/v8/Input/t01.in]]





  
Specify the number of Legendre polynomials used for the calculation of Green's
function in CTQMC code from the library TRIQS. Default is 30. The value of
coefficients are given in file whose name ending is
"Legendre_coefficient.dat". (see also [ Phys. Rev. B 84, 075145 (2010))
](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.075145)


* * *

## **dmftqmc_l** 


*Mnemonics:* Dynamical Mean Fied Theory: Quantum Monte Carlo time sLices  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
*Only relevant if:* [[dmft_solv]]>=4  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]], [[tests/paral/Input/t99.in]]
- v6:  [[tests/v6/Input/t07.in]]
- v7:  [[tests/v7/Input/t27.in]], [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]], [[tests/v7/Input/t30.in]], [[tests/v7/Input/t31.in]]
- v8:  [[tests/v8/Input/t01.in]]





  
Number of time slices used to represent the time green function. This value
should be carefully chosen according to Niquist frequency and the [[tsmear]]
value.


* * *

## **dmftqmc_n** 


*Mnemonics:* Dynamical Mean Fied Theory: Quantum Monte Carlo Number of sweeps  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Only relevant if:* [[dmft_solv]]>=4  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]], [[tests/paral/Input/t99.in]]
- v6:  [[tests/v6/Input/t07.in]]
- v7:  [[tests/v7/Input/t27.in]], [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]], [[tests/v7/Input/t30.in]], [[tests/v7/Input/t31.in]]
- v8:  [[tests/v8/Input/t01.in]]





  
Number of Monte Carlo sweeps. Should be at least 10^6.


* * *

## **dmftqmc_seed** 


*Mnemonics:* Dynamical Mean Fied Theory: Quantum Monte Carlo SEED  
*Mentioned in topic(s):* DMFT_useful  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* [[jdtset]]  
*Only relevant if:* [[dmft_solv]]>=4  
Test list:

- v7:  [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]]





  
Seed to initilize the random number generator.  
Should not be relevant except for testing purpose.  
NOTE : If the CT-QMC ([[dmft_solv]]=5) is used on many CPUs, each CPU
initializes its random number generator with dmftqmc_seed+rank where rank is
the rank of the cpu in the MPI communicator.


* * *

## **dmftqmc_therm** 


*Mnemonics:* Dynamical Mean Fied Theory: Quantum Monte Carlo THERMalization  
*Mentioned in topic(s):* DMFT_compulsory  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1000  
*Only relevant if:* [[dmft_solv]]==5  
Test list:

- paral:  [[tests/paral/Input/t92.in]], [[tests/paral/Input/t92.in]], [[tests/paral/Input/t99.in]]
- v7:  [[tests/v7/Input/t27.in]], [[tests/v7/Input/t28.in]], [[tests/v7/Input/t29.in]], [[tests/v7/Input/t30.in]], [[tests/v7/Input/t31.in]]
- v8:  [[tests/v8/Input/t01.in]]





  
Number of Monte Carlo sweeps for the thermalization


* * *
