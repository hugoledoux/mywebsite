---
layout: page
title: software
permalink: /software/
---

# Open-source software


<div class="grid">
  {% for i in site.data.software %}
  <div class="unit one-third">
    <a href="{{ i.url }}" title="{{ i.description }}">
    <img src="{{ "/img/software/" | append: i.image | prepend: site.baseurl }}"/>
    <p>{{ i.name }}</p>
    </a>
  </div>
  {% endfor %}
</div>

