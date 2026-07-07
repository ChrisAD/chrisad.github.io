---
title: "Deception concepts: the elements of deception"
description: "Deception is not just for attackers. Four abstractions (NEDI, NEFI, EEDI, EEFI) to structure defensive deception planning."
date: 2022-11-16
tags: [deception, defense, blue-team]
---

Deception is not reserved for attackers. Defenders can play the deceptive game too, and it can be game changing. Here are four abstractions worth considering during deception planning. They come from the military deception literature, and they map cleanly onto defending a network.

Think of every piece of information as belonging to one of four quadrants, split on two questions: is it true or fictional, and do we want to reveal it or hide it?

### NEDI: nonessential elements of deceptive information

Fictional information that is to be hidden. Information we can let attackers find, but not too obviously, because we do not want the deception to read as deceitful. Examples:

- Fake emails seeded into user inboxes containing NEDI
- Password files on shares that hold credentials to notional systems

### NEFI: nonessential elements of friendly information

Truths that are to be revealed. Information we are happy to share, truths that strengthen our position, affirm the attacker's understanding, or otherwise support the story we want them to keep believing. Make them verifiable. Examples:

- Network information that is true but not sensitive
- Disclosure of real, harmless files and information

### EEDI: essential elements of deceptive information

Fictional information that is to be revealed to the adversary. The traps, lures, and fiction we present, hoping to deceive and influence the adversary's decisions and actions. These are our falsehoods. Examples:

- Notional systems, users, files, and honeypots
- Modified network traffic that reveals lures

### EEFI: essential elements of friendly information

Truths that are to be hidden. Our real strengths, weaknesses, and anything we do not want the adversary to exploit or reveal. Examples:

- Network diagrams of important networks
- Credentials to real users and systems
- Defensive capabilities that should not be evaded

Framing your deception program around these four buckets makes it much easier to reason about what to plant, what to confirm, what to fake, and what to protect.
