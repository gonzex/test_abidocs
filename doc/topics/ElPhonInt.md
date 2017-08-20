---
authors: MV
---

## ** Introduction **

The theory and details of the implementation are described in [[Gonze2009]]
and [[Gonze2016]].

Basic calculations of electron-phonon interaction in ABINIT: one performs a
normal ground state, then DFPT phonon calculations (using [[rfphon]], with
added keywords [[prepgkk]] and [[prtgkk]], which saves the matrix elements to
files suffixed GKK. The main change in this respect is that [[prtgkk]] now
disables the use of symmetry in reducing q-points and perturbations. This
avoids ambiguities in wave function phases due to band degeneracies. The
resulting GKK files are merged using the mrggkk utility, and processed by
anaddb.

With the implementation of phonons in PAW DFPT, the electron phonon coupling
is also available in PAW, though this has not yet been tested extensively. The
input variables for electron-phonon coupling in anaddb are described in
[[Gonze2009]] and [[Gonze2016]].

Some details about the calculation of electron-phonon quantities in ABINIT and
ANADDB can be found [here](../documents/elphon_manual.pdf).

Subsequently, the GKK file is used to compute many quantities, as explained in
[[topic_PhononWidth]], [[topic_TDepES]] and [[topic_ElPhonTransport]].

A brand new ABINIT driver, focusing on the treatment of electron-phonon
interaction is under development. Most of the input variables for experts,
with [[optdriver]]==7 are related to this development, that is not yet
operational as of v8.5 .



## ** Related Input Variables **

*expert:*

- [[anaddb:ep_prt_yambo]]  Electron Phonon PRinTout YAMBO data
- [[anaddb:symgkq]]  SYMmetrize the GKk matrix elements for each Q
 
*useful:*

- [[anaddb:gkqwrite]]  GKk for input Q grid to be WRITtEn to disk
 

## ** Selected Input Files **

*v5:*

- [[tests/v5/Input/t96.in]]
- [[tests/v5/Input/t97.in]]
- [[tests/v5/Input/t98.in]]
 
*v7:*

- [[tests/v7/Input/t89.in]]
- [[tests/v7/Input/t90.in]]
- [[tests/v7/Input/t91.in]]
- [[tests/v7/Input/t92.in]]
 

