---
title: "On paying the ransom: my comment to Digi.no on the Canvas case"
description: "Digi.no asked me to weigh in after Canvas's owner reached an agreement with the attackers behind a breach affecting universities. My short answer: paying feeds the problem."
date: 2026-05-13
tags: [ransomware, incident-response]
---

Digi.no featured my reaction to the news that the owner of Canvas reached an agreement with the group behind the data breach affecting universities. You can read their piece (in Norwegian) here: [Sikkerhetseksperter advarer etter Canvas-betaling](https://www.digi.no/artikler/sikkerhetseksperter-advarer-etter-canvas-betaling/571963).

My position on paying is not complicated. Every payment is a signal to the market that this business model works, and that signal does not stay contained to one victim. It funds the next campaign, sharpens the tooling, and tells other groups that organizations in your sector will pay. In other words, paying to make one incident go away helps attract the next one, to you and to everyone around you.

I understand why it happens. When systems are down, data is gone, and the pressure is real, a payment can look like the fastest way out. But it comes with no guarantees. You are trusting criminals to delete what they stole and to hand over working keys, and you are now a known payer. The money also rarely buys back trust, disclosure obligations, or the time spent rebuilding.

The uncomfortable truth is that the decision is usually made long before the incident, in whether you invested in the things that make paying unnecessary:

- Backups you have actually tested restoring, kept offline or immutable.
- An incident response plan people have rehearsed, not just filed.
- Enough visibility and segmentation that an intruder cannot reach everything at once.
- Knowing your attack surface before an attacker maps it for you.

If you get to the moment where paying feels like the only option, the real failure happened earlier. Build so that "no" is a decision you can afford to make.
