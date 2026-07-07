# chrisad.github.io

Jekyll site (GitHub Pages) collecting Chris Dale's cyber security videos as a
chronological archive — own-channel tutorials plus talks, webcasts, and podcast
appearances from other channels.

## Structure

- `_posts/` — one post per video, dated by YouTube upload date
- `_data/videos/*.jsonl` — video metadata pulled with yt-dlp (one JSON object per line)
- `scripts/generate_posts.py` — regenerates `_posts/` from the metadata

## Updating with new videos

```sh
# Fetch metadata for new video IDs (append to the relevant jsonl):
yt-dlp --skip-download --print "%(.{id,title,upload_date,duration,view_count,channel,webpage_url,description})j" \
  "https://www.youtube.com/watch?v=VIDEO_ID" >> _data/videos/channel.jsonl   # or featuring.jsonl

# Regenerate posts:
python scripts/generate_posts.py
```

Sources: [youtube.com/c/chrisdale](https://www.youtube.com/c/chrisdale) and the
[Videos featuring Chris Dale](https://www.youtube.com/playlist?list=PLag7W-lJE2AwoUXtXcYmnnrqnL6LMPhvT) playlist.
