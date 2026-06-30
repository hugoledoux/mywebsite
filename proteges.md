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
  (<a href="{{ i.homepage }}"><i class="bi bi-house-door-fill"></i></a>)
{% endif %}
{% if i.thesis %} 
  <span class="label success">{{ i.period }}</span>
{% else %}
  <span class="label success">{{ i.period }}</span>
{% endif %}
{% if i.now %} 
  <span class="label info">now {{ i.now | markdownify | remove: '<p>' | remove: '</p>' }}</span>
{% endif %}
{% if i.note %} 
  <span class="label note">{{ i.note | markdownify | remove: '<p>' | remove: '</p>' }} </span>
{% endif %}
<br>
{{ i.title }}
{% if i.thesis %} 
  <a href="{{ i.thesis }}"><i class="bi bi-file-earmark-pdf"></i></a>
{% endif %}
</p>

{% endfor %}



- - -

## MSc students 

{% assign ongoing = site.data.protegesmsc | where_exp: 'item', 'item.year == nil' | sort: 'surname' %}
{% assign completed = site.data.protegesmsc | where_exp: 'item', 'item.year != nil' %}
{% assign groups = completed | group_by: 'year' | sort: 'name' | reverse %}

{% for group in groups %}
  {% assign sorted = group.items | sort: 'surname' %}
  {% for i in sorted %}

<p>
  <strong>{{ i.name }} {{ i.van }} {{ i.surname }}</strong> <span class="label success">{{ i.year }}</span>
  {% if i.paper %}
    <a href="{{ i.paper }}"><i class="bi bi-file-earmark-pdf" title="paper"></i></a>
  {% endif %}
  {% if i.github %}
    <a href="{{ i.github }}"><i class="bi bi-github" title="github"></i></a>
  {% endif %}
  {% if i.note %} 
    <span class="label note">{{ i.note | markdownify | remove: '<p>' | remove: '</p>' }}</span>
  {% endif %}
  <br>
  <a href="{{ i.link }}">{{ i.title }}</a>
</p>

  {% endfor %}
{% endfor %}

{% for i in ongoing %}

<p><strong>{{ i.name }} {{ i.van }} {{ i.surname }}</strong> (ongoing)<br>{{ i.title }}</p>

{% endfor %}
