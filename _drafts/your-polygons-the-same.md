---
layout: post
title: Are your polygons the same as my polygons? 
author: Hugo Ledoux
category: blog
tags: GIS, OGC
comments: true
---


When someone outside the field of GIS thinks of a 'polygon', she usually pictures something like one of these:

![]({{ site.baseurl }}/img/simplepolygons.png)

And I can't blame her, that's what we learned in school. Squares, triangles, pentagons, hexagons.
However, when I speak about a polygon with my [colleagues](http://3dgeoinfo.bk.tudelft.nl/about/), we usually think of something more complex:

![]({{ site.baseurl }}/img/gispolygons.png)


## Simple Features polygons

We use the definition as found in the [*Simple Feature Access* document](http://www.opengeospatial.org/standards/sfa) of the [OGC](http://www.opengeospatial.org): 

> A Polygon is defined as a planar Surface defined by 1 exterior boundary and 0 or more interior boundaries. Each interior boundary defines a hole in the Polygon.

There are different rules for the interactions between the different rings (boundaries) of a polygon, and it is easy to imagine that things can quickly get complex and messy.
The following figure shows 12 examples of rather simple polygons that are invalid, and these highlight the most important validity rules.

![]({{ site.baseurl }}/img/unitpolygons.png)

  - each ring defining the exterior and interior boundaries should be *simple*, ie non-self-intersecting ($$p_{1}$$ and $$p_{10}$$). Notice that this prevents the existence of rings with zero-area ($$p_{6}$$), and of rings having two consecutive points at the same location. It should be observed that the polygon $$p_{1}$$ is not allowed either (in a valid representation of the polygon, the triangle should be represented as an interior boundary touching the exterior boundary), but some implementations do allow it (eg ESRI's Shapefile).
  - each ring should be closed ($$p_{11}$$): its first and its last points should be the same.
  - the rings of a polygon should not cross ($$p_{3}$$, $$p_{7}$$, $$p_{8}$$ and $$p_{12}$$) but may intersect at one tangent point (the interior ring of $$p_{2}$$ is a valid case, although $$p_2$$ as a whole is not since the other interior ring is located *outside* the interior one).
  - a polygon may not have cut lines, spikes or punctures ($$p_{5}$$ or $$p_{6}$$); removing these is known as the *regularisation* of a polygon (a standard point-set topology operation).
  - the interior of every polygon is a connected point set, ie one can 'walk' everywhere within its interior without having to go outside ($$p_{4}$$).
  - each interior ring creates a new area that is disconnected from the exterior. Thus, an interior ring cannot be located outside the exterior ring ($$p_{2}$$) or inside other interior rings ($$p_{9}$$).


## BIG polygons

Many real-world polygons are very large, both in terms of number of vertices and of rings.
An example is this polygon, taken from the [Canada Land Cover](http://www.geobase.ca/geobase/en/data/landcover/index.html).
It has 148,612 vertices in total, and 5,132 interior rings.
"How was such a large polygon created in the first place?" I hear you ask. 
Automatically from reclassified raster imagery.
It is---like several polygons that are that big---invalid since it contains self-intersections. 

{% gist ee23076b6b35cdcc4ac1 %}


## My all-time favourite polygons

Of all the polygons I've seen in my life, these 2 are my favourite.

### 1. the Swedish polygon

[<img src="{{ site.baseurl }}/img/bigpolygon_sweden.png">](https://github.com/hugoledoux/BIGpolygons/blob/master/EU-199948.geojson)

The polygon with ID 'EU-199948' in the [Corine land cover dataset](http://www.eea.europa.eu/data-and-maps/data/clc-2006-vector-data-version-3) has 1,189,903 vertices, and 7,672  inner rings.
You can get it and zoomin on it [there](https://github.com/hugoledoux/BIGpolygons/blob/master/EU-199948.geojson).

### 2. the Cleveland polygon

[<img src="{{ site.baseurl }}/img/bigpolygon_cleveland.png">](https://github.com/hugoledoux/BIGpolygons/blob/master/cleveland.geojson)

I obtained it from someone working at the [Cleveland Metroparks](http://clevelandmetroparks.com), and you can get it [there](https://github.com/hugoledoux/BIGpolygons/blob/master/cleveland.geojson).
Although it covers a much smaller area than the Swedish one, it is **monstrous**: 1,689,703 vertices, 66,908 inner rings, and its biggest ring has 500,373 vertices. Wow.

I can't decide which one I like most, perhaps because the Swedish polygon should probably be bigger than the Cleveland one: observe that it was truncated at the bottom and on the left, probably because of a different [CRS zone](https://en.wikipedia.org/wiki/Spatial_reference_system), or perhaps because the GIS couldn't handle the full one?


## A repository of BIG polygons

I've setup a repository in which I keep these big polygons and other interesting ones:

<a href="https://github.com/hugoledoux/BIGpolygons"><i class="fa fa-github fa-lg"></i> github.com/hugoledoux/BIGpolygons</a>

I usually use them to test the capabilities of code I write to process GIS datasets, eg [prepair](https://github.com/tudelft3d/prepair).

I'd be grateful if you submitted other interesting ones and/or your favourite ones. 
