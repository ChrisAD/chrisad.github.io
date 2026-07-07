---
title: "Case study: breaking into the smartest smart house"
description: "A live hack of Norway's smartest home for NRK: from the parking lot onto the LAN, through a HomeSeer zero-day, and up to the production controller."
date: 2017-10-04
tags: [iot, physical, story]
---

Because the media coverage could not cover all the technical details, and because I would rather not argue in the comment sections of news sites, I want to share the methodology here. I have taken some care in the text below to protect the homeowner's information, as we agreed I would not share anything sensitive.

Accessing this house from the internet proved hard. I made several attempts against the solutions hosted at the target's IP address, and none gave me a good foothold. I found one vulnerability that could have led to remote code execution, but scope limitations meant I could not proceed, so I notified the homeowner. I even sent phishing emails to try to capture his VPN credentials, to no avail. This guy was tight, well done. He was clearly well above average when it came to being security-conscious and proactive.

On to the next step. Could I reach the home's IoT if I was in the vicinity? I travelled to Stavanger with a film team from NRK for one of the most exciting live demos I have ever done. Anyone who knows me knows I rarely turn down a live hacking challenge, and the chance to try to break into the smartest of all the smart houses was a great project. I arrived on-site, sat in a white van in the parking lot, and started.

My gut told me I had to get onto the LAN to demonstrate anything interesting. I brought an SDR in case I wanted to attack the devices directly, but my instinct pointed at the LAN for maximum effect.

Attacking a wireless LAN usually means sniffing for packets, sending a deauthentication request while spoofing the access point, and capturing the 4-way handshake when a device reconnects. That handshake can be cracked, but how quickly depends entirely on the password strength and the attacker's resources. I fired up Hashcat on my GPU, but that would come down to luck and the quality of my wordlists. If the homeowner had a strong password, the whole trip would be wasted. So I used a HID attack instead: I plugged a USB device into one of his computers for ten seconds and simply stole the wireless key that way. Getting onto someone's wireless LAN should not be your last line of defense. Treat it as one barrier you expect to fail, and have others behind it.

Once on the LAN I was baffled by the sheer number of devices. As an attacker I love that, it is more attack surface. Where to start? I ran Nmap alongside EyeWitness to scan the network and screenshot every HTTP, HTTPS, VNC, and RDP service, which let me navigate quickly. I found a conference solution I could reconfigure, and through its menus I got it to reveal already-set passwords for my dossier. The lawn mower had a similar flaw exposing its clear-text password. Useful, but not enough. I wanted full access, so I kept looking.

Eventually I found a HomeSeer application. I had already studied smart-home technology and knew HomeSeer was one of the controllers used to administer a house. It looked complex and I had never worked with it, but this was clearly where I needed to be. After a while I found a zero-day authentication bypass in the HomeSeer controller that let me administer it remotely with a Linux shell. As a side note that apparently needs stating: a zero-day is a vulnerability with no vendor patch, and this one was not documented anywhere. I discovered it myself, not by googling. We went through responsible disclosure with the HomeSeer folks afterwards.

Jackpot, I thought. But as I explored, the controller could only see a fraction of the devices from my Nmap scan. Maybe I was using the product wrong, or missing a menu. On a very tight deadline, I had to be efficient, so I went and asked the homeowner, partly to see his reaction to my little Linux shell. He was surprised, then said "Aha, you are on my test HomeSeer, not my production HomeSeer." There were two controllers. Reviewing my scans showed nothing resembling the box I had broken into. Why? The other controller was `.htaccess` protected, sitting behind a web-server password before you even reached the application, so I had dismissed the prompt as "just another IoT".

That was obviously the place to break into, so I started multi-threaded password guessing: dictionary lists on some threads, word-mangling of the passwords I had already stolen on others, appending 0000-9999 and doing leetspeak substitution. Nothing worked.

Time was becoming a real problem. We were about to leave, and this was where I wanted to demo, so after a discussion we decided to share this one password so the demos could go ahead. In hindsight that was unnecessary, and I was a bit surprised at the "fake news" reaction to a password being shared. Does that void the risk for every other smart-house owner? I had already broken into several devices and proven the brain itself, the controller, could be compromised with a zero-day. In hindsight I should have run a clean ARP cache poisoning attack and had the homeowner authenticate, opening up sniffing of the credentials. Other options included hacking more devices to find one that shared the `.htaccess` password, or a flaw on the web server that let me read or modify the `.htaccess`.

That shared password was the only one given to me in the whole engagement, and the point of doing so was to prove the consequences of someone gaining access to your smart-home devices. I would challenge my fellow geeks to open their perspective beyond the hardcore security enthusiast and think about everyone else: friends, family, neighbours, people who get smart-home features as "part of the package" and have no idea how to operate them safely.

That is my two cents. It was a fun live demo, that is all.
