# Key Visual Builder: monthly retest, 2 November 2026

Skill tested: `products/skills/key-visual-builder/skill/` as on branch `tests/key-visual-2026-11-02` before any change (SKILL.md, the six reference files, the East Africa module, the HTML template). Two new invented briefs, each run once exactly as SKILL.md instructs, as if sent in one message. Markets and categories are new: no earlier test used Melbourne, Tanzania, sun care or breakfast flour.

| Run | Files | Routes | Prompts | Motion briefs | Radio |
|---|---|---|---|---|---|
| Brief A, Halfshade Daily SPF 50+ face fluid, Melbourne | `brief-a.md`, `brief-a.html` | 6 (2 safe, 3 strong, 1 wild) | 27: 6 masters, 3 variants, 18 reprompts | 3 (fire routes) | none in the spine |
| Brief B, Mawio instant porridge flour, Dar es Salaam and Mombasa | `brief-b.md`, `brief-b.html` | 6 (2 safe, 3 strong, 1 wild) | 21: 6 masters, 3 market variants, 12 reprompts | 0 (no moving channel) | 12 scripts, one per route per market |
| Reruns of the failing parts, after the fixes | `brief-a-rerun.md`, `brief-a-rerun.html`, `brief-b-rerun.md`, `brief-b-rerun.html` | as above | as above | as above | as above |

How the checks were made: the same 44 checks as the October test. Rule checks were scripted over every prompt, the Markdown from the title down (inline code and file paths excluded) and all visible HTML text: dashes, banned names, negation words, stacked casting, ratio in words, percent text zone, palette lock, every colour word tied to a hex, craft tags, month and city, pack treatment, headline and subline word counts, billboard word caps, radio words per 15 s, and motion text holds against the readability law. The HTML was opened headless in Chromium with Python Playwright at 390 px and 1280 px, in light and dark. Pass means the output meets the promise because the skill told it how; where the run had to improvise, the evidence says so and points to a fix.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | 6 to 8 distinct routes | Pass | 6 routes on 6 archetypes | Pass | 6 routes on 5 archetypes and 6 different laws |
| R2 | Works for any market | Pass | Melbourne built from research; 0 East Africa terms anywhere in A | Pass | Dar es Salaam and Mombasa placed separately (Sinza, Mbagala, Tegeta; Kisauni, Likoni, Changamwe) |
| R3 | A copy ready image prompt per route | Pass | 6 masters, 297 to 442 words, pasteable as is | Pass | 6 masters, 369 to 436 words |
| R4 | A full copy suite | Pass | 3 headlines, subline, paired endline, proof, two CTAs, local line per route | Pass | Same set in Swahili and English, local line per market, radio per market |
| R5 | A channel adaptation kit | Pass | 9 formats per route, each called | Pass | 11 formats per route, but two were invented by the run (see S21) |
| R6 | A designer build sheet | Pass | 9 items per route; the legal line item was added by the run (fix 3) | Pass | 9 items per route with price plate and billboard copy |
| R7 | Motion brief when the campaign moves | Pass | 3 bumper briefs on the beat grid for the fire routes | Pass | Correctly not triggered |
| R8 | Interactive route book with copy buttons | Pass | 85 copy buttons, index and numbering build themselves | Pass | 97 copy buttons |
| R9 | With a market module, every route is cast, placed and worded for the market | Pass | No module; the researched layer drives every prompt and line | Pass | Tanzania leads in Swahili from the module. The module's Kenya rule leads in English, which the run followed on the coast with Swahili at equal size; an interpretation, fixed (fix 5) |
| R10 | Builds casting, places, language, channels and cultural dates from the market | Pass | December light and UV, tram supersides, brolly and a grey one | Pass | Swahili time, bajaji, daladala, the Likoni ferry, January back to school, Ramadan 2027 as a pointer |
| R11 | Builds prices from the market | Pass | Price row says no price shows; correct for the brief | Pass | TSh X,XXX and KSh XXX marked placeholders, one currency per execution, said once in every radio script |
| R12 | Prompts tuned for leading models, adapt to others | Pass | Tools named generically; composites flagged for the refusal ladder fallback | Pass | Same; Cup of Dawn offered as a real telephoto shoot |

### From SKILL.md (quality check, standing rules and step rules)

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market confirmed, module loaded or researched first | Pass | No Australia module; light, outdoor formats and register researched before any prompt | Pass | East Africa module loaded; Languages by country sets the order |
| S2 | KV spine shown back before prompts | Pass | Section 2 | Pass | Section 2 |
| S3 | At most three questions, only on axes that change the work | Pass | Claims, legal wording, a UV figure, each with an assumption | Pass | Nutrition claims, price, coast language order |
| S4 | All five routing axes resolved | Pass | Routing table plus one held register | Pass | Same |
| S5 | Reference law table only if references | Pass | None supplied, correctly omitted | Pass | Same |
| S6 | Spread: two safe, three strong, one or more wild | Pass | 2, 3, 1 | Pass | 2, 3, 1 |
| S7 | No two routes in one sentence | Pass | 6 laws | Pass | 6 laws |
| S8 | Every route on rung three or four | Pass | 4 on rung four | Pass | 4 on rung four |
| S9 | Eight part card anatomy in order | Pass | Every route | Pass | Every route |
| S10 | Name of two or three words, idea in one sentence | Pass | Scripted: names 2 to 3 words, one sentence each | Pass | Same |
| S11 | Hex on every colour, percent text zone, craft tags | Pass | Scripted over 27 prompts; 1 hex gap fixed during the run | Pass | Scripted over 21 prompts; 1 hex gap fixed during the run |
| S12 | Zero negative clauses, zero stacked casting | Pass | 0 negation words in 27 prompts | Pass | 0 in 21 |
| S13 | Pack label face clean wherever the pack appears | Pass | Blank panel in every tube; Drizzle Burn uses a clean plate | Pass | Blank panel on every pouch |
| S14 | Brief mandates on every KV | Pass | Pack, SPF 50+ and the legal line on all 6, the legal held in every text zone and every bumper | Pass | Pouch, both languages and the price plate on all 6 |
| S15 | Copy suite complete with local line | Pass | Melbourne register line, or carried by the headline where it already speaks it | Pass | Tanzania and Kenya coast lines on every route |
| S16 | Three endlines when the brief has none | Pass | Written once for the set; each route names its pair | Pass | Same, in both languages |
| S17 | No hyphens or em dashes in client copy | Pass | 0 in the deliverable | Pass | 0 |
| S18 | Claims flagged, never invented | Pass | Broad spectrum suspended; no UV figure; sunburn styled as make up | Pass | Nutrition suspended; Bell Full headline B flagged as a possible learning claim |
| S19 | Kit marks every format | Pass | Crop, Reprompt or Motion brief on every row | Pass | Crop, Reprompt, Designer build or Script on every row |
| S20 | Reprompts are full standalone prompts | Pass | 18 reprompts and 3 variants, none a change note | Pass | 12 reprompts and 3 variants |
| S21 | Kit formats come from the skill's own tables | Pass | Tram superside from public transport branding, 6 sheet and billboard from section 3 | Fail | Daladala and matatu backs have no row (public transport branding is a long side panel), so the run invented the ratio and call; painted shop walls only map to the bespoke wall wrap row, which says nothing about a sign writer (fix 2) |
| S22 | Build sheet per route, all items | Pass | Every route; legal line item invented by the run because Step 8 has none (fix 3) | Pass | Every route |
| S23 | Motion brief: beat grid, readability law, logo on a downbeat | Pass | Scripted: every text hold meets the law (the 9 word legal holds 3.5 to 4.0 s); logo on 3.1 in all three | Pass | Not triggered |
| S24 | Fire three, disruptive alternate, what is missing | Pass | Section 8 and the close | Pass | Same |
| S25 | Single interactive HTML from the template, readable | Fail | The template has no style for the gloss inside a copy line, so every gloss runs into its line ("Grey one today. Still counts.A grey one is"). Both October runs patched this in their own files, so it never surfaced (fix 1) | Fail | Same, on every bilingual line ("Dakika tano. Basi.Five minutes.") |
| S26 | Route book from the template works on a phone | Pass | 390 px wide at 390 px, light and dark; 0 page errors | Pass | Same |
| S27 | No readable text in images except type as terrain | Pass | No type route; clocks and beads carry no marks | Pass | Clock faces carry hands only |
| S28 | Kill list avoided | Pass | Checked per route | Pass | Checked; Cup of Dawn is a small sun held by the mug, not a sunset behind a silhouette; no child in frame |
| S29 | Casting by context | Pass | One figure, by street, weather and moment | Pass | One father, by district, hour and work shirt |
| S30 | Place, light and season named in every prompt | Pass | Scripted: a Melbourne district and December in all 27 | Pass | A named district and January in all 21 |
| S31 | Variant pairs where the effect is optional | Pass | Commuter, rooftop and hood down variants | Pass | A full other city variant for each fire route |
| S32 | Palette as hex, never left to the model | Pass | Proposed, labelled, real palette under What is missing | Pass | Same |

**Pass count, first run: Brief A 43 of 44. Brief B 42 of 44.**

A fails: S25. B fails: S21, S25.

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| No hyphens and no em or en dashes | Pass | Pass | Script over the Markdown and all visible HTML text, inline code and file paths excluded: 0 hyphens, 0 em dashes, 0 en dashes |
| No real brand, employer or client names | Pass | Pass | Script for about 120 names: sun care, flour, retail, transit operators, media owners, platforms, image models, payment, agencies, the employer and every client named in Stephen's memory: 0 hits. One local line used the Swahili word for coast, which is also a client name, and was rewritten during the run |
| Prompts are full standalone prompts | Pass | Pass | All 48 carry their own framing with the ratio in words, subject, place and month, light, palette lock with hex, pack treatment, percent text zone and craft tags; none says as above or leans on another |
| East Africa is a module, not the default, for Brief A | Pass | n/a | Module not loaded for A; script for Swahili, Sheng, Nairobi, Kenya, matatu, shilling, Tanzania, Uganda and similar: 0 hits |
| Copy lengths | Pass | Pass | Headlines 2 to 7 words, sublines under 12, billboards 7 words or fewer across both languages; two lines rewritten during the run (a 12 word Swahili subline, an 8 word English headline) |
| Radio at about 2.5 words a second | n/a | Pass | 26 to 31 spoken words per 15 s script; the line twice, the endline once, the price once |
| Template renders | Pass | Pass | Headless Chromium at 390 and 1280 px, light and dark: page width equals viewport, 0 elements past the edge, 0 script errors. The only console error was the web font request blocked by the sandbox proxy; with it stubbed, 0 console errors |

## 3. Verdicts, first run

**Brief A: Yes, once the template is fixed.** Six routes with a real spread. Under the Grey and Sheer Cover are ownable ideas that prove the proposition without a number, and Drizzle Burn is the route that makes the meeting memorable. The legal line is held in every frame and every bumper. The only thing stopping a creative director sending it unchanged is the route book itself: every gloss runs into its line.

**Brief B: No.** The work is strong (Dakika Tano, Cup of Dawn and Bell Full are good, local ideas, and Swahili time and the Likoni ferry are true details), but two things would come back. The route book runs every English line into its Swahili, which is most of the copy panel. And the vehicle backs and painted walls the brief names were improvised, with no ratio or craft guidance from the skill.

## 4. Fix list, applied

1. **`assets/kv-library-template.html`: the gloss inside a copy line has no style.** Added `.copy .val small{display:block;...}` so the English gloss or second language sits on its own line, and a `.flag` style plus a Flag slot in the copy panel, since Step 6 asks for suspended claims in the card.
2. **`references/adaptation-kit.md`, section 3: no vehicle back and no hand painted wall.** Added "Vehicle back (minibus, bus, tuk tuk)", about 2:1 round the rear window, a Crop of the billboard plate, and "Hand painted wall or shop front", a Designer build by a sign writer from a flat colour build.
3. **`SKILL.md`, Step 8, and the template build sheet: no item for a mandatory legal line.** Added "Legal line: the exact wording, position, minimum size, and the zone held for it in every prompt's text zone and every motion brief", and a Legal line row in the template.
4. **`references/copy-craft.md`, section 5: the billboard cap is silent on two mandated languages.** Added: the seven words cover both, the lead language carries the headline and the second language the endline.
5. **`references/markets/east-africa.md`, Languages by country: Kenya is written from Nairobi.** Added that on the coast Swahili is the everyday street language, that a coast brief may lead in Swahili at equal size with English, and that a coast writer checks every line.

README promises are all true as written; README unchanged.

## 5. Rerun of the failing parts

Both route books were rebuilt from the fixed template; Brief B's adaptation kit, billboard copy and language order were rebuilt from the fixed kit, copy craft and module; Brief A's legal line now comes from Step 8. Prompts and copy are unchanged.

| # | Check | A rerun | B rerun | Evidence |
|---|---|---|---|---|
| S21 | Kit formats come from the skill's own tables | Pass | Pass (was Fail) | Vehicle back called Crop of the billboard plate and hand painted shop wall called Designer build, both from adaptation kit section 3 |
| S22 | Build sheet, all items | Pass | Pass | Legal line now a Step 8 item, not a run invention |
| S25 | Single interactive HTML from the template, readable | Pass (was Fail) | Pass (was Fail) | Gloss renders on its own line under every headline and local line; flag styled |
| S26 | Phone | Pass | Pass | 390 px and 1280 px, light and dark: no horizontal scroll, 0 page errors |
| R9 | Market wording | Pass | Pass | Mombasa executions lead in Swahili at equal size with English, now from the module; still raised with the client as question 3 |

Rule checks rerun on the rerun files: 0 dashes, 0 banned names, 0 prompt issues, 0 copy length issues.

**Pass count after the fixes: Brief A 44 of 44. Brief B 44 of 44.**

**Verdict after the fixes: both Yes.** A creative director would send either route book to the client as the first route presentation. Everything left under What is missing is a client decision (real palette, prices, cleared claims, legal wording, media specs), not a gap in the work.

Build: `python3 scripts/build_products.py` ran clean (exit 0) and rebuilt `dist/key-visual-builder.zip` with the fixed skill.

## 6. Notes for the next pass (not defects)

* The Budget row still speaks only to low budgets; A read mid as six routes with the full kit. A line for mid and high budgets would remove the guess.
* Every Swahili line in B is marked for a native check, one writer in Dar and one in Mombasa. That is right, but it means B cannot ship to artwork without them.
* The template has no slot for a test record header or the market layer table, so those live only in the Markdown. Fine for buyers; noted for consistency.
