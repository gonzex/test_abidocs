---
authors: GG
---
Similarly to the PIMD, finding minimum energy paths and in particular
transition states for chemical transformations is of great importance in many
different fields. In ABINIT we have implemented two different flavours based
on interpolation methods [[Weinan2007]],[[Henkelman2000]], [[Mills1994]] and
controlled by the keyword [[imgmov]].

The calculation starts with the knowledge of the initial and final state
(local minima in the configuration space) and an educated guess for the
reaction pathway.

If the reaction path is not given, a linear interpolation between the
reactants and final products is constructed by a series of images
(configurations) that connect the two states, which are given by the keyword
[[nimage]].

The energy path that joins the series of images is then modified at each step
to allow the search over the lowest energy path joining the reactants and
products.

In the Nudged Elastic Band method (NEB), the images are connected through
springs, with a spring constant that has to be chosen such that the images are
uniformly spaced during the path search. The forces on each image come from
the potential energy surface of that configuration and a spring force from the
two closest configurations. The change in images is calculated by projecting
out the true force perpendicular to the path and the parallel projection of
the spring force with respect to the path [[Henkelman2000]].

The spring constant is obtained from the keyword [[neb_spring]] and the number
of iterations is given by [[ntimimage]]. In the String method, the system set
up is exactly the same as in the NEBM with the difference that no spring
constant needs to be defined. In this case, the forces are obtained as in the
NEB method from the true force perpendicular but now the configurations are
equally redistributed along the path at each iteration [[Weinan2007]]. In both
methods, the search stops if the number of predefined iterations
([[ntimimage]]) or the tolerance convergence criteria ([[tolimg]]) is reached.

As in the PIMD, each of the images can be treated in parallel and the
requested parallelization mode is set with the keyword [[npimage]].

Specified lattice parameters, or angles, or atomic positions, can be kept
fixed if needed, see [[topic_GeoConstraints]].

