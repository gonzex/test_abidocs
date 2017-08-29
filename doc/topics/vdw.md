---
authors: YPouillon, BVanTroeye
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to use Van der Waals functionals with the ABINIT package.

## Introduction

It is well known that long range correlations responsible of van der Waals
interactions are out of reach for both LDA and GGA approximations to the
exchange-correlation energy in DFT. In recent years several methods have been
devised to include such interactions, which can be grouped into two
strategies, namely _ad hoc_ methods and self-consistent approaches. Currently
ABINIT can perform calculations based on either the DFT-D methods or the vdW-
WF methods, as described later, both belonging to the first group.

A fully customizable implementation of the vdW-DF method [[Dion2004]], a self-
consistent approach, and an adaptation of the strategy followed by G.Roman-
Perez _et al._ [[Romanperez2009]] to the case of ABINIT are under development.
It will offer around 25 ajustable parameters and be delivered with graphical
tools to help users assess the quality of their kernels. It does not only aim
at performing production calculations with vdW-DF, but also at helping
researchers who develop new density functionals optimised for systems
requiring van-der-Waals interactions.

The DFT-D methods have been implemented inside ABINIT, namely DFT-D2
[[Grimme2006]], DFT-D3 [[Grimme2010]] and DFT-D3(BJ) [[Grimme2010a]]. In these
cases, pair-wise terms (and 3-body corrections for DFT-D3 and DFT-D3(BJ)) are
added to the DFT energy, which are independent of the electronic density, in
order to mimic the vdW interactions. The implementation includes the
contributions of these methods to forces and stresses, in view of geometry
optimization, as well as to first-order response functions like dynamical
matrices, clamped elastic constants and internal strain coupling parameters.

To activate DFT-D dispersion correction, two keywords are in use: [[vdw_xc]] =
5/6/7 to choose between DFT-D2, DFT-D3 and DFT-D3(BJ), and [[vdw_tol]], to
control the inclusion of largely distant pairs (those giving a contribution
below [[vdw_tol]] are ignored). It is also possible to include 3-body
corrections [[Grimme2010]] (for ground-state only) with the keyword
[[vdw_tol_3bt]], which also controls the tolerance over this term.

Methods based on maximally localized Wannier functions (MLWFs) to calculate
vdW energy corrections have also been implemented in ABINIT. In this case the
pair-wise terms come from contributions of pairs of MLWFs rather than from
atoms. Among the implemented methods in ABINIT it is found vdW-WF1
[[Silvestrelli2008]],[[Silvestrelli2009]] vdW-WF2 [[Ambrosetti2012]] and vdW-
QHO-WF [[Silvestrelli2013]]. A full description of the implementation of vdW-
WF1 is reported in [[Espejo2012]].

Selection of one of these 3 methods is achieved by using [[vdw_xc]]=10/11/14
respectivelly. Since vdW-WF1 and vdW-WF2 methods are approximations for the
dispersion energy of non overlapping electronic densities, it is necessary to
define the interacting fragments of the system whose dispersion energy is
going to be calculated. The latter is achieved by using the input variables
[[vdw_nfrag]] and [[vdw_typfrag]] to define the number of interacting
fragments in the unit cell and to assign each atom to a fragment. A given MLWF
belongs to the same fragment as its closer atom. The need for defining the
interacting fragments is overridden in the vdW-QHO-WF, for which these input
variables are not used. When dealing with periodic systems the input variable
[[vdw_supercell]] controls the number of neighbor unit cells that will be
included in the calculation. Each one of the 3 components of [[vdw_supercell]]
indicates the maximum number of cells along both positive or negative
directions of the corresponding primitive vector. This is useful for studying
the spacial convergency of the vdW energy. It should be noticed that the user
must set the variables associated to the calculation of MLWFs and that the
resulting vdW energies strongly depend on the obtained Wannier functions.



## Related Input Variables

*basic:*

- [[abinit:vdw_nfrag]]  Van Der Waals Number of interacting FRAGments
- [[abinit:vdw_supercell]]  Van Der Waals correction from Wannier functions in SUPERCELL
- [[abinit:vdw_tol_3bt]]  Van Der Waals TOLerance for 3-Body Term
- [[abinit:vdw_typfrag]]  Van Der Waals TYPe of FRAGment
 
*compulsory:*

- [[abinit:vdw_tol]]  Van Der Waals TOLerance
- [[abinit:vdw_xc]]  Van Der Waals eXchange-Correlation functional
 
*expert:*

- [[abinit:vdw_df_acutmin]]  vdW-DF MINimum Angular CUT-off
- [[abinit:vdw_df_aratio]]  vdW-DF Angle RATIO between the highest and
lowest angles.
- [[abinit:vdw_df_damax]]  vdW-DF Delta for Angles, MAXimum 
- [[abinit:vdw_df_damin]]  vdW-DF Delta for Angles, MINimum
- [[abinit:vdw_df_dcut]]  vdW-DF D-mesh CUT-off
- [[abinit:vdw_df_dratio]]  vdW-DF, between the highest and
lowest D, RATIO.
- [[abinit:vdw_df_dsoft]]  vdW-DF Distance for SOFTening.
- [[abinit:vdw_df_gcut]]  vdW-DF G-space CUT-off
- [[abinit:vdw_df_ndpts]]  vdW-DF Number of D-mesh PoinTS
- [[abinit:vdw_df_ngpts]]  vdW-DF Number of G-mesh PoinTS
- [[abinit:vdw_df_nqpts]]  vdW-DF Number of Q-mesh PoinTS
- [[abinit:vdw_df_nrpts]]  vdW-DF Number of R-PoinTS
- [[abinit:vdw_df_nsmooth]]  vdW-DF Number of SMOOTHening iterations
- [[abinit:vdw_df_phisoft]]  vdW-DF PHI value SOFTening.
- [[abinit:vdw_df_qcut]]  vdW-DF Q-mesh CUT-off
- [[abinit:vdw_df_qratio]]  vdW-DF, between highest and lowest Q, RATIO .
- [[abinit:vdw_df_rcut]]  vdW-DF Real-space CUT-off
- [[abinit:vdw_df_rsoft]]  vdW-DF radius SOFTening.
- [[abinit:vdw_df_threshold]]  vdW-DF energy calculation THRESHOLD
- [[abinit:vdw_df_tolerance]]  vdW-DF global TOLERANCE.
- [[abinit:vdw_df_tweaks]]  vdW-DF TWEAKS.
- [[abinit:vdw_df_zab]]  vdW-DF ZAB parameter
 
*useful:*

- [[abinit:irdvdw]]  Integer that governs the ReaDing of _VDW files
- [[abinit:prtwf]]  PRinT the WaveFunction
 

## Selected Input Files

*v7:*

- [[tests/v7/Input/t97.in]]
- [[tests/v7/Input/t98.in]]
- [[tests/v7/Input/t99.in]]
 
*vdwxc:*

- [[tests/vdwxc/Input/t10.in]]
 
*wannier90:*

- [[tests/wannier90/Input/t11.in]]
- [[tests/wannier90/Input/t12.in]]
- [[tests/wannier90/Input/t13.in]]
 
