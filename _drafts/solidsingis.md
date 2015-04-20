---
layout: post
title: Solids in GIS packages
author: Hugo Ledoux
category: blog
tags: 3D, OGC
comments: true
---

## What about GIS packages?

This definition, that a solid is a 2-manifold, is also often used in the CAD world and in GIS.
One of the main reason is simplicity: representing and storing a 2-manifold can be done with data structures that are intrinsically 2D since each edge is guaranteed to have a maximum of two incident faces and that around each vertex the incident faces form one "umbrella".
This means that one doesn't have to dramatically change the internal of her systems since the good old *node-arc-face* generalises directly to 3D.
While this sounds great, it also means that non-manifold objects are impossible to represent, and, perhaps worse, 3D objects are *individually* stored and represented.
That is, the topological relationships between 2 adjacent buildings cannot be explicitly stored.

### esri ArcGIS 10.3

No solid type, only [Multipatches](http://resources.arcgis.com/en/help/main/10.2/index.html#//00q8000000mv000000).

> For a multipatch to be considered closed, it must be constructed in the correct fashion. The feature must represent one distinct volume. The patches it is composed of must all have the same counterclockwise orientation of their coordinates and participate in defining the shell of the volume. The patches must not intersect each other, and there must be no gaps or empty spaces in the shell.



[Is Closed 3D](http://resources.arcgis.com/en/help/main/10.2/index.html#//00q90000006p000000)
Evaluates multipatch features to determine whether each feature completely encloses a volume of space.
Are self-intersection detected? 
Are dangling pieces allowed?

There is no Is_Valid()`, which means no definition.

[3D Boolean operations](http://resources.arcgis.com/en/help/main/10.2/index.html#/Working_with_3D_set_operators/00q80000009v000000/)

### FME

[different types of Solids](http://docs.safe.com/fme/2014beta/html/FME_Workbench/Default.htm#3D/IFMESolids.htm)

IFMEBRepSolid: b-rep solid
But also IFMEExtrusion for simpler solids (without inner shells) and IFMECSGSolid.

> In general, an IFMEBRepSolid must contain one exterior surface and zero or more interior surfaces.

> IFMECompositeSurface, with the additional requirement that this composite surface must be closed, in order to form a volume.

[`GeometryValidator](http://docs.safe.com/fme/html/FME_Transformers/FME_Transformers.htm#Transformers/geometryvalidator.htm)
[List of errors](http://docs.safe.com/fme/html/FME_Transformers/FME_Transformers.htm#Transformers/geometryvalidator.htm)



### Oracle Spatial


Most commercial GIS companies also ignore interior shells, ESRI (with ArcGIS 10) and Bentley being two examples.
Oracle Spatial considers interior shells in their validation function, but do not allow holes in surfaces~\citep{Oracle11g}.
Also, while they claim to validate according to the international rules, in practice there are several inconsistencies since they use a graph-approach and perform graph-traversal algorithms to validate, see \citet{Kazar08}. 
This approach is suitable for 2-manifold objects, but for solids having interior shells interacting with other shells it is not sufficient.

In GIS-related applications, the definitions are also more restrictive than these of the international standards.
\citet{Bogdahn10} and \citet{Wagner12} discuss the validation of solids for city modelling, but do not consider holes in surfaces and totally omit that interior shells are possible.
\citet{Groger11} give axioms to validate 3D city models, but also do not consider holes in primitives of dimensions 2 and 3; what they define as solids are in fact shells without holes in surfaces.

### PostGIS

SFCGAL
POLYHEDRALSURFACE