---
layout: page
title: protégés
permalink: /proteges/
---

# Protégés


## PhD students

[**Du Xin**](https://3d.bk.tudelft.nl/duxin) (2015@now)<br>
Quality control of 3D city models

[**Kavisha**](https://3d.bk.tudelft.nl/kavisha) (2015@now)<br>
[Storage and dissemination of massive 3D city models](http://www.3d4em.nl/rl2/)

[**Ravi Peters**](http://3d.bk.tudelft.nl/rypeters) (2013@now)<br>
[Feature-aware DSM analysis and generalisation based on the 3D medial axis transform](http://3d.bk.tudelft.nl/projects/3dsm)

[**Filip Biljecki**](http://3d.bk.tudelft.nl/biljecki) (2012@now)<br> 
[The concept of level of detail in 3D city modelling](http://3d.bk.tudelft.nl/biljecki/phd.html)

[**Ken Arroyo Ohori**](http://3d.bk.tudelft.nl/ken) (defended 2016/04/06)<br> 
[Higher-dimensional modelling of geographic information](https://3d.bk.tudelft.nl/ken/en/thesis/)

---

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




  