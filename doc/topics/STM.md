---
authors: XG
---

## ** Introduction **

The charge density of states close to the Fermi energy can be output, and
provide a simple approach to STM image calculations (not for PAW). See input
variable [[prtstm]] and [[stmbias]] for explanations. The example input file
will also be useful. The angular momentum decomposed DOS can be evaluated in a
sphere around any point, and provide STS analysis.



## ** Related Input Variables **

*basic:*

- [[abinit:tsmear]]  Temperature of SMEARing
 
*compulsory:*

- [[abinit:occopt]]  OCCupation OPTion
- [[abinit:prtstm]]  PRinT the STM density
- [[abinit:stmbias]]  Scanning Tunneling Microscopy BIAS voltage
 

## ** Selected Input Files **

*v4:*

- [[tests/v4/Input/t46.in]]
 

