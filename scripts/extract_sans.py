"""Extract the SANS pen-testing blog article bodies for posts 5 and 6."""

import os
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

SRC = Path(os.environ["TEMP"]) / "ssn"
OUT = SRC / "out"

for stem in ["05-doc-metadata-xss-sans", "06-azure-xss-sandbox-escape-sans"]:
    path = SRC / (stem + ".html")
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    for sel in ["#wm-ipp-base", "#wm-ipp", "script", "style", "noscript", "header", "footer", "nav"]:
        for tag in soup.select(sel):
            tag.decompose()
    body = soup.select_one(".post-entry") or soup.select_one("article")
    if body:
        for tag in body.select(".post-meta, .post-title, .post-footer, .post-links, .post-comments, .post-comment"):
            tag.decompose()
    if not body:
        print(f"NO BODY {stem}")
        continue
    md = markdownify(str(body), heading_style="ATX", bullets="-")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    (OUT / (stem + ".md")).write_text(md, encoding="utf-8")
    print(f"OK {stem} ({len(md)} chars)")
