---
title: "DevSecOps can take development to new heights"
description: "My guest post on Kode24: how folding security into DevOps lets developers ship fast and safely, from defensive coding and reusable libraries to behavioural monitoring."
date: 2023-03-14
tags: [devsecops, appsec]
---

I wrote a guest post for [Kode24](https://www.kode24.no/) on DevSecOps and why folding security into DevOps lets teams keep shipping fast without shipping vulnerabilities: [DevSecOps kan ta utvikling til nye høyder](https://www.kode24.no/artikkel/devsecops-kan-ta-utvikling-til-nye-hoyder/166268) (in Norwegian).

The core argument is that security, development, and operations are not competing priorities. Merged well, they become a competitive advantage. A few of the points I made:

- **Be defensive.** Prefer allowlists (permit only what is known-good) over blocklists (chase every bad input). Defensive code is safer code, even if it means handling more rejected edge cases up front.
- **Respond rapidly.** You will not catch everything before release, so build the muscle to identify and patch issues quickly once they surface.
- **Lean on existing libraries.** Use well-tested security building blocks like AJV for JSON validation rather than hand-rolling your own protections across every app.
- **Monitor continuously.** The DevOps tooling you already have, like Grafana dashboards, can double as security telemetry. A sudden spike in HTTP 500s can be the first sign of someone probing you.
- **Behaviour over signatures.** Instead of relying only on signature-based detection, establish a baseline of normal and alert on deviations. It catches the things no signature has seen yet.

The theme throughout: give developers the tools and the mindset to build safely, and security stops being the team that says no.
