---
authors: GG
---
Three molecular dynamics algorithm (Numerov, Verlet, Blanes and Moanes) allow
to perform simulations in real (simulated) time, see [[ionmov]]. The
displacement of atoms may be computed according to Newton's law, or by adding
a friction force to it. Nose-Hoover thermostat is available with Verlet
algorithm. Langevin dynamics is also available.

Specified lattice parameters, or angles, or atomic positions, can be kept
fixed if needed, see [[topic_GeoConstraints]].

The trajectories can be analyzed thanks to the [[topic:APPA|APPA
postprocessor]].

