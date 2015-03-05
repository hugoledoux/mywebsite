---
layout: page
title: research
permalink: /research/
---

# Research projects

<div class="message">
For most of these projects, my colleagues and I develop software prototypes that we release under open-source licences. These are available at 
<a href="https://github.com/tudelft3d"> github.com/tudelft3d</a>
</div>

- - -

## Validation & automatic repair of geo-datasets

![]({{ site.baseurl }}/img/repair3d.png)

Recently, out of frustration at the poor quality of GIS datasets and of 3D city models I obtained, I have focussed my efforts on the validation and the *automatic* repair of polygons and polyhedra. This has lead to different programs that have matured enough to not be called prototypes anymore: [prepair](https://github.com/tudelft3d/prepair), [pprepair](https://github.com/tudelft3d/pprepair) and [val3dity](https://github.com/tudelft3d/val3dity). I hope these will help practitioners who often spend hundreds of hours manually repairing their datasets. 

Some of these are also available as [web-applications](http://geovalidation.bk.tudelft.nl).


- - -

## Higher-dimensional modelling of geoinformation

![]({{ site.baseurl }}/img/geo5d.png)

The aim of the research project is to integrate the multi-dimensional characteristics of geographical data (eg space, time and scale), together in one higher-dimensional model. We develop data structures and operations to realise such a model, and we apply this model to the integration of CityGML models at different scales for instance.

The research project is funded by a Vidi grant from the [Dutch Technology Foundation STW](http://www.stw.nl) awarded to [Jantien Stoter](http://3dgeoinfo.bk.tudelft.nl/jstoter). 

More information at [www.geo5d.nl](http://3dgeoinfo.bk.tudelft.nl/projects/geo5d/)

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

More information at [3dsm.bk.tudelft.nl](http://3dsm.bk.tudelft.nl)
