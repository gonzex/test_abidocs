---
authors: MT
description: PhononBands Abinit topic
rpath: /topics/PhononBands.md
---
<!--
This file is automatically generated by mksite.py. All changes will be lost.
Change the input yaml files or the python code
-->

This page gives hints on how to compute phonon bands, density of states, interatomic force constants, sound
velocity ... with the ABINIT package.

## Introduction

The Fourier transformation of the phonon dynamical matrices generates
interatomic force constants in real space, as explained in [[Gonze1997a]].
Backtransforming to reciprocal space gives the Fourier interpolation of the
initial phonon band structure. After such Fourier interpolation, the DOS can
be produced (see [[Lee1995]]), the phonon eigenenergies plotted along lines,
the slope of the energy versus cristalline momentum evaluated (to give sound
velocity).

The two-phonon sum and difference spectra can also be obtained, see
[[anaddb:dossum]].

For the related computation of temperature-dependent properties, see
[[topic_Temperature]].



## Related Input Variables

*basic:*

- [[anaddb:asr]]  Acoustic Sum Rule
- [[anaddb:atifc]]  AToms for IFC analysis
- [[anaddb:dipdip]]  DIPole-DIPole interaction
- [[anaddb:dossum]]  DOS SUM
- [[anaddb:ndivsm]]  Number of DIVisions for the SMallest segment
- [[anaddb:ngqpt]]  Number of Grids points for Q PoinTs
- [[anaddb:nph1l]]  Number of PHonons in List 1
- [[anaddb:nph2l]]  Number of PHonons in List 2
- [[anaddb:nqpath]]  Number of Q wavevectors defining a PATH
- [[anaddb:prtdos]]  PRinT the phonon Density Of States
- [[anaddb:qpath]]  Q wavevectors defining a PATH
- [[anaddb:qph1l]]  Q for PHonon List 1
- [[anaddb:qph2l]]  PHonon List 2
 
*compulsory:*

- [[anaddb:ifcflag]]  Interatomic Force Constants FLAG
 
*expert:*

- [[anaddb:freeze_displ]]  FREEZE DISPLacement of phonons into supercells
- [[anaddb:nchan]]  Number of CHANnels
- [[anaddb:ngrids]]  Number of GRIDS
- [[anaddb:outboltztrap]]  OUTput files for BOLTZTRAP code
- [[anaddb:outscphon]]  OUTput files for Self Consistent PHONons
- [[anaddb:prtbltztrp]]  PRinT input files for BoLTZTRaP code.
- [[anaddb:qrefine]]  Q-point REFINEment order (experimental)
 
*useful:*

- [[anaddb:brav]]  BRAVais
- [[anaddb:dosdeltae]]  DOS DELTA in Energy
- [[anaddb:dossmear]]  DOS SMEARing value
- [[anaddb:dostol]]  DOS TOLerance
- [[anaddb:eivec]]  EIgenVECtors
- [[anaddb:enunit]]  ENergy UNITs
- [[anaddb:iatprj_bs]]  Indices of the AToms for the PRoJection of the phonon Band Structure
- [[anaddb:ifcana]]  IFC ANAlysis
- [[anaddb:ifcout]]  IFC OUTput
- [[anaddb:natifc]]  Number of AToms for IFC analysis
- [[anaddb:natprj_bs]]  Number of AToms for PRoJection of the Band Structure
- [[anaddb:ng2qpt]]  Number of Grids points for Q PoinTs (grid 2)
- [[anaddb:nqshft]]  Number of Q SHiFTs
- [[anaddb:nsphere]]  Number of atoms in SPHERe
- [[anaddb:nwchan]]  Number of Widths of CHANnels
- [[anaddb:prt_ifc]]  PRinT the Interatomic Force Constants
- [[anaddb:prtddb]]  PRinT the Derivative DataBase files
- [[anaddb:prtphbands]]  PRinT PHonon BANDS
- [[anaddb:prtsrlr]]  PRinT the Short-Range/Long-Range decomposition of phonon FREQuencies
- [[anaddb:prtvol]]  PRinT VOLume
- [[anaddb:q1shft]]  Q shifts for the grid number 1
- [[anaddb:q2shft]]  Q points SHiFTs for the grids 2
- [[anaddb:rifcsph]]  Radius of the Interatomic Force Constant SPHere
- [[anaddb:symdynmat]]  SYMmetrize the DYNamical MATrix
- [[anaddb:vs_qrad_tolkms]]  Speed of Sound Q-radius, TOLerance KiloMeter/Second
 

## Selected Input Files

*v2:*

- [[tests/v2/Input/t15.in]]
- [[tests/v2/Input/t16.in]]
- [[tests/v2/Input/t17.in]]
- [[tests/v2/Input/t19.in]]
- [[tests/v2/Input/t20.in]]
- [[tests/v2/Input/t22.in]]
- [[tests/v2/Input/t25.in]]
- [[tests/v2/Input/t28.in]]
- [[tests/v2/Input/t29.in]]
- [[tests/v2/Input/t32.in]]
- [[tests/v2/Input/t39.in]]
 
*v5:*

- [[tests/v5/Input/t95.in]]
 
*v6:*

- [[tests/v6/Input/t76.in]]
 

## Tutorials

* [[lesson_rf2|The lesson Response-Function 2 (RF2)]] presents the analysis of the DDBs that have been introduced in the [[lesson_rf1]]. The computation of the interatomic forces and the computation of thermodynamical properties is an outcome of this lesson.
