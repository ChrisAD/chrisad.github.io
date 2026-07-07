import { getCollection } from 'astro:content';
import { OGImageRoute } from 'astro-og-canvas';

const posts = await getCollection('posts', ({ data }) => import.meta.env.DEV || !data.draft);

const pages = Object.fromEntries(posts.map((post) => [post.id, post.data]));

export const { getStaticPaths, GET } = await OGImageRoute({
  param: 'route',
  pages,
  getImageOptions: (_id, data: (typeof posts)[number]['data']) => ({
    title: data.title,
    description: data.description,
    bgGradient: [
      [13, 17, 23],
      [22, 27, 34],
    ],
    border: { color: [63, 185, 80], width: 12, side: 'inline-start' },
    padding: 60,
    font: {
      title: { color: [230, 237, 243], size: 58, weight: 'Bold', lineHeight: 1.2 },
      description: { color: [139, 148, 158], size: 28, lineHeight: 1.4 },
    },
  }),
});
