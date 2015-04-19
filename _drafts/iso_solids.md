---
layout: post
title: Are your solids the same as my solids?
author: Hugo Ledoux
category: blog
tags: 3D, OGC
comments: true
---

While the definitions found in the OGC/ISO Simple Features specifications for 2D primitives are well-accepted and used in practice by virtually everyone, I have noticed that the ones for 3D primitives (especially for the volumetric primitive, called a *solid* or a *polyhedron*) are in almost all cases ignored by software vendors, by practitioners and even by academics[^academics].
Most vendors now have a 3D module (whatever that means), but unfortunately they take great liberties in defining what "3D GIS" means---and no a perspective view on a 2.5D terrain doesn't qualify in my opinion.
They are all implementing their own version of what they think a solid should be, or rather, what they can technically implement at the moment.
<!-- The data structure they have drives the definition---shouldn't it be the opposite? -->
And to make things worse, the definition they used is rarely defined or documented.
Exchanging and converting datasets from one format/platform to another is thus highly problematic, and in my opinion it hinders severely the use and the development of 3D functions.


I must admit that representing a solid is far more complex than representing a 2D polygon, and that different disciplines have rather different definitions.
This is best illustrated by Grünbaum (2003)[^Grunbaum03] who states that even in the field of mathematics opinions differ as to what constitutes the term "polyhedron".
Some use it only for a regular polyhedron, or only for a convex one, and some consider non-planar faces as part of the definition.
The authoritative textbook on computational geometry[^compgeobook] characterises the term as "difficult to define", and give a simple definition that is probably the most common one: a polyhedron is a 3D solid bounded by planar faces. 
The bounding faces are thus planar surfaces embedded in the 3D Euclidean space, and the bounding surfaces form a *closed two-dimensional manifold* (or 2-manifold for short).
A 2-manifold is a topological space that is topologically equivalent to a 2D space---an obvious example is the surface of the Earth, for which near to every point the surrounding area is topologically equivalent to a plane. 


This definition, that a solid is a 2-manifold, is also often used in the CAD world and in GIS.
One of the main reason is simplicity: representing and storing a 2-manifold can be done with data structures that are intrinsically 2D since each edge is guaranteed to have a maximum of two incident faces and that around each vertex the incident faces form one "umbrella".
This means that one doesn't have to dramatically change the internal of her systems since the good old *node-arc-face* generalises directly to 3D.
While this sounds great, it also means that non-manifold objects are impossible to represent, and, perhaps worse, 3D objects are *individually* stored and represented.
That is, the topological relationships between 2 adjacent buildings cannot be explicitly stored.


# What is an ISO19107 solid? 

ISO19107[^ISO19107] defines different geometric primitives: a 0D primitive is a GM_Point, a 1D a GM\_Curve, a 2D a GM\_Surface, and a 3D a GM\_Solid. 
A primitive is built with lower-dimensional primitives, eg in the following figure the GM\_Surface is composed of 2 (closed) GM\_Curves, which are composed on several GM\_Points.

![]({{ site.baseurl }}/img/isoprimitives.pdf.png)

Observe that primitives do not need to be linear or planar, ie curves defined by mathematical functions are allowed.
In our context, the following three definitions from ISO19107 are relevant:

> A GM_Solid is the basis for 3-dimensional geometry. The extent of a solid is defined by the boundary surfaces. The boundaries of GM_Solids shall be represented as GM_SolidBoundary. […] The GM_OrientablesSurfaces that bound a solid shall be oriented outward.

> A GM\_Shell is used to represent a single connected component of a GM\_SolidBoundary. It consists of a number of references to GM\_OrientableSurfaces connected in a topological cycle (an object whose boundary is empty). [...] Like GM\_Rings, GM\_Shells are simple.

> A GM\_Object is *simple* if it has no interior point of self-intersection or self-tangency. In mathematical formalisms, this means that every point in the interior of the object must have a metric neighbourhood whose intersection with the object is isomorphic to an *n*-sphere, where *n* is the dimension of this GM\_Object.

The bounding surfaces of a shell thus form a *closed* and *orientable* 2-manifold. 
Closed means that there should not be 'holes' in the surface (in other words, it should be watertight).

A solid that respects that definition is as follows:

![One solid which respects the international definition. It has one exterior shell and one interior shell (forming a cavity).](figs/isosolid.pdf)

First observe that the solid is composed of two shells (both forming its boundaries), one being the exterior and one being the interior shell. 
This is conceptually the same as a 2D polygon that has an inner ring.
The exterior shell has eleven surfaces, and the interior one six. 
An interior shell creates a cavity in the solid---cavities are also referred to as 'voids' or holes in a solid. 
A solid can have no inner shells, or several. 
Observe that a cavity is not the same as a hole in a torus (a donut) such as that in the following figure: it can be represented with one exterior shell having a genus of 1 and no interior shell.

![A 'squared torus' is modelled with one exterior boundary formed of ten surfaces. Notice that there are no interior boundary.](figs/torus.png)


# Interactions between the shells of a solid

According to the ISO abstract specifications, the different boundaries of a solid are allowed to interact with each other, but only under certain circumstances.
To understand these, we have to generalise to 3D the implementation specifications defined in 2D by the OGC (since they do not exist yet in 3D):

> 1. Polygons are topologically closed;
  2. The boundary of a Polygon consists of a set of LinearRings that make up its exterior and interior boundaries;
  3. No two Rings in the boundary cross and the Rings in the boundary of a Polygon may intersect at a Point but only as a tangent, eg 
    $$\forall P \in Polygon, \forall c1, c2 \in P.Boundary(), c1 \neq c2,$$
    $$\forall p, q \in Point, p, q \in c1, p \neq q, [p \in c2 \Rightarrow q \notin c2];$$
  4. A Polygon may not have cut lines, spikes or punctures, eg 
    $$\forall P \in Polygon, P = P.Interior.Closure;$$
  5. The interior of every Polygon is a connected point set;
  6. The exterior of a Polygon with 1 or more holes is not connected. Each hole defines a connected component of the exterior.

Observe that all of them, except the 3rd one, generalise directly to 3D since a point-set topology nomenclature is used.
The only modifications needed are that, in 3D, polygons become solids, rings become shells, and holes become cavities.

To further explain what the assertions are in 3D, Figure~\ref{fig:validornot} shows 12 solids, some of them valid, some not; all the statements below refer to solids in this figure.
The first assertion of the OGC means that a solid must be closed, or 'watertight' (even if it contains interior shells).
The solid *s*<sub>1</sub> is thus not valid but *s*<sub>2</sub> is since the hole in the top surface is `filled' with other faces.

The second assertion implies that each shell must be simple, ie that it is a 2-manifold.

The third assertion means that the boundaries of shells can intersect each others, but the intersection between the shells can only contain primitives of dimensionality 0 (vertices) and 1 (edges).
If a surface or a volume is contained, then the solid is not valid.
The solid *s*<sub>3</sub> is an example of a valid solid: it has two interior shells whose boundaries intersect at one point (at the apexes of the tetrahedra), and the apex of one of the tetrahedra is coplanar with the exterior shell.
If the interior of the two interior shells intersects (as in *s*<sub>4</sub>) the solid is not valid; this is also related to the sixth assertion stating that each cavity must define one connected component: if the interior of two cavities are intersecting they define the same connected component.
Notice also that *s*<sub>5</sub> is not valid since one surface of its cavity intersects with one surface of the exterior shell (they "share a surface"); *s*<sub>5</sub> should be represented with one single exterior shell (having a 'dent'), and no interior shell.

The fourth assertion states that a shell is a 2-manifold and that no dangling pieces can exist (such as that of *s*<sub>6</sub>); it is equivalent to the *regularisation* of a point-set in 3D.

The fifth assertion states that the interior of a solid must form a connected point-set (in 3D).
Consider the solid *s*<sub>7</sub>, it is valid since its interior is connected and it fulfils the other assertions; notice that it is a 2-manifold but that unlike other solids in the figure (except *s*<sub>8</sub>) its genus is 1.
If we move the location of the triangular prism so that it touches the boundary of the exterior shell (as in *s*<sub>8</sub>), then the solid becomes invalid since its interior is not connected anymore, and also since its exterior shell is not simple anymore (2 edges have 4 incident planar faces, which is not 2-manifold).
It is also possible that the interior shell of a solid separates the solid into two parts: the interior shell of *s*<sub>9</sub> is a pyramid having four of its edges intersecting with the exterior shell, but no two surfaces are shared, thus these interactions are allowed.
However, the presence of the pyramid separates the interior of the solid into two unconnected volumes (violating assertion 5); for both *s*<sub>8</sub> and *s*<sub>9</sub>, the only possible valid representation is with two different solids.

Notice also that for a solid to be valid, all its lower-dimensionality primitives must be valid.
That is, each surface of the shells (represented with polygons) has to be individually valid according to the Simple Features assertions.
Since these are embedded in 3D, they have to be planar.
That is a polygon must have all its points lying on a plane.
An example of an invalid surface would be one having a hole (an inner ring) overlapping the exterior ring (see *s*<sub>10</sub>).

# Solids as implemented in practice (eg with CityGML)

![UML diagram of the CityGML geometry model.](figs/citygmlgeom)

CityGML uses the ISO19107 geometric primitives for representing the geometry of its objects. 
However, only a subset is used, with the following two restrictions: (1) GM\_Curves can only be *linear* (thus only LineStrings and LinearRings are used); (2) GM\_Surfaces can only be *planar* (thus Polygons are used). The primitives for constructing Shells and Solids are:

![2D CityGML primitives.](figs/citygmlprimitives)

A LineString is a Curve with linear interpolation between each Point; each two consecutive Points defines a line segment. 
A LinearRing is a LineString that is both closed and simple.

A Polygon is a surface patch that is defined by a set of boundary curves and an underlying surface to which these curves adhere. 
The default is that the curves are coplanar and the polygon uses planar interpolation in its interior.

Each shell of a solid is thus composed of Polygons, and these can have inner rings (which are often referred to as holes). 
Observe that the top polygon of the ISO solid above has one inner ring, but that other polygons 'fill' that hole so that the exterior shell is 'watertight' (ie it has no holes and is thus closed).


# Requirements for validity of solids

Each primitive used to construct a higher-dimensional primitive should be valid. 
This means that in order to validate a solid, we need to also ensure that each ring and polygon used be valid. 
For rings and polygons, observe that these will be embedded in 3D (ie the points used to construct rings will have (*x,y,z*) coordinates).


## Planarity requirement

A polygon must be planar, ie all its points (used for both the exterior and interior rings) must lie on a plane. 



In GIS-related applications, the definitions are also more restrictive than these of the international standards.
\citet{Bogdahn10} and \citet{Wagner12} discuss the validation of solids for city modelling, but do not consider holes in surfaces and totally omit that interior shells are possible.
\citet{Groger11} give axioms to validate 3D city models, but also do not consider holes in primitives of dimensions 2 and 3; what they define as solids are in fact shells without holes in surfaces.
I use their work on the validity of shells as a building block of the methodology presented in this paper.

Most commercial GIS companies also ignore interior shells, ESRI (with ArcGIS 10) and Bentley being two examples.
Oracle Spatial considers interior shells in their validation function, but do not allow holes in surfaces~\citep{Oracle11g}.
Also, while they claim to validate according to the international rules, in practice there are several inconsistencies since they use a graph-approach and perform graph-traversal algorithms to validate, see \citet{Kazar08}. 
This approach is suitable for 2-manifold objects, but for solids having interior shells interacting with other shells it is not sufficient.


[^1]: All the geometric primitive have the prefix ‘GM\_’
[^ISO19107]: ISO 19107:2003: Geographic information---Spatial schema. International Organization for Standardization (2003).
[^OGC]: OpenGIS implementation specification for geographic information---Simple fea- ture access. Open Geospatial Consortium inc. Document 06-103r3 (2006).
[^Grunbaum03]: B. Grünbaum. Are your polyhedra the same as my polyhedra? In B. Aronov, S. Basu, J. Pach, and M. Sharir, editors, *Discrete and Computational Geometry: The Goodman-Pollack Festschrift*, pages 461– 488. Springer, 2003.
[^academics]: we have the (deserved!) reputation of over-complicating simple things, so I'm puzzled as to why even academics in GIS tend to reduce solids to much simpler objects.
[^compgeobook]: M. de Berg, M. van Kreveld, M. Overmars, and O. Schwarzkopf. *Computational geometry: Algorithms and applications*. Springer-Verlag, Berlin, second edition, 2000.