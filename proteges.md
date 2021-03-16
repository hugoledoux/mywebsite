---
layout: page
title: protégés
permalink: /proteges/
---

# Protégés


## PhD students

{% for i in site.data.protegesphd %}

<p><strong>{{ i.name }} {{ i.van }} {{ i.surname }}</strong>
{% if i.homepage %} 
  (<a href="{{ i.homepage }}"><i class="fa fa-home"></i></a>)
{% endif %}
{% if i.thesis %} 
  <span class="label success">{{ i.period }}</span>
{% else %}
  <span class="label label">{{ i.period }}</span>
{% endif %}
{% if i.now %} 
  <span class="label info">now {{ i.now | markdownify | remove: '<p>' | remove: '</p>' }}</span>
{% endif %}
<br>
{{ i.title }}
{% if i.thesis %} 
  <a href="{{ i.thesis }}"><i class="fa fa-file-pdf-o"></i></a>
{% endif %}
</p>

{% endfor %}



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

<p><strong>{{ i.name }} {{ i.van }} {{ i.surname }}</strong> <span class="label label">{{ i.year }}</span><br><a href="{{ i.url }}">{{ i.title }}</a></p>

{% endif %}
{% endfor %}




  