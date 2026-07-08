---
title: "Revisiting the Azure Kudu XSS: what Microsoft said"
description: "Ten years on, the email thread behind the Azure Kudu XSS is more interesting than the bug. A look at the disclosure, why MSRC kept rejecting it, and why they were wrong."
date: 2026-07-08
tags: [xss, azure, cloud, disclosure]
---

Back in 2015 I reported a bug in Azure that let a compromised tenant attack the administrator of the SaaS platform hosting it. I wrote up the technical side in [An Azure zero-day XSS with sandbox escape](/posts/azure-zero-day-xss-with-sandbox-escape/). What I never published was the disclosure thread, and honestly that thread is the better story. Reading it back years later, it is a small case study in how cloud trust boundaries were understood at the time, and in how hard it can be to get a triage team to look at the actual claim you are making.

### The bug, in one paragraph

I found a command injection on a website hosted in an Azure web app. That much is the customer's problem, not Microsoft's, and I agreed with that from the start. The interesting part was what I could do next. Azure ships Kudu with every web app, reachable by adding `scm` to the hostname. Kudu's Process Explorer lets an administrator open a process and view its full environment. Filenames cannot contain `<` or `>`, but environment variables can hold anything, and my command injection let me set them. So I set an environment variable to `<script>alert(1)</script>`, made the process hang so it stayed visible, and waited. When the SaaS administrator opened Process Explorer to debug the stuck process, my JavaScript ran in their authenticated Kudu session. From there you swap `alert(1)` for a BeEF hook and go to work on the operator, not just the customer.

That is the whole point: a bug in one tenant reaching out and executing code in the platform operator's browser.

### The thread

I reported it to MSRC in June 2015. The first reply was a form acknowledgement. The second was more telling:

> However, it sounds as though the product you mention is not owned by our company. Is there some indication you've received that this is not the case? If not, please contact the relevant service provider.

Kudu is a Microsoft project. It is on Microsoft's GitHub, written by Microsoft employees, shipped by default with every Azure web app. I pointed this out, linked the repository and the maintainers, and noted you cannot opt out of it. The reply moved the goalposts rather than the conclusion:

> I will pass this information on to the team responsible for reporting third-party vulnerabilities. Unfortunately, though, they will not be able to contact you directly in this matter, so I recommend that you report this matter directly to the Kudu as well.

Report it to "the Kudu." So I made the point that stuck with me the most: is every line of Windows written by Microsoft? Of course not. A vulnerability in third-party code shipped as part of your platform is still your platform's vulnerability. Using someone else's code does not move the responsibility off the product you ship.

Then the substance rejection arrived, and it repeated across three separate replies over two months:

> Your report says the attacker needs to have access to the web site first by compromising the website or stealing credentials of another user. If you have already compromised the account there are other malicious things you could do.

And later:

> if you need to first compromise the account or gain remote access, there is no vuln in the product; the vuln is in the user for allowing you to gain access.

I tried to draw the line as plainly as I could:

1. I sell a solution through Azure to one of my clients.
2. The client's site has a vulnerability and gets compromised. Fine, not the point.
3. Through that vulnerability I compromise not just the customer, but the SaaS provider itself.

The final answer:

> Upon investigation we have determined that this is not a valid vulnerability as it requires the attacker to first compromise the victim's credentials.

That was the end of the official conversation. The bug was quietly patched afterwards.

### Why they were wrong

The rejection collapses two different principals into one. Compromising the *customer's website* and compromising the *SaaS operator's Kudu session* are not the same thing. They are different accounts, different privilege levels, often different companies. The entire finding lives in the gap between them. MSRC kept answering "you already have access" as if the access I had (a shell on one tenant's site) were the same as the access I was reaching for (code running in the platform administrator's browser). It was not. Crossing from one to the other is the vulnerability.

The job of a shared hosting platform is to contain a compromised tenant. A malicious or merely vulnerable customer should not be able to reach the operator, or other customers, from inside their own box. This bug showed that containment failing, through an admin console that rendered tenant-controlled data without escaping it. That is a textbook stored XSS in a privileged tool, delivered over a channel nobody was watching.

I will be fair about the other side. By MSRC's strict definition of a product vulnerability in 2015, "requires prior access" was a real bar, and it was designed to filter out reports that boil down to "if I already own the machine I can do bad things." The problem is that this report was not that. The prior access was to a *different* trust zone, and the bug was precisely the escape from it. The bar was reasonable; applying it here was a category error.

### What I would do differently

Two things, mostly about framing.

First, I leaned on the words "sandbox escape" and "semi VM escape," and that gave the triage team an easy target. Nothing about a VM or a runtime sandbox breaks here. Calling it a *tenant-to-operator trust-boundary escape via blind stored XSS* is less punchy but harder to wave away, because it names the exact boundary being crossed. Precision in the title is worth more than drama when the reader is looking for a reason to close the ticket.

Second, I would lead with the two-principal diagram, not the payload. The technical mechanism was never really in dispute. What needed selling was that customer-compromise and operator-compromise are different events. Spending the first paragraph on that, and only then showing the environment-variable trick, would have made the report harder to misread.

### The takeaway

Cloud is someone else's server, and the boundaries between tenants and operators are where the interesting bugs live. When you report one, the hard part is often not the exploit. It is getting the reader to see which boundary you crossed. If your framing lets them substitute a simpler, weaker claim for the one you actually made, they will, and they will reject the weaker one. Name the boundary, show the two principals, and make the escalation impossible to miss.
