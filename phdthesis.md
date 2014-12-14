---
layout: default
title: PhD
permalink: /phdthesis/
---

# PhD thesis

![](/img/3dVoronoi2.png)

<p><strong>Modelling three-dimensional fields in geoscience with the Voronoi diagram and its dual</strong>. Hugo Ledoux. PhD thesis, School of Computing, University of Glamorgan, 2006.  <a href="/pdfs/thesisLedoux.pdf"><i class="fa fa-file-pdf-o"></i></a> <a href="#bib_thesis" data-toggle="collapse"><i class="fa fa-toggle-down"></i></a><div id="bib_thesis" class="collapse"  tabindex="-1"><pre class="bibtex">@phdthesis{_thesis,
  author = {Ledoux, Hugo},
  title = {Modelling three-dimensional fields in geoscience with the {Voronoi} diagram and its dual},
  school = {School of Computing, University of Glamorgan},
  year = {2006},
  address = {Pontypridd, Wales, UK}
}</pre></div></p>

The objects studied in geoscience are often not man-made objects, but rather the spatial distribution of three-dimensional continuous geographical phenomena such as the salinity of a body of water, the humidity of the air or the percentage of gold in the rock (phenomena that tend to change over time). These are referred to as fields, and their modelling with geographical information systems is problematic because the structures of these systems are usually two-dimensional and static. Raster structures (voxels or octrees) are the most popular solutions, but, as I argue in this thesis, they have several shortcomings for geoscientific fields.

As an alternative to using rasters for representing and modelling three-dimensional fields, I propose using a new spatial model based the Voronoi diagram (VD) and its dual the Delaunay tetrahedralization (DT). I argue that constructing the VD/DT of the samples that were collected to study the field can be beneficial for extracting meaningful information from it. Firstly, the tessellation of space obtained with the VD gives a clear and consistent definition of neighbourhood for unconnected points in three dimensions, which is useful since geoscientific datasets often have highly anisotropic distributions. Secondly, the efficient and robust reconstruction of the field can be obtained with natural neighbour interpolation, which is entirely based on the properties of the VD. Thirdly, the tessellations of the VD and the DT make possible, and even optimise, several spatial analysis and visualisation operations. A further important consideration is that the VD/DT is locally modifiable (insertion, deletion and movement of points), which permits us to model the temporal dimension, and also to interactively explore a dataset, thus gaining insight by observing on the fly the consequences of manipulations and spatial analysis operations.

The development of this new spatial model is from an algorithmic point of view, ie I describe in details algorithms to construct, manipulate, analyse and visualise fields represented with the VD/DT. A strong emphasis is put on the implementation of the spatial model, and, for this reason, the many degeneracies that arise in three-dimensional geometric computing are described and handled. A new data structure, the <em>augmented quad-edge</em>, is also presented. It permits us to store simultaneously both the VD and the DT, and helps in the analysis of fields. Finally, the usefulness of this Voronoi-based spatial model is demonstrated with a series of potential applications in geoscience.
