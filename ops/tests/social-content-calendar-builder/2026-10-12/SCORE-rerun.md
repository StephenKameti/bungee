# Social Content Calendar Builder: rerun score, Briefs A and B, 12 October 2026

Skill tested: `products/skills/social-content-calendar-builder/skill/` after the SCORE.md fix list (all ten fixes applied to SKILL.md, `global-cultural-moments.md`, `markets/east-africa.md`, `markets/east-africa-calendar.md`, `markets/TEMPLATE.md` and README.md). Both briefs failed the first run, so both were run once more, exactly as the updated SKILL.md instructs, as if sent in one message.

| Run | Files | Posts | Captions | Prompts | Motion briefs |
|---|---|---|---|---|---|
| Brief A rerun, Milgyeol Bakehouse, Seoul, February 2027 | `brief-a-rerun.md`, `brief-a-rerun.html` | 12 | 12 in Korean plus 2 broadcasts | 12 | 5 |
| Brief B rerun, Ladha Njema, Dar es Salaam, March 2027 | `brief-b-rerun.md`, `brief-b-rerun.html` | 14 and 1 quiet day card | 14 in Swahili plus 3 trade broadcasts | 14 | 6 |

How the checks were made: the same 40 checks as SCORE.md. Rule checks were scripted over the Markdown from section 1 down: caption and gloss word counts, hashtag counts per platform, every prompt for the full feed look (all five hex values), a percent text zone, ratio in words, cross references and any label sentence without "blank", hyphens and dashes, and about 70 brand names. The HTML was opened headless at 390 px and 1280 px in light and dark with every tab clicked. Pass means the output meets the promise because the skill told it how, not because the run improvised.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | Complete monthly calendar for any brand in any market | Pass | 12 posts, four Monday to Sunday weeks | Pass | 14 posts, a quiet day card, four weeks with the tail joined to week 4 as Step 2 now says |
| R2 | Pillars | Pass | 25, 25, 33, 17 | Pass | 21, 29, 29, 21 |
| R3 | Platform specific posts | Pass | Four formats, each to its own rule | Pass | Same, plus the trade register |
| R4 | Captions in the market's languages | Pass | Korean | Pass | Swahili first |
| R5 | Motion brief for every short video post | Pass | 5 of 5 | Pass | 6 of 6 |
| R6 | Cultural moments that track moveable feasts and know when to go quiet | Pass | Lunar new year and Daeboreum now named in the global file's moveable dates; Samiljeol kept out of the sell | Pass | Ramadan 2027 and Eid come from the module's new Islamic calendar section; Good Friday is a quiet day card under Step 3, paid posts paused (was Fail) |
| R7 | Ships with the East Africa module; build your own from the template | Pass | Research path unchanged and working | Pass | Tanzania's dates, the Islamic calendar and a Tanzania hashtag set now in the module; no platform brand left in any tag (was Fail) |
| R8 | Builds prices and the rest from the market | Pass | Prices from the brief; everything missing is a placeholder | Pass | TSh [bei, thibitisha] on posts 7 and 10 under Step 1 input 8, listed in Open items (was Fail) |
| R9 | Image prompts tuned for the leading image models | Pass | 12 prompts, 144 to 228 words | Pass | Every bottle and pouch is a blank Chilli Red panel with no lettering; the film uses the real bottle (was Fail) |
| R10 | README copy is clean | Pass | Comma fixed; promise line now names moveable feasts and brief led prices (was Fail) | Pass | Same file |

### From SKILL.md

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market layer first | Pass | Research table | Pass | Module, now covering Tanzania |
| S2 | Ask only what is missing | Pass | Nothing asked | Pass | Price missing, handled by input 8 without a question |
| S3 | Pillar on every post | Pass | 12 of 12 | Pass | 14 of 14 |
| S4 | Split within the row and the caps | Pass | Brand 25 percent; community over the row, explained | Pass | Brand 21 percent; no pillar over 40 |
| S5 | Pillar rules agree with each other | Pass | Hospitality row now 30, 35, 25, 10, inside the cap (was Fail) | Pass | B2B row now inside the cap too (was Fail) |
| S6 | At least one community post a week | Pass | One in each week | Pass | One in each week, weeks as Step 2 defines them |
| S7 | Cultural anchors on every relevant date | Pass | 10 of 12 | Pass | 10 of 14, from the module this time |
| S8 | Sensitive dates avoided; quiet days handled | Pass | No quiet day in February; Samiljeol never used | Pass | Quiet day card, slot moved, ads paused, no CTA demanded (was Fail) |
| S9 | All six components on every post | Pass | 12 of 12 | Pass | 14 of 14 |
| S10 | Motion brief complete | Pass | 5 of 5 | Pass | 6 of 6 |
| S11 | Caption lengths per platform | Pass | Read against the gloss: photo feed 70 to 92 words, the four storytelling posts 76 to 118, short video 48 to 52 (was Fail) | Pass | Photo feed 67 to 96, the four storytelling posts 99 to 128, short video 46 to 59 (was Fail) |
| S12 | Hashtag counts | Pass | One rule now: photo feed 8 to 10, short video 5, none on stories and broadcasts (was Fail) | Pass | Photo feed 8 to 11, short video 5 (was Fail) |
| S13 | Opener rules | Pass | 12 of 12 | Pass | 14 of 14 |
| S14 | One sourced local reference a week | Pass | Kept from the first run | Pass | Kept |
| S15 | CTA on every caption, except a quiet day | Pass | 12 of 12 | Pass | 14 of 14; the quiet day has none, as Step 6 now allows |
| S16 | Register right for the market | Pass | 해요체, dry | Pass | Plain Dar Swahili |
| S17 | Rewrites, not translations | Pass | Korean first | Pass | Swahili first |
| S18 | Pasteable prompt, overlay stated | Pass | 12 of 12 | Pass | 14 of 14 |
| S19 | Full standalone prompts | Pass | Script: 0 cross references; each writes out the feed look in full | Pass | Same |
| S20 | Product truth in stills | Pass | Gift box lid and bakery bag are blank panels | Pass | 3 of 3 pack sentences say blank panel, no lettering (was Fail) |
| S21 | The month reads as one designed grid | Pass | 12 of 12 prompts carry all five hex values of the proposed feed look | Pass | 14 of 14 carry all five; turquoise, tarpaulin and shelf colours pulled into Ocean Teal and Lime Wash (was Fail) |
| S22 | Specific posting times | Pass | Day and clock time | Pass | Ramadan and module windows |
| S23 | Output in six parts | Pass | Open items added | Pass | Same |
| S24 | Interactive widget | Pass | One HTML file, tabs, flags, swatches, copy on every block | Pass | Same, plus the quiet day card |
| S25 | Widget spec covers what a post carries | Pass | Step 7 now lists every component, copy buttons on prompts and motion briefs, 390 px and dark mode (was Fail) | Pass | Quiet day card is now in the spec (was Fail) |
| S26 | Copy short, punchy, emotive | Pass | Every caption halved; the first line carries each post (was Fail) | Pass | Same (was Fail) |
| S27 | No invented prices, brand facts or promises | Pass | Opening hours, prize, layer count, anecdote, sell out and history gone; allergen line carries the three brief nuts plus a marked placeholder (was Fail) | Pass | Callback, availability and prize gone or marked; Open items lists every placeholder (was Fail) |
| S28 | No hyphens or em dashes | Pass | Script: 0 | Pass | Script: 0 |
| S29 | No real brand names | Pass | Script: 0 | Pass | Script: 0, run and skill files |
| S30 | Market kept clean | Pass | 0 East Africa terms | Pass | 0 Kenyan terms |

**Pass count: Brief A 40 of 40 (first run 33). Brief B 40 of 40 (first run 26).**

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| No hyphens and no em dashes in client facing copy | Pass | Pass | Script over the Markdown from section 1 down and all visible HTML text: 0. Lines added to the skill files carry none outside file paths |
| No real brand names | Pass | Pass | About 70 names over both reruns and every skill file: 0 hits; #KenyaTwitter and #NairobiTwitter replaced |
| Prompts are full standalone prompts | Pass | Pass | 26 prompts: ratio in words, place, month or time, light, the five feed look hex values written in full, a percent text zone; none points at another post |
| Pack text in prompts | Pass | Pass | Every label sentence says blank panel; 0 ask for lettering |
| Placeholders listed | Pass | Pass | Every bracket in a caption appears under Open items |
| HTML at phone width | Pass | Pass | 390 px wide at 390 px on every tab, light and dark; 0 script errors |

## 3. Verdicts

**Brief A rerun: Yes.** A creative director would send this to the client as the February plan. The captions now read like the brand talking, not writing: the box carrier, the last piece and the moon in the crumb each land in their first line. Nothing the bakery has not told us is stated as fact, and the two things only the client can supply (the full allergen list, the real palette and box artwork) are listed, not guessed. The proposed feed look holds twelve images in one warm ivory key.

**Brief B rerun: Yes.** A Dar es Salaam client would recognise its own month: the last ten days of Ramadan, Eid moving with the moon, Women's Day given to the mama lishe in their own words, Good Friday left silent, Easter Monday at the beach. All of it now comes from the module rather than the run. The bottle is never lettered by a model, the grid holds to five colours, and every price, prize and date still open is a marked client question.

## 4. Notes for the next pass (not defects)

* No market module exists for Korea; a Seoul module built from this run's research table would save the next Korean brief the research step.
* The hex values in the feed look are proposed; once a client palette arrives, the five values change in every prompt. A one line find and replace note in Open items would help.
* SKILL.md and the module files still carry about 75 compound hyphens in instruction text, untouched as in the earlier pack tests.
* The 2028 Ramadan and Eid dates in the module are approximate by design; the module tells the user to confirm each year.
