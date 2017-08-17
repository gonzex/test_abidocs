---
authors: FJ
title: Crystalline structure and symmetries
---

This file gives hints on how to specify a crystal with the ABINIT package.

### **1\. Introduction.**

The cell may be orthogonal or non-orthogonal. Any kind of symmetries and
corresponding sets of k-point can be input, and taken into account in the
computation. The crystal structure and the position of the atoms in the unit
cell must be specified. Details about the way the crystal structure is defined
in ABINIT can be found [here](../documents/geometry.pdf).  
The code can automatically generate symmetries from the primitive cell and the
position of atoms. In this case, it identifies automatically the Bravais
lattice, point group and space group. Alternatively, it can start from the
symmetries and generate the atomic positions from the irreducible set. Also, a
database of the 230 spatial groups of symmetry is built inside ABINIT.  

* * *



### **2\. Related lesson(s) of the tutorial.**

* [The lesson 1](../../tutorial/generated_files/lesson_base1.html) deals with the H2 molecule : get the total energy, the electronic energies, the charge density, the bond length, the atomisation energy 
* [The lesson 2](../../tutorial/generated_files/lesson_base2.html) deals again with the H2 molecule: convergence studies, LDA versus GGA 
* [The lesson 3](../../tutorial/generated_files/lesson_base3.html) deals with crystalline silicon (an insulator): the definition of a k-point grid, the smearing of the cut-off energy, the computation of a band structure, and again, convergence studies ...
* [The lesson 4](../../tutorial/generated_files/lesson_base4.html) deals with crystalline aluminum (a metal), and its surface: occupation numbers, smearing the Fermi-Dirac distribution, the surface energy, and again, convergence studies ...


* * *



### **3\. Related input variables.**

Compulsory input variables:

... [acell](../../input_variables/generated_files/varbas.html#acell) [CELL
lattice vector scaling]  
... [rprim](../../input_variables/generated_files/varbas.html#rprim) [Real
space PRIMitive translations]  
... [xangst](../../input_variables/generated_files/varbas.html#xangst)
[vectors (X) of atom positions in cartesian coordinates -length in ANGSTrom-]  
... [xcart](../../input_variables/generated_files/varbas.html#xcart) [vectors
(X) of atom positions in CARTesian coordinates]  
... [xred](../../input_variables/generated_files/varbas.html#xred) [vectors
(X) of atom positions in REDuced coordinates]  

Useful input variables:

... [angdeg](../../input_variables/generated_files/varbas.html#angdeg) [ANGles
in DEGrees]  
... [chkprim](../../input_variables/generated_files/vargs.html#chkprim) [CHecK
whether the cell is PRIMitive]  
... [nsym](../../input_variables/generated_files/varbas.html#nsym) [Number of
SYMmetry operations]  
... [scalecart](../../input_variables/generated_files/varbas.html#scalecart)
[SCALE CARTesian coordinates]  
... [symrel](../../input_variables/generated_files/varbas.html#symrel)
[SYMmetry in REaL space]  
... [tnons](../../input_variables/generated_files/varbas.html#tnons)
[Translation NON-Symmorphic vectors]  

Input variables for experts:

... [brvltt](../../input_variables/generated_files/vargeo.html#brvltt)
[BRaVais LaTTice type]  
... [maxnsym](../../input_variables/generated_files/vardev.html#maxnsym)
[MAXimum Number of SYMetries]  
... [natrd](../../input_variables/generated_files/vargeo.html#natrd) [Number
of AToms ReaD]  
... [nobj](../../input_variables/generated_files/vargeo.html#nobj) [Number of
OBJects]  
... [objaat](../../input_variables/generated_files/vargeo.html#objaat) [OBJect
A : list of AToms]  
... [objaax](../../input_variables/generated_files/vargeo.html#objaax) [OBJect
A : AXis]  
... [objan](../../input_variables/generated_files/vargeo.html#objan) [OBJect A
: Number of atoms]  
... [objarf](../../input_variables/generated_files/vargeo.html#objarf) [OBJect
A : Repetition Factors]  
... [objaro](../../input_variables/generated_files/vargeo.html#objaro) [OBJect
A : ROtations]  
... [objatr](../../input_variables/generated_files/vargeo.html#objatr) [OBJect
A : TRanslations]  
... [objbat](../../input_variables/generated_files/vargeo.html#objbat) [OBJect
B : list of AToms]  
... [objbax](../../input_variables/generated_files/vargeo.html#objbax) [OBJect
B : AXis]  
... [objbn](../../input_variables/generated_files/vargeo.html#objbn) [OBJect B
: Number of atoms]  
... [objbrf](../../input_variables/generated_files/vargeo.html#objbrf) [OBJect
B : Repetition Factors]  
... [objbro](../../input_variables/generated_files/vargeo.html#objbro) [OBJect
B : ROtations]  
... [objbtr](../../input_variables/generated_files/vargeo.html#objbtr) [OBJect
B : TRanslations]  
... [spgaxor](../../input_variables/generated_files/vargeo.html#spgaxor)
[SPace Group : AXes ORientation]  
... [spgorig](../../input_variables/generated_files/vargeo.html#spgorig)
[SPace Group : ORIGin]  
... [spgroup](../../input_variables/generated_files/vargeo.html#spgroup)
[SPace GROUP number]  
... [symmorphi](../../input_variables/generated_files/vardev.html#symmorphi)
[SYMMORPHIc symmetry operation selection]  
... [vaclst](../../input_variables/generated_files/vargeo.html#vaclst)
[VACancies LiST]  
... [vacnum](../../input_variables/generated_files/vargeo.html#vacnum)
[VACancies NUMber]  
... [xyzfile](../../input_variables/generated_files/vargeo.html#xyzfile) [XYZ
FILE input for geometry]  


* * *



### **4\. Selected input files.**

The user can find some related example input files in the ABINIT package in
the directory /tests, or on the Web:

tests/v1/Input: [t40.in](../../tests/v1/Input/t40.in)
[t42.in](../../tests/v1/Input/t42.in) [t43.in](../../tests/v1/Input/t43.in)

tests/v3/Input: [t21.in](../../tests/v3/Input/t21.in)
[t23.in](../../tests/v3/Input/t23.in) [t24.in](../../tests/v3/Input/t24.in)
[t25.in](../../tests/v3/Input/t25.in) [t26.in](../../tests/v3/Input/t26.in)
[t27.in](../../tests/v3/Input/t27.in) [t28.in](../../tests/v3/Input/t28.in)
[t29.in](../../tests/v3/Input/t29.in) [t32.in](../../tests/v3/Input/t32.in)
[t33.in](../../tests/v3/Input/t33.in) [t34.in](../../tests/v3/Input/t34.in)
[t35.in](../../tests/v3/Input/t35.in) [t36.in](../../tests/v3/Input/t36.in)

tests/v5/Input: [t14.in](../../tests/v5/Input/t14.in)  

