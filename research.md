---
layout: page
title: research
permalink: /research/
---

# Research 

I would charasterise my research as an equal mix of:

  - __GIS__: preparing and crunching real-world datasets so that they can be used for spatial analysis;
  - __computational geometry__: extending and adapting theoretical results to real-world problems;
  - __implementation__: I strongly believe in implementing my research results, see my [open-source software]({{ site.baseurl }}/software/)) page.

- - -

## Validation & automatic repair of geo-datasets

![]({{ site.baseurl }}/img/repair3d.png)

A few years ago, out of frustration at the poor quality of GIS datasets and of 3D city models I obtained, I have focussed my efforts on the validation and the *automatic* repair of polygons and polyhedra. This has lead to different programs that have matured enough to not be called prototypes anymore: [prepair](https://github.com/tudelft3d/prepair), [pprepair](https://github.com/tudelft3d/pprepair) and [val3dity](https://github.com/tudelft3d/val3dity). 
I hope these will help practitioners who often spend hundreds of hours manually repairing their datasets. 

Some of these are also available as [web-applications](http://geovalidation.bk.tudelft.nl).


- - -

## Higher-dimensional modelling of geoinformation

![]({{ site.baseurl }}/img/geo5d.png)

The aim of the research project is to integrate the multi-dimensional characteristics of geographical data (eg space, time and scale), together in one higher-dimensional model. We develop data structures and operations to realise such a model, and we apply this model to the integration of CityGML models at different scales for instance.

The research project is funded by a Vidi grant from the [Dutch Technology Foundation STW](http://www.stw.nl) awarded to [Jantien Stoter](http://3d.bk.tudelft.nl/jstoter). 

<a href="http://3d.bk.tudelft.nl/projects/geo5d/"><i class="fa fa-external-link"></i> Project website</a>

- - -

## Smart simplification of LiDAR datasets

![]({{ site.baseurl }}/img/3dsm.jpg)

The aim of this project, funded by the [Dutch Technology Foundation STW](http://www.stw.nl), is to investigate algorithms to simplify LiDAR datasets. 
In recent years, these have considerably grown in size because of advances in acquisition technologies such as airborne laser-scanning. 
A vivid example is the [AHN2 datasets](http://www.ahn.nl) in the Netherlands: it contains around 640 billion points (639,477,709,621 to be exact). 

We reduce their size while keeping their main characteritics. 
While current methods often portray DSMs as 2D objects (and thus valuable information is lost), we investigate new simplification algorithms that:

  1. use 3D tools and 3D data structures, specificially the 3D medial axis transform (MAT);
  2. permit us to define 3D features—buildings, dikes, etc—and consider these while simplifying. The knowledge of the features will permit us to remove unimportant points and focus only on those of interest for a given application.

<a href="http://3d.bk.tudelft.nl/projects/3dsm/"><i class="fa fa-external-link"></i> Project website</a>


- - -

## Storage, update and dissemination of massive 3D city objects

![]({{ site.baseurl }}/img/3d4em.png)

The aim of this research project, also funded by the [Dutch Technology Foundation STW](http://www.stw.nl), is to investigate and develop methods to efficiently store and maintain 3DTOP10NL in a database, and to disseminate it to practitioners.
The [existing open-source database solutions](http://www.3dcitydb.org) for managing 3D volumetric objects are being tested with massive datasets and improved, if necessary.

The biggest challenge is the management of massive TINs (triangulated irregular networks) in a database.
We investigate, design and develop new data structures, implement them, and compare different alternatives (in terms of storage space, query time, etc).

<a href="http://www.3d4em.nl"><i class="fa fa-external-link"></i> Project website</a>

- - - 

## Some older research projects 

  - [FieldGML]({{ site.baseurl }}/fieldgml): a GML-based representation for fields in 2D and 3D, my attempt at improving [ISO19123, the standard for coverages](http://www.iso.org/iso/catalogue_detail.htm?csnumber=40121)
  - [Modelling geoscientific data with the 3D Voronoi diagram]({{ site.baseurl }}/phdthesis): my PhD thesis on the topic.