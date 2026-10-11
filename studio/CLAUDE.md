# Bungee Studio

Creative production suite for agencies and brand teams anywhere in the world. Five tools in one shell: Key Visual, Retail Theatre, Deck Designer, Content Calendar, Campaign Strategy. One brief can feed all five.

## Read first
- docs/PRD.md for what we are building and why
- docs/USER-JOURNEYS.md for the flow every tool follows
- docs/apps/<tool>.md for each tool's stages, schemas and screens
- DESIGN.md for every visual decision (exported from Google Stitch, it wins over everything else)
- PLAN.md for the agreed plan and milestones (created in the first session)

## Stack
- apps/web: React 18, Vite, TypeScript strict, Tailwind, Motion (import from "motion/react"), React Router, TanStack Query
- apps/api: Node 20, Express, TypeScript strict, Zod, Drizzle ORM, Neon Postgres, pino
- packages/shared: Zod schemas and types used by both
- AI text: Claude API. Default model claude-sonnet-5, Deep mode claude-opus-5. Model IDs live only in apps/api/src/config/models.ts
- AI images: Gemini API. Default gemini-3.1-flash-image-preview, Pro toggle gemini-3-pro-image-preview
- Billing: Stripe by default behind a PaymentProvider interface; regional providers plug in per country; prices shown in local currency from a daily exchange table with USD as base
- Storage: S3 compatible object storage with signed URLs
- Jobs: background queue on Redis for long AI runs

## Commands
- pnpm dev (web and api together)
- pnpm test, pnpm typecheck, pnpm lint
- pnpm db:generate, pnpm db:migrate

## Environment variables
ANTHROPIC_API_KEY, GEMINI_API_KEY, DATABASE_URL, REDIS_URL, STORAGE_ENDPOINT, STORAGE_BUCKET, STORAGE_KEY, STORAGE_SECRET, AUTH_SECRET, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, EMAIL_FROM, EMAIL_API_KEY, REGIONAL_PAYMENT_KEYS (json), EXCHANGE_RATE_API_KEY, STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET, APP_URL, STT_PROVIDER_KEY

## Rules that never bend
1. The engines are the skill files in prompts/skills/. Never paraphrase them into code. Load them as system prompts.
2. Every AI stage returns JSON validated by a Zod schema from packages/shared. No free text parsing.
3. No raw hex values or font names outside the theme files generated from DESIGN.md.
4. Interface copy and generated client copy contain no hyphens and no em dashes. No brand names in interface copy.
5. Market context is the default: every output is cast, placed and worded for the markets in the brief; market modules in prompts/skills/*/references/markets plug in per market; mobile first and low bandwidth friendly everywhere.
6. Workspace isolation is checked server side on every query. Entitlements and credits are checked server side on every run.
7. Every generate button shows its credit cost before the click.
8. Accessibility: keyboard reachable, visible focus, 4.5:1 contrast, reduced motion respected.

## How we work
- Start every feature in plan mode. Write or update the plan before code.
- Small commits with clear messages. One feature per branch.
- Before calling a feature done, have the reviewer agent check the diff against PLAN.md in a fresh context.
- If a Stitch screen and the spec disagree, ask me.
