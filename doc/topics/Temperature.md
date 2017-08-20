---
authors: XG
---

## ** Introduction **

When the phonon band structure and corresponding eigenvectors are known over
the whole Brillouin Zone, thanks fo Fourier interpolation (see
[[topic:PhononBands]]), integrals can be performed, allowing to obtain a
wealth of properties, like free energy, entropy, specific heat, as well as
atomic temperature factors. For applications of this technique, see
[[Lee1995]].

Moreover, knowing such information for different volumes allows one to compute
the thermal expansion, see [[anaddb:gruns_ddbs]].

The input variables needed to perform the interpolation over the Brillouin
Zone are described in [[topic:PhononBands]] and are not listed again in the
present topic.



## ** Related Input Variables **

*basic:*

- [[anaddb:gruns_nddbs]]  GRUNeiSen Number of DDB files
- [[anaddb:ntemper]]  Number of TEMPERatures
- [[anaddb:temperinc]]  TEMPERature INCrease
- [[anaddb:tempermin]]  TEMPERature MINimum
 
*compulsory:*

- [[anaddb:thmflag]]  THerMal FLAG
 
*expert:*

- [[anaddb:atftol]]  ATomic Temperature Factor TOLerance
 
*useful:*

- [[anaddb:gruns_ddbs]]  GRUNeiSen DDBS
- [[anaddb:prtvol]]  PRinT VOLume
- [[anaddb:thmtol]]  THerModynamic TOLerance
 

## ** Selected Input Files **

*v2:*

- [[tests/v2/Input/t15.in]]
- [[tests/v2/Input/t16.in]]
 

