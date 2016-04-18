---
layout: post
title: Version 1.0 of val3dity is released!
author: Hugo Ledoux
date: 2016-04-18 16:59
category: blog
tags: validation
comments: true
---

![]({{ site.baseurl }}/img/val3dity.png)

Today I'm happy to officially release the v1.0 of [val3dity](https://github.com/tudelft3d/val3dity): my code to validate 3D geometries (solids, composite- and multi-surfaces) against the [ISO 190107](http://www.iso.org/iso/catalogue_detail.htm?csnumber=26012) rules.
[The source code of v1.0 is available here](https://github.com/tudelft3d/val3dity/releases/tag/v1.0).

I started in 2010 to work on it (thanks to a sponsorship from [Safe Software](http://www.safe.com)), and I've been working on it part-time since then.
During the OGC CityGML Quality Interoperability Experiment (QIE) in 2015, I've tested and improved it a lot.
It's now mature, robust and complete enough to be used by anyone.

To use it, you can either compile the code yourself (it's trivial under Mac and Linux) or use the [web application](http://geovalidation.bk.tudelft.nl/val3dity/).
The latter is a simple server that I maintain: upload your GML file, the latest version of val3dity will validate it and you'll get a detailed report back. 
Your uploaded file is deleted right after it's been validated, I promise.

Oh, and one nice option: you can even validate your CityGML files directly on your phone!
I'm sure this has happened to you too: you go to bed in the evening and then realise you totally forgot to validate the `<gml:Solid>` in your file...
Now you don't need to go back to your computer, you can do that from the comfort of your bed.

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://player.vimeo.com/video/163272193' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>






