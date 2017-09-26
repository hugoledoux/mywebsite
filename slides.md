---
layout: page
title: slides
permalink: /slides/
---

# Presentations

<div class="message">
  I was told that no one reads articles anymore, "people want PPT slides".
  So here you are, the slides of some of the presentations I recently gave.
</div>


<div class="grid">
  {% for i in site.data.pres %}
  <div class="unit half">
    <p>{{ i.url }}</p>
  </div>
  {% endfor %}
</div>

