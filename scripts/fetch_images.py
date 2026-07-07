"""Download content-essential images for the imported securesolutions.no posts
into public/img/ssn, routing through the Wayback Machine and validating that
each response is really an image (not a soft-404 HTML wall).
"""

import os
import re
import time
import urllib.request
from pathlib import Path

SRC = Path(os.environ["TEMP"]) / "ssn" / "out"
DEST = Path(r"C:\Users\ChrisADM\riversec-repos\chrisdale\public\img\ssn")
DEST.mkdir(parents=True, exist_ok=True)

JOBS = {
    "05-doc-metadata-xss-sans": ("doc-metadata-xss", "2016"),
    "06-azure-xss-sandbox-escape-sans": ("azure-xss", "2018"),
}

IMG_RE = re.compile(r"!\[[^\]]*\]\((\S+?)\)")
MAGIC = {b"\x89PNG": ".png", b"\xff\xd8\xff": ".jpg", b"GIF8": ".gif"}

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]


def sniff(data):
    for magic, ext in MAGIC.items():
        if data.startswith(magic):
            return ext
    return None


for stem, (prefix, ts) in JOBS.items():
    text = (SRC / (stem + ".md")).read_text(encoding="utf-8")
    urls = []
    for u in IMG_RE.findall(text):
        if u.startswith("http") and u not in urls:
            urls.append(u)
    for i, u in enumerate(urls, 1):
        wb = f"https://web.archive.org/web/{ts}id_/{u}"
        ok = False
        for attempt in range(3):
            try:
                data = opener.open(wb, timeout=60).read()
                ext = sniff(data)
                if ext:
                    (DEST / f"{prefix}-{i:02d}{ext}").write_bytes(data)
                    print(f"OK   {prefix}-{i:02d}{ext}  ({len(data)} bytes)")
                    ok = True
                    break
                print(f"  not-image attempt {attempt + 1} for {prefix}-{i:02d}")
            except Exception as e:
                print(f"  err attempt {attempt + 1} for {prefix}-{i:02d}: {e}")
            time.sleep(4)
        if not ok:
            print(f"FAIL {prefix}-{i:02d}  {u}")
        time.sleep(1)
