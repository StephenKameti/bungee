# Deck Designer

Engine: prompts/skills/designed-deck-builder. Stitch screens: S11, S12.

## Stages
| # | Stage | Input | Output schema | Checkpoint |
|---|---|---|---|---|
| 1 | Ingest | PPTX, PDF or pasted copy, comments | SlideCopy[] and Comment[] | User edits copy |
| 2 | Research | Brand kit, website URL if given | BrandWorld | None |
| 3 | Languages | BrandWorld, SlideCopy | DesignLanguage[3] | User picks one |
| 4 | Type lock | Chosen language | TypeSpec | Locked |
| 5 | Slide prompts | SlideCopy, language, TypeSpec | SlidePrompt[] | Per slide regenerate |

## Schemas
```ts
SlideCopy = { index, headline, body, footnote, notes, comments: string[] }
DesignLanguage = { name, colour: {name, hex, role}[], type: { headline, body, footnote }, grid, photography, signatureMove, sampleSlideIndex }
TypeSpec = { headline: {family, weight, size, style}, body: {...}, footnote: {...} }
SlidePrompt = { index, prompt: { text, aspect: "16:9" }, commentsActioned: string[] }
```

## Rules enforced in code
TypeSpec injected verbatim into every slide prompt. Comments actioned before generation and listed.

## Exports
Slides PDF, PPTX with full bleed images, prompt pack.
