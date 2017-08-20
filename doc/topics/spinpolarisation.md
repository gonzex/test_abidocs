---
authors: FJ
---

## ** Introduction **

The electronic system may be computed in the spin-unpolarized or spin-
polarized case, with the possibility to impose occupation numbers of majority
and minority spins, and the spins of the starting configuration. A specific
option for efficient treatment of anti-ferromagnetism (Shubnikov groups) is
available. The treatment of non-collinear magnetism is available (some details
of the implementation can de found [here](../documents/noncol.pdf)). The total
magnetic moment of the unit cell can be constrained. The local magnetization
can also be constrained.



## ** Related Input Variables **

*basic:*

- [[abinit:nspden]]  Number of SPin-DENsity components
- [[abinit:nspinor]]  Number of SPINORial components of the wavefunctions
- [[abinit:nsppol]]  Number of SPin POLarization
- [[abinit:spinat]]  SPIN for AToms
 
*internal:*

- [[abinit:ptgroupma]]  PoinT GROUP number for the MAgnetic space group
 
*useful:*

- [[abinit:diemixmag]]  model DIElectric MIXing factor for the MAGgnetization
- [[abinit:genafm]]  GENerator of the translation for Anti-FerroMagnetic space group
- [[abinit:pawspnorb]]  PAW - option for SPiN-ORBit coupling
- [[abinit:so_psp]]  Spin-Orbit treatment for each PSeudoPotential
- [[abinit:spgroupma]]  SPace GROUP number defining a MAgnetic space group
- [[abinit:spinmagntarget]]  SPIN-MAGNetization TARGET
- [[abinit:spnorbscl]]  SPin-ORBit SCaLing
- [[abinit:symafm]]  SYMmetries, Anti-FerroMagnetic characteristics
 

## ** Selected Input Files **

*v1:*

- [[tests/v1/Input/t21.in]]
- [[tests/v1/Input/t39.in]]
 
*v2:*

- [[tests/v2/Input/t74.in]]
- [[tests/v2/Input/t75.in]]
 
*v3:*

- [[tests/v3/Input/t22.in]]
- [[tests/v3/Input/t23.in]]
- [[tests/v3/Input/t51.in]]
 
*v5:*

- [[tests/v5/Input/t16.in]]
- [[tests/v5/Input/t17.in]]
- [[tests/v5/Input/t51.in]]
 
*v7:*

- [[tests/v7/Input/t05.in]]
- [[tests/v7/Input/t06.in]]
- [[tests/v7/Input/t07.in]]
 

