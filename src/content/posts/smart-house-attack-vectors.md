---
title: "Smart house attack vectors"
description: "Beyond WPA2 and a firewall: WPS, pre-compromised LAN hosts, evil-maid USB attacks, weak ISP routers, leaked credentials, and sub-GHz radio protocols."
date: 2017-10-09
tags: [iot, appsec]
---

There is a healthy debate in Norway right now about smart home security. Internet of Things security is poor, as researchers, malware, and worms have proven repeatedly. Are our devices and private information safe just because we run a WPA2-PSK wifi network with strict firewall rules? Here are some other ways to get through a smart house's outer defenses.

**WPS may be enabled.** Wi-Fi Protected Setup is on by default in many devices and adds to the attack surface. For years it has been a go-to way to break into wireless networks. There are protections, but in a world where not every device runs the latest firmware, it remains a valid method.

**Pre-compromised computers on the internal network.** Botnets run into the millions of hosts. If any infected computer sits on a smart house's LAN, the attacker is already inside. With access being bought and sold, shopping for bots that are already inside smart homes could become a real thing. IoT is famously insecure, so a foothold on the LAN makes extending into those devices much easier. Then there is metamorphic malware that changes behavior based on the network it lands on: is there a Z-Wave device here? Phone home, pull down modules, compromise it too.

**The evil-maid attack.** Most people have heard of the cleaner who gets bribed, or coerced, into plugging in a USB. For a home that is unlikely, but the threat is still there in a different form. What about family, friends, friends of friends, anyone who has ever been on your wifi and knows the password? Do you trust them all? A sad truth about a lot of crime, especially against children, is that it is often committed by someone close to the family.

**The ISP's cheap router.** The commodity box your ISP rents you is not perfect. We have seen weak PRNG functions leak WPA passwords just from a device's MAC address, or in some cases a brute-forceable serial number. Assume your edge devices contain vulnerabilities, and plan to stay somewhat secure when they fail.

**Leaked credentials.** Every month or so a major breach hits the news. Your passwords, or a family member's, could leak tomorrow. If those are synced to a VPN into your house or an app on your phone, the breach can reach into your smart home. If I lose the password to my Nissan Leaf, someone could control functions of the car remotely. Expect the same from all our gadgets, locks, and cameras.

**Sub-GHz radio protocols.** Many smart-home gadgets talk on bands other than 802.11, for example the proprietary Z-Wave protocol around 900 MHz. With the right equipment, such as an SDR, those protocols can have vulnerabilities too. Z-Wave devices have been hacked on several occasions, and being proprietary means little transparency about their security. Newer generations ship with strong encryption and signing, but that does not make them secure. A flaw in the devices themselves could open your front door without ever touching your wifi.

**Predictable pre-shared keys.** The WPA key is often not randomized, so dictionary attacks work fine against many homes. People pick predictable passwords: words from their language, numbers 0000-9999 (often 1980-2030 at the end of a word), street names, phone numbers, last names. People will be people, and they have picked bad passwords throughout the history of IT. If you want to make your life easier, use a password manager.

I am not fear-mongering here. I just want us to be realistic and to stop anyone thinking "I have an unhackable house." That is nonsense. Know the risks you are running and decide what risk level is acceptable. Personally I would like a semi-smart house. My TV does not need to be smart, and I would like my front door and alarm decoupled from everything else for defense in depth. I am not telling you to avoid gadgets, just do not be surprised when you see them hacked, and have a plan for when you do.
