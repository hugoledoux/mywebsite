---
layout: page
title: research
permalink: /research/
---

# Research 

I would charasterise my research as an equal mix of:

  - __GIS__: preparing and crunching real-world datasets so that they can be used for spatial analysis;
  - __computational geometry__: extending and adapting theoretical results to real-world problems;
  - __implementation__: I strongly believe in implementing my research results, see my [open-source software]({{ site.baseurl }}/software/) page.



- - -

## CityJSON: Making CityGML a useful format to exchange 3D city models

![]({{ site.baseurl }}/img/cityjson.jpg)

CityJSON is a format for encoding a subset of the CityGML data model using JavaScript Object Notation (JSON). A CityJSON file represents both the geometry and the semantics of the city features of a given area, eg buildings, roads, rivers, the vegetation, and the city furniture.
The aim of CityJSON is to offer an alternative to the GML encoding of CityGML, which can be verbose and complex, and thus rather frustrating to work with. 
CityJSON aims at being easy-to-use, both for reading datasets, and for creating them. 
It was designed with programmers in mind, so that tools and APIs supporting it can be quickly built.

<a href="https://cityjson.org"><i class="fa fa-external-link"></i> CityJSON website</a>

<a href="https://github.com/tudelft3d/cjio"><i class="fa fa-external-link"></i> cjio: Python CLI to process and manipulate CityJSON files</a>

- - -

## Validation & automatic repair of geo-datasets

![]({{ site.baseurl }}/img/repair3d.png)

A few years ago, out of frustration at the poor quality of GIS datasets and of 3D city models I obtained, I have focussed my efforts on the validation and the *automatic* repair of polygons and polyhedra. This has lead to different programs that have matured enough to not be called prototypes anymore: [prepair](https://github.com/tudelft3d/prepair), [pprepair](https://github.com/tudelft3d/pprepair) and [val3dity](https://github.com/tudelft3d/val3dity). 
I hope these will help practitioners who often spend hundreds of hours manually repairing their datasets. 

Some of these are also available as [web-applications](http://geovalidation.bk.tudelft.nl).


- - -

## Segmentation of urban textured meshes

![]({{ site.baseurl }}/img/sum.jpg)

We develop (this is [Weixiao Gao](https://3d.bk.tudelft.nl/weixiao/) PhD project, which I supervise with [Liangliang Nan](https://3d.bk.tudelft.nl/liangliang/)) algorithms and software to semantically segment very large urban textured meshes.

We have annoted part of the open [Helsinki 3D dataset](https://www.hel.fi/helsinki/en/administration/information/general/3d/3d) and released it as open dataset ([code+dataset](https://3d.bk.tudelft.nl/projects/meshannotation/)).

Our methodology outperforms other segmentation methods, see our [paper](https://arxiv.org/abs/2202.03209).

- - - 

## Some other research projects (completed)

  - [UMnD: Urban modelling in higher dimensions](https://3d.bk.tudelft.nl/projects/umnd/)
  - [iNous: Building an Eco-System for Indoor Spatial Information](https://3d.bk.tudelft.nl/projects/inous/)
  - [Point cloud modelling with the 3D MAT](https://3d.bk.tudelft.nl/projects/3dsm/)
  - [3D4EM: Design and implementation of an SDI for integrated environmental modelling in 3D](https://3d4em.netlify.app/)
  - [GeoBIM: Bridging the gap between Geo and BIM](https://3d.bk.tudelft.nl/projects/geobim/)
  - [Automatic generation of semantic 3D city models from 3D textured meshes](https://3d.bk.tudelft.nl/projects/mesh2lod/)
  - [5D geo-modelling](https://3d.bk.tudelft.nl/projects/geo5d/)
  - [Automatic reconstruction of simulation-ready 3D city models](https://3d.bk.tudelft.nl/projects/simwind/)
  - [FieldGML]({{ site.baseurl }}/fieldgml): a GML-based representation for fields in 2D and 3D, my attempt at improving [ISO19123, the standard for coverages](http://www.iso.org/iso/catalogue_detail.htm?csnumber=40121)
  - [Modelling geoscientific data with the 3D Voronoi diagram]({{ site.baseurl }}/phdthesis): my PhD thesis on the topic.