---
title: "One word for the most important security solution"
description: "Scraping a LinkedIn word game where infosec professionals named the single most important thing in security, and visualizing the answers."
date: 2012-05-12
tags: [awareness, data]
---

On LinkedIn there was a word game in the "Information Security Community" group. The idea was to name, in a single word, what you think is the most important thing in IT security. The discussion ran for over a year and kept resurfacing in my newsletters. I do not actually believe you can reduce it to one word, but the discussion was interesting for the perspective the collected data could give.

### Collecting the data

I browsed the thread, extracted every answer, and processed it to visualize what people thought was their single most important thing. I wrote a small Java tool that pulled the text from the thread, stripped the noise, and collected the words. It gave me:

- 268 unique words
- 471 words total
- 697 total comments in the thread

I only counted posts that were submitted as a single word, so I missed replies where the word was buried in a longer post. I did not want to overcomplicate the code or do it by hand, and the excerpt is still representative.

### The results

Ranking the words by how often they were mentioned, the top ten were:

| Word | Mentions |
| --- | --- |
| awareness | 44 |
| education | 34 |
| people | 13 |
| training | 11 |
| diligence | 8 |
| knowledge | 7 |
| intelligence | 6 |
| experience | 5 |
| monitoring | 5 |
| prevention | 5 |

My conclusion is that general security awareness matters enormously and clearly needs to improve. If we can train and educate our people, we raise awareness, and in turn become inherently more secure. It is telling that the top answers are all about people rather than products.
