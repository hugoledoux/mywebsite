---
layout: post
title: Validate your 3D geometries with val3dity
author: Hugo Ledoux
category: blog
tags: validation
comments: true
---

Today I'm happy to release officially the v0.9 of [val3dity](https://github.com/tudelft3d/val3dity): my code to validate 3D geometries (solids/volumes and surfaces).

I started in 2010 to work on it (thanks to a sponsorship from [Safe Software](www.safe.com)), and I've been working on it part-time since then.
Through an OGC CityGML Quality Interoperability Experiment (QIE), I've tested and improved it a lot the last few months.
It's now robust and complete enough---touch wood---to be used by anyone.


Validation of solids according to the international standard ISO 19107.

The validation of a solid is performed hierarchically, ie first every surface is validated in 2D (with [GEOS](http://trac.osgeo.org/geos/)), then every shell is validated (must be watertight, no self-intersections, orientation of the normals must be consistent and pointing outwards, etc), and finally the interactions between the shells are analysed.

Most of the details of the implementation are available in this scientific article:

> Ledoux, Hugo (2013). On the validation of solids represented with the
international standards for geographic information. *Computer-Aided Civil and Infrastructure Engineering*, 28(9):693-706. [ [PDF] ](http://3dgeoinfo.bk.tudelft.nl/hledoux/pdfs/13_cacaie.pdf) [ [DOI] ](http://dx.doi.org/10.1111/mice.12043)


![]({{ site.baseurl }}/img/Rotterdam-Cool.png)

[Report of one part of Rotterdam](http://geovalidation.bk.tudelft.nl/val3dity/reports/988a164b-ce0c-4d67-9a74-62ea355914ae)

