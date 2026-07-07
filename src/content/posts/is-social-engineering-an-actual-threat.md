---
title: "Is social engineering an actual threat?"
description: "Why social engineering keeps working, the psychological levers behind it, and classic examples including the HBGary hack."
date: 2012-12-23
tags: [social-engineering, story]
---

A question came up on [security.stackexchange.com](https://security.stackexchange.com/) about whether social engineering is still a threat. It referenced Kevin Mitnick's 2002 book *The Art of Deception: Controlling the Human Element of Security*, and asked whether, after a decade of technology and learning, we should not be immune by now.

Social engineering is very much alive today, and I doubt that changes in decades, if ever. Here are some brief explanations of why it works. It is a broad field and impossible to cover fully, but the levers below capture a lot of it:

- Most people want to be polite, especially to strangers.
- Professionals want to appear well informed and intelligent.
- If you praise people, they often talk more and divulge more.
- Most people would not lie for the sake of lying.
- Most people respond kindly to someone who appears concerned about them.

**Being helpful.** Humans generally want to help each other. I run into the reception of a big corporate office with my papers soaked in coffee, explain that I have a job interview in five minutes, and ask the receptionist to please reprint them from this USB stick. That may infect the receptionist's PC and give me a foothold in the network.

**Using fear.** The fear of failing or of not doing as ordered. The director's Facebook page shows he has just left on a three-week cruise. I call the secretary with a commanding voice: "Hi, it is Chris. I just got off the phone with John Smith, he is having a great time on his cruise. We are in the middle of integrating an important business system and he asked me to call you. He could not call himself because they are heading on a safari, but this is urgent. Just take the USB stick addressed to him in the mail, plug it in, and we are done. Thank you, you have been a great help, I am sure John will recognize you for it." 

**Playing on reciprocation.** The tailgate. I hold the entry door for you and walk close behind. At the next door, which is access-controlled, most people repay the favor by holding it for me, letting me into a place I should not be. Worried about getting caught? You just say sorry and that you went the wrong way.

**Exploiting curiosity.** Drop ten USB sticks around an organization, not in obvious places. If they carry an auto-run phone-home program, you see when someone plugs one in. A variant is a single PDF named something like "John Smith - Norway.pdf" that carries a reader exploit tailored to the target's software. It feels natural to open it to find the owner. The same curiosity drives all those spam mails claiming you have won something or that a prince needs your help. They have not stopped because they still work.

Those are just examples. There are countless more.

### A historic case: HBGary

HBGary was famously hacked in 2011, an attack with many steps and a social-engineering component. In short, the attacker compromised the email account of a company VIP and emailed a system administrator something like: "Hi John, I am in Europe bouncing between airports. Can you open SSH on a high port for me from any IP? I need to get some work done." Coming from a trusted source, the admin felt it natural to comply.

That was not all. The attacker had the password but the login was not working, so they emailed back: "It is not working, the password is still right? What was the username again?" This both supplied the real password (obtained earlier in the same breach) to build trust, and prompted the admin to hand over the username. He complied.

I will sum up with the Bruce Schneier line: *amateurs hack systems, professionals hack people.*
