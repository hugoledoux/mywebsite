---
layout: post
title: Tinkering with the first test area of 3DTOP10NL
category: blog
tags: 3dtop10nl
comments: true
---

The Netherlands has recently launched a ["3D map"](http://www.kadaster.nl/web/Nieuws/Nieuwsberichten/Bericht/Ontwikkeling-3Dkaart-van-Nederland-in-volle-gang.htm) covering the whole country in which all buildings, roads, trees, canals are 3D geometries.
It was constructed by adding the third dimension, obtained from airborne laser-scanners ([AHN](http://www.ahn.nl) was used), to the objects in the 1:10k topographic map (some details [here](http://3dgeoinfo.bk.tudelft.nl/hledoux/pdfs/13_pers.pdf)).
This leads to a massive amount of information: 15M+ objects, billions of elevation points, and billions of triangles.

At this moment, the full dataset can be requested but only the test area is [directly downloadable](https://www.pdok.nl/nl/producten/pdok-downloads/basis-registratie-topografie/top10nl-3d).
The test area is Valkenburg (in the South of the country), so yes the hills you see are real, and they are the only ones in the country (we cherish them).

<iframe src="https://player.vimeo.com/video/118325504" width="500" height="408" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/118325504">3D TOP10NL -- Valkenburg</a> from <a href="https://vimeo.com/user24693433">hgldx</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

While the dataset is publicly available and open (under this [creative commons licence](http://creativecommons.org/licenses/by/3.0/nl/)), the format currently offered is only [ESRI geodatabases (GDB)](http://www.esri.com/news/arcnews/winter0809articles/the-geodatabase.html).
Rather ironic, but I was promised that other formats would soon be available.
CityGML would in theory be a good candidate, but storing all these triangles in GML would create *gigantic* files, so other formats are currently being investigated.

If, like me, you don't have ArcGIS, do not despair. 
It's possible to read the GDB file (or should I say folder?): GDAL/OGR has an implementation of the [OpenFileGDB driver](http://www.gdal.org/drv_openfilegdb.html).
And it works with 3D objects out-of-the-box, eg to know which layers are in the GDB:

```
$ ogrinfo Valkenburg.gdb/
Had to open data source read-only.
INFO: Open of `Valkenburg.gdb/'
      using driver `OpenFileGDB' successful.
1: terreinVlak (Multi Polygon)
2: waterdeelVlak (Multi Polygon)
3: wegdeelVlak (Multi Polygon)
4: gebouwVlak (Multi Polygon)
5: gebouwVlak_stat (Multi Polygon)
6: terreinpunten (3D Point)
7: wegdeelVlak_3D_LOD0 (3D Multi Polygon)
8: terreinVlak_3D_LOD0 (3D Multi Polygon)
9: gebouw_3D_LOD0 (3D Multi Polygon)
10: waterdeelVlak_3D_LOD0 (3D Multi Polygon)
11: gebouw_3D_LOD1 (3D Multi Polygon)
12: brugWater (3D Multi Polygon)
13: brugWeg (3D Multi Polygon)
14: TerreinOnder (3D Multi Polygon)
```

To convert the buildings (layer `gebouw_3D_LOD1`) to a shapefile with 3D MultiPatches (to a folder `out`), simply do this:

```
$ ogr2ogr out Valkenburg.gdb/ gebouw_3D_LOD1
```

and if you do this for the terrain (`terreinVlak_3D_LOD0`) and the roads (`wegdeelVlak_3D_LOD0`), you get this:

![]({{ site.baseurl }}/img/valkenburg3d.png)

Voilà.

- - -

A word of caution though.
I have noticed that the conversion done with the OpenFileGDB has errors: several triangles are corrupted!
Triangles that have---as they should---3 vertices in the GDB file (I checked with ArcGIS) are after conversion to the shapefile having 4+ vertices and inner rings (triangles are simply polygons, thus it's possible and "correct").
An example is this one (the red geometries are 1 geometry that is corrupted, and it is not a triangle):

![]({{ site.baseurl }}/img/openfilegdbproblems.png)

Why does this happen? I have no idea. 
It happens for me with GDAL v1.11.0, under Mac OS X (Yosemite).

Since it was driving mad, I wrote a small script to know if the triangles in a shapefile are valid: [aretrianglesvalid.py](https://gist.github.com/hugoledoux/0798ee79fe76a1b0ed8f).

If you solve this problem, please let me know.












