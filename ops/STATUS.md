# Status log

Newest first. One entry per check in.

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
