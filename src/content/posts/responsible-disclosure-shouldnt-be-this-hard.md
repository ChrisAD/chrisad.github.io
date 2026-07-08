---
title: "Responsible disclosure shouldn't be this hard"
description: "I found open cloud buckets with 10,000+ PII documents and spent months trying to get someone, anyone, to act. It took going to NRK before the data was finally secured."
date: 2025-10-11
tags: [disclosure, cloud, privacy]
featured: false
---

Responsible disclosure is often a thankless job.

When I find open cloud buckets containing 10,000+ PII documents, what is the first step? Try to attribute ownership, so I can disclose responsibly.

My first attribution turned out to be wrong. The company replied that it probably belonged to someone else. Progress, right? I reached out to the other company through LinkedIn DMs and their website: "I have identified a vulnerability and would like to report it so you can fix it as soon as possible."

No response.

Months later, the same buckets reappeared on my radar through River Security's continuous data hunts, with new files exposed. Still unpatched. Still public.

So what do you do next? How far do you go to protect the public and the innocent? How many doors do you knock on before someone listens? Who can be responsible?

I reported it to the Norwegian National Security Authority (NSM / NorCERT): "Thank you for your report, we will investigate." Then silence. Months passed. I escalated to Datatilsynet. Still nothing. The files remained public.

At some point you start asking: does harm actually need to happen before someone reacts? Around the same time I read about 100,000 Italian PII records leaked online, and here I was staring at a "small" 10,000+ dataset just waiting to be taken.

That is when I went to NRK, who published the story. Finally, through journalists, something happened: the buckets were removed and the data secured. You can read it (in Norwegian) here: [Fant personopplysninger fra bilklage-selskap åpent på nett](https://www.nrk.no/norge/fant-personopplysninger-fra-bilklage-selskap-apent-pa-nett-1.17363602).

It should not have to be this hard. Thanks to Julie Helene Günther at NRK for getting it done.
