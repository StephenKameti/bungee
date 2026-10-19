# Status log

Newest first. One entry per check in.

## Mon 19 Oct 2026

- Nothing new from you in the roadmap, the Decisions table or the repo since Thursday. PLAN.md is still waiting, so the Studio build (CC2 to CC4) stays on hold. Week 2 and week 3 stay In progress; no other roadmap changes.
- This is week 2 (19 to 25 Oct). All my week 2 and week 3 sell actions were already done, so I prepared launch week, which is yours to run.
- Launch kit: `ops/launch/`. Launch day hour by hour in Nairobi time, one skill film a day from Wed 4 Nov, the 50 personal messages in four versions (planner, creative director, agency owner, friend), one follow up, ready replies, and a list template for your 50 names.
- Two proposals for you in `ops/launch/LAUNCH-PLAN.md`: a launch price for 3 to 9 Nov (one pack USD 24, all six USD 99, Everything USD 119) and a Black Friday offer (Everything USD 99, 27 to 30 Nov, the same day the Moments early bird ends). Post copy is written for both.
- Monday moment posts: 25 drafts in `ops/launch/monday-posts/`, 9 Nov 2026 to 26 Apr 2027. Each one covers the moments eight weeks ahead, so readers still have time to brief. Trademarked event names swapped for plain words. Built by `ops/launch/monday_posts.py`, which fails if a trademarked name or a dash slips in. Posts that lead with an East Africa hook wait on the native speaker check.
- Checks: site build passes (same four blockers: policy blanks, checkout links, email list link), posts check passes.
- Next: recheck the KES rate on Thursday (week before launch), CC2 the day PLAN.md is approved, checkout links and deploy once the store and domain exist.

## Thu 15 Oct 2026

- Nothing new from you in the roadmap or the Decisions table since Monday. Week 1 and week 2 stay In progress until your accounts, Stitch screens and approvals land. Week 3 set to In progress: I started its Me actions.
- Website built: `site/`. One landing page (hero with the cord, the six packs, a Moments 2027 section with a chart of all 160 moments by month, bundles, install steps, markets, FAQ, email signup) plus refund, terms and privacy pages generated from `ops/store/POLICIES.md`. Fonts self hosted, works on phone and desktop, no third party brands or event names. `python3 site/build.py` checks the copy and lists what blocks going live: policy blanks, nine checkout links, the email list link. See `site/README.md`.
- Brand kit in one folder: `brand/kit/` (logo guide, colours, type, font files with licences, app icon). Roadmap item ticked.
- Moments 2027 calendar test: two real bugs found and fixed. Exported picks landed a day early for anyone east of London, Nairobi included. And every moment showed as busy, which would have blocked buyers' calendars all year. Both fixed and proven in three time zones; files now meet the calendar standard. Report: `ops/tests/moments-2027/2026-10-15/CALENDAR-TEST.md`. Zips rebuilt.
- Native speaker check list ready: `ops/tests/moments-2027/2026-10-15/NATIVE-SPEAKER-CHECK.md`. 29 Swahili lines, 3 Kinyarwanda, 7 others. Two findings: Swahili hooks are tagged to all five East African markets (should be Kenya and Tanzania), and two Sheng hooks only work in Kenya. Waiting on a Swahili checker before changing data.
- Blocked on you: CC2 to CC4 (week 3 Studio) wait for your PLAN.md approval. Going live waits on the store, domain and policies.
- Next: CC2 scaffold as soon as PLAN.md is approved; apply native speaker answers; wire checkout links once products exist; deploy the site once the domain is live.

## Mon 12 Oct 2026

- Week 1: my actions were already done, so I started week 2's. Week 1 stays In progress until your accounts and Stitch screens are done. Week 2 set to In progress in the roadmap.
- Packs: the other four tested on invented briefs, one outside Africa and one in East Africa each. All failed somewhere on the first run; fixes applied, reruns now pass in full. Audience and Persona 31 of 31 (Seoul, Kigali). Designed Deck 33 of 33 (Seoul, Dar es Salaam). Retail Display Theatre 41 of 41 (Warsaw, Dar es Salaam). Content Calendar 40 of 40 (Seoul, Dar es Salaam). Results in `ops/tests/`. All six packs are now tested.
- Main fixes: dashes stripped from the packs and their output, one message briefs proceed on stated assumptions, no invented prices or facts, full standalone prompts in every example, price rules, more Tanzania, Uganda and Rwanda detail in the East Africa modules, README promises matched to what each skill does.
- Pack READMEs said skills need a paid plan. Claude's support page says skills work on Free too, with code execution on. All six READMEs corrected.
- Moments 2027: all 25 expected and confirm dates rechecked against sources; 14 updated (five moved, eight now fixed, two wrong fixed dates corrected). Report in `ops/tests/moments-2027/2026-10-12/DATE-CHECK.md`. Moon sighted dates stay Expected.
- Store copy: pages for all six packs, Moments 2027 and both bundles, ready to paste, with KES prices for Paystack, in `ops/store/`. Draft refund policy, terms and privacy notice in `ops/store/POLICIES.md` for your approval. Event names kept out of the store copy.
- Zips rebuilt with `scripts/build_products.py`.
- Next: native speaker check list for the almanac hooks, calendar import test, landing page build (week 3), CC2 scaffold once PLAN.md is approved.

## Sun 11 Oct 2026, evening

- Decisions recorded: both tracks together (products 3 Nov, Studio 19 Jan), Lemon Squeezy, proposed prices, Moments 2027 keeps real event names. Roadmap doc, tracker and timeline updated.
- Studio: CC1 drafted `studio/PLAN.md` (architecture, database, AI pipeline, milestones, eight open questions with recommended answers). Build plan moved to start 12 Oct.
- Packs: Key Visual Builder and Campaign Strategy Builder tested on invented briefs in Lisbon, Kenya and Uganda, Mexico City, Nairobi and Dar es Salaam. Fixes applied; reruns now pass (Key Visual 44 of 44, Strategy 66 of 66). Results in `ops/tests/`.
- East Africa module corrected in all six packs: Luganda leads in Kampala, Swahili leads business in Tanzania, kanga and kitenge as everyday wear.
- Next: test the other four packs, store copy for every product, recheck the almanac's expected dates.

## Sun 11 Oct 2026

- Roadmap published as a doc with a weekly tracker, decisions, budget and metrics.
- Reversed logo made: white letters, lime tick, transparent PNG, checked on the Studio dark backgrounds and on slate. In `brand/`.
- Repo set up with every product, the film source and the Studio starter pack. `scripts/build_products.py` rebuilds the seven sellable zips.
- Check ins set for Monday and Thursday mornings.
- Next: test Key Visual Builder and Campaign Strategy Builder on invented briefs; swap the trademarked names in Moments 2027 on a branch; draft store copy.
