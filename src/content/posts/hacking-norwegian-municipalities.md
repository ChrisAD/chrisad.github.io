---
title: "I was challenged to hack Norwegian municipalities, and I hit the jackpot"
description: "Given a challenge to hack Norway's municipalities, I went broad: all 357 at once. The payoff was a third-party AWS-hosted CMS behind 101 webservers, and a lesson about who sets your pentest scope."
date: 2026-07-01
tags: [recon, asm]
featured: true
---

I hit the jackpot. Recently I got to show Norwegian municipalities the importance of doing broad reconnaissance and continuous penetration testing.

I was challenged to hack municipalities, and I did. I went with a very broad approach, targeting all **357 municipalities** at once, looking for vulnerabilities across the whole surface rather than one target at a time. Sure enough, I hit the jackpot: I gained access to a system in AWS that many dozens of municipalities were using as their CMS, **101 webservers in total**. What makes it even more interesting is that the system was hosted and operated by a third party.

That last detail is the point. When you run a penetration test, ask yourself: who is setting the scope? If it is you, then how are you ever going to know where I, the hacker, will find the next vulnerability? The attacker does not respect your scope, your asset inventory, or the boundary between you and your suppliers. They follow the path of least resistance, and that path very often runs straight through a third party you assumed someone else was watching.

This is one of the many reasons we set up River Security: to help customers with exactly this kind of challenge. Broad, continuous reconnaissance across your real attack surface, including the parts you do not operate yourself, is how you find the exposure before someone else does.
