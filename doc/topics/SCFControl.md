---
authors: XG
---
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

