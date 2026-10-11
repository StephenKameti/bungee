---
name: designed-deck-builder
description: Turn any deck into AI image prompts that generate fully DESIGNED slides, with the deck's copy rendered inside the image, in a bespoke design language invented for that specific brand after researching its colours, logo, products and typography, for any market in the world via an optional market module. Use this skill whenever the user wants a deck that "looks designed", wants slide images with the copy in them, asks to "design the deck" with AI images, wants "designed deck prompts", complains that deck visuals look "too corporate" or "like a template", or uploads a deck and asks for it to be turned into finished-looking slides via an image model. Also use it for reworking designed-slide prompts that were rejected on taste. Do not use it when the user only wants background or accent images with NO text rendered in them, or when the deliverable is one campaign master visual rather than a deck.
---

# Designed Deck Builder

## Market layer (do this first)

Before any design thinking, establish the market or markets this deck belongs to: the brand's home market, and the audience's market, when the two differ. The design language's textures, retail and street references, typography behaviour for rendered local-language copy, casting and photography settings, and any regulatory notes the on-slide copy must observe, all derive from the stated market.

If the brief does not state a market, ask one question to confirm it, unless the user has already stated their own home market earlier in the conversation, in which case use that without asking again.

Once the market is known, look for `references/markets/<market>.md`. If a file exists for that market, load it and use it as the source of texture, retail, casting and regulatory detail. If no file exists, build the local specificity directly from the brief and from research into that market's visual culture, retail environment and regulatory environment, never generic filler.

`references/markets/east-africa.md` is supplied as a worked market module. `references/markets/TEMPLATE.md` is a blank copy for building a new one.

## Core Mandate

Generate image prompts where the generated image IS the finished slide: layout, typography, photography and the deck's actual copy, all rendered by the image model. The result should look like it came from an award-winning design studio, and it should look like it was designed for THIS brand, in THIS market, not adapted from the last one.

The single most important rule: **the design language is invented fresh per brand and market.** If two decks for two different brands would look interchangeable with the logos swapped, the skill has failed. Style comes from the brand's own world and the market it is speaking to; only the craft standards are constant.

## Step 1 · Ingest the deck

Get the full slide-by-slide copy before any design thinking. Sources, in order of preference: an uploaded file (read it), a cloud drive file (fetch it), or copy pasted in chat. If only a topic is given, say what a deck outline is needed for and offer to draft one first.

Extract every slide's verbatim text. While extracting, note obviously broken source lines (typos, autocorrect wrecks, half-sentences). Do not silently keep or silently fix them: correct them in the prompts and list every correction in a "copy flags" section so the user can revert. Everything else stays word for word, this is the client's approved copy, not raw material.

## Step 2 · Research the brand

Research before designing, using web search plus anything the user uploaded. Build a compact **Brand Sheet**:

- **Colours**: the real brand hexes (primary, secondary, accent). If sources conflict, prefer the brand's own site/guidelines and say which you used.
- **Logo and lockups**: describe it; the user will attach the real file to the image model, so the prompts must treat it as an attached asset, never redrawn.
- **Products / hero SKUs**: what the bottle, pack, device or storefront actually looks like, this is Image 2 in every prompt.
- **Typography**: the brand's typeface if known, plus the closest widely available equivalents described in image-prompt language ("bold condensed grotesque", "high-contrast editorial serif"), image models follow style descriptions, not font names.
- **Brand world**: taglines, current campaign, tone, category conventions, and the market's visual vernacular, drawn from both the brand's home market and the audience's market, which are not always the same place. As an example, a Nairobi founded FMCG brand decked for a Nairobi retail audience draws on Kenyan design codes and Nairobi's own retail texture, load `references/markets/east-africa.md` for that case; the same method applied to a Berlin founded fintech decked for a Berlin audience draws on Berlin's design codes instead, and would need its own market module built the same way.

Ask the user only about genuine gaps: an obscure brand with no reliable sources, conflicting palettes, or a rebrand in progress. Otherwise present the Brand Sheet and move on.

## Step 3 · Invent the design language

This is the heart of the skill. Invent a **named** design language for this deck, a name the user can approve, reject, or ask you to push further ("Editorial Storm", "Night Harvest", "Ledger & Neon").

Derive it from the brand's own world, not from a house style:

- **Material truth**: what does the product touch? Tiles, foam, soil, malt, chrome, skin, receipts, road dust. Those become the textures.
- **Category tension**: what does every deck in this category look like, and which of those codes is worth breaking? (Beer decks are amber and laughing groups; a beer deck in ledger-and-ink stands out.)
- **Brand temperament**: heritage brands can carry print and archival devices; challenger brands can carry stickers, tape and shouting type; premium brands carry restraint and one perfect flourish.
- **Market vernacular**: the local design culture of the market layer above is a source of devices, used with respect and specificity, never as costume.

Compose the language from device families, pick differently for every brand so no two decks share a fingerprint:

| Family | Example devices (non-exhaustive) |
|---|---|
| Type behaviour | cropped-off-frame condensed caps · liquid/elastic letterforms · ink-trap grotesque · typewriter dossier · high-contrast serif pull quotes · vertical spine titles |
| Texture | film grain · halftone dots · torn paper · risograph misprint · fabric weave · condensation/frost · paper ledger rules · pixel/glitch |
| Photo treatment | brand-colour duotone · flash-lit night documentary · muted archival · hyper-clean studio · infrared/surreal grade |
| Collage devices | sticker cutouts with die-cut borders · tape strips · rubber stamps · polaroids · ticket stubs · price tags · receipts · pinned casting cards |
| Structure | ghost numerals · bento grid · magazine columns with hairline rules · gig-poster lineup · contact-sheet filmstrip · asymmetric layouts with depth |
| Accent | one signature accent per deck: a marker underline, a red thread, a foil chip, a neon rule, never more than one family of flourish |

Define a **two-mood system** with brand-specific names: a quiet mode for content slides (the argument) and a loud mode for hero slides (cover, big idea, closing, one or two mid-deck moments). Rhythm between the two is what makes a deck feel designed rather than decorated.

Offer 2 or 3 named languages via a multiple-choice question with vivid one-sentence descriptions, recommend one, and wait for the pick when the user is present. Working unattended, pick the strongest, name it, and state the choice up front.

Craft standards that hold for every language: one idea per slide dominates; generous whitespace even in maximal styles; real hierarchy (one huge thing, one medium, the rest small); content-through-medium wherever possible, offers as price tags, retail mechanics printed on a receipt, a talent roster as a casting wall, a route as ticket stubs on a map. A slide whose medium retells its message needs no decoration.

## Step 4 · Ask the production questions

One round of multiple-choice questions before writing prompts (skip any already answered): target image model (default the image model with the strongest text rendering and the best preservation of attached brand assets, or the user's own named stack if they already have one); copy handling (verbatim everything vs. headlines verbatim with overlong body tightened and flagged); pure-table slides (render the table in-image vs. designed frame with empty panels for live text); aspect (16:9 default).

## Step 5 · Write the prompts

One prompt per slide, fully self-contained so any slide can regenerate alone. Every prompt carries:

1. **Format**: "Design a 16:9 presentation slide in [language name] style", the word *design* (not "photo of a slide") pushes the model into layout mode.
2. **Asset contract**: "Image 1 is the [brand] logo, Image 2 is the [product]. Place exactly as provided, never redrawn." Add after the first approved render: "Image 3 is the approved style reference; match its design system."
3. **The style DNA**: 2–3 sentences of this deck's language, ground, textures, type behaviour, photo treatment, accent, with brand hexes inline.
4. **Layout in spatial language**: top to bottom, left to right, thirds, what dominates. Name where every copy block sits.
5. **Copy in double quotes**: quoting forces character-by-character rendering. Structure so each block stays short, under ~15 words a block renders near-perfectly; 30+ word paragraphs degrade badly, so break them into stacked lines, cards, rows or columns that are each independently fixable.
6. **Closing bar**: "Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks."

Give every slide a one-line rationale (why this treatment for this message). Mark text-dense slides **HEAVY** with a fix strategy: which zones to repair, in what order, one zone per edit ("Keep everything identical. In card 3 the text must read exactly: '…'"). Repair beats regeneration, targeted edits succeed roughly three times in four, while regeneration discards every already-correct line. After 5–7 edit rounds, restart from the best frame. Numbers get proofread first; a swapped digit is worse than a typo.

Match treatment to slide type rather than one template: covers and big-idea slides go loud mode full bleed; frameworks become pinboards, cycles, or filmstrips, never consulting boxes; data slides make one number the hero and the rest fine print; mockup slides (vehicles, merch) shoot like product-culture photography with swing tags; closings end on one word and one object.

## Step 6 · Deliver as a prompt library

Deliver a copyable prompt library, not a wall of text. When an artifact/page tool is available, build an HTML library page: masthead with deck name, palette chips and the language's name; a "attach these assets every time" card; the copy-flags card; prompts grouped into acts with per-card copy buttons, badges (mood + HEAVY), rationale lines and fix notes; a footer with run order (lock the look with the cover first, then light slides, heavy slides last), the repair rules, and a one-line rescue edit for renders that drift generic ("Add heavy film grain, rougher textures. Change no text."). Without an artifact tool, deliver the same structure as a markdown file.

Style consistency workflow to include in every delivery: run one image-model chat session per act so multi-turn context holds the style; generate the cover until it is loved, then attach it as the standing style reference for every later prompt; keep the same attachment set on every message including edits.

## What good looks like

For a Kenyan market toilet-cleaner roadshow deck, this skill produced "Editorial Storm": culture-magazine spreads on tile-textured paper, cobalt duotone market photography with film grain, cropped condensed type, sticker cutouts and red tape, offers rendered as swing price tags and a retail mechanic printed on a till receipt with a REDEEMED stamp, pulling its texture and retail references from `references/markets/east-africa.md`. For a Bogota market deck for the same brand, the method is identical but the materials are not: the market module would point toward Bogota's own retail texture and street graphics instead, and the two design languages should read as unmistakably different cities, not the same deck with a new coat of paint. For a different brand in either market, the next language must be built fresh from that brand's own materials; the test is that no two libraries could ever be mistaken for siblings.
