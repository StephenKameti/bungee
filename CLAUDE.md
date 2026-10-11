# Bungee

Stephen Kameti's independent product line: six Claude skill packs, the Moments 2027 almanac, the launch films, the Bungee website and Bungee Studio, a web app. This repo holds all of it. The plan lives in the roadmap doc below.

## Where things are

| Path | What |
| --- | --- |
| `brand/` | Logos: slate on light, reversed white with the lime tick for dark, the tick on its own |
| `products/skills/<slug>/` | `skill/` (the folder buyers upload to Claude), `README.md`, `LICENSE.txt` |
| `products/moments-2027/` | `build.py` and the data; `python3 build.py` writes the page, calendar file, CSV and JSON into `out/` |
| `films/` | Source for the eight launch films. Renders are kept out of git; see `films/README.md` to rebuild |
| `studio/` | Bungee Studio starter pack: PRD, research, user journeys, Stitch prompts S1 to S17, Claude Code prompts CC1 to CC19, build plan. `studio/build-kit/` makes the guide page |
| `site/` | The Bungee website (built in week 3) |
| `ops/` | `STATUS.md` (a log of every check in), `NEEDS-YOU.md` (open asks for Stephen), store copy, launch messages, test results |
| `scripts/build_products.py` | Builds the sellable zips into `dist/` (not committed) |

## The roadmap

Bungee Launch Roadmap, a Claude Docs doc: https://claude.ai/code/artifact/7429fab5-408f-432f-bcec-e18d1f8c2c06

For the docs tools: doc id `7429fab5-408f-432f-bcec-e18d1f8c2c06`, tab `101b4d9f-2ac3`, body node `c4fe92e9-566e`, Status enum `782a8c80-07fd` (Not started, In progress, Done, Slipped). The Weekly tracker table (id `mx6y0ad1sw6.18527`) has a Sell track and a Studio track per week, each action marked Me or You, and a Status dropdown per week. Read the outline first, then only the tables you need.

Key dates: store live Sun 1 Nov 2026. Products launch Tue 3 Nov 2026. Black Friday offer 27 to 30 Nov. Holiday pause 21 Dec to 3 Jan. Studio beta 4 to 10 Jan 2027. Studio launch Tue 19 Jan 2027. 100 paying Studio workspaces by Mon 19 Apr 2027.

## Standing rules from Stephen

1. Never name Stephen's employer or any client anywhere in the products, the site or Studio.
2. No brand mentions in any product: no client brands, no third party brands. One exception Stephen chose on 11 Oct 2026: Moments 2027 keeps the real event names. The films, store pages and posts still leave trademarked event names out.
3. Every product works for any market in the world. East Africa is a regional module, never the default.
4. No hyphens or em dashes in document, deck, page or store copy.
5. Anything designed needs strong design flair.
6. Image prompts are always full standalone prompts, never a shared preamble plus fragments.
7. Copy is short, punchy and emotive.

## What always needs Stephen

- Payments, purchases, identity checks, bank or payout details, accepting terms of service.
- Publishing or sending anything as him: posts, emails, the store going live, price changes on a live store.
- API keys. He adds them to dashboards himself. Never ask for a key in chat and never commit one.
- Real client material.
- Gmail is for drafts only. Never send.

## Decisions (answered 11 Oct 2026)

1. Order of work: both tracks together. Products launch 3 Nov, Studio launches 19 Jan.
2. Moments 2027 keeps the real event names.
3. Prices: one pack USD 29, all six USD 129, Moments 2027 USD 39 (USD 29 early bird to 30 Nov), Everything USD 149.
4. Store: Lemon Squeezy, with Paystack alongside for mobile money.
5. Reversed logo: made, waiting for Stephen's approval.
6. Visual Direction Library: stays inside the packs, revisit Feb 2027.
7. Name and tax checks: Stephen, by 30 Oct.

Check the Decisions table in the roadmap for anything newer before acting.

## Studio

Bungee Studio is built in `studio/` (pnpm workspace root, apps and packages live there). Run the prompts in `studio/claude-code/BUILD-PROMPTS.md` in order, one per session, and run the check under each before moving on. Stephen designs in Stitch and approves each milestone; ask him to check milestones in the browser. Keys live in the environment settings, never in the repo.

## The check in routine (Monday and Thursday)

1. Read `ops/NEEDS-YOU.md`, then the roadmap: the Weekly tracker and the Decisions table. Note anything Stephen changed or answered.
2. Find this week's row in the tracker and do every action that needs no access from him. When this week's Me actions are done, start next week's Me actions. Use a branch per task, commit with clear messages, merge to `main` when checks pass.
3. Update the roadmap: set this week's Status, tick finished items in the step by step sections. Never undo his edits.
4. Add a dated entry to `ops/STATUS.md`: what was done, where it is, what is next.
5. Rewrite `ops/NEEDS-YOU.md` as at most three items only Stephen can do, each with a link and a time estimate.
6. Send Stephen a short message: what changed and the NEEDS-YOU list.

## How to test a skill pack

Use an invented brief, never client work. Run each pack twice: once set in a market outside Africa, once in East Africa. Follow the pack's `SKILL.md` exactly and save the full output in `ops/tests/<slug>/<date>/`. Score it against the README's promises; the pass mark is that a creative director would send it to a client unchanged. List the fixes, apply them to `products/skills/<slug>/skill/`, then rebuild with `python3 scripts/build_products.py`.
