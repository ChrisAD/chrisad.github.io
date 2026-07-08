---
title: "Digi.no on the Nordic Choice data leak"
description: "Digi.no covered the Nordic Choice breach, where employee personal data was dumped online. I commented on what double-extortion ransomware means for the people whose data leaks."
date: 2021-12-16
tags: [ransomware, media]
---

Digi.no covered the leak of employee data from Nordic Choice after their breach, and asked me to comment: [Enorm lekkasje fra Nordic Choice lagt ut på nettet](https://www.digi.no/artikler/enorm-lekkasje-fra-nordic-choice-lagt-ut-pa-nettet/515833) (in Norwegian, subscription).

The detail worth dwelling on is what actually leaked: personal identification numbers, salaries, bank account details, and other sensitive information about thousands of employees. This is the modern shape of ransomware. It is no longer just about encrypting your systems, it is double extortion: steal the data first, then publish it if you do not pay. That means the harm lands on individuals who never made the decision, the employees whose most sensitive details are now public and permanent.

For defenders the lesson is uncomfortable but clear. Backups protect you from the encryption half of the attack, but they do nothing about the leak half. Once data is exfiltrated, the only real defenses were the ones you put in place beforehand: knowing where sensitive data lives, minimizing what you collect and retain, segmenting access, and detecting the exfiltration while it is happening rather than reading about it online afterwards.
