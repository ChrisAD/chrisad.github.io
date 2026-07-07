---
layout: page
title: Talks & Appearances
permalink: /talks/
---

Conference talks, webcasts, interviews, and podcast appearances, newest first.
Videos from my own channel live on the [home page](/).

<ul class="post-list">
{% for post in site.posts %}{% if post.tags contains "appearance" %}
  <li>
    <span class="post-meta">{{ post.date | date: "%B %-d, %Y" }} — {{ post.channel }}</span>
    <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
  </li>
{% endif %}{% endfor %}
</ul>
