# Claude Code build prompts

Run in order. One prompt per session, /clear between them, commit after every passing check.

## CC1 Read, then plan (plan mode)

_Start Claude Code in the repo, switch to plan mode first (Shift+Tab until it shows plan mode)._

```
Read CLAUDE.md, DESIGN.md, docs/PRD.md, docs/USER-JOURNEYS.md, docs/RESEARCH.md and every file in docs/apps/. Also skim prompts/skills/ so you understand the five engines.

Do not write code yet. Produce PLAN.md in the repo root with:
1. The architecture you will build, as a short diagram in text.
2. The database schema as a table list with key columns.
3. The AI run pipeline: how a brief becomes staged, streamed, schema validated output for each tool.
4. Milestones matching docs/BUILD-PLAN.md, each with acceptance checks I can verify in the browser.
5. Risks and open questions for me, maximum eight, each with your recommended answer.

Keep PLAN.md under 400 lines. Ask me the open questions before we leave plan mode.
```

**Check:** PLAN.md exists, reads clearly, and every open question has your answer before you approve the plan.

## CC2 Scaffold the monorepo

_Leave plan mode. Approve the plan first._

```
Scaffold the project exactly as PLAN.md describes:
apps/web: React 18, Vite, TypeScript strict, Tailwind CSS, Motion (import from "motion/react"), React Router, TanStack Query.
apps/api: Node 20, Express, TypeScript strict, Zod, Drizzle ORM on Neon Postgres, pino logging.
packages/shared: Zod schemas and TypeScript types shared by web and api (brief, brand kit, and one output schema per tool, taken from docs/apps/*.md).
Tooling: pnpm workspaces, ESLint, Prettier, Vitest, Playwright, a root "dev" script that runs web and api together, .env.example with every variable from CLAUDE.md.

Add a /health endpoint and a web page that calls it. Commit with a clear message when both run locally.
```

**Check:** pnpm dev starts both apps, the web page shows the api health response, lint and typecheck pass.

## CC3 Pull the Stitch design into code

_Needs the Stitch MCP connected (see Step 4 of the guide)._

```
Use the Stitch MCP to read my Bungee Studio project. Pull the latest DESIGN.md into the repo root, replacing the starter version, and list the screens you found.

Then turn DESIGN.md into code:
1. Tailwind theme tokens and CSS variables for every colour, type style, radius and spacing value. No raw hex values anywhere else in the codebase.
2. Load Instrument Serif, Hanken Grotesk and JetBrains Mono with proper fallbacks.
3. Build these primitives in apps/web/src/ui with a Storybook style playground page at /dev/ui: Button (primary, secondary, ghost), Input, Textarea, Select, Tag (safe, strong, wild, danger, neutral), Card, PaperSheet (the lightbox surface), PromptPlate (dark mono block with copy), CopyButton, Drawer, Modal, Tabs, Tooltip, Toast, Skeleton, EmptyState, StepTracker (Brief, Read back, Explore, Refine, Deliver), StreamingText (word by word with a Clay caret), PlanList (stages that tick off), HorizonLine, CreditsMeter, CommandPalette.
4. Every component keyboard accessible with visible Clay focus rings and 4.5:1 contrast.

Match the Stitch screens pixel close. Where Stitch and DESIGN.md disagree, DESIGN.md wins. Tell me every place you had to guess.
```

**Check:** Open /dev/ui and compare side by side with Stitch. Fonts, colours and radii should be identical.

## CC4 App shell, navigation and command palette



```
Build the signed in app shell from the Stitch screen "Home and project library":
Sidebar (248px, collapsible to icons), top bar with search, the HorizonLine on the top edge, and routes: /home, /projects, /projects/:id, /brand-kits, /brand-kits/:id, /moments, /new, /tools/key-visual, /tools/retail-theatre, /tools/deck-designer, /tools/content-calendar, /tools/campaign-strategy, /settings/*.

Add the command palette on Cmd K / Ctrl K with groups: Create (new brief, new brand kit), Go to (every route), Recent projects, and Actions on the current page. Add keyboard shortcuts: N new brief, G then H home, G then P projects, ? shows all shortcuts.

Page transitions: 180ms fade and 8px rise with Motion, respecting prefers reduced motion. Build real empty states with the plain words from DESIGN.md, switchable per workspace language.
```

**Check:** Every route renders inside the shell, Cmd K works everywhere, reduced motion disables animation.

## CC5 Auth, workspaces and database



```
Add authentication and multi tenant workspaces:
Email magic link plus Google sign in. Each user belongs to one or more workspaces with roles owner, editor, viewer.

Create the Drizzle schema and migrations for: users, workspaces, memberships, brand_kits, assets (files in object storage with type, size, checksum), projects, briefs (raw input, parsed read back, status), runs (tool, stage, model, tokens in and out, cost, duration, status), outputs (tool, schema version, JSON payload, version number), images (prompt, model, aspect, storage key, credits used), subscriptions, entitlements (which tools a workspace can use), credit_ledger (every grant and spend), share_links, audit_log.

Uploads go to S3 compatible object storage with signed URLs, 25 MB limit, and virus scan hook left as a TODO with a clear interface. Row level access checks in one middleware: a user can only ever touch rows from their workspace. Write tests that prove a user cannot read another workspace's brief.
```

**Check:** Sign in works, the cross workspace access test fails correctly when you break the middleware on purpose.

## CC6 The AI engine

_The heart of the product. Take your time here._

```
Build apps/api/src/ai as a small engine every tool uses:

1. Skill loader: read the matching file in prompts/skills/<tool>/SKILL.md plus its references at startup and use it as the system prompt. Use prompt caching on the system prompt so repeat runs are cheaper.
2. Staged runs: each tool is a list of stages defined in docs/apps/<tool>.md. A stage has an input, a Zod output schema from packages/shared, a model, and a max token budget. Stages run in order; the user can pause between stages when "Ask me before each step" is on.
3. Structured output: every stage returns JSON through tool use with a JSON schema generated from the Zod schema. Validate with Zod. On failure, send one repair request with the validation errors, then fail gracefully with a readable message.
4. Streaming: stream progress to the browser with Server Sent Events: stage started, partial text for human readable fields, stage complete, errors. The web client renders these with StreamingText and PlanList.
5. Models: default "claude-sonnet-5" for all stages; "claude-opus-5" when the workspace turns on Deep mode. Keep model names in one config file.
6. Guards applied to every piece of client facing copy before it is saved: replace hyphens and em dashes in copy fields with spaces or commas, and flag output that names a third party brand (anything that is not the user's own brand kit) so the user reviews it before export. Log every guard hit.
7. Cost and usage: record tokens, cost and duration per run in the runs table.
8. Long runs execute as background jobs with a job id so a closed tab does not kill the work; the client can reconnect to the stream.

Write unit tests for the loader, the repair loop and the guards.
```

**Check:** A test script runs one stage end to end and stores valid JSON. Kill the tab mid run, reopen, and the stream resumes.

## CC7 Brief intake and read back (shared by all tools)

_Match the Stitch screens New brief intake and Brief read back._

```
Build /new and the read back step:
Input: paste text, upload (PDF, PPTX, DOCX, images of chat screenshots), or a voice note. Extract text server side: PDF text, PPTX slide text and speaker notes and comments, DOCX text, OCR for images through the vision capable model, speech to text for voice notes through a configurable speech to text provider.
Brand kit selector, reference images, and the five tool toggles.
Run the "read back" stage: fill the spine (product hero, business problem, single minded proposition, insight, audience, channels, mandatories, no gos). Mark every field the model inferred with assumed: true so the UI shows the Saffron "Assumed" tag.
Ask at most one sharp clarifying question when a gap would change the work; show it as the question card.
Every spine field is editable inline and saved. The "What we still need" checklist updates live.
One brief can feed several tools. Store it once and link runs to it.
```

**Check:** Paste a messy chat style brief and get a clean spine with assumed fields tagged, and at most one question.

## CC8 Key Visual tool

_Stitch screens: route spread and route detail. Spec: docs/apps/key-visual.md._

```
Build the Key Visual tool on the AI engine using prompts/skills/key-visual-builder as the system prompt and the stages in docs/apps/key-visual.md.

Route spread page: grid and wall views, filter by Safe, Strong, Wild, shortlist, compare two to four routes side by side, the "Fire these first" panel and the disruptive alternate.
Route detail page: preview area with variations filmstrip, master prompt plate with copy, copy suite rows with copy, adaptation kit table where each format can be generated, designer build sheet, and a Motion brief tab for shortlisted routes (spec chips, beat grid shot list, sound line, Copy brief). Validate every motion brief in code: holds meet the readability law, the logo lands on a downbeat, the shots cover the full length.
"Direct this route" input with the chips Make it simpler, Make it clearer, Warmer light, Pack bigger, Too serious, More local. Map each chip to the feedback table in the skill so the route is rebuilt, not just reworded.
Keep every version of a route and let me step back through versions.
```

**Check:** Run a real brief. You should get six to eight distinct routes with a real spread, and chips should visibly change the idea, not only the words.

## CC9 Image previews and credits

_Uses the Gemini image models. Needs billing enabled on the Google key._

```
Add an image service in apps/api/src/images:
Default model "gemini-3.1-flash-image-preview" with an option for "gemini-3-pro-image-preview" as a Pro quality toggle. Keep model IDs in config.
Support aspect ratios 1:1, 4:5, 9:16, 16:9, 2:1, 3:4, reference images from the brand kit (pack shots and logo), and variations.
Spend credits from credit_ledger before calling the model, refund on failure. Show cost in credits on every generate button before the click.
Store images in object storage with the prompt and model used. Generate small WebP thumbnails for grids.
Queue concurrent generations per workspace to protect rate limits. Show a skeleton with the HorizonLine loading bar while generating.
```

**Check:** Generate two previews, see credits drop by two, force a failure and see the refund in the ledger.

## CC10 Retail Theatre tool

_Stitch screen: family planner. Spec: docs/apps/retail-theatre.md._

```
Build Retail Theatre with prompts/skills/fsu-display-units as the engine and the stages in docs/apps/retail-theatre.md.
Environment selector, the family lineup (floor, gondola end, shelf, counter) sharing one material language, the device library with one device per unit, unit cards with render previews, collapsed prompts with copy, dimensions, and production notes.
The honesty check drawer lists what is buildable locally, what costs more and what to fake in post.
Enforce the skill rules in code: exactly one theatrical device per unit, and every unit prompt keeps panels blank for type in post.
```

**Check:** Choose Pharmacy, pick two devices, and receive a coherent family where every unit shares materials.

## CC11 Deck Designer tool

_Stitch screens: language picker and storyboard. Spec: docs/apps/deck-designer.md._

```
Build Deck Designer with prompts/skills/designed-deck-builder as the engine:
1. Ingest a PPTX or PDF deck or pasted copy. Extract slide by slide copy and any comments. Show extracted copy for editing before design starts. Comments are actioned first and listed in a "Comments actioned" note.
2. Generate three named design language proposals, each with type, colour, grid, photography rules and a signature move, plus a sample slide preview. The user picks one.
3. Lock typography: once chosen, one type spec (family, weight, size, styling for headline, body and footnote) is stored and injected into every slide prompt. No slide may drift.
4. Storyboard strip, large slide view, Copy, Prompt and Comments tabs, regenerate per slide, generate all with credit cost shown.
5. Export: prompt pack as text, generated slides as a PDF, and a PPTX with one full bleed image per slide using pptxgenjs.
```

**Check:** Upload a 10 slide deck with two comments; confirm both comments are actioned and all slides share the same type spec.

## CC12 Content Calendar tool

_Stitch screen: month view. Spec: docs/apps/content-calendar.md._

```
Build Content Calendar with prompts/skills/social-content-calendar-builder as the engine.
Import data/moments-2027.json (88 global moments plus regional packs) into a moments table and show moments on the month grid, filtered by the regions and countries selected. Sensitive moments render with the red stripe and the post generator must not place promotional posts on them.
Month grid with pillar colour edges, drag and drop to move posts between days, a post drawer with one caption tab per market language from the brand kit, hashtags, format, best time, visual direction, a compact motion brief block for every short video, story or animated post, Approve and Regenerate.
Pillar balance meter in the left rail that warns when a pillar drifts more than 10 points from its target.
Exports: XLSX (with a motion briefs tab, one row per beat), CSV, an ICS calendar file and a PDF month view.
```

**Check:** Generate October for Portugal and Brazil: moments appear, no promo lands on a sensitive date, exports open cleanly.

## CC13 Campaign Strategy tool

_Stitch screen: strategy builder. Spec: docs/apps/campaign-strategy.md._

```
Build Campaign Strategy with prompts/skills/campaign-strategy-builder as the engine and the nine section architecture.
Outline rail with section status, a paper document canvas that streams each section, and human checkpoints at The insight (three options, user chooses) and Creative territories (three territories, user chooses or merges).
Evidence panel that shows which facts came from the brief or uploaded research, each with a source chip.
Deep mode switches to the deeper model for board papers.
Every moving hero execution gets a motion brief after the sign off, using the shared MotionBrief schema.
Exports: DOCX with proper headings and the motion briefs as an appendix, PDF, and a deck outline that can be sent straight into Deck Designer as a new deck.
```

**Check:** Build a full strategy, change the chosen insight, and confirm later sections regenerate to match it.

## CC14 Exports and share links



```
Unify exports in apps/api/src/exports:
Route book: render templates/route-book.html with the Key Visual output (it already builds its own route index) into a self contained HTML file.
PDF: render any output page with Playwright to A4 or 16:9 PDF with the HorizonLine at the top of each page.
DOCX via the docx library, PPTX via pptxgenjs, XLSX via exceljs, CSV and ICS natively.
Share links: read only public pages with an access setting (anyone with link, team only), optional expiry, and a draft watermark toggle. Log views in audit_log.
```

**Check:** Export every format once and open each file on a phone and a laptop.

## CC15 Billing: global provider abstraction

_Create products and prices in both dashboards first._

```
Add billing with two providers:
Stripe as the global default, plus a PaymentProvider interface so regional providers can be added per country (for example a mobile money or local wallet provider for African markets, a UPI capable provider for India, a boleto and Pix capable provider for Brazil). Choose provider by the workspace country and show prices in local currency from a daily exchange table with USD as the base.
Plans: Solo (one tool), Studio (five tools), Agency (five tools, five seats, shared brand kits). Monthly credits per plan from config. Extra credit packs as one off purchases.
Webhooks for both providers update subscriptions and entitlements idempotently. Grace period of three days on failed payment, then read only mode, never data loss.
Gate every tool route and every run on entitlements server side, not only in the UI.
Billing settings page from the Stitch screen with invoices and usage chart.
```

**Check:** Complete a test payment in the default provider and one regional provider's test mode, then cancel and confirm the workspace goes read only after the grace period.

## CC16 Marketing site, pricing and onboarding

_Stitch screens: landing, pricing, onboarding._

```
Build the public pages from the Stitch screens: landing, pricing with the auto detected currency menu and credit estimator, and the three step onboarding that creates the first brand kit.
Performance budget for the landing page on a mid range phone over 3G: largest contentful paint under 2.5 seconds, total JavaScript under 180 KB compressed, images in AVIF or WebP with responsive sizes. The launch film never loads with the page: the hero shows its poster frame, and the video and captions load only when "Watch the film" is pressed. Until CC19 delivers the film, the button is hidden.
Add meta tags, Open Graph images, a sitemap and a privacy page that states briefs and brand files are private and never used for training.
```

**Check:** Run Lighthouse in mobile mode: performance and accessibility both 90 or higher.

## CC17 Quality pass with a fresh reviewer

_Use the reviewer agent in .claude/agents/._

```
Run a full quality pass before launch:
1. Use the reviewer subagent to review the whole diff since the first commit against PLAN.md and CLAUDE.md, in a fresh context, and report gaps as a numbered list.
2. Run the code review on the current branch.
3. Use the ui critic subagent to compare every built screen with the Stitch screens and DESIGN.md and list mismatches.
4. Security: check every route for workspace isolation, rate limits on AI and upload endpoints, secret handling, webhook signature checks, and file type validation.
5. Accessibility: keyboard only walkthrough of the main journey, screen reader labels, focus order.
6. Fix everything marked high. List the rest in LAUNCH-NOTES.md.
```

**Check:** LAUNCH-NOTES.md exists and has no open high items.

## CC18 Deploy



```
Prepare production deployment:
Web on a static host with a CDN. API on a container host that supports long lived Server Sent Event connections and background workers, with the job queue on managed Redis. Neon production branch with daily backups. Object storage bucket with private access and signed URLs.
Set up environments (preview and production), environment variables from .env.example, error tracking, uptime checks on /health, and structured logs.
Write DEPLOY.md with the exact steps, and a rollback procedure.
```

**Check:** A preview deploy works end to end from brief to export, then promote to production.

## CC19 Launch film for Bungee Studio

_Run after CC18, once production works end to end. Needs the motion-studio skill loaded in Claude Code._

```
Use the motion-studio skill to make the Bungee Studio launch film inside this repo, so the film uses the real app.

Film: 20 seconds, 16:9 first, then 1:1 and 9:16 from the same timeline. Code drawn route: build a film page under film/ that renders the app's real React components and DESIGN.md tokens. No screenshots of imagined screens, no redrawn UI.
Brand: the Bungee logo from brand/ (transparent PNG, never recoloured or stretched), the app tokens for everything else.
Story on a 120 BPM grid, one container that never cuts:
1. Hook, 0 to 2 s: "From brief to board ready." in giant serif type.
2. A brief is pasted into the real intake screen; the read back fills and tags its assumptions.
3. The hero journey: an insight is chosen, eight key visual routes fan out, the winning route becomes a retail family and a month of posts, the deck storyboard locks its type.
4. One proof line taken from the real product. Nothing invented.
5. Lockup: Bungee logo, "Bungee Studio" and the launch URL, logo landing on a downbeat.
Sound: an original 120 BPM score and UI sound effects synthesized in code, a click on every cursor press, a thump on the logo. Mix to about -14 LUFS with true peak at or below -1.5 dBFS.
Gates: show me the shot list on the beat grid before any animation code. Then contact sheets, an animatic, at least three critique rounds until every axis scores 8 out of 10, then the final renders, the poster frame and a share caption.
Also export a 6 second muted loop of the hero journey for the landing page, and wire the landing page "Watch the film" button to the 16:9 film with a captions file.
```

**Check:** The film plays from the landing page, every frame shows real app UI, the mix measures about -14 LUFS, and you have listened to it with headphones before posting.


# Iteration prompts

## Stitch: refine one detail

```
Keep this screen's layout, content and colours exactly as they are. Only change: [the one detail, for example make the route numbers larger, 72px Instrument Serif in Clay]. Do not regenerate other elements.
```

## Stitch: add a state

```
Using the same screen and design system, create the [empty / loading / error] state of this screen. Loading uses skeleton blocks and the horizon line as a progress bar. Empty uses a warm illustration free message with one clear action. Error explains what happened in one sentence and offers Retry.
```

## Stitch: mobile version

```
Create the 390px mobile version of this screen. Keep the design system. Stack columns vertically in reading order, make every tap target at least 44px, move secondary panels into a bottom sheet.
```

## Claude Code: fix a bug

```
In [component or file], [describe the problem and how to reproduce it]. Keep all existing styles, animations and behaviour. Only fix this issue. Add a test that fails before the fix and passes after.
```

## Claude Code: match Stitch

```
Use the Stitch MCP to open the screen [name]. Compare it with [route or component]. List every mismatch in spacing, type, colour, radius and states, then fix them using tokens from DESIGN.md only.
```

## Claude Code: add a page

```
Build the [page name] page at /[route]. Extend the existing design system exactly. Match the Stitch screen [name]. Include loading, empty and error states. Plan first, then build.
```

## Claude Code: start clean

```
Knowing everything you know now, scrap this implementation of [feature] and build the simplest elegant version that meets docs/apps/[tool].md. Plan first.
```
