---
layout: post
title: Plagiarism in academia and how our case was handled
author: Hugo Ledoux
category: blog
tags: academia
comments: true
---


I've hesitated a lot before writing this blog post. 
Should I or should I not openly discuss what happened to my coauthors and me in recent months? Is it fair to name the authors and point to the paper? 
I've decided that yes it's worth writing what happened to us, firstly because there are a lot of positive aspects to it, and second because if we all sweep these cases "under the carpet" then there is little hope that things will improve.

Here's what happened. My colleague [Martijn Meijers](http://www.gdmc.nl/martijn) and myself developped in 2009 a method to validate planar partitions stored in Simple Features.
The prototype was first published in the SDH 2010 proceedings (paper [here](http://www.isprs.org/proceedings/XXXVIII/part2/Papers/24_Paper.pdf)), and shortly after [Ken Arroyo Ohori](http://3dgeoinfo.bk.tudelft.nl/ken) extended the ideas for his MSc thesis.
He added automatic repair functions, did a great C++ implementation that scaled to large datasets, released the [code open-source](https://github.com/tudelft3d/pprepair) 


![]({{ site.baseurl }}/img/plaex1.png)

- - -

![]({{ site.baseurl }}/img/plaex2.png)

- - -

![]({{ site.baseurl }}/img/plaex3.png)

- - -


We:

> If the set of input polygons forms a planar partition, then each segment will be inserted twice (except those forming the outer boundary of the set of input polygons). This is usually not a problem for triangulation libraries because they ignore points and segments at the same location (as is the case with the solution we use, see Section 4). When segments are found to intersect, they are split with a new point created at the intersection.

They:

> If two polygons share an edge e, the edge e is drawn twice. Because most triangulation programming libraries discard one point in the case of duplicate points, this step does not require further manipulation. Likewise, when edges intersect, they are split using a new vertex that is created at the intersection point. 

- - - 

We:

> If the set of input polygons forms a planar partition then all the triangles will be labelled with one and only one label. The problems are easily detected: Gaps are detected by finding triangles without any labels. Overlaps are detected by finding triangles with two or more labels.

They: 

> If all polygons in a data set form a planar partition, all triangles will be tagged as 1. Gaps or overlaps are easily recognised by checking whether the tag value is equal to 1 or not.

- - - 

Is their paper a copy of ours? No, it also differs significantly. 
However, the thrust of the paper is that triangle-based algorithm to form a planar partition from a set of polygons.
Without this algorithm, there is no paper.

They discuss how to split regions based on triangles as one way to resolve problematic regions. 
This was part of our future work, and was described in our original paper though.

plagiarism? What to do?
http://www.tandfonline.com/doi/pdf/10.1080/13658816.2014.937716
http://www.tandfonline.com/doi/abs/10.1080/13658816.2015.1008949

- - - 

Dear Brian,
 
Thank you for your prompt response. Here are the main similarities in both papers:
- Both papers deal with the same problem: generating planar partitions from a set of polygons with gaps/overlaps
- Both papers use the same criticism of the current standard solution: snapping within a predefined threshold requires finding an acceptable threshold (which may or may not exist) and might create various topological inconsistencies.
- The analysis and figures for how this snapping threshold is defined is identical. See their Section 2.2 and our 2.3, or alternatively their Figure 4 and our Figure 2.
- The way in which these topological inconsistencies are explained is extremely similar. Among the possibilities to highlight problems, we have chosen exactly the same examples for the paper: spikes/punctures and splitting polygons. See their Figure 5 and our Figure 3, or their Figure 6 and our Figure 4.
- Both papers propose an identical solution. Use a constrained triangulation of the polygons as a base, label each polygon with the polygons that it belongs to, and reconstruct the polygons from the triangulation.
- Both papers argue for using a triangulation based on the same reasoning, that a triangulation is by definition a planar partition and that triangulation libraries create edges only once, and can in practice handle duplicate points and intersections with ease. These latter practical aspects are non-trivial.
- Their allocation method to split a collection of triangles was suggested in our future work.
 
Individually, these could be coincidences, but taken together it all seems a bit too much. Moreover, it seems utterly impossible that the authors were not aware of our work on this topic, which spans several papers. Simple Google searches using their own keywords and terms directly lead to our work. See (no quotes, and done through Startpage to ensure that we get the same results):
“inconsistent boundaries sliver polygons” https://startpage.com/do/search?query=inconsistent%20boundaries%20sliver%20polygons (the first two results)
“constrained triangulation polygons” https://startpage.com/do/search?query=constrained%20triangulation%20polygons (2 results in first page)
“constrained triangulation polygons slivers” https://startpage.com/do/search?query=constrained%20triangulation%20polygons%20slivers (4 results in first page)
 
Please let me know if you require any more details, and thanks again.