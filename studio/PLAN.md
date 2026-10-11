# Bungee Studio plan

Draft from CC1, 11 Oct 2026. Status: waiting for Stephen's approval (target Sun 25 Oct). Nothing is coded until the open questions in section 5 are answered.

Studio launches **Tue 19 Jan 2027**. Five tools in one shell (Key Visual, Retail Theatre, Deck Designer, Content Calendar, Campaign Strategy), one brief feeding all five, every tool following Brief, Read back, Explore, Refine, Deliver.

## 1. Architecture

```
Browser: apps/web (React 18, Vite, TypeScript strict, Tailwind, Motion, React Router, TanStack Query)
   |  JSON over /api/*   +   Server Sent Events for run progress
   v
API: apps/api (Node 20, Express, Zod, Drizzle, pino)
   |-- auth: sessions, email magic link, Google sign in
   |-- middleware, in this order: session -> workspace scope -> entitlements -> credits
   |-- routes: workspaces, brand kits, assets, projects, briefs, runs, outputs, images, exports, share links, billing webhooks
   |-- ai/: skill loader -> stage runner -> Claude (tool use, JSON schema) -> Zod validate -> one repair -> copy guards
   |-- queue producer (BullMQ on Redis)
   v
Worker: apps/api/src/worker.ts (same codebase, separate process)
   |-- runs stages as jobs, publishes events to Redis pub/sub, the API relays them as SSE
   |-- reconnect: the client resumes by run id from the last event id
Data: Neon Postgres (Drizzle migrations) · Redis (queue, pub/sub, rate limits) · S3 compatible storage (uploads, images, exports, signed URLs)
Outside: Claude API (text) · Gemini API (images) · Stripe and Paystack (billing) · email provider (magic links)
Shared: packages/shared holds every Zod schema and type used by web and api
```

Folder layout inside `studio/`: `apps/web`, `apps/api`, `packages/shared`, `prompts/skills` (the engines, loaded verbatim), `data/moments-2027.json`, `templates/route-book.html`, `docs/`, `DESIGN.md`, `PLAN.md`.

## 2. Database

| Table | Key columns |
| --- | --- |
| users | id, email, name, avatar_url, created_at |
| workspaces | id, name, country, currency, language, deep_mode, ask_before_each_step |
| memberships | user_id, workspace_id, role (owner, editor, viewer) |
| brand_kits | id, workspace_id, name, colours json, type json, voice, logo_asset_id, markets text[] |
| assets | id, workspace_id, kind, mime, size, checksum, storage_key, uploaded_by |
| projects | id, workspace_id, name, brand_kit_id, created_by, archived_at |
| briefs | id, project_id, raw_text, source_asset_ids, spine json, assumptions json, status |
| runs | id, project_id, brief_id, tool, stage, model, tokens_in, tokens_out, cost_usd, duration_ms, status, error, job_id |
| outputs | id, run_id, project_id, tool, schema_version, payload json, version, parent_output_id, shortlisted |
| images | id, output_id, prompt, model, aspect, storage_key, credits_used, status |
| subscriptions | id, workspace_id, provider, plan, status, current_period_end, grace_until |
| entitlements | workspace_id, tool, seats, from_plan |
| credit_ledger | id, workspace_id, delta, reason, run_id, image_id, created_at |
| share_links | id, project_id, token, expires_at, scope json |
| audit_log | id, workspace_id, user_id, action, target, meta json, created_at |

Every query goes through a repository layer that takes `workspaceId` as its first argument. One test per repository proves a user in workspace A cannot read workspace B.

## 3. The AI run pipeline

1. **Intake.** Paste, upload (PDF, DOCX, PPTX, images, chat screenshots) or speak. Text is extracted server side; images go through Claude vision. Output: raw brief text plus what is missing.
2. **Read back.** One stage returns `BriefSpine` (objective, audience, markets, single message, mandatories, channels, timing, budget, tone, assumptions tagged as assumed). The user edits and answers at most one question. The plan for the chosen tools is shown with timing.
3. **Tool stages.** Each tool is an ordered list of stages from `docs/apps/<tool>.md`. A stage has: input builder, Zod output schema, model, max tokens, checkpoint flag.
4. **Call.** System prompt = the tool's `SKILL.md` plus its references, loaded verbatim at startup and sent with prompt caching. User message = the stage inputs as JSON. The model must answer through one tool whose input schema is generated from the Zod schema.
5. **Validate.** Zod parse. On failure, one repair request with the validation errors; on a second failure the stage fails with a plain message and nothing half valid is saved.
6. **Guards.** Every client facing copy field: hyphens and em dashes replaced; any brand that is not in the workspace's brand kit flagged for review before export. Every guard hit is logged.
7. **Save and stream.** Output saved as a new version (never overwritten). Events stream to the browser: stage started, partial text for readable fields, stage complete, error. PlanList ticks; StreamingText shows words as they arrive.
8. **Checkpoints.** With "Ask me before each step" on, the run pauses after each stage. Insight, territory, route shortlist and design language are always checkpoints.
9. **Cost.** Tokens, cost and duration recorded per run. Text runs are free within fair use; image previews and Deep mode spend credits, shown on the button before the click, spent before the call and refunded on failure.

Models live only in `apps/api/src/config/models.ts`.

## 4. Milestones

| # | Week ending | Prompts | Acceptance checks you can do in the browser |
| --- | --- | --- | --- |
| M0 | Sun 25 Oct | CC1 | You approve this plan and answer section 5 |
| M1 | Sun 1 Nov | CC2, CC3, CC4 | `pnpm dev` runs both apps; /dev/ui matches Stitch for fonts, colours and radii; the shell has the sidebar, tool switcher, Cmd K palette and empty states |
| M2 | Sun 8 Nov | CC5 | Sign in by magic link and Google; create a second workspace and confirm the first one's brief is invisible |
| M3 | Sun 15 Nov | CC6, CC7 | Paste five real style briefs; each reads back correctly; close the tab mid run, reopen, the run resumes |
| M4 | Sun 22 Nov | CC8, CC9 | One brief gives 6 to 8 routes (two Safe, two Strong, one Wild at least); two previews cost two credits; a forced failure refunds |
| M5 | Sun 29 Nov | CC10, CC12 | Retail Theatre gives a pharmacy family with one device per unit; Content Calendar gives a month with moments, no promo on a sensitive date |
| M6 | Sun 6 Dec | CC11 | A ten slide deck keeps one type spec on every slide and exports to PPTX and PDF |
| M7 | Sun 13 Dec | CC13, CC14 | One brief runs through all five tools in one project and opens as one share link |
| M8 | Sun 20 Dec | CC15, CC16 | Test payments pass in Stripe and Paystack; pricing shows local currency; onboarding creates the first brand kit |
| Pause | 21 Dec to 3 Jan | none | none |
| M9 | Sun 10 Jan | CC17 | Reviewer verdict Ship after fixes or better; ten beta users export real work |
| M10 | Sun 17 Jan | CC18, CC19 | Preview deploy works brief to export; production promoted; launch film approved |
| Launch | Tue 19 Jan | none | Studio live, payments live |

## 5. Open questions, each with my recommended answer

1. **Text models.** The spec names `claude-sonnet-5` and `claude-opus-5`. The current API names are `claude-sonnet-5-5` and `claude-opus-5-5`. Recommended: use those, Sonnet by default and Opus for Deep mode, and recheck the list at CC6.
2. **Image models.** The spec names two Gemini image preview models. Recommended: confirm the current names and prices in Google's docs at CC9 and keep them in config only.
3. **Hosting.** Recommended: web on Vercel (you already use it for Pitch Engine), API and worker on a container host that keeps SSE connections open (Railway or Fly.io), Redis on Upstash, storage on Cloudflare R2, Postgres on Neon, email on Resend, errors on Sentry. All have free or low tiers for the build.
4. **Auth.** Recommended: Better Auth with its Drizzle adapter for magic links and Google sign in, sessions in Postgres.
5. **Billing.** Recommended: Stripe as the default and Paystack as the first regional provider, reusing the accounts you run for Pitch Engine. Lemon Squeezy stays for the downloads store only.
6. **Plans.** Recommended starting point, decided before CC15: Solo USD 19 a month (one tool, 100 preview credits), Studio USD 49 (five tools, 400 credits), Agency USD 149 (five tools, five seats, shared brand kits, 1,500 credits), extra packs of 100 credits for USD 10.
7. **Stitch to code.** CC3 reads the design through the Stitch MCP. My sessions run in the cloud, so the MCP may not reach your Stitch account. Recommended: when a screen is approved, export its PNG and the DESIGN.md into `studio/design/`, and I build from those files.
8. **Markets.** `docs/RESEARCH.md` still says images show "the five markets". Recommended: global by default, market modules per brief, and that line rewritten. Moments data keeps the real event names in the planner view, but generated post copy never uses trademarked event names.
