---
layout: default
title: FieldGML 
permalink: /fieldgml/
---

# FieldGML

FieldGML is a GML-based representation for fields in 2D and 3D, one that permits us to represent efficiently not only rasters, but also fields in other forms. 
It is my attempt at improving [ISO19123, the standard for coverages](http://www.iso.org/iso/catalogue_detail.htm?csnumber=40121).

FieldGML is based on current standards, is flexible, extensible and is also more appropriate than raster structures to model the kind of datasets found in GIS-related applications. 
To know more FieldGML, you can read either of these documents:

**Representing Continuous Geographical Phenomena with FieldGML**. This is the final report of the project during which it was developed. It contains details about the GML application schema, and there are some examples of files. <a href="/hledoux/pdfs/fieldgml.pdf"><i class="fa fa-file-pdf-o"></i></a>

<p><strong>FieldGML: an alternative representation for fields</strong>. Hugo Ledoux. In Anne Ruas and Christopher M. Gold (eds.), <em>Headway in Spatial Data Handling</em>, Lecture Notes in Geoinformation and Cartography, Springer, 2008, pp. 385&ndash;400.  <a href="/hledoux/pdfs/08_sdh.pdf"><i class="fa fa-file-pdf-o"></i></a> <a href="http://dx.doi.org/10.1007/978-3-540-68566-1_22"><i class="fa fa-bookmark"></i></a> <a href="#bib_08sdh" data-toggle="collapse"><i class="fa fa-toggle-down"></i></a><div id="bib_08sdh" class="collapse"  tabindex="-1"><pre class="bibtex">@incollection{_08sdh,
  author = {Ledoux, Hugo},
  title = {FieldGML: An Alternative Representation for Fields},
  booktitle = {Headway in Spatial Data Handling},
  publisher = {Springer},
  year = {2008},
  editor = {Ruas, Anne and Gold, Christopher M.},
  series = {Lecture Notes in Geoinformation and Cartography},
  pages = {385--400}
}</pre></div></p>


## GML application schema

The application schema <a href="./fieldgml.xsd">fieldgml.xsd</a><br />
The <a href="./doc/short/fieldgml.xsd.html">documentation of the schema</a> without the GML types.<br />
The <a href="./doc/withgml/fieldgml.xsd.html">long documentation of the schema</a> with all the GML types.<br />

## Examples of FieldGML files

<a href="./examples/5k_pts.xml">5k_pts.xml</a> is a file with 5000 scattered points, representing the elevation of a region. The interpolation method defined in this file is natural neighbour interpolation.

<a href="./examples/5k_tess.xml">5k_tess.xml</a> contains the same 5000 points, but here these are stored in a TessPointsRule of type "Delaunay", which means that a Delaunay TIN has to be created to interpolate. The interpolation method is based on the tessellation, and inside each triangle a linear function is used.

<a href="./examples/contours.xml">contours.xml</a> contains contour lines representation the same terrain as the 2 previous examples. The interpolation method defined here is inverse-distance to a power, with a search radius of 12 units.

<a href="./examples/array2d.xml">array2d.xml</a> is a FieldGML file pointing to a GTiff file <a href="./examples/array2d.tif">array2d.tif</a>. The file is the result of creating a raster of the 5000 scattered points above (5k_pts.xml). The interpolation method defined here is piecewise constant, that is the value estimated at location (x,y) is the value of the pixel at that location.

<a href="./examples/geology3d.xml">geology3d.xml</a> contains 150 points scattered in 3D space. The interpolation method defined in this file is natural neighbour interpolation.
