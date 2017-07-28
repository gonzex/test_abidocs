---
authors: FJ
---

### This file gives hints on how to set parameters related to the k-points
with the ABINIT package.

* * *

[TOC]

### **1\. Introduction.**

Any kind of symmetries and corresponding sets of k-point can be input, and
taken into account in the computation.  
Since ABINIT is based on periodic boundary conditions, the Brillouin zone must
be sampled adequately. The number of k-points to be used for this sampling, in
the full Brillouin zone, is inversely proportional to ucvol, but may also vary
a lot from system to system. As a rule of thumb, a system with a large band
gap will need few k-points, while metals will need lot of k-points to produce
converged results. For large systems, the inverse scale with respect to ucvol
is unfortunately stopped because at least one k-point must be used. The
effective number of k-points to be used will be strongly influenced by the
symmetries of the system, since only the irreducible part of the Brillouin
zone must be sampled. Moreover the time-reversal symmetry (k equivalent to -k)
can be used for ground-state calculations, to reduce sometimes even further
the portion of the brillouin zone to be sampled. The number of k points to be
used in a calculation is named nkpt. There is another way to take advantage of
the time-reversal symmetry, in the specific case of k-points that are
invariant under k => -k , or are sent to another vector distant of the
original one by some vector of the reciprocal lattice. See below for more
explanation about the advantages of using these k-points.  
As a rule of thumb, for homogeneous systems, a reasonable accuracy may be
reached when the product of the number of atoms by the number of k-points in
the full Brillouin zone is on the order of 50 or larger, for wide gap
insulators, on the order of 250 for small gap semiconductors like Si, and
beyond 500 for metals, depending on the value of the input variable tsmear. As
soon as there is some vacuum in the system, the product natom * nkpt can be
much smaller than this (for an isolated molecule in a sufficiently large
supercell, one k-point is enough).  
The generation of special k point sets (Monkhorst-Pack sets) and band
structure k points can be done directly inside ABINIT. A list of interesting k
point sets, can be generated automatically, including a measure of their
accuracy in term of integration within the Brillouin Zone.  

* * *



### **2\. Related lesson(s) of the tutorial.**

* [The lesson 3](../../tutorial/generated_files/lesson_base3.html) deals with crystalline silicon (an insulator): the definition of a k-point grid, the smearing of the cut-off energy, the computation of a band structure, and again, convergence studies ...


* * *



### **3\. Related input variables.**

Basic input variables:

...
[chksymbreak](../../input_variables/generated_files/vargs.html#chksymbreak)
[CHecK SYMmetry BREAKing]  
... [kptopt](../../input_variables/generated_files/varbas.html#kptopt)
[KPoinTs OPTion]  
... [ngkpt](../../input_variables/generated_files/varbas.html#ngkpt) [Number
of Grid points for K PoinTs generation]  

Useful input variables:

... [istwfk](../../input_variables/generated_files/vardev.html#istwfk)
[Integer for choice of STorage of WaveFunction at each k point]  
... [kpt](../../input_variables/generated_files/varbas.html#kpt) [K - PoinTs]  
... [kptnrm](../../input_variables/generated_files/varbas.html#kptnrm) [K -
PoinTs NoRMalization]  
... [kptrlatt](../../input_variables/generated_files/vargs.html#kptrlatt) [K -
PoinTs grid : Real space LATTice]  
... [kptrlen](../../input_variables/generated_files/vargs.html#kptrlen) [K -
PoinTs grid : Real space LENgth]  
... [nkpt](../../input_variables/generated_files/varbas.html#nkpt) [Number of
K - Points]  
... [nshiftk](../../input_variables/generated_files/varbas.html#nshiftk)
[Number of SHIFTs for K point grids]  
... [shiftk](../../input_variables/generated_files/varbas.html#shiftk) [SHIFT
for K points]  
... [wtk](../../input_variables/generated_files/varbas.html#wtk) [WeighTs for
K points]  

Relevant internal variables:

... [%kptns](../../input_variables/generated_files/varint.html#kptns)
[K-PoinTs re-Normalized and Shifted]  

Input variables for experts:

... [kptbounds](../../input_variables/generated_files/vargs.html#kptbounds) [K
PoinT BOUNDarieS]  
... [ndivk](../../input_variables/generated_files/vargs.html#ndivk) [Number of
DIVisions of K lines]  
... [ndivsm](../../input_variables/generated_files/vargs.html#ndivsm) [Number
of DIVisions for the SMallest segment]  
... [vacuum](../../input_variables/generated_files/vargs.html#vacuum) [VACUUM
identification]  
... [vacwidth](../../input_variables/generated_files/vargs.html#vacwidth)
[VACuum WIDTH]  


* * *



### **4\. Selected input files.**

The user can find some related example input files in the ABINIT package in
the directory /tests, or on the Web:

tests/v2/Input: [t43.in](../../tests/v2/Input/t43.in)
[t44.in](../../tests/v2/Input/t44.in) [t61.in](../../tests/v2/Input/t61.in)
[t62.in](../../tests/v2/Input/t62.in) [t63.in](../../tests/v2/Input/t63.in)
[t64.in](../../tests/v2/Input/t64.in)  

