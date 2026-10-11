# Bungee Studio starter pack

Everything Claude Code needs to build Bungee Studio: the specs, the design starter, the five engines, the moments data and the route book template.

## Step by step

### 1. Open the accounts and keys
- A Claude plan that includes Claude Code, for building.
- An Anthropic API key with billing on, for the app's text generation.
- A Google AI Studio key with billing on. Image generation has no free quota.
- Postgres on Neon, Redis, and an S3 compatible storage bucket.
- Stripe in test mode first; add a regional payment provider later if your market needs one.
- A GitHub repo and a domain for the product.

### 2. Set up your machine
- Install Node 20, pnpm, git and Claude Code.
- Unzip the starter pack into an empty folder, run git init and make the first commit.
- Copy .env.example to .env once Claude Code creates it, and add your keys. Never commit .env.

### 3. Design every screen in Google Stitch
- Create one Stitch project called Bungee Studio. Keeping every screen in one project keeps the design system consistent.
- Paste the Design System prompt first. Then paste S1 to S17, one prompt per screen, in order.
- Refine with the Stitch iteration prompts below. Change one thing at a time.
- Approve a screen only when it passes the checks under each prompt.

### 4. Hand the design to Claude Code
- Export DESIGN.md from Stitch and replace the starter DESIGN.md in the repo root. Commit it.
- Connect the Stitch MCP server to Claude Code using the current command on Stitch's MCP setup page, then run /mcp in Claude Code to confirm it is connected.
- Test it: ask Claude Code to list your Stitch screens. If it can, the bridge works.

### 5. Build with the Claude Code prompts
- Run CC1 in plan mode. Answer its open questions and approve PLAN.md.
- Run CC2 to CC19 in order, one prompt per session. Use /clear between prompts to keep context clean.
- After each prompt, run the check listed under it before moving on. Commit after every green check.
- For any big feature, start in plan mode again. Before calling a feature done, ask the reviewer agent to check the diff.

### 6. Beta, then launch
- Invite ten trusted users. Give each a real brief and watch where they stall.
- Fix the top five issues, switch payments to live mode, deploy with CC18, then make the launch film with CC19.
- Soft launch in January with the 2027 calendar as the hook.

## What is in this pack
- CLAUDE.md: the rules Claude Code follows in every session
- DESIGN.md: starter design system, replace with your Stitch export
- docs/PRD.md, docs/USER-JOURNEYS.md, docs/RESEARCH.md, docs/BUILD-PLAN.md
- docs/apps/: one spec per tool with stages, schemas and exports
- prompts/skills/: the five engines, loaded as system prompts
- data/moments-2027.json: 160 moments (88 global plus the East Africa pack) for the Content Calendar
- templates/route-book.html: the Key Visual export template, with the motion brief panel
- brand/: the Bungee logo (transparent PNG, trimmed PNG, white background PNG)
- .claude/agents/: reviewer and ui critic
- stitch/STITCH-PROMPTS.md and claude-code/BUILD-PROMPTS.md
