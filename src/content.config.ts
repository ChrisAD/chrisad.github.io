import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});

const talks = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/talks' }),
  schema: z.object({
    title: z.string(),
    event: z.string(),
    date: z.coerce.date(),
    type: z.enum(['talk', 'podcast', 'webinar', 'video', 'tv', 'article']),
    url: z.string().url().optional(),
    slides: z.string().optional(),
    spotify: z.string().url().optional(),
  }),
});

const videos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/videos' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    youtubeId: z.string(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { posts, talks, videos };
