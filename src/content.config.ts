import { glob } from "astro/loaders";

import { z, defineCollection } from "astro:content";

const papers = defineCollection({
    loader: glob({ pattern: '**/[^_]*.md', base: "./src/paper_list"}),
    schema: z.object({
        title: z.string(),
        url: z.string(), // doi url
        conference: z.string(),
        author: z.array(z.string()),
        year: z.number(),
        publisher: z.string(),
        month: z.string(),
        abstract: z.string(),
        doi: z.string(),
        ID: z.string(),
    })
})

function paperToBibtex(paper) {
    var authors = paper.data.author.join(' and ');
    return `@article{${paper.data.ID},
    title={${paper.data.title}},
    confierence={${paper.data.conference}},
    publisher={${paper.data.publisher}},
    author={${authors}},
    year={${paper.data.year}},
    month={${paper.data.month}}
}`
}

export const collections = { papers };
export { paperToBibtex };