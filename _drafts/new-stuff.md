---
layout: post
title: Stuff I've recently discovered
author: Hugo Ledoux
category: blog
tags: misc
comments: true
---


[ESRI geodatabases (GDB)](http://www.esri.com/news/arcnews/winter0809articles/the-geodatabase.html) can be read/written with [GDAL/OGR](http://www.gdal.org/). 
And it works with 3D objects, eg to convert the buildings in a `city.gdb` to a shapefile `out` with 3D MultiPatches:

```
$ ogr2ogr out city.gdb buildings_LOD2
```

[via [Webmapper](http://www.webmapper.nl/lab/top10nl-3d-brought-to-life-with-osm-buildings/)]

- - -

While esri has in recent years promoted [open formats](http://blogs.esri.com/esri/arcgis/tag/open-data/), open standards and even released [open-source code](https://github.com/Esri), they are also developing their own compressed LAS format. While there is an open one with a LGPL implementation ([LASzip](http://www.laszip.org)). Frustrating.

[via [rapidlasso](http://rapidlasso.com/2014/11/06/keeping-esri-honest/)]


- - -

2. FME doesn't parse xlinks in CityGML 

- - -

Finally, some people like their drones *a lot*:

<iframe width="560" height="315" src="//www.youtube.com/embed/VsHMjWORFvI" frameborder="0" allowfullscreen></iframe>


