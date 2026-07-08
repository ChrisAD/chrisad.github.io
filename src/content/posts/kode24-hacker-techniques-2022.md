---
title: "Hacker techniques developers should know in 2022"
description: "My Kode24 guest post walking developers through four attack classes worth understanding: SQL injection, XXE, XSS, and SSRF, with the defensive takeaway for each."
date: 2022-01-20
tags: [appsec, web]
---

I wrote a guest post for [Kode24](https://www.kode24.no/) on the hacker techniques developers should understand going into 2022: [Hacker-knepene du bør vite om i 2022](https://www.kode24.no/artikkel/hacker-knepene-du-bor-vite-om-i-2022-sql-injection-xxe-xxs-og-ssrf/139205) (in Norwegian). Four attack classes, and the defence for each.

- **SQL injection.** The application fails to separate data from commands, so user input like `chrisdale' OR '1'='1` becomes part of the query and returns everything. Fix: parameterized queries and prepared statements. Never concatenate user input into SQL.
- **XXE (XML External Entities).** XML parsers can be told to resolve entities that read local files or make network requests, for example pulling `file:///etc/passwd` into the response. Fix: disable external entity resolution in your parser and validate input.
- **XSS (Cross-Site Scripting).** Unencoded user input reflected into a page runs as script in the victim's browser; stored XSS persists and hits every viewer. Fix: output-encode for the context you render into, do not rely on input filtering alone.
- **SSRF (Server-Side Request Forgery).** You trick the server into making requests on your behalf, reaching internal services or cloud metadata endpoints. Fix: restrict outbound requests and validate destinations against an allowlist.

The through-line is the same one I keep coming back to: assume input is hostile, and understand these techniques well enough that you can design them out rather than patch them later.
