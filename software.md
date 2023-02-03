---
layout: page
title: software
permalink: /software/
---

# Open-source software

<div class="message">
Most of the software I write is available under a permissive licence. Here are links to my most popular and mature projects, but <a href="https://github.com/hugoledoux">my GitHub page</a> and <a href="https://github.com/tudelft3d">that of my research group</a> contain more.
<br><br>
<i class="bi bi-exclamation-circle-fill" aria-hidden="true"></i> My <a href="http://www.onlinemagazine.library.tudelft.nl/?p=2060">open-source efforts have been featured in the TU Delft library magazine</a> as a best practice for researchers.
</div>


{% assign s = site.data.software | sort %}

{% for i in s %}
  <a href="https://github.com/{{ i }}"><img src="https://gh-card.dev/repos/{{ i }}.svg"></a>
{% endfor %}


