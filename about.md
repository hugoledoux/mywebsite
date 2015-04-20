---
layout: page
title: about
permalink: /about/
---


<div style='width:200px;margin:0 auto;'> 
  <img class="centre" alt="image" src="{{ site.baseurl }}/img/me.png">
</div>

I am an assistant-professor in the [3D geoinformation research group](http://3dgeoinfo.bk.tudelft.nl), which is part of the [Department of Urbanism](http://www.bk.tudelft.nl/en/about-faculty/departments/urbanism/) of the [Faculty of Architecture & the Built Environment](http://bk.tudelft.nl/en) at the [Delft University of Technology](http://www.tudelft.nl).

I hold a [PhD]({{ site.baseurl }}/phdthesis) in computer science from the [University of South Wales](http://www.southwales.ac.uk) in the UK, and a BSc in geomatics engineering from the [Université Laval](http://www.ulaval.ca) in Québec City, Canada.

For my research, I am particularly interested in combining the fields of GIS and computational geometry. Put simply, I often try to solve geographical problems---either in 2D or in 3D---by first decomposing the world into triangles/tetrahedra or into another tessellation such as the Voronoi diagram. My work involves developing topological data structures to store these tessellations, and designing algorithms to analyse and extract information from the datasets. I strongly believe in implementing my research ideas.

I am currently working on the validation and the automatic repair of polygons and polyhedra as found in GIS, the [higher-dimensional modelling of geographical information](http://www.geo5d.nl) (ie 4D+), and the [smart simplification of LiDAR datasets](http://3dsm.bk.tudelft.nl).

Teaching-wise, I am the responsible lecturer for the course *Geographical Information Systems and Cartography* in the [MSc Geomatics programme](http://geomatics.tudelft.nl) at TU Delft. For some years already, I've been using only free and open-source software for the labs, eg [QGIS](http://www.qgis.org/), [GRASS](http://grass.osgeo.org/), [Shapely](https://github.com/Toblerity/Shapely), and [TileMill](http://www.mapbox.com/tilemill/).

---

## Contact

<ul class="fa-ul">
  <li><i class="fa-li fa fa-envelope"></i>h.ledoux@tudelft.nl</li>
  <li><i class="fa-li fa fa-phone"></i>+31 15 27 86114</li>
  <li><i class="fa-li fa fa-home"></i><a href="http://tudelft.nl/hledoux">tudelft.nl/hledoux</a></li>
  <li><i class="fa-li fa fa-twitter"></i><a href="https://twitter.com/hugoledoux">hugoledoux</a></li>
  <li><i class="fa-li fa fa-github"></i><a href="https://github.com/hugoledoux">hugoledoux</a></li>
</ul>

<ul class="fa-ul">
  <li><i class="fa-li fa fa-map-marker"></i>Room BG.West.010</li>
  <li><i></i>Faculty of Architecture & the Built Environment</li>
  <li><i></i>(building #8)</li>
  <li><i></i>Delft University of Technology</li>
  <li><i></i>Julianalaan 134, Delft 2628BL, the Netherlands</li>
  <li><i></i><a href="http://www.tudelft.nl/en/about-tu-delft/contact-and-accessibility/housing-tu-delft/accessibility/building-8/">How to get here</a></li>
</ul>

<div id="map"></div>

<script src="//cdn.leafletjs.com/leaflet-0.4/leaflet.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/proj4js/1.1.0/proj4js-compressed.js"></script>
<script src="{{ "/assets/js/mymap.js" | prepend: site.baseurl }}"></script>