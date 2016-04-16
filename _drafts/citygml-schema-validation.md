---
layout: post
title: Validation of CityGML files against the schemas
author: Hugo Ledoux
category: blog
tags: validation
comments: true
---

While I work a lot on the data quality of 3D city models, I often brush aside the validation of a CityGML file against the schemas (*.xsd) of CityGML as a simple and solved problem.
However, while it's indeed a solved problem, I realised that there are, to my knowledge, no free and easy tools to validate a CityGML file.
Which means that in practice we often see files that are not valid.
I usually use [oXygen XML](http://www.oxygenxml.com), but this is not free and rather cumbersome when the `xsi:schemaLocation` for the schemas are not properly setup as in the following, then one must manually find the appropriate schema (v0.4, v1.0 or v.20) and have them locally ("where have I put these again?")

{% highlight xml %}
<?xml version="1.0" encoding="UTF-8"?>
<CityModel 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:pfx0="http://www.citygml.org/citygml/profiles/base/1.0" xmlns:xlink="http://www.w3.org/1999/xlink" 
...
xsi:schemaLocation="http://www.citygml.org/citygml/profiles/base/1.0 http://schemas.opengis.net/citygml/profiles/base/1.0/CityGML.xsd">
{% endhighlight %} 

So I wrote a small Python script that takes as input a CityGML file, determines which version of CityGML is used, validate the file and give the first error, if any.
[Get it there](https://github.com/tudelft3d/CityGML-schema-validation)
The CityGML schemas of all versions are included.

To use:

{% highlight bash %}
$ ./valxsdcitygml.py input.gml
{% endhighlight %} 

or you can also give a folder and all XML and GML files in that folder (and in all the folders inside that one) are validated

{% highlight bash %}
$ ./valxsdcitygml.py /home/elvis/data/
{% endhighlight %} 

