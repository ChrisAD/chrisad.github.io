"""Extract clean article body markdown from archived securesolutions.no HTML.

Reads the Wayback snapshots saved under %TEMP%/ssn, strips the archive toolbar
and WordPress chrome, converts the entry-content body to markdown, and writes
one .md per post to %TEMP%/ssn/out for review/renewal before import.
"""

import os
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

SRC = Path(os.environ["TEMP"]) / "ssn"
OUT = SRC / "out"
OUT.mkdir(exist_ok=True)


def clean(md):
    md = re.sub(r"\n{3,}", "\n\n", md)
    # drop wayback rewritten link prefixes if any slipped through
    md = md.replace("/web/", "/web/")
    return md.strip()


for path in sorted(SRC.glob("*.html")):
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")

    # remove wayback toolbar and scripts/styles
    for sel in ["#wm-ipp-base", "#wm-ipp", "script", "style", "noscript"]:
        for tag in soup.select(sel):
            tag.decompose()

    body = soup.select_one(".entry-content") or soup.select_one(".post-content") or soup.select_one("article")
    if not body:
        print(f"NO BODY  {path.name}")
        continue

    # strip share/related/nav widgets commonly appended inside entry-content
    for tag in body.select(".sharedaddy, .jp-relatedposts, .post-navigation, .yarpp-related, .addtoany_share_save_container, .wp-caption-text"):
        tag.decompose()

    md = clean(markdownify(str(body), heading_style="ATX", bullets="-"))
    (OUT / (path.stem + ".md")).write_text(md, encoding="utf-8")
    print(f"OK  {path.stem}  ({len(md)} chars)")
