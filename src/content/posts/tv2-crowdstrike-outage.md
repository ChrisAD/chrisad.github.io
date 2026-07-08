---
title: "TV2 asked me about the global CrowdStrike outage"
description: "A faulty CrowdStrike update blue-screened Windows systems worldwide. TV2 spoke with me about what happened and why a single vendor update could cause that much disruption."
date: 2024-07-19
tags: [incident-response, media]
---

On July 19, 2024, a faulty update from CrowdStrike sent Windows systems around the world into the blue screen of death, disrupting airlines, hospitals, banks, and countless other services. TV2 spoke with me about it: [Omfattende dataproblemer i hele verden](https://www.tv2.no/nyheter/omfattende-dataproblemer-i-hele-verden-1/16854851/).

The key point I wanted to get across: this was not a cyberattack. It was a bad update to software that runs deep in the operating system, on an enormous number of machines, pushed broadly at once. That is exactly why the blast radius was so large.

The uncomfortable lesson is about concentration and fragility. When one vendor's agent runs at kernel level across a huge share of the world's critical systems, a single mistake becomes a global event. The defenses are not glamorous, but they matter: staged and canaried rollouts rather than pushing to everyone at once, tested recovery procedures so you can actually get machines back, and enough resilience in your architecture that one component failing does not take everything with it.

Security is not only about keeping attackers out. It is also about surviving the day something you depend on simply breaks.
