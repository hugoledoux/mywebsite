---
layout: page
title: software
permalink: /software/
---

# Open-source software

<div class="message">
Most of the software I write is available under a permissive licence, below the most popular and mature of my projects.
My code is spread mostly over:
 <ul>
  <li><a href="https://github.com/hugoledoux">github.com/hugoledoux</a></li>
  <li><a href="https://github.com/tudelft3d">github.com/tudelft3d</a></li>
  <li><a href="https://github.com/cityjson">github.com/cityjson</a></li>
</ul> 

<i class="bi bi-exclamation-circle-fill" aria-hidden="true"></i> My <a href="https://web.archive.org/web/20221224231100/http://www.onlinemagazine.library.tudelft.nl/?p=2060">open-source efforts have been featured in the TU Delft library magazine</a> as a best practice for researchers.
</div>


{% assign s = site.data.software | sort %}

{% for i in s %}
  <a href="https://github.com/{{ i }}"><img src="https://gh-card.dev/repos/{{ i }}.svg"></a>
{% endfor %}


