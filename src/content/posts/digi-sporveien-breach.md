---
title: "Digi.no on the Sporveien breach: you can't investigate what you didn't log"
description: "Digi.no covered Sporveien's data breach, where a lack of logging meant the case couldn't really be investigated. That gap is the story."
date: 2021-09-24
tags: [incident-response, media]
---

Digi.no covered a data breach at Sporveien, Oslo's public transport operator: [Sporveien utsatt for datainnbrudd](https://www.digi.no/artikler/sporveien-utsatt-for-datainnbrudd/513594) (in Norwegian, subscription).

The most instructive detail was not the intrusion itself but the aftermath: there was not enough logging and information to support a real investigation, so the case could not meaningfully be pursued. That is a pattern I see constantly, and it is worth calling out.

Detection and response live or die on telemetry you decided to collect before anything happened. When an incident hits and the logs are not there, you cannot answer the questions that matter: how did they get in, what did they touch, did data leave, is it over. Logging is not glamorous and it rarely gets budget until it is too late, but it is the difference between an incident you can scope and close and one you can only shrug at. Decide what you need to see, collect it, retain it long enough to be useful, and make sure someone is actually looking.
