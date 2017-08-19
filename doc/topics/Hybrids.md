---
authors: FJ
---
The Fock exchange term has been implemented in ABINIT, both in the norm-
conserving pseudopotential framework and in the PAW one. Some details about
the implementation in ABINIT can be found
[here](../documents/hybrids-2017.pdf).  
For an ABINIT user, to make a calculation of Fock exchange:  
\- do a first GGA dataset for the ground state  
\- do a second dataset for the Fock calculation choosing [[ixc]]=40-42 (HF,
PBE0, PBE0-1/3), -406 (PBE0-Libxc), -456 (PBE0-1/3 Libxc), or -427, -428
(HSE03, HSE06).

  
The energy and forces are available in the norm-conserving and PAW frameworks.
Stresses are available in the norm-conserving framework only for the moment.

WARNING:  
Forces and stresses cannot be calculated simultaneously for the moment.  
The spin polarised case has not been extensively tested for the moment.  
Use [[istwfk]]=1, [[iscf]]=2, [[paral_kgb]]=0, [[paral_atom]]=0.  
The efficiency of the calculation is not optimal. Work is in progress
concerning this point.

