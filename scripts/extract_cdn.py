import os
from pathlib import Path
from bs4 import BeautifulSoup

SRC = Path(os.environ["TEMP"]) / "cdn"
for stem in ["home", "contact"]:
    soup = BeautifulSoup((SRC / (stem + ".html")).read_text(encoding="utf-8", errors="ignore"), "html.parser")
    for sel in ["#wm-ipp-base", "#wm-ipp", "script", "style", "noscript", "header", "footer", "nav"]:
        for tag in soup.select(sel):
            tag.decompose()
    main = soup.select_one("main") or soup.select_one("#site-content") or soup.select_one(".entry-content") or soup.body
    text = "\n".join(line.strip() for line in main.get_text("\n").splitlines() if line.strip())
    print(f"===================== {stem} =====================")
    print(text[:3000])
    print()
