---
layout: page
title: protégés
permalink: /proteges/
---

# Protégés


## PhD students


[**GAO Weixiao**](https://3d.bk.tudelft.nl/weixiao) (2017--now)<br>
Automatic generation of semantic 3D city models from 3D textured meshes

[**Bob Heester**](https://3d.bk.tudelft.nl/bheester/) (2017--now)<br>
Integration of GIS and BIM through blockchain technology

[**Anna Labetski**](https://3d.bk.tudelft.nl/alabetski) (2016--now)<br>
Generalisation of 3D city models

[**Kavisha**](https://3d.bk.tudelft.nl/kavisha) (2015--now)<br>
[Storage and dissemination of massive 3D city models](http://www.3d4em.nl/rl2/)

[**Ravi Peters**](http://3d.bk.tudelft.nl/rypeters) (2013--2018)
<span class="label label">defended 2018/03/14</span><br> 
[Geographical point cloud modelling with the 3D medial axis transform](http://dx.doi.org/10.4233/uuid:f3a5f5af-ea54-40ba-8702-e193a087f243)

[**Filip Biljecki**](https://filipbiljecki.com/) (2012--2017)
<span class="label label">defended 2017/05/01</span><br> 
[Level of detail in 3D city models](http://doi.org/b463)

[**Ken Arroyo Ohori**](http://3d.bk.tudelft.nl/ken) (2011--2016) 
<span class="label label">defended 2016/04/06</span><br> 
[Higher-dimensional modelling of geographic information](https://3d.bk.tudelft.nl/ken/en/thesis/)

- - -

## MSc students 

{% assign msc = site.data.protegesmsc | sort: 'year' %}

{% for i in msc %}
{% if i.year == null %}

<p><strong>{{ i.name }} {{ i.van }} {{ i.surname }}</strong> (ongoing)<br>{{ i.title }}</p>

{% endif %}
{% endfor %}

{% for i in msc reversed %}
{% if i.year != null %}

<p><strong>{{ i.name }} {{ i.van }} {{ i.surname }}</strong> ({{i.year}})<br><a href="{{ i.url }}">{{ i.title }}</a></p>

{% endif %}
{% endfor %}




  