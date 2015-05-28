---
layout: post
title: Plagiarism in academia and how a paper of mine was handled
author: Hugo Ledoux
category: blog
tags: academia
comments: true
---

I've hesitated a lot before writing this blog post. 
Should I or should I not openly discuss what happened to my coauthors and me in recent months? Is it fair to name the authors and point to the paper? 
I've decided that yes it's worth writing what happened to us, firstly because there are a lot of positive aspects to it, and second because if we all sweep these cases "under the carpet" then there is little hope that things will improve and people will be tempted to cheat (since there is no punishment).

Here's what happened. My colleague [Martijn Meijers](http://www.gdmc.nl/martijn) and myself developed in 2009 a method to validate planar partitions stored in Simple Features (to detect gaps and overlaps).
The methodology and the prototype were first published in the SDH 2010 proceedings ([the paper](http://www.isprs.org/proceedings/XXXVIII/part2/Papers/24_Paper.pdf)), and shortly after [Ken Arroyo Ohori](http://3dgeoinfo.bk.tudelft.nl/ken) extended the ideas during his [MSc thesis](http://repository.tudelft.nl/view/ir/uuid%3A78807acb-4115-478c-93de-68b9db884c8e/).
He added automatic repair functions, did a great C++ implementation that scales to large datasets, and [released the code open-source](https://github.com/tudelft3d/pprepair).
The code is rather popular: among others, it's been integrated in [FME](http://www.safe.com/fme/) and the [American Red Cross uses it to build their datasets](https://github.com/AmericanRedCross/simplegadm).
Simply put, the methodology is based on a constrained triangulation of the input polygons; we validate planar partitions by labelling triangles and ensuring that each triangle has one and only one label, and we repair by modifying the labels. 
We have published our methodology in a journal paper in 2012:

> Ken Arroyo Ohori, Hugo Ledoux and Martijn Meijers (2012).
Validation and automatic repair of planar partitions using a constrained triangulation. 
*Photogrammetrie, Fernerkundung, Geoinformation* 1(5):613–630. [[PDF]](http://3dgeoinfo.bk.tudelft.nl/hledoux/pdfs/12_pfg.pdf) [[link to paper]](http://dx.doi.org/10.1127/1432-8364/2012/0143)


We noticed in December 2014 that a new paper in the [International Journal of Geographical Information Science (IJGIS)](http://www.tandfonline.com/toc/tgis20/current) was, in our opinion, eerily similar to ours:

> Sunghwan Cho, M. Xavier Punithan, Jonggun Gim and Yong Huh (2014).
Tagging-the-triangle algorithm for partitioning features with inconsistent boundaries.
International Journal of Geographical Information Science 28(12):2533-2550 [[link to paper]](http://dx.doi.org/10.1080/13658816.2014.937716)

Also, our work was neither cited nor acknowledged.
I say eerily similar because of the following.


### 1. Exact same solution for the exact same problem

The problem in both papers is the construction of a planar partition from a set of polygons with gaps/overlaps, and both solutions are identical: the use of a constrained triangulation of the polygons as a base, labelling each polygon with the polygons that it belongs to, and reconstruction of the polygons from the triangulation. It is fair to mention that their paper goes one step further (subdivision of the problematic areas), but they use the exact solution we mentioned in our future work and that was implemented in 2011 by Martijn Meijers in his [PhD thesis](http://www.gdmc.nl/publications/2011/Variable-scale_Geo-information.pdf).
The thesis of Martijn is also not cited.

### 2. Both papers use the same criticism of the current standard solution

That is, snapping within a predefined threshold requires finding an acceptable threshold (which may or may not exist) and might create various topological inconsistencies.

### 3. Several figures are extremely similar

The figures concerning the problems with snapping are almost identical, see for instance these 3 (left our paper; right theirs).

![]({{ site.baseurl }}/img/plaex1.png)

- - -

![]({{ site.baseurl }}/img/plaex2.png)

- - -

![]({{ site.baseurl }}/img/plaex3.png)


### 4. Several sentences on key issues are extremely similar

We:

> If the set of input polygons forms a planar partition, then each segment will be inserted twice (except those forming the outer boundary of the set of input polygons). This is usually not a problem for triangulation libraries because they ignore points and segments at the same location (as is the case with the solution we use, see Section 4). When segments are found to intersect, they are split with a new point created at the intersection.

They:

> If two polygons share an edge e, the edge e is drawn twice. Because most triangulation programming libraries discard one point in the case of duplicate points, this step does not require further manipulation. Likewise, when edges intersect, they are split using a new vertex that is created at the intersection point. 

- - - 

We:

> If the set of input polygons forms a planar partition then all the triangles will be labelled with one and only one label. The problems are easily detected: Gaps are detected by finding triangles without any labels. Overlaps are detected by finding triangles with two or more labels.

They: 

> If all polygons in a data set form a planar partition, all triangles will be tagged as 1. Gaps or overlaps are easily recognised by checking whether the tag value is equal to 1 or not.


### What is plagiarism?
 
Individually, all of these could be coincidences.
But taken together it all seems a bit too much. 

Is their paper a copy of ours? No, it also differs significantly. 
And strictly speaking, no full sentences were copied.
However, the thrust of their paper is the triangle-based algorithm to form a planar partition from a set of polygons.
Without this algorithm, there is no paper in my opinion.

Moreover, it seems utterly impossible that the authors were not aware of our work on this topic, which spans several papers.
Simple Google searches, using their own keywords and terms, lead to several instances of our work in the first page ([one example](https://startpage.com/do/search?q=gaps+overlaps+triangulation+partitioning), [another one](https://startpage.com/do/search?query=inconsistent%20boundaries%20sliver%20polygons)).


### IJGIS editors reacted quickly

We notified the editors of IJGIS and they took the issue very seriously and responded quickly.
Which I appreciated a lot.
They followed the [COPE (Committee on Publishing Ethics) guidelines](http://publicationethics.org), which basically forces the authors to explain the similarities within a given frame of time.

Their answer was that they were not aware of the paper, and that if they had been, they would have cited it.
It has just been published online as a [corrigendum](http://dx.doi.org/10.1080/13658816.2015.1008949).
In the official PDF there is no mention of a correction, only on the [webpage of the paper](http://dx.doi.org/10.1080/13658816.2014.937716) can one see a correction, which is not very obvious.

![]({{ site.baseurl }}/img/tttcorrection.png)

<em>
Update: I was just informed by Taylor&Francis ([in a tweet](https://twitter.com/tandfauthorserv/status/603830792859561984), very 2015) that the CrossMark above the title also links to the corrigendum.
I didn't know that, and I had actually never clicked on any CrossMarks nor noticed them.
Good to know though.
</em>


![]({{ site.baseurl }}/img/crossmark.png)


Not surprisingly, I am not very happy with this outcome.
But is it worth pursuing the matter?
We decided not to, because proving that this is plagiarism is complex it seems and we do not gain much from it.
So instead I decided to write this blog post.

Could the editors have done more?
Perhaps, but proving plagiarism is also complex for them.
I think they handled this case rather well.

Thus, case closed. 
It's time to go back to writing more papers 😕

