---
authors: FJ
---
The PAW atomic data can be used with plane waves as well as with wavelets.
Specificities of PAW for use with planewaves are presented here. See
[[topic_Wavelets]] for its use with wavelets.

The way the PAW method is implemented with planewaves in ABINIT is described
in [[Torrent2008]].  
The use of PAW atomic data (equivalent to pseudopotential file for the norm-
conserving case) automatically launch a PAW calculation. ABINIT is provided
with the JTH [[Jollet2014]] PAW atomic data table on the ABINIT web site.  
To perform a standard PAW calculation, the input file is the same than for a
norm-conserving one, except that the variable [[pawecutdg]] must be specified
(see below). In the case the input variable [[accuracy]] is used, the input
variable [[pawecutdg]] is automatically used.  
Some physical functionalities are available only in the PAW framework: DFT+U,
DMFT, local exact exchange,...

