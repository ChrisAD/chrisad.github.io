# chrisdale.no

Personal site and blog for Chris Dale. Everything is markdown: write a `.md` file, push, and it's live.

Built with [Astro](https://astro.build), deployed to GitHub Pages via GitHub Actions on every push to `main`.

## Publish a post

1. Create `src/content/posts/my-post.md`:

   ```yaml
   ---
   title: "My post title"
   description: "One line shown in lists, RSS, and link previews"
   date: 2026-07-07
   tags: [asm, recon]   # optional
   featured: true        # optional, pins to top of front page with a ★
   draft: true           # optional, excluded from the published site
   ---

   Markdown body goes here. Code blocks get syntax highlighting automatically.
   ```

2. Push it:

   ```
   git add . && git commit -m "post: my post" && git push
   ```

3. Live on https://chrisdale.no in about a minute. The filename becomes the URL: `my-post.md` → `/posts/my-post/`.

Images: drop them in `public/img/` and reference as `![alt](/img/name.png)`.

## Add a talk / podcast / webinar / video

Create `src/content/talks/whatever.md`, frontmatter only, no body needed:

```yaml
---
title: "Talk title"
event: "Conference or show name"
date: 2026-11-01
type: talk            # talk | podcast | webinar | video | tv | article
url: https://...      # optional, main link (title becomes the link)
slides: https://...   # optional, shown as [slides]
spotify: https://...  # optional, shown as [spotify]
---
```

## Preview locally

```
npm install       # first time only
npm run dev       # http://localhost:4321, drafts ARE visible here, but never in the published site
npm run build     # what CI runs
```

## Structure

- `src/content/posts/`: blog posts (markdown)
- `src/content/talks/`: talks & media entries (markdown frontmatter)
- `src/content/videos/`: own-channel video archive, each page embeds the YouTube video (frontmatter: `title`, `date`, `youtubeId`, optional `tags`; body becomes the description)
- `src/pages/`: page templates (home, posts, talks, contact, RSS)
- `src/layouts/Base.astro` + `src/styles/global.css`: design
- `.github/workflows/deploy.yml`: build & deploy pipeline

## ⚠️ Seeded content to verify

The talks & media list was seeded from into.bio/chrisdale plus public search results. URLs come straight from those sources; the site only displays month + year, but many dates are **approximations** (set to the 1st of a plausible month). Fix any that matter:

- Exact dates known: `pentest-methodology-reform.md` (2025-07-22), `asm-continuous-pentesting.md` (2025-01-21), `tv2-ddos.md` (2022-06-29), `gulfnews-break-into-tech.md` (2019-04-17)
- `hacker-valley.md`: still no episode URL
- `automating-asm.md`: podcast name unknown, event says "Podcast, episode 76"
- `day-in-life-incident-responder.md`, `qa-security-testing.md`, `help-to-self-help.md`: venue unknown, event says "Presentation"
- `improving-penetration-tradecraft.md`: links to a SANS Zoom recording that may expire; the slides PDF is the stable link
