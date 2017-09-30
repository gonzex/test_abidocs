---
description: paral input variables
rpath: /variables/paral.md
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->
# paral input variables

This document lists and provides the description of the name (keywords) of the
paral input variables to be used in the input file for the abinit executable.

## **autoparal** 


*Mnemonics:* AUTOmatisation of the PARALlelism  
*Characteristics:* [[DEVELOP]]  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  

??? note "Test list (click to open). Moderately used, [11/920] in all abinit tests, [1/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t69.in|t69.in]], [[tests/mpiio/Input/t69.in|t69.in]]
    - paral:  [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t26.in|t26.in]]
    - tutoparal:  [[tests/tutoparal/Input/tgspw_01.in|tgspw_01.in]]
    - v67mbpt:  [[tests/v67mbpt/Input/t36.in|t36.in]]






This input variable is used only when running ABINIT in parallel and for
Ground-State calculations.  
It controls the automatic determination of parameters related to parallel work
distribution (if not imposed in input file). Given a total number of
processors, ABINIT can find a suitable distribution that fill (when possible)
all the different levels of parallelization. ABINIT can also determine optimal
parameters for the use of parallel Linear Algebra routines (using Scalapack or
Cuda, at present).  
The different values for [[autoparal]] are:

  * ** 0: ** The [[autoparal]] feature is deactivated. For ground-state and response function calculations, ABINIT can only activate automatically the parallelism over spins and k-points. 
  * ** 1: ** The number of processors per parallelization level is determined by mean of a simple (but relatively efficient) heuristic. A scaling factor is attributed to each level and an simple speedup factor is computed. The selected parameters are those giving the best speedup factor.   
Possibly concerned parameters: [[npimage]], [[npkpt]], [[npspinor]],
[[npfft]], [[npband]], [[bandpp]].

  * ** 2: ** The number of processors per parallelization level is first determined by mean of a simple (but relatively efficient) heuristic (see 1 above). Then the code performs a series of small benchmarks using the scheme applied for the LOBPCG algorithm (see: [[wfoptalg]]=4 or 14). The parallel distribution is then changed according to the benchmarks.   
Possibly concerned parameters: [[npimage]], [[npkpt]], [[npspinor]],
[[npfft]], [[npband]], [[bandpp]].

  * ** 3: ** Same as [[autoparal]]=1, plus automatic determination of Linear Algebra routines parameters.   
In addition, the code performs a series of small benchmarks using the Linear
Algebra routines (ScaLapack or Cuda-GPU). The parameters used to optimize
Linear Algebra work distribution are then changed according to the benchmarks.  
Possibly concerned parameters (in addition to those modified for
[[autoparal]]=1): [[use_slk]], [[np_slk]], [[gpu_linalg_limit]]

  * ** 4: ** combination of [[autoparal]]=2 and [[autoparal]]=3. 

Note that [[autoparal]]=1 can be used on every set of processors;
[[autoparal]] &gt; 1 should be used on a sufficiently large number of MPI
process.  
Also note that [[autoparal]] can be used simultaneously with [[max_ncpus]]; in
this case, ABINIT performs an optimization of process distribution for each
total number of processors from 2 to [[max_ncpus]]. A weight is associated to
each distribution and the higher this weight is the better the distribution
is. After having printed out the weights, the code stops.

## **bandpp** 


*Mnemonics:* BAND Per Processor  
*Characteristics:* [[DEVELOP]]  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[paral_kgb]]==1  

??? note "Test list (click to open). Rarely used, [7/920] in all abinit tests, [2/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t24.in|t24.in]], [[tests/mpiio/Input/t25.in|t25.in]]
    - paral:  [[tests/paral/Input/t24.in|t24.in]], [[tests/paral/Input/t25.in|t25.in]], [[tests/paral/Input/t29.in|t29.in]]
    - tutoparal:  [[tests/tutoparal/Input/tgspw_03.in|tgspw_03.in]], [[tests/tutoparal/Input/tstring_01.in|tstring_01.in]]






Control the size of the block in the LOBPCG algorithm. This keyword works only
with [[paral_kgb]]=1 and has to be either 1 or a multiple of 2.  
  
\-- With [[npband]]=1:

  * 1 =&gt; band-per-band algorithm 
  * n =&gt; The minimization is performed using [[nband]]/n blocks of n bands. 

Note: [[nband]]/n has to be an integer.  
  
\-- With [[npband]]/=1:

  * 1 =&gt; The minimization is performed using [[nband]]/[[npband]] blocks of [[npband]] bands. 
  * n =&gt; The minimization is performed using [[nband]]/([[npband]]*n) blocks of [[npband]]*n bands. 

Note: [[nband]]/([[npband]]*n) has to be an integer.  
  
By minimizing a larger number of bands together in LOBPCG, we increase the
convergency of the residual. The better minimization procedure (as concerns
the convergency, but not as concerns the speed) is generally performed by
using [[bandpp]]*[[npband]]=[[nband]]. Put [[bandpp]]=2 when [[istwfk]]=2 (the
time spent in FFTs is divided by two).

## **gpu_devices** 


*Mnemonics:* GPU: choice of DEVICES on one node  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* (5)  
*Default value:* [-1, -1, -1, -1, -1]  
*Only relevant if:* [[use_gpu_cuda]]==1 (CUDA functionality)  

??? note "Test list (click to open). Rarely used, [3/920] in all abinit tests, [0/116] in abinit tutorials"
    - gpu:  [[tests/gpu/Input/t05.in|t05.in]], [[tests/gpu/Input/t05.in|t05.in]], [[tests/gpu/Input/t05.in|t05.in]]






To be used when several GPU devices are present on each node, assuming the
same number of devices on all nodes.  
Allows to choose in which order the GPU devices are chosen and distributed
among MPI processes (see examples below). When the default value (-1) is set,
the GPU devices are chosen by order of performance (FLOPS, memory).  
  
Examples:

  * 2 GPU devices per node, 4 MPI processes per node, **gpu_device**=[-1,-1,-1,-1,-1] (default):  
MPI processes 0 and 2 use the best GPU card, MPI processes 1 and 3 use the
slowest GPU card.

  * 3 GPU devices per node, 5 MPI processes per node, **gpu_device**=[1,0,2,-1,-1]:  
MPI processes 0 and 3 use GPU card 1, MPI processes 1 and 4 use GPU card 0,
MPI process 2 uses GPU card 2.

  * 3 GPU devices per node, 5 MPI processes per node, **gpu_device**=[0,1,-1,-1,-1]:  
MPI processes 0, 2 and 4 use GPU card 0, MPI processes 1 and 3 use GPU card 1;
the 3rd GPU card is not used.

GPU card are numbered starting from 0; to get the GPU devices list, type
"nvidia-smi" or "lspci | grep -i nvidia".

## **gpu_linalg_limit** 


*Mnemonics:* GPU (Cuda): LINear ALGebra LIMIT  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2000000  
*Only relevant if:* [[use_gpu_cuda]]==1 (CUDA functionality)  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - gpu:  [[tests/gpu/Input/t04.in|t04.in]], [[tests/gpu/Input/t05.in|t05.in]], [[tests/gpu/Input/t05.in|t05.in]], [[tests/gpu/Input/t05.in|t05.in]]






Use of linear algebra and matrix algebra on GPU is only efficient if the size
of the involved matrices is large enough. The [[gpu_linalg_limit]] parameter
defines the threshold above which linear (and matrix) algebra operations are
done on the Graphics Processing Unit.  
The considered matrix size is equal to:  

* SIZE=([[mpw]]*[[nspinor]]/ [[npspinor]])* ([[npband]]*[[bandpp]])**2 
  
When SIZE&gt;=[[gpu_linalg_limit]], [[wfoptalg]] parameter is automatically
set to 14 which corresponds to the use of LOBPCG algorithm for the calculation
of the eigenstates.

## **gwpara** 


*Mnemonics:* GW PARAllelization level  
*Mentioned in topic(s):* [[topic:parallelism]], [[topic:GW]], [[topic:Susceptibility]], [[topic:SelfEnergy]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 2  
*Comment:* The default value has been changed in v8. From 1 to 2   
*Only relevant if:* [[optdriver]] in [3,4]  

??? note "Test list (click to open). Moderately used, [51/920] in all abinit tests, [4/116] in abinit tutorials"
    - libxc:  [[tests/libxc/Input/t41.in|t41.in]], [[tests/libxc/Input/t42.in|t42.in]], [[tests/libxc/Input/t43.in|t43.in]]
    - paral:  [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t73.in|t73.in]], [[tests/paral/Input/t73.in|t73.in]], [[tests/paral/Input/t73.in|t73.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t75.in|t75.in]], [[tests/paral/Input/t75.in|t75.in]], [[tests/paral/Input/t75.in|t75.in]], [[tests/paral/Input/t75.in|t75.in]]
    - tutoparal:  [[tests/tutoparal/Input/tmbt_2.in|tmbt_2.in]], [[tests/tutoparal/Input/tmbt_3.in|tmbt_3.in]], [[tests/tutoparal/Input/tmbt_4.in|tmbt_4.in]]
    - tutorial:  [[tests/tutorial/Input/tbs_1.in|tbs_1.in]]
    - v3:  [[tests/v3/Input/t30.in|t30.in]], [[tests/v3/Input/t31.in|t31.in]]
    - v4:  [[tests/v4/Input/t84.in|t84.in]], [[tests/v4/Input/t85.in|t85.in]], [[tests/v4/Input/t88.in|t88.in]]
    - v5:  [[tests/v5/Input/t71.in|t71.in]]
    - v67mbpt:  [[tests/v67mbpt/Input/t01.in|t01.in]], [[tests/v67mbpt/Input/t02.in|t02.in]], [[tests/v67mbpt/Input/t03.in|t03.in]], [[tests/v67mbpt/Input/t04.in|t04.in]], [[tests/v67mbpt/Input/t05.in|t05.in]], [[tests/v67mbpt/Input/t09.in|t09.in]], [[tests/v67mbpt/Input/t11.in|t11.in]], [[tests/v67mbpt/Input/t16.in|t16.in]], [[tests/v67mbpt/Input/t19.in|t19.in]], [[tests/v67mbpt/Input/t22.in|t22.in]], [[tests/v67mbpt/Input/t29.in|t29.in]], [[tests/v67mbpt/Input/t31.in|t31.in]], [[tests/v67mbpt/Input/t33.in|t33.in]], [[tests/v67mbpt/Input/t34.in|t34.in]], [[tests/v67mbpt/Input/t36.in|t36.in]], [[tests/v67mbpt/Input/t50.in|t50.in]], [[tests/v67mbpt/Input/t51.in|t51.in]]
    - v7:  [[tests/v7/Input/t78.in|t78.in]], [[tests/v7/Input/t79.in|t79.in]]
    - wannier90:  [[tests/wannier90/Input/t03.in|t03.in]]






[[gwpara]] is used to choose between the two different parallelization levels
available in the GW code. The available options are:

  * =1 =&gt; parallelisation on k points 
  * =2 =&gt; parallelisation on bands 

Additional notes:  
In the present status of the code, only the parallelization over bands
([[gwpara]]=2) allows to reduce the memory allocated by each processor.  
Using [[gwpara]]=1, indeed, requires the same amount of memory as a sequential
run, irrespectively of the number of CPUs used.

## **localrdwf** 


*Mnemonics:* LOCAL ReaD WaveFunctions  
*Characteristics:* [[DEVELOP]]  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  

??? note "Test list (click to open). Moderately used, [41/920] in all abinit tests, [0/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t01.in|t01.in]], [[tests/mpiio/Input/t01.in|t01.in]], [[tests/mpiio/Input/t01.in|t01.in]]
    - paral:  [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t03.in|t03.in]], [[tests/paral/Input/t03.in|t03.in]], [[tests/paral/Input/t03.in|t03.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]]






This input variable is used only when running abinit in parallel. If
[[localrdwf]]=1, the input wavefunction disk file or the KSS/SCR file in case
of GW calculations, is read locally by each processor, while if
[[localrdwf]]=0, only one processor reads it, and broadcast the data to the
other processors.

The option [[localrdwf]]=0 is NOT allowed when parallel I/O are activated
(MPI-IO access), i.e. when [[iomode]]==1.

In the case of a parallel computer with a unique file system, both options are
as convenient for the user. However, if the I/O are slow compared to
communications between processors, , [[localrdwf]]=0 should be much more
efficient; if you really need temporary disk storage, switch to localrdwf=1 ).

In the case of a cluster of nodes, with a different file system for each
machine, the input wavefunction file must be available on all nodes if
[[localrdwf]]=1, while it is needed only for the master node if
[[localrdwf]]=0.

## **max_ncpus** 


*Mnemonics:* MAXimum Number of CPUS  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  

??? note "Test list (click to open). Rarely used, [1/920] in all abinit tests, [1/116] in abinit tutorials"
    - tutoparal:  [[tests/tutoparal/Input/tgspw_01.in|tgspw_01.in]]






If [[autoparal]] &gt; 1 and [[max_ncpus]] is greater than 0, ABINIT analyzes
the efficiency of the process distribution for each possible number of
processors from 2 to [[max_ncpus]]. After having printed out the efficiency,
the code stops.

## **np_slk** 


*Mnemonics:* Number of mpi Processors used for ScaLapacK calls  
*Characteristics:* [[DEVELOP]]  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1000000  
*Only relevant if:* [[optdriver]]==1 and [[paral_kgb]]==1 (Ground-state calculations with LOBPCG algorithm)  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - paral:  [[tests/paral/Input/t22.in|t22.in]], [[tests/paral/Input/t30.in|t30.in]]






When using Scalapack (or any similar Matrix Algebra library), the efficiency
of the eigenproblem resolution saturates as the number of CPU cores increases.
It is better to use a smaller number of CPU cores for the LINALG calls.  
This maximum number of cores can be set with [[np_slk]].  
A large number for [[np_slk]] (i.e. 1000000) means that all cores are used for
the Linear Algebra calls.  
np_slk must divide the number of processors involved in diagonalizations
([[npband]]*[[npfft]]*[[npspinor]]).  
Note: an optimal value for this parameter can be automatically found by using
the [[autoparal]] input keyword.

## **npband** 


*Mnemonics:* Number of Processors at the BAND level  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[paral_kgb]]==1  

??? note "Test list (click to open). Moderately used, [29/920] in all abinit tests, [4/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t21.in|t21.in]], [[tests/mpiio/Input/t22.in|t22.in]], [[tests/mpiio/Input/t24.in|t24.in]], [[tests/mpiio/Input/t25.in|t25.in]], [[tests/mpiio/Input/t26.in|t26.in]], [[tests/mpiio/Input/t27.in|t27.in]], [[tests/mpiio/Input/t28.in|t28.in]], [[tests/mpiio/Input/t42.in|t42.in]], [[tests/mpiio/Input/t49.in|t49.in]], [[tests/mpiio/Input/t51.in|t51.in]], [[tests/mpiio/Input/t99.in|t99.in]]
    - paral:  [[tests/paral/Input/t21.in|t21.in]], [[tests/paral/Input/t22.in|t22.in]], [[tests/paral/Input/t24.in|t24.in]], [[tests/paral/Input/t25.in|t25.in]], [[tests/paral/Input/t26.in|t26.in]], [[tests/paral/Input/t28.in|t28.in]], [[tests/paral/Input/t29.in|t29.in]], [[tests/paral/Input/t30.in|t30.in]], [[tests/paral/Input/t41.in|t41.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t77.in|t77.in]]
    - tutoparal:  [[tests/tutoparal/Input/tdfpt_03.in|tdfpt_03.in]], [[tests/tutoparal/Input/tgspw_02.in|tgspw_02.in]], [[tests/tutoparal/Input/tgspw_03.in|tgspw_03.in]], [[tests/tutoparal/Input/tstring_01.in|tstring_01.in]]
    - v67mbpt:  [[tests/v67mbpt/Input/t15.in|t15.in]]






Relevant only for the band/FFT parallelisation (see the [[paral_kgb]] input
variable).  
[[npband]] gives the number of processors among which the work load over the
band level is shared. [[npband]], [[npfft]], [[npkpt]] and [[npspinor]] are
combined to give the total number of processors (nproc) working on the
band/FFT/k-point parallelisation.  
See [[npfft]], [[npkpt]], [[npspinor]] and [[paral_kgb]] for the additional
information on the use of band/FFT/k-point parallelisation. [[npband]] has to
be a divisor or equal to [[nband]]  
Note: an optimal value for this parameter can be automatically found by using
the [[autoparal]] input keyword.

## **npfft** 


*Mnemonics:* Number of Processors at the FFT level  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[paral_kgb]]==1  

??? note "Test list (click to open). Moderately used, [28/920] in all abinit tests, [4/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t21.in|t21.in]], [[tests/mpiio/Input/t22.in|t22.in]], [[tests/mpiio/Input/t24.in|t24.in]], [[tests/mpiio/Input/t25.in|t25.in]], [[tests/mpiio/Input/t26.in|t26.in]], [[tests/mpiio/Input/t27.in|t27.in]], [[tests/mpiio/Input/t28.in|t28.in]], [[tests/mpiio/Input/t42.in|t42.in]], [[tests/mpiio/Input/t49.in|t49.in]], [[tests/mpiio/Input/t51.in|t51.in]], [[tests/mpiio/Input/t99.in|t99.in]]
    - paral:  [[tests/paral/Input/t21.in|t21.in]], [[tests/paral/Input/t22.in|t22.in]], [[tests/paral/Input/t24.in|t24.in]], [[tests/paral/Input/t25.in|t25.in]], [[tests/paral/Input/t26.in|t26.in]], [[tests/paral/Input/t29.in|t29.in]], [[tests/paral/Input/t30.in|t30.in]], [[tests/paral/Input/t41.in|t41.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t77.in|t77.in]]
    - tutoparal:  [[tests/tutoparal/Input/tdfpt_03.in|tdfpt_03.in]], [[tests/tutoparal/Input/tgspw_02.in|tgspw_02.in]], [[tests/tutoparal/Input/tgspw_03.in|tgspw_03.in]], [[tests/tutoparal/Input/tstring_01.in|tstring_01.in]]
    - v67mbpt:  [[tests/v67mbpt/Input/t15.in|t15.in]]






Relevant only for the band/FFT/k-point parallelisation (see the [[paral_kgb]]
input variable).  
[[npfft]] gives the number of processors among which the work load over the
FFT level is shared. [[npfft]], [[npkpt]], [[npband]] and [[npspinor]] are
combined to give the total number of processors (nproc) working on the
band/FFT/k-point parallelisation.  
See [[npband]], [[npkpt]], [[npspinor]], and [[paral_kgb]] for the additional
information on the use of band/FFT/k-point parallelisation.

Note : [[ngfft]] is automatically adjusted to [[npfft]]. If the number of
processor is changed from a calculation to another one, [[npfft]] may change,
and then [[ngfft]] also.  
Note: an optimal value for this parameter can be automatically found by using
the [[autoparal]] input keyword.

## **nphf** 


*Mnemonics:* Number of Processors for (Hartree)-Fock exact exchange  
*Mentioned in topic(s):* [[topic:Hybrids]], [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  

??? note "Test list (click to open). Rarely used, [6/920] in all abinit tests, [0/116] in abinit tutorials"
    - libxc:  [[tests/libxc/Input/t53.in|t53.in]]
    - paral:  [[tests/paral/Input/t93.in|t93.in]], [[tests/paral/Input/t94.in|t94.in]]
    - v7:  [[tests/v7/Input/t65.in|t65.in]], [[tests/v7/Input/t66.in|t66.in]], [[tests/v7/Input/t70.in|t70.in]]






Relevant only for the k-point/fock parallelisation (option [[paral_kgb]] input
variable).  
[[nphf]] gives the number of processors among which the work load over the
occupied states level is shared. [[nphf]] and [[npkpt]] are combined to give
the total number of processors (nproc) working on the parallelisation.  

Note : [[nphf]] should be a divisor or equal to the number of k-point times
the number of bands for exact exchange ([[nkpthf]]*[[nbandhf]]) in order to
have the better load-balancing and efficiency.  

## **npimage** 


*Mnemonics:* Number of Processors at the IMAGE level  
*Mentioned in topic(s):* [[topic:parallelism]], [[topic:PIMD]], [[topic:TransPath]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - paral:  [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]]






Relevant only when sets of images are activated (see [[imgmov]] and [[nimage]]
).  
[[npimage]] gives the number of processors among which the work load over the
image level is shared. It is compatible with all other parallelization levels
available for ground-state calculations.  
Note: an optimal value for this parameter can be automatically found by using
the [[autoparal]] input keyword.  
  
_See [[paral_kgb]], [[npkpt]], [[npband]], [[npfft]] and [[npspinor]] for the
additional information on the use of k-point/band/FFT parallelisation. _

## **npkpt** 


*Mnemonics:* Number of Processors at the K-Point Level  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[paral_kgb]]==1  

??? note "Test list (click to open). Moderately used, [32/920] in all abinit tests, [1/116] in abinit tutorials"
    - libxc:  [[tests/libxc/Input/t53.in|t53.in]]
    - mpiio:  [[tests/mpiio/Input/t21.in|t21.in]], [[tests/mpiio/Input/t22.in|t22.in]], [[tests/mpiio/Input/t24.in|t24.in]], [[tests/mpiio/Input/t25.in|t25.in]], [[tests/mpiio/Input/t26.in|t26.in]], [[tests/mpiio/Input/t27.in|t27.in]], [[tests/mpiio/Input/t28.in|t28.in]], [[tests/mpiio/Input/t42.in|t42.in]], [[tests/mpiio/Input/t49.in|t49.in]], [[tests/mpiio/Input/t51.in|t51.in]], [[tests/mpiio/Input/t99.in|t99.in]]
    - paral:  [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t21.in|t21.in]], [[tests/paral/Input/t22.in|t22.in]], [[tests/paral/Input/t24.in|t24.in]], [[tests/paral/Input/t25.in|t25.in]], [[tests/paral/Input/t26.in|t26.in]], [[tests/paral/Input/t29.in|t29.in]], [[tests/paral/Input/t30.in|t30.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t93.in|t93.in]], [[tests/paral/Input/t94.in|t94.in]]
    - tutoparal:  [[tests/tutoparal/Input/tdfpt_03.in|tdfpt_03.in]]
    - v7:  [[tests/v7/Input/t65.in|t65.in]], [[tests/v7/Input/t66.in|t66.in]], [[tests/v7/Input/t70.in|t70.in]]






Relevant only for the band/FFT/k-point parallelisation (see the [[paral_kgb]]
input variable).  
[[npkpt]] gives the number of processors among which the work load over the
k-point/spin-component level is shared. [[npkpt]], [[npfft]], [[npband]] and
[[npspinor]] are combined to give the total number of processors (nproc)
working on the band/FFT/k-point parallelisation.  
See [[npband]], [[npfft]], [[npspinor]] and [[paral_kgb]] for the additional
information on the use of band/FFT/k-point parallelisation.

[[npkpt]] should be a divisor or equal to with the number of k-point/spin-
components ([[nkpt]]*[[nsppol]]) in order to have the better load-balancing
and efficiency.  
Note: an optimal value for this parameter can be automatically found by using
the [[autoparal]] input keyword.

## **nppert** 


*Mnemonics:* Number of Processors at the PERTurbation level  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[paral_rf]]==1  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t69.in|t69.in]], [[tests/mpiio/Input/t69.in|t69.in]]






This parameter is used in connection to the parallelization over
perturbations(see [[paral_rf]] ), for a linear response calculation.
[[nppert]] gives the number of processors among which the work load over the
perturbation level is shared. It can even be specified separately for each
dataset.

## **npspinor** 


*Mnemonics:* Number of Processors at the SPINOR level  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  
*Only relevant if:* [[paral_kgb]]==1  

??? note "Test list (click to open). Rarely used, [2/920] in all abinit tests, [0/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t28.in|t28.in]]
    - paral:  [[tests/paral/Input/t28.in|t28.in]]






Can be 1 or 2 (if [[nspinor]]=2).  
Relevant only for the band/FFT/k-point parallelisation (see the [[paral_kgb]]
input variable).  
[[npspinor]] gives the number of processors among which the work load over the
spinorial components of wave-functions is shared. [[npspinor]], [[npfft]],
[[npband]] and [[npkpt]] are combined to give the total number of processors
(nproc) working on the band/FFT/k-point parallelisation.  
Note: an optimal value for this parameter can be automatically found by using
the [[autoparal]] input keyword.  
  
_See [[npkpt]], [[npband]], [[npfft]], and [[paral_kgb]] for the additional
information on the use of band/FFT/k-point parallelisation._  

## **paral_atom** 


*Mnemonics:* activate PARALelization over (paw) ATOMic sites  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1  

??? note "Test list (click to open). Rarely used, [9/920] in all abinit tests, [0/116] in abinit tutorials"
    - libxc:  [[tests/libxc/Input/t53.in|t53.in]]
    - mpiio:  [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t62.in|t62.in]]
    - paral:  [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]]
    - v5:  [[tests/v5/Input/t06.in|t06.in]]
    - v7:  [[tests/v7/Input/t32.in|t32.in]], [[tests/v7/Input/t70.in|t70.in]]






Relevant only for PAW calculations.  
This keyword controls the parallel distribution of memory over atomic sites.
Calculations are also distributed using the "kpt-band" communicator.
Compatible with ground-state calculations and response function calculations  

## **paral_kgb** 


*Mnemonics:* activate PARALelization over K-point, G-vectors and Bands  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  

??? note "Test list (click to open). Moderately used, [124/920] in all abinit tests, [5/116] in abinit tutorials"
    - gpu:  [[tests/gpu/Input/t02.in|t02.in]]
    - mpiio:  [[tests/mpiio/Input/t01.in|t01.in]], [[tests/mpiio/Input/t01.in|t01.in]], [[tests/mpiio/Input/t01.in|t01.in]], [[tests/mpiio/Input/t21.in|t21.in]], [[tests/mpiio/Input/t22.in|t22.in]], [[tests/mpiio/Input/t24.in|t24.in]], [[tests/mpiio/Input/t25.in|t25.in]], [[tests/mpiio/Input/t26.in|t26.in]], [[tests/mpiio/Input/t27.in|t27.in]], [[tests/mpiio/Input/t28.in|t28.in]], [[tests/mpiio/Input/t42.in|t42.in]], [[tests/mpiio/Input/t49.in|t49.in]], [[tests/mpiio/Input/t51.in|t51.in]], [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t99.in|t99.in]]
    - paral:  [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t01.in|t01.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t02.in|t02.in]], [[tests/paral/Input/t03.in|t03.in]], [[tests/paral/Input/t03.in|t03.in]], [[tests/paral/Input/t03.in|t03.in]], [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t05.in|t05.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t06.in|t06.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t07.in|t07.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t08.in|t08.in]], [[tests/paral/Input/t21.in|t21.in]], [[tests/paral/Input/t22.in|t22.in]], [[tests/paral/Input/t24.in|t24.in]], [[tests/paral/Input/t25.in|t25.in]], [[tests/paral/Input/t26.in|t26.in]], [[tests/paral/Input/t27.in|t27.in]], [[tests/paral/Input/t28.in|t28.in]], [[tests/paral/Input/t29.in|t29.in]], [[tests/paral/Input/t30.in|t30.in]], [[tests/paral/Input/t41.in|t41.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t51.in|t51.in]], [[tests/paral/Input/t52.in|t52.in]], [[tests/paral/Input/t53.in|t53.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t54.in|t54.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t55.in|t55.in]], [[tests/paral/Input/t56.in|t56.in]], [[tests/paral/Input/t56.in|t56.in]], [[tests/paral/Input/t56.in|t56.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t57.in|t57.in]], [[tests/paral/Input/t59.in|t59.in]], [[tests/paral/Input/t59.in|t59.in]], [[tests/paral/Input/t59.in|t59.in]], [[tests/paral/Input/t59.in|t59.in]], [[tests/paral/Input/t62.in|t62.in]], [[tests/paral/Input/t62.in|t62.in]], [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t71.in|t71.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t72.in|t72.in]], [[tests/paral/Input/t73.in|t73.in]], [[tests/paral/Input/t73.in|t73.in]], [[tests/paral/Input/t73.in|t73.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t74.in|t74.in]], [[tests/paral/Input/t75.in|t75.in]], [[tests/paral/Input/t75.in|t75.in]], [[tests/paral/Input/t75.in|t75.in]], [[tests/paral/Input/t75.in|t75.in]], [[tests/paral/Input/t76.in|t76.in]], [[tests/paral/Input/t76.in|t76.in]], [[tests/paral/Input/t76.in|t76.in]], [[tests/paral/Input/t77.in|t77.in]], [[tests/paral/Input/t91.in|t91.in]], [[tests/paral/Input/t91.in|t91.in]], [[tests/paral/Input/t91.in|t91.in]], [[tests/paral/Input/t92.in|t92.in]], [[tests/paral/Input/t92.in|t92.in]]
    - tutoparal:  [[tests/tutoparal/Input/tdfpt_03.in|tdfpt_03.in]], [[tests/tutoparal/Input/tgspw_01.in|tgspw_01.in]], [[tests/tutoparal/Input/tgspw_02.in|tgspw_02.in]], [[tests/tutoparal/Input/tgspw_03.in|tgspw_03.in]], [[tests/tutoparal/Input/tstring_01.in|tstring_01.in]]
    - v5:  [[tests/v5/Input/t76.in|t76.in]]
    - v67mbpt:  [[tests/v67mbpt/Input/t15.in|t15.in]]
    - v7:  [[tests/v7/Input/t71.in|t71.in]], [[tests/v7/Input/t72.in|t72.in]], [[tests/v7/Input/t78.in|t78.in]], [[tests/v7/Input/t79.in|t79.in]]






** If paral_kgb is not explicitely put in the input file ** , ABINIT automatically detects if the job has been sent in sequential or in parallel. In this last case, it detects the number of processors on which the job has been sent and calculates values of [[npkpt]], [[npfft]], [[npband]], [[bandpp]] , [[npimage]] and [[npspinor]] that are compatible with the number of processors. It then set paral_kgb to 0 or 1 (see hereunder) and launches the job. 

** If paral_kgb=0 ** , the parallelization over k-points only is activated. In this case, [[npkpt]], [[npspinor]], [[npfft]] and [[npband]] are ignored. Require compilation option --enable-mpi="yes". 

** If paral_kgb=1 ** , the parallelization over bands, FFTs, and k-point/spin-components is activated (see [[npkpt]], [[npfft]] [[npband]] and eventually [[npspinor]]). With this parallelization, the work load is split over four levels of parallelization (three level of parallelisation (kpt-band-fft )+ spin) The different communications almost occur along one dimension only. Require compilation option --enable-mpi="yes". 

HOWTO fix the number of processors along one level of parallelisation:  
At first, try to parallelise over the k point and spin (see
[[npkpt]],[[npspinor]]). Otherwise, for unpolarized calculation at the gamma
point, parallelise over the two other levels: the band and FFT ones. For
nproc&lt;=50, the best speed-up is achieved for [[npband]]=nproc and
[[npfft]]=1 (which is not yet the default). For nproc&gt;=50, the best speed-
up is achieved for [[npband]] &gt;=4*[[npfft]].

For additional information, download F. Bottin presentation at the [ ABINIT
workshop 2007 ](http://www.abinit.org/community/events/program3rd)

Suggested acknowledgments :  
F. Bottin, S. Leroux, A. Knyazev and G. Zerah, _ Large scale ab initio
calculations based on three levels of parallelization _ , Comput. Mat. Science
** 42 ** , 329 (2008), also available on arXiv, http://arxiv.org/abs/0707.3405
.

If the total number of processors used is compatible with the four levels of
parallelization, the values for [[npkpt]], [[npspinor]], [[npfft]], [[npband]]
and [[bandpp]] will be filled automatically, although the repartition may not
be optimal. To optimize the repartition use:

** If paral_kgb=1 ** and ** max_ncpus = n /= 0 ** ABINIT will test automatically if all the processor numbers between 2 and n are convenient for a parallel calculation and print the possible values in the log file. A weight is attributed to each possible processors repartition. It is adviced to select a processor repartition for which the weight is high (as closed to the number of processors as possible). The code will then stop after the printing. This test can be done as well with a sequential as with a parallel version of the code. The user can then choose the adequate number of processor on which he can run his job. He must put again paral_kgb=1 in the input file and put the corresponding values for [[npkpt]], [[npfft]], [[npband]],[[bandpp]] and eventually [[npspinor]] in the input file. 

## **paral_rf** 


*Mnemonics:* activate PARALlelization over Response Function perturbations  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t62.in|t62.in]], [[tests/mpiio/Input/t69.in|t69.in]], [[tests/mpiio/Input/t69.in|t69.in]]






This parameter activates the parallelization over perturbations which can be
used during RF-Calculation. It is possible to use this type of parallelization
in combination to the parallelization over k-points.

Currently total energies calculated by groups, where the master process is not
in, are saved in .status_LOGxxxx files.

If [[paral_rf]] is set to -1, the code reports the list of irreducible
perturbations for the specified q-point in the log file (YAML format) and then
stops.

[[paral_rf]] can be specified separately for each dataset.

## **pw_unbal_thresh** 


*Mnemonics:* Plane Wave UNBALancing: THRESHold for balancing procedure  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 40%  
*Only relevant if:* [[paral_kgb]]==1  

??? note "Test list (click to open). Rarely used, [1/920] in all abinit tests, [0/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t26.in|t26.in]]






This parameter (in %) activates a load balancing procedure when the
distribution of plane wave components over MPI processes is not optimal. The
balancing procedure is activated when the ratio between the number of plane
waves treated by a processor and the ideal one is higher than
_pw_unbal_thresh_ %.

## **use_gpu_cuda** 


*Mnemonics:* activate USE of GPU accelerators with CUDA (nvidia)  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 1 if [[optdriver]]==0 and [[CUDA]],
0 otherwise.
  

??? note "Test list (click to open). Rarely used, [7/920] in all abinit tests, [0/116] in abinit tutorials"
    - gpu:  [[tests/gpu/Input/t01.in|t01.in]], [[tests/gpu/Input/t02.in|t02.in]], [[tests/gpu/Input/t03.in|t03.in]], [[tests/gpu/Input/t05.in|t05.in]], [[tests/gpu/Input/t05.in|t05.in]], [[tests/gpu/Input/t05.in|t05.in]]
    - v5:  [[tests/v5/Input/t75.in|t75.in]]






Only available if ABINIT executable has been compiled with cuda nvcc compiler.  
This parameter activates the use of NVidia graphic accelerators (GPU) if
present.  
If [[use_gpu_cuda]] = 1, some parts of the computation are transmitted to the
GPUs.  
If [[use_gpu_cuda]] = 0, no computation is done on GPUs, even if present.  
  
Note that, while running ABINIT on GPUs, it is recommended to use MAGMA
external library (i.e. Lapack on GPUs). The latter is activated during
compilation stage (see "configure" step of ABINIT compilation process). If
MAGMA is not used, ABINIT performances on GPUs can be poor.

## **use_slk** 


*Mnemonics:* USE ScaLapacK  
*Characteristics:* [[DEVELOP]]  
*Mentioned in topic(s):* [[topic:parallelism]]  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  

??? note "Test list (click to open). Rarely used, [4/920] in all abinit tests, [0/116] in abinit tutorials"
    - mpiio:  [[tests/mpiio/Input/t27.in|t27.in]]
    - paral:  [[tests/paral/Input/t24.in|t24.in]], [[tests/paral/Input/t25.in|t25.in]], [[tests/paral/Input/t29.in|t29.in]]






If set to 1, enable the use of ScaLapack within LOBPCG.
