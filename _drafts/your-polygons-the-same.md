---
layout: post
title: Are your polygons the same as my polygons? 
author: Hugo Ledoux
category: blog
comments: true
---


When someone outside the field of GIS thinks of a 'polygon', I assume that she usually pictures something like one of these:

And I can blame her, that's what we learned in school. Squares, triangles, pentagons, hexagons.

However, when I speak about a polygon with my [colleagues](http://3dgeoinfo.bk.tudelft.nl/about/), we think of something rather different:


This is probably because we have been developping for a while 

To test the efficiency of \prepair, we have tested it with complex real-world polygons from the CORINE land cover dataset (CLC2006)\footnote{\url{www.eea.europa.eu/publications/COR0-landcover}}.
Since they are constructed from reclassified raster imagery, they can be very large, both in terms of number of points and of rings.
As a test dataset, we used the 100 largest (in terms of number of points) invalid polygons in the CLC2006 dataset.
The smallest of these 100 polygons (ID = EU-2018418) contains 44~051 points and 126 rings; the largest (ID = EU-199949) contains 1~189~903 points and 7~672 rings.
The average numbers of points and rings per polygon are respectively 146~478 and 776; the median values are 90~526 and 434.

New CORINE download:
http://www.eea.europa.eu/data-and-maps/data/clc-2006-vector-data-version-3




Title heavily inspired by the excellent paper: 

[^1]: B. Grünbaum (2003). *Are your polyhedra the same as my polyhedra?* In B. Aronov, S. Basu, J. Pach, and M. Sharir, editors, Discrete and Computïational Geometry: The Goodman-Pollack Festschrift, pages 461–488. Springer.
