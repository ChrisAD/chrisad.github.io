---
title: "Welcome, and how this site works"
description: "chrisdale.no is now live. Here is how content gets published here, and how you can write for a site like this in nothing but markdown."
date: 2026-07-07
tags: [meta]
featured: true
---

Welcome to chrisdale.no. This site is where I'll be featuring writing on offensive security, incident response, and attack surface management, plus pointers to talks, podcasts, and videos.

The whole site is driven by plain markdown files. Publishing a post looks like this:

1. Create a file in `src/content/posts/`, for example `my-post.md`
2. Give it some frontmatter:

```yaml
---
title: "My post title"
description: "One line shown in lists, RSS, and link previews"
date: 2026-07-07
tags: [asm, recon]   # optional
featured: true        # optional, pins it to the top of the front page
draft: true           # optional, excluded from the published site
---
```

3. Write markdown below the frontmatter
4. Commit and push, and GitHub Actions builds and deploys it in about a minute

Code blocks get proper syntax highlighting out of the box:

```bash
# the authoring workflow, in full
git add src/content/posts/my-post.md
git commit -m "post: my post"
git push
```

That's it. More to come.
