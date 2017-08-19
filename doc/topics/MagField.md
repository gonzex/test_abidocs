---
authors: EB
---
An applied external magnetic field has been implemented in ABINIT by
considering the Zeeman spin response only (i.e., neglecting the orbital
contribution).

Following the procedure of Bousquet et al.,[[Bousquet2011]] the applied **B**
field is introduced by adding the "Zeeman term" term in the non-collinear
Kohn-Sham potential:

This contribution is trivial to implement, and also dominant in amplitude, but
has historically been neglected with respect to the orbital responses, which
are rich in more complex physics.

Unlike an applied electric field, such a Zeeman term in the potential is
compatible with periodic boundary conditions. It is also compatible with
collinear calculations by reducing its application on ``up'' and ``down'' spin
channels with **B**=B**e**z.

In ABINIT, the finite Zeeman field is controlled by the keyword
[[zeemanfield]] which allows to control the amplitude of the applied
**B**-field (in Tesla) along the three cartesian directions.

Such an applied Zeeman field allows one to calculate the spin contribution of
the magnetic and magnetoelectric susceptibilities, and to observe phase
transitions under finite magnetic field, if present.

