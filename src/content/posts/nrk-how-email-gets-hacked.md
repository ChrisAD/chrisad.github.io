---
title: "NRK: how your email account gets hacked"
description: "NRK had me demonstrate how email accounts get taken over. The uncomfortable truth: most of it is trivial, because we reuse passwords. Two-factor is what actually gets in an attacker's way."
date: 2020-09-07
tags: [phishing, awareness, media]
---

NRK asked me to show how email accounts actually get hacked, in the wake of the 2020 breach affecting Norwegian parliament email accounts: [Slik kan e-postkontoen din bli hacket](https://www.nrk.no/norge/slik-kan-e-postkontoen-din-bli-hacket-1.15145667) (in Norwegian).

My honest reaction to a lot of these breaches is that the techniques are trivial. As I told NRK, "what you are writing about now, it is so trivial." The reason it keeps working is us: nearly all of us reuse the same password in several places. An attacker takes credentials leaked from one breach and simply tries them everywhere else.

The main techniques I walked through:

- **Password reuse** from previous breaches, sprayed across other services.
- **Phishing**, sending a convincing fake email to capture both the password and the two-factor code.
- **SMS interception**, including fake cell towers to grab codes sent over text.
- **Malware** on the device to bypass protections entirely.

The encouraging part is where the difficulty flips. As I put it, once you move to two-factor authentication, I as the attacker actually have a problem. It does not make you invincible, but it turns "trivial" into "real work," and for most people that is the single highest-value thing you can turn on today.
