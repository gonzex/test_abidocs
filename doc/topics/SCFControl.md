---
authors: XG
---

## ** Introduction **

The numerical precision of the calculations depends on many settings, among
which the precision in solving the Kohn-Sham self-consistent equation.

Several parameters govern the SCF loop. The maximum number of cycles is given
by [[nstep]], but the iterative procedure might be stopped earlier, as soon as
the criterion chosen by the user is fulfilled. The user is asked to give a
tolerance on some measure of the convergence. The user must choose among
[[toldfe]], [[toldff]], [[tolrff]], [[tolvrs]] and [[tolwfr]].

  * The most theoretically justified for the density/potential self-consistency is [[tolvrs]].
  * [[tolwfr]] is interesting for non-self-consistent calculations.
  * For molecular dynamics (which rely on the accuracy of forces), one might prefer [[tolrff]].

Some input variables relate to the solution of the Schrodinger equation.
However, usually the related iterative techniques are well-tuned, so that
these input variables ([[nline]] and [[tolrde]]) are usually used only by
experts. However, in cases where the convergence is difficult, it might be
interesting to test improving them, as well as modifying [[nnsclo]].

The [[accuracy]] variable enables to tune the accuracy of a calculation by
setting automatically up to seventeen variables.



## ** Related Input Variables **

*basic:*

- [[abinit:accuracy]]  ACCURACY
- [[abinit:nstep]]  Number of (non-)self-consistent field STEPS
- [[abinit:toldfe]]  TOLerance on the DiFference of total Energy
- [[abinit:toldff]]  TOLerance on the DiFference of Forces
- [[abinit:tolrff]]  TOLerance on the Relative diFference of Forces
- [[abinit:tolvrs]]  TOLerance on the potential V(r) ReSidual
- [[abinit:tolwfr]]  TOLerance on WaveFunction squared Residual
 
*expert:*

- [[abinit:nline]]  Number of LINE minimisations
- [[abinit:nnsclo]]  Number of Non-Self Consistent LOops
- [[abinit:tolrde]]  TOLerance on the Relative Difference of Eigenenergies
 
*useful:*

- [[abinit:nbdbuf]]  Number of BanDs for the BUFfer
 

## ** Selected Input Files **

No input file associated to this topic.

