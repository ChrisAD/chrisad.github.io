"""Generate Jekyll posts from YouTube video metadata.

Reads JSONL metadata (one video per line, from yt-dlp) in _data/videos/ and
writes one post per video into _posts/, dated by upload date.

Usage: python scripts/generate_posts.py
"""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "videos"
POSTS = ROOT / "_posts"

PODCAST_CHANNELS = {
    "The Entropy Podcast", "ktrlpanel", "Josh Amishav-Zlatin", "EYD Tech",
    "Blåskjerm Brødrene", "Monica Talks Cyber", "Security Weekly - A CRA Resource",
    "The XSS Rat", "Hacker Valley Media", "Göran Tømte", "tahawultech-com",
    "tahawultech com",
}
CONFERENCE_CHANNELS = {
    "BSides Oslo", "DefCamp", "OWASP Oslo", "Bergen Linux User Group",
    "Off By One Security",
}


def slugify(title):
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:70].rstrip("-")


def categorize(video, source):
    title = video["title"]
    channel = video.get("channel", "")
    if source == "featuring":
        if channel in CONFERENCE_CHANNELS or "Bsides" in title or "DefCamp" in title:
            return "conference-talk", f"A talk I gave, recorded by {channel}."
        if channel in PODCAST_CHANNELS or "podcast" in title.lower():
            return "podcast", f"An interview / podcast appearance on {channel}."
        if "webcast" in title.lower() or channel.startswith("SANS"):
            return "webcast", f"A webcast / appearance published by {channel}."
        return "appearance", f"An appearance published by {channel}."
    if "Natas" in title:
        return "natas-walkthrough", (
            "Part of my walkthrough series on the OverTheWire Natas web "
            "security challenges — hands-on, practical web hacking, one level "
            "at a time."
        )
    if "Book shelf" in title or "Bookshelf" in title:
        return "bookshelf", "A tour of my bookshelf — infosec and IT books I own and recommend."
    return "video", "A video from my YouTube channel."


def front_matter_escape(text):
    return text.replace('"', '\\"')


def make_post(video, source):
    date = video["upload_date"]  # YYYYMMDD
    date_fmt = f"{date[:4]}-{date[4:6]}-{date[6:]}"
    slug = slugify(video["title"])
    category, intro = categorize(video, source)
    tags = ["appearance" if source == "featuring" else "own-channel", category]

    lines = [
        "---",
        "layout: post",
        f'title: "{front_matter_escape(video["title"])}"',
        f"date: {date_fmt}",
        f"tags: [{', '.join(dict.fromkeys(tags))}]",
        f'channel: "{front_matter_escape(video.get("channel", ""))}"',
        f"youtube_id: {video['id']}",
        "---",
        "",
        intro,
        "",
        f'{{% include youtube.html id="{video["id"]}" title="{front_matter_escape(video["title"])}" %}}',
        "",
    ]
    description = (video.get("description") or "").strip()
    if description:
        lines += ["{% raw %}", description, "{% endraw %}", ""]
    channel = video.get("channel") or ""
    lines.append(
        f"[Watch on YouTube]({video['webpage_url']})"
        + (f" · via **{channel}**" if source == "featuring" and channel else "")
    )
    lines.append("")

    path = POSTS / f"{date_fmt}-{slug}.md"
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return path


def main():
    POSTS.mkdir(exist_ok=True)
    count = 0
    for source, filename in [("channel", "channel.jsonl"), ("featuring", "featuring.jsonl")]:
        for line in (DATA / filename).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            make_post(json.loads(line), source)
            count += 1
    print(f"Generated {count} posts in {POSTS}")


if __name__ == "__main__":
    main()
