"""One-time import of posts from the legacy chrisad.github.io Jekyll archive.

Own-channel videos become the videos collection; appearances merge into the
talks collection, matched against existing entries by YouTube ID or
normalized title so seeded approximate dates get upgraded to exact ones.
"""

import re
import sys
from pathlib import Path

LEGACY = Path(r"C:\Users\ChrisADM\riversec-repos\chrisad.github.io\_posts")
SITE = Path(r"C:\Users\ChrisADM\riversec-repos\chrisdale\src\content")
VIDEOS_DIR = SITE / "videos"
TALKS_DIR = SITE / "talks"

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
RAW_RE = re.compile(r"\{% raw %\}\n?(.*?)\n?\{% endraw %\}", re.DOTALL)


def parse_post(path):
    m = FM_RE.match(path.read_text(encoding="utf-8"))
    fm_text, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip().strip('"')
    tags = re.findall(r"[\w-]+", fm.get("tags", ""))
    raw = RAW_RE.search(body)
    description = raw.group(1).strip() if raw else ""
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    return {
        "slug": slug,
        "title": fm["title"],
        "date": fm["date"],
        "tags": tags,
        "channel": fm.get("channel", ""),
        "youtube_id": fm.get("youtube_id", ""),
        "description": description,
    }


def norm_title(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def yaml_quote(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def talk_type(tags):
    if "webcast" in tags:
        return "webinar"
    if "podcast" in tags:
        return "podcast"
    if "conference-talk" in tags:
        return "talk"
    return "video"


def load_existing_talks():
    existing = []
    for path in TALKS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        title = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.MULTILINE)
        yt = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)", text)
        existing.append(
            {
                "path": path,
                "text": text,
                "title": title.group(1) if title else "",
                "youtube_id": yt.group(1) if yt else None,
            }
        )
    return existing


def update_existing(entry, post, report):
    text = entry["text"]
    actions = []
    new_date_line = f"date: {post['date']}"
    text, n = re.subn(r"^date: .*$", new_date_line, text, count=1, flags=re.MULTILINE)
    if n:
        actions.append(f"date -> {post['date']}")
    watch = f"https://www.youtube.com/watch?v={post['youtube_id']}"
    if "url:" not in text:
        text = re.sub(r"^type: (.*)$", rf"type: \1\nurl: {watch}", text, count=1, flags=re.MULTILINE)
        actions.append("added url")
    entry["path"].write_text(text, encoding="utf-8")
    report.append(f"UPDATED {entry['path'].name}: {', '.join(actions)} (from {post['slug']})")


def write_talk(post, report):
    out = TALKS_DIR / f"{post['slug']}.md"
    if out.exists():
        report.append(f"SKIPPED {out.name}: file already exists")
        return
    lines = [
        "---",
        f"title: {yaml_quote(post['title'])}",
        f"event: {yaml_quote(post['channel'])}",
        f"date: {post['date']}",
        f"type: {talk_type(post['tags'])}",
        f"url: https://www.youtube.com/watch?v={post['youtube_id']}",
        "---",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")
    report.append(f"NEW talk {out.name} [{talk_type(post['tags'])}] ({post['channel']})")


def write_video(post, report):
    VIDEOS_DIR.mkdir(exist_ok=True)
    out = VIDEOS_DIR / f"{post['slug']}.md"
    keep_tags = [t for t in post["tags"] if t not in ("own-channel", "video")]
    lines = [
        "---",
        f"title: {yaml_quote(post['title'])}",
        f"date: {post['date']}",
        f"youtubeId: {post['youtube_id']}",
    ]
    if keep_tags:
        lines.append(f"tags: [{', '.join(keep_tags)}]")
    lines += ["---", ""]
    if post["description"]:
        lines += [post["description"], ""]
    out.write_text("\n".join(lines), encoding="utf-8")
    report.append(f"NEW video {out.name}")


def main():
    posts = sorted((parse_post(p) for p in LEGACY.glob("*.md")), key=lambda x: x["date"])
    existing = load_existing_talks()
    by_yt = {e["youtube_id"]: e for e in existing if e["youtube_id"]}
    by_title = {norm_title(e["title"]): e for e in existing if e["title"]}
    report = []

    videos = talks = 0
    for post in posts:
        if "own-channel" in post["tags"]:
            write_video(post, report)
            videos += 1
        elif "appearance" in post["tags"]:
            match = by_yt.get(post["youtube_id"]) or by_title.get(norm_title(post["title"]))
            if match:
                update_existing(match, post, report)
            else:
                write_talk(post, report)
            talks += 1

    print("\n".join(report))
    print(f"\n{videos} videos, {talks} appearances processed")


if __name__ == "__main__":
    main()
