---
title: "On paying the ransom: my comment to Digi.no on the Canvas case"
description: "Digi.no asked me to weigh in after Canvas's owner reached an agreement with the attackers behind a breach affecting universities. My short answer: paying feeds the problem."
date: 2026-05-13
tags: [ransomware, incident-response]
---

Digi.no featured my reaction to the news that the owner of Canvas reached an agreement with the group behind the data breach affecting universities. You can read their piece (in Norwegian) here: [Sikkerhetseksperter advarer etter Canvas-betaling](https://www.digi.no/artikler/sikkerhetseksperter-advarer-etter-canvas-betaling/571963).

My position on paying is not complicated. Criminals have for a long time learned that this business model works, and sometimes companies have to pay to keep themselves alive; it is a business decision, and it sucks. What are you going to do if your backups are deleted, and everything is gone..? Go bankrupt, or consider paying? 

In terms of paying, you never pay without first seeing proof of life / recovery. That is up to the criminals to prove. Once you see that you can get your files back, payment becomes and option and negotiations can commence. The website https://ransomch.at/ has information about such negotiations. 

The uncomfortable truth is that the decision is usually made long before the incident, in whether you invested in the things that make paying unnecessary:

- Backups you have actually tested restoring, kept offline or immutable.
- An incident response plan people have rehearsed, not just filed.
- Enough visibility and segmentation that an intruder cannot reach everything at once.
- Knowing your attack surface before an attacker maps it for you.

If you get to the moment where paying feels like the only option, the real failure happened earlier. Build so that "no" is a decision you can afford to make.
