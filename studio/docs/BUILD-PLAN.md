# Build plan, Q4 2026 to January 2027

Runs alongside the product launch (3 Nov). Starts 12 October, pauses 21 December to 3 January, launches Tue 19 January 2027. Claude writes the code (CC1 to CC19); Stephen designs in Stitch, sets up accounts and keys, approves each milestone and runs the beta. Optional freelance QA tester in the beta week.

| Week | Dates | Tasks | Done when |
|---|---|---|---|
| 1 | 12 to 18 Oct | Stephen: Stitch design system, S1 to S6. Claude: CC1 drafts PLAN.md | Six screens approved, PLAN.md drafted |
| 2 | 19 to 25 Oct | Stephen: S7 to S17, export DESIGN.md and screen PNGs. Both: approve PLAN.md | PLAN.md approved |
| 3 | 26 Oct to 1 Nov | CC2 scaffold. CC3 design system. CC4 shell | /dev/ui matches Stitch |
| 4 | 2 to 8 Nov | Stephen: keys and database in the environment settings. CC5 auth and database, start CC6 | Sign in works, isolation test passes |
| 5 | 9 to 15 Nov | Finish CC6. CC7 brief intake. Test with five briefs | Five briefs read back correctly |
| 6 | 16 to 22 Nov | CC8 Key Visual. CC9 images and credits. Review | Routes and previews working |
| 7 | 23 to 29 Nov | CC10 Retail Theatre. CC12 Content Calendar. Moments import | Two tools working |
| 8 | 30 Nov to 6 Dec | CC11 Deck Designer. Type lock tests. PPTX export | Ten slide deck exports cleanly |
| 9 | 7 to 13 Dec | CC13 Campaign Strategy. CC14 exports. Hero journey test | One brief runs through all five tools |
| 10 | 14 to 20 Dec | CC15 billing. CC16 marketing site. Pricing in test mode | Test payments pass in both providers |
| Pause | 21 Dec to 3 Jan | None | None |
| 11 | 4 to 10 Jan | CC17 quality pass. Closed beta with ten users | Beta users export real work |
| 12 | 11 to 17 Jan | Fix beta issues. CC18 deploy. CC19 launch film | Production live, film approved |
| Launch | Tue 19 Jan | Studio live, payments live | First paying workspaces |

## Monthly running costs (estimates, check current pricing)
| Item | Build phase | At 100 paying workspaces |
|---|---|---|
| Claude API (text) | USD 50 to 150 | Track per workspace; target under 30 percent of revenue |
| Gemini images | Around USD 0.10 per 2K image | Covered by credits in each plan |
| Postgres | Free tier | About USD 19 |
| Container host and Redis | About USD 20 | USD 50 to 100 |
| Object storage | Under USD 5 | USD 10 to 20 |
| Email, error tracking, uptime | Free tiers | USD 30 to 60 |

## Launch metrics
Activation 40 percent first export in 20 minutes. Shortlist rate 60 percent of routes. Week 4 retention 50 percent. 100 paying workspaces in 90 days, by Mon 19 Apr 2027.
