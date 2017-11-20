---
layout: page
title: software
permalink: /software/
---

# Open-source software

<div class="message">
Most of the software I write is available under a permissive licence. Here are links to my most popular and mature projects, but <a href="https://github.com/hugoledoux">my GitHub page</a> and <a href="https://github.com/tudelft3d">that of my research group</a> contain more.
<br><br>
My <a href="http://www.onlinemagazine.library.tudelft.nl/?p=2060">open-source efforts have been featured in the TU Delft library magazine</a> as a best practice for researchers.
</div>

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

