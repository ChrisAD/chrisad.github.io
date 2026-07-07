"""Extract article bodies for the second batch of securesolutions.no posts."""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify

SRC = Path(os.environ["TEMP"]) / "ssn2"
OUT = SRC / "out"
OUT.mkdir(exist_ok=True)

for path in sorted(SRC.glob("*.html")):
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    for sel in ["#wm-ipp-base", "#wm-ipp", "script", "style", "noscript"]:
        for tag in soup.select(sel):
            tag.decompose()
    body = soup.select_one(".entry-content") or soup.select_one(".post-content") or soup.select_one("article")
    if not body:
        print(f"NO BODY {path.name}")
        continue
    for tag in body.select(".sharedaddy, .jp-relatedposts, .addtoany_share_save_container, .post-navigation"):
        tag.decompose()
    md = re.sub(r"\n{3,}", "\n\n", markdownify(str(body), heading_style="ATX", bullets="-")).strip()
    (OUT / (path.stem + ".md")).write_text(md, encoding="utf-8")
    print(f"OK {path.stem} ({len(md)} chars)")
