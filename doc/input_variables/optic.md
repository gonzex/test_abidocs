## **broadening** 


*Mnemonics:* BROADENING  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.d-3 Ha  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





In Eq. 46 of [Ref. 1](../../users/generated_files/help_optic.html#Ref1), it is
clear that when ever wnm(k) is equal to w, there is a resonance. Numerically
this would lead to an infinity. In order to avoid this one could do two
things. You could change the sum over k-points to integration and then use
linear tetrahedron method (see [Ref.
2](../../users/generated_files/help_optic.html#Ref2) for details). Another way
to get around the problem is, like we do in the present case, avoid this
singularity by adding a small complex number to the denominator. This prevents
the denominator from ever going to 0 and acts as a broadening to the spectrum.
The broadening should not be too large as this would wash out the features in
the spectrum.


* * *

## **ddkfile** 


*Mnemonics:* DDK FILE  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* string  
*Dimensions:* scalar  
*Default value:* None  
*Comment:* no default  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





Specify the filename that has been produced by the preparatory Abinit run.
This file must contain the matrix elements of the d/dk operator along
direction X. It must not contain the first-order wavefunctions and may be
generated using [[prtwf]] 3.  
You should make sure that the number of bands, of spin channels and of
k-points are the same in all the files.

use as string with the filename: ddkfile_X, where X is the file number.


* * *

## **domega** 


*Mnemonics:* Delta OMEGA  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.d-3 Ha  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





The step and maximum sets your energy grid for the calculation using the
formula number of energy mesh points=maximum/step (zero excluded). So in order
to capture more features you can decrease the step size to get a finer energy
grid. In order to go to higher frequency, increase the maximum.


* * *

## **lin_comp** 


*Mnemonics:* LINear COMPonents  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* integer  
*Dimensions:* (['num_lin_comp'])  
*Default value:* 0  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





This tells which component of the dielectric tensor you want to calculate.
These numbers are called a and b Eqs. 46 in [Ref.
1](../../users/generated_files/help_optic.html#Ref1). 1 2 3 represent x y and
z respectively. For example 11 would be xx and 32 would mean zy.


* * *

## **maxomega** 


*Mnemonics:* MAXimum value of OMEGA  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1 Ha  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





The step and maximum sets your energy grid for the calculation using the
formula number of energy mesh points=maximum/step (zero excluded). So in order
to capture more features you can decrease the step size to get a finer energy
grid. In order to go to higher frequency, increase the maximum.


* * *

## **nonlin_comp** 


*Mnemonics:* NON-LINear COMPonents  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* integer  
*Dimensions:* (['num_nonlin_comp'])  
*Default value:* 0  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





This tells which component of the dielectric tensor you want to calculate.
These numbers are called a, b and c in [Ref.
1](../../users/generated_files/help_optic.html#Ref1). 1 2 3 represent x y and
z respectively. For example 111 would be xxx and 321 would mean zyx.


* * *

## **num_lin_comp** 


*Mnemonics:* NUMber of LINear COMPonents  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





How many components out of 9 of the linear optical dielectric tensor do you
want to calculate. Most of these are either equal or zero depending upon the
symmetry of the material (for detail see [Ref.
3](../../users/generated_files/help_optic.html#Ref3)).  
Note that the directions are along the Cartesian axis.


* * *

## **num_nonlin_comp** 


*Mnemonics:* NUMber of NON-LINear COMPonents  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* integer  
*Dimensions:* scalar  
*Default value:* 0  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





How many components out of 27 of the non-linear optical dielectric tensor do
you want to calculate. Most of these are either equal or zero depending upon
the symmetry of the material (for detail see [Ref.
3](../../users/generated_files/help_optic.html#Ref3)).  
Note that the directions are along the Cartesian axis.


* * *

## **scissor** 


*Mnemonics:* SCISSOR operator  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 0.0  
*Comment:* in Ha  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





LDA/GGA are well known to underestimate the band-gap by up to 100%. In order
to get the optical spectrum and make a realistic comparison with experiments
one needs to correct for this. This can be achieved in two ways. The scissors
shift is normally chosen to be the difference between the experimental and
theoretical band-gap and is used to shift the conduction bands only. Another
way in which you do not have to rely on experimental data is to determine the
self energy using the [GW
approach](../../tutorial/generated_files/lesson_gw1.html). In this case the
opening of the gap due to the GW correction can be used as scissor shift.


* * *

## **tolerance** 


*Mnemonics:* TOLERANCE  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* real  
*Dimensions:* scalar  
*Default value:* 1.d-3 Ha  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





When energy denominators are smaller than **tolerance**, the term is discarded
from the sum.


* * *

## **wfkfile** 


*Mnemonics:* WaveFunction K FILE  
*Mentioned in topic(s):* Optic_basic  
*Variable type:* string  
*Dimensions:* scalar  
*Default value:* None  
*Comment:* no default  
Test list:

- tutorespfn:  [[tests/tutorespfn/Input/toptic_2.in]], [[tests/tutorespfn/Input/toptic_4.in]]
- v4:  [[tests/v4/Input/t57.in]]
- v67mbpt:  [[tests/v67mbpt/Input/t53.in]]
- v7:  [[tests/v7/Input/t42.in]], [[tests/v7/Input/t48.in]]





Specify the filename that has been produced by the preparatory Abinit run.
This file must contain the matrix elements of the d/dk operator along
direction X. It must not contain the first-order wavefunctions and may be
generated using [[prtwf]] 3.  
You should make sure that the number of bands, of spin channels and of
k-points are the same in all the files.


* * *
