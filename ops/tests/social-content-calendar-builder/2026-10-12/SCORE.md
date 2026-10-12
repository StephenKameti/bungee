# Social Content Calendar Builder: test score, 12 October 2026

Skill tested: `products/skills/social-content-calendar-builder/skill/` at commit 8268e03 (SKILL.md and all five reference files). Two invented briefs, run once each exactly as SKILL.md instructs, as if sent in one message.

| Run | Files | Posts | Captions | Prompts | Motion briefs |
|---|---|---|---|---|---|
| Brief A, Milgyeol Bakehouse, Seoul, February 2027 | `brief-a.md`, `brief-a.html` | 12 (Mon, Wed, Fri) | 12 in Korean plus 2 messaging broadcasts | 12 | 5 (3 short videos, 2 story sets) |
| Brief B, Ladha Njema cooking oil, Dar es Salaam, March 2027 | `brief-b.md`, `brief-b.html` | 14 (Good Friday silent, slot moved to Thursday) | 14 in Swahili plus 3 trade broadcasts | 14 | 6 (4 short videos, 2 story sets) |

How the checks were made: rule checks were scripted over the Markdown from section 1 down (caption word counts, hashtag counts per platform, every prompt for ratio, hex, cross references and pack text, every motion brief for hook, sound off test and poster frame, hyphens and dashes, about 70 platform, retail, oil, bakery, payments, image model and app names). The HTML was opened headless at 390 px and 1280 px in light and dark, every tab clicked. Pass means the output meets the promise. Where it only passes because the run went beyond what the skill tells it to do, the evidence says so and points to the fix.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | Complete monthly calendar for any brand in any market | Pass | 12 posts, every anchor day, four week sections | Pass | 14 posts and 3 trade broadcasts across four sections |
| R2 | Pillars | Pass | Every post carries one; 25, 25, 33, 17 | Pass | 21, 29, 29, 21 |
| R3 | Platform specific posts | Pass | Photo feed, stories, short video and messaging each written to their own format; no caption reused | Pass | Same, plus a trade register for shopkeepers |
| R4 | Captions in the market's languages | Pass | Korean throughout, 해요체, the brand's dry voice | Pass | Swahili first, as the module's Languages by country sets for Tanzania |
| R5 | Compact motion brief for every short video post | Pass | 5 of 5 moving posts; every one has a hook in 0 to 2 s, a sound off test and a poster frame | Pass | 6 of 6 |
| R6 | Cultural moments layer that knows when to go quiet | Pass | No module, so researched: Seollal block and substitute day, Daeboreum, graduation, the tax refund pay packet; Samiljeol treated as remembrance | Fail | The module, which SKILL.md says takes precedence, has no Tanzanian date and no Islamic calendar. The last ten days of Ramadan and Eid el Fitr, which shape the whole month in Dar, came from the run's own research. The global file names no moveable faith date either (fixes 6, 7). Going quiet on Good Friday had to be improvised against the skill's own rules (fix 5) |
| R7 | Ships with the East Africa module; build your own from the template | Pass | No Korea module; the research path in the market layer worked as written | Fail | Module is Kenya only for dates, hashtags and the month by month file; its general hashtag set carries a platform brand name (#KenyaTwitter, #NairobiTwitter); its 10 October Kenyan holiday name is out of date (fix 7) |
| R8 | Builds casting, places, language, channels, prices and cultural dates from the market | Pass | Prices came from the brief; places, casting and channels researched | Fail | No price in the brief and no rule in the skill; the run improvised marked placeholders (fix 3) |
| R9 | Image prompts tuned for the leading image models | Pass | 12 prompts, 129 to 203 words, ratio in words, light, colour and text zone in each | Fail | Posts 6, 7 and 10 ask the model to render the brand label "facing camera": models garble lettering and invent a pack. The skill's product truth law lives only in the motion brief file (fix 4) |
| R10 | README copy is clean | Fail | First line: "captions in the market's languages a compact motion brief" is missing a comma (fix 10) | Fail | Same file |

Not testable in a one pass run: "push back and it reworks", "attach whatever you have", the Mumbai and Lisbon try it prompts.

### From SKILL.md (steps, quality check and standing rules)

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market layer first; module or research | Pass | Research table in section 1 | Pass | Module loaded; gaps researched and declared |
| S2 | Read the brief before asking; ask only what is missing | Pass | Nothing missing; no questions | Pass | Price missing but not a listed input, so not asked |
| S3 | Pillar on every post before writing | Pass | 12 of 12 | Pass | 14 of 14 |
| S4 | Split within the brand type row and the caps | Pass | Brand 25 percent, under the cap | Pass | Brand 21 percent, no pillar over 40 |
| S5 | Pillar rules agree with each other | Fail | Hospitality row asks 35 percent Brand; Step 2 and the check cap it at 30. The run chose the cap (fix 1) | Fail | Same contradiction in the B2B row (fix 1) |
| S6 | At least one community post a week | Pass | One in each week | Pass | Only because the run joined the 29 to 31 March tail to week 4; the skill does not define a week (fix 1) |
| S7 | Cultural anchors on every relevant date | Pass | 10 of 12 posts carry a moment | Pass | 10 of 14, all by research (scored under R6) |
| S8 | Sensitive dates avoided; quiet days handled | Pass | Samiljeol never named or sold | Fail | Good Friday is an anchor day; the skill demands a post on every anchor day and a CTA on every caption, and has no quiet day mechanism. The run left the day silent and moved the slot itself (fix 5) |
| S9 | All six components on every post | Pass | Theme, platform, caption, visual, time, format, CTA on 12 of 12 | Pass | 14 of 14 |
| S10 | Motion brief: hook on screen in 2 s, beats, sound off test, poster frame | Pass | 5 of 5, 4 to 7 beats each | Pass | 6 of 6, 4 to 7 beats each |
| S11 | Caption lengths per platform | Fail | Rule counts English words. Korean units carry a particle each: photo feed captions are 131 to 158 units (150 to 175 words in gloss), six of seven under the literal 150 (fix 2) | Fail | Swahili photo feed captions 125 to 154 words (137 to 187 in gloss), five of eight under 150; post 11 is 99 words on a 100 floor (fix 2) |
| S12 | Hashtag counts | Fail | Step 1 says 8 to 12 per post; Step 5 says 4 to 6 on short video and none on messaging. Run used Step 5 (fix 2) | Fail | Same (fix 2) |
| S13 | Opener rules | Pass | No opener with the brand, a hashtag or "we are excited" | Pass | Same; "Idd Mubarak" opens post 5, a greeting not the brand |
| S14 | One sourced local reference a week | Pass | Mangwon market, the train home, the jjajangmyeon lunch, Daeboreum nuts | Pass | Temeke futari, Kariakoo mama lishe, Kigamboni, the tin roof in masika |
| S15 | CTA on every caption | Pass | 12 of 12 | Pass | 14 of 14 (the silent day has no caption) |
| S16 | Register right for the market | Pass | Warm 해요체, dry, never cute | Pass | Plain Dar Swahili, mass market, no Sheng |
| S17 | Local language captions are rewrites, not translations | Pass | Written in Korean first; glosses follow | Pass | Written in Swahili first |
| S18 | Visual direction is a pasteable prompt with the overlay stated | Pass | 12 of 12 state no overlay and a clean percent zone | Pass | 14 of 14 |
| S19 | Prompts are full standalone prompts | Pass | Script: 0 cross references; every prompt names ratio, place, time, light, colour, text zone | Pass | Script: 0 cross references |
| S20 | Product truth in stills | Pass | Only the bakery's own blank ivory box appears | Fail | 3 prompts ask for the printed brand label (fix 4) |
| S21 | The month reads as one designed grid (design flair) | Pass | The run held one warm ivory and oat key by its own taste; the skill sets no feed look and no hex (fix 4) | Fail | Turquoise courtyard, blue tarpaulin, kanga red, rain grey, sky blue shelf: every post its own palette, no hex anywhere, so the grid will not hang together (fix 4) |
| S22 | Specific posting times | Pass | Day and clock time, tied to Seoul windows including the late scroll | Pass | Ramadan times around futari, module times after |
| S23 | Output in the five parts | Pass | Overview, weeks, posts, hashtag list, image priority | Pass | Same, plus open items |
| S24 | Interactive widget per Step 7 | Pass | Week tabs, pillar badges, cultural flags, copy buttons; 390 px wide at 390 px in light and dark | Pass | Same |
| S25 | Widget spec covers what a post carries | Fail | Step 7's card lists date, pillar, theme, caption, visual and time only; platform, format, CTA, motion brief, broadcasts and copy on prompts were added by the run, with no file, phone or theme rule (fix 9) | Fail | Same; a silent day has no card type (fix 9) |
| S26 | Copy short, punchy, emotive (standing rule) | Fail | The 150 to 300 word floor forces seven blog length captions; a creative director would cut each by half (fix 2) | Fail | Same, eight captions (fix 2) |
| S27 | No invented prices, brand facts or promises | Fail | Two invented facts went out flagged ("gone by Tuesday last year", "three years in Mangwon") and five went out unflagged: 8 AM opening hours (posts 4, 6, 12), a sea salt roll prize (post 3), a 27 layer count (post 5), a staff anecdote (post 7), wheat, milk and egg in the allergen line (post 9). The skill has no rule (fix 3) | Fail | Invented a one day callback (flagged), an unnamed prize and a closing date, and city wide availability "from Kariakoo to Mbagala" (post 7, unflagged); price placeholders improvised (fix 3) |
| S28 | No hyphens or em dashes in copy | Pass | Script: 0 in deliverable text and visible HTML | Pass | Script: 0 |
| S29 | No real brand names | Pass | Script: 0 platform, app, model or retail names; platforms by type | Pass | Script: 0; Coco and Kigamboni are public places |
| S30 | Market kept clean | Pass | 0 East Africa terms in A | Pass | 0 Kenyan terms; Swahili "matatu" here means three |

**Pass count: Brief A 33 of 40. Brief B 26 of 40.**

A fails: R10, S5, S11, S12, S25, S26, S27. B fails: R6, R7, R8, R9, R10, S5, S8, S11, S12, S20, S21, S25, S26, S27.

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| No hyphens and no em dashes in client facing copy | Pass | Pass | Script over the Markdown from section 1 down and all visible HTML text: 0 hyphens, 0 em dashes, 0 en dashes |
| No real brand names | Pass | Pass | Script for about 70 names (platforms, messaging apps, portals, image models, bakeries, oil brands, retailers, payments, telcos): 0 hits in either run. The skill file `east-africa.md` line 105 carries #KenyaTwitter and #NairobiTwitter (fix 7) |
| Prompts are full standalone prompts | Pass | Pass | 26 prompts: every one names ratio in words, place, month or time, light, colour and a percent text zone; 0 say "as above" or point at another post |
| Hex in prompts | Fail | Fail | 0 hex values in 26 prompts; the skill never asks for a palette (fix 4) |
| Pack text in prompts | Pass | Fail | 0 in A; 3 in B ask for the brand label |
| Hashtags per platform | Pass | Pass | Photo feed 8 to 11, short video 5, stories and messaging 0, by Step 5. One slip in A: post 5, a short video in the photo feed, carries 6, read as a short video count; the muddled rules invite it (fix 2) |
| Story text at 3 to 5 words | Pass | Pass | Every frame 2 to 5 words |
| East Africa is a module, not the default, for Brief A | Pass | n/a | Script for Swahili, Sheng, Nairobi, Kenya, shilling and similar: 0 hits in A |
| HTML at phone width | Pass | Pass | 390 px wide at 390 px on every tab, light and dark; 0 script errors |

### Cultural dates used, checked

| Date | Run | Confidence |
|---|---|---|
| Seollal, Sat 6 Feb 2027; holiday Fri 5 to Sun 7; substitute Mon 8 | A | Seollal date sure. Substitute day follows the rule for a block touching Sunday; confirm in the 2027 government list (flagged in the run) |
| Jeongwol Daeboreum, Sat 20 Feb 2027 | A | Sure: 15th day of the first lunar month |
| Valentine's Day Sun 14 Feb; Samiljeol Mon 1 Mar | A | Sure |
| Graduation season mid February; payday on the 25th; tax refund in February pay | A | Typical, varies by school and employer; the run words them loosely |
| Ramadan from about 8 or 9 Feb; Eid el Fitr expected Wed 10 Mar 2027 | B | Moon sighting sets it; may be 9 or 11 March (flagged, post 5 moves with it) |
| Good Friday 26, Easter Sunday 28, Easter Monday 29 Mar 2027 | B | Sure |
| International Women's Day Mon 8 Mar | B | Sure; observed, not a public holiday in Tanzania |
| Masika arriving mid to late March | B | Climatological, varies year to year; post 8 is held for a rainy day |
| Fire emergency number 114 | B | Believed current; flagged to confirm |
| Module: Kenya 10 October "Huduma Day" | n/a | Out of date: the day has carried several names and was gazetted as Mazingira Day in 2024; confirm the current name (fix 7) |

## 3. Verdicts

**Brief A: No.** The creative is good: the box carrier, the last piece and the moon in the crumb are ownable, and the Korean reads like a person. Three things stop it going out unchanged. The skill's 150 to 300 word floor turns seven feed posts into blog entries; a creative director would halve them. Brand facts were invented: two flagged (a sell out last year, three years in Mangwon) and five not (opening hours, a prize, a layer count, a staff anecdote, three allergens), and the allergen line is a mandatory. And the plan's own rules disagree on pillars and hashtags, so a careful reader of the overview sees numbers the skill contradicts.

**Brief B: No.** The month is right only because the run went past the module: Ramadan and Eid are missing from both the module and the global file, and a calendar built on the module alone would have opened March in Dar with no futari and no Eid. Three prompts ask the image model to letter the brand label, so the hero film still and both sale posts would come back with an invented pack. There is no feed look, so fourteen posts arrive in fourteen palettes. Prices and a service promise were improvised, and Good Friday's silence was the run's own rule. The ideas (the three second test, the mama lishe series, the family recipe challenge) are strong; the skill could not deliver them without improvising.

## 4. Fix list for the skill files

Ordered by buyer impact. Replacement text avoids hyphens so it can ship as written.

1. **SKILL.md Step 2: the pillar table breaks the pillar cap, and a week is undefined.** Lines 74 and 77 give Brand 35 percent for hospitality and B2B against the 30 percent cap on line 59 and in the check. Change line 74 to `| Hospitality / restaurant | 30% | 35% | 25% | 10% |` and line 77 to `| B2B / institutional | 30% | 15% | 20% | 35% |`. After line 54 add: "Weeks run Monday to Sunday. A part week of three days or fewer at either end of the month joins the week next to it."
2. **SKILL.md Steps 1 and 5: hashtag counts contradict, caption lengths are blog length and only work in English.** Line 48: replace "8 to 12 tags per post" with "the count set per platform in Step 5". Line 143: replace with "Length: 40 to 120 words. One storytelling post a week may run to 200. The first line carries the post." Line 158: replace with "Length: 30 to 80 words". After the Step 5 intro add: "Word counts are English words. Languages that fold more meaning into a word or are written without spaces (Korean, Japanese, Chinese, Thai, Swahili and others) match the length of the English gloss, not the literal count."
3. **SKILL.md Step 1: no rule on prices, offers or brand facts.** Add input 8: "**Prices, offers and brand facts**, prices in local currency, offer dates, stock, history, prizes and service promises. Use only what the brief gives. Where a post needs one that is missing, write a marked placeholder such as TSh [price, to confirm] and list it under Open items. Never invent a sell out, an anniversary, a delivery time or a prize." Add "Open items" as part 6 of the Step 7 output and a line to the quality check.
4. **SKILL.md Steps 4 and 7: no feed look, no hex, no product truth in stills.** In the Step 4 block replace the visual direction lines with a full standalone prompt rule (ratio in words, place, season and time, light, the feed look palette with hex, a percent text zone, the tool), and add: "The real pack and logo are placed in design. In the prompt, a pack is a plain shape in the brand colours with a smooth blank label panel and no lettering." Add to the Step 7 overview: "Feed look: four or five hex colours (from the brand, or proposed and marked), one light and grade, one type zone rule. Every prompt writes it out in full."
5. **SKILL.md Step 3 and the check: no way to go quiet.** After line 87 add a quiet day rule: on a sensitive date, or a day of worship the market keeps solemn (Good Friday, a remembrance day, national mourning), post nothing promotional and pause paid posts; either leave the day silent or post one plain line with no product, no CTA and no hashtags, and move the anchor slot to the nearest suitable day. The CTA and anchor day rules do not apply to a quiet day. Update the quality check line.
6. **references/global-cultural-moments.md: no moveable faith or lunar dates.** Add a section for moveable calendars: Ramadan and the two Eids (about 11 days earlier each year, set by moon sighting), the lunar new year, Diwali, Holi, Vesak, Passover, Rosh Hashanah and Yom Kippur, Western and Orthodox Easter; check the target month for each, and in a fasting month time food posts to the evening meal and after. SKILL.md line 85: append that a module never lists every date, so moveable dates are always checked.
7. **references/markets/east-africa.md: Kenya only, a platform brand in the hashtags, a stale holiday, no Islamic calendar.** Add fixed dates for Tanzania, Uganda and Rwanda, the Islamic holidays observed across the region, Rwanda's Kwibuka mourning period, and Umuganda; fix the 10 October line; replace #KenyaTwitter and #NairobiTwitter; add short per country hashtag sets; fix "JAN 2-7".
8. **references/markets/east-africa-calendar.md: says nothing about Ramadan.** Add a note at the top pointing to the moveable dates in the module and saying the month by month file is Kenyan.
9. **SKILL.md Step 7: the widget spec is thin.** Replace the Visual format list: one self contained HTML file; week tabs; a card carrying every component including platform, format, CTA and the motion brief; a copy button on every caption, broadcast, prompt and motion brief; cultural flags in a distinct colour; quiet days as their own card; overview, hashtags, image priority and open items as tabs; readable at 390 px with no sideways scroll, in light and dark.
10. **README.md line 3: missing comma.** "captions in the market's languages a compact motion brief" becomes "captions in the market's languages, a compact motion brief". Also add the quiet day and price behaviour to the promise line so it matches the skill.

Not fixed, noted: SKILL.md and the module files carry about 75 compound hyphens in instruction text (production-ready, code-switch). Earlier pack tests left instruction text alone; buyer facing copy (README, store pages) is clean.
