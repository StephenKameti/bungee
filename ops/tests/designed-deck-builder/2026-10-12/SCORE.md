# Designed Deck Builder: test score, 12 October 2026

Skill tested: `products/skills/designed-deck-builder/skill/` as shipped (SKILL.md, `references/markets/TEMPLATE.md`, `references/markets/east-africa.md`). Two invented briefs, each with an invented source deck carrying planted faults (typos, a 30 plus word paragraph, team comments, a hyphen and an em dash in the client's copy, an unverified claim, and in B a swapped digit and no hex codes). Each run once, exactly as SKILL.md instructs, as if sent in one message.

| Run | Files | Language | Slides | HEAVY | Rendered copy blocks |
|---|---|---|---|---|---|
| Brief A, Mulgyeol Refill apartment partner deck, Seoul, Korean and English | `brief-a.md`, `brief-a.html` | Danji Bulletin (moods: Notice, Gable) | 11 | 5 | 83 |
| Brief B, Kipaji Alizeti trade roadshow deck, Dar es Salaam, Swahili and English | `brief-b.md`, `brief-b.html` | Kariakoo Ledger (moods: Daftari, Ubao) | 11 | 5 | 80 |

How the checks were made: rule checks were scripted over every prompt, every quoted copy block inside the prompts, the Markdown from section 1 down, and every file in the pack. A fidelity script traced each source deck line to the prompts. The HTML was opened headless at 390 px and 1280 px in light and dark. Pass means the output meets the promise. Where it only passes because the run went beyond what the skill tells it to do, the evidence says so and points to the fix.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | Plain deck in, image prompts for fully designed slides out, copy included | Pass | 11 prompts, every slide's copy quoted inside its prompt | Pass | 11 prompts, same |
| R2 | A design language invented for that brand and its market | Pass | Danji Bulletin: lift lobby notice board and painted gable numerals, only possible in a Seoul complex | Pass | Kariakoo Ledger: order book and painted Kariakoo shop boards, only possible for a Dar es Salaam trade audience |
| R3 | Consistent typography across every slide | Pass | One type description per mood, same two families in both; but the two moods word the type differently, and nothing in SKILL.md asks for a fixed type line (fix 4) | Pass | Same; slab serif and typewriter mono in both moods, worded differently (fix 4) |
| R4 | Comments actioned before design starts | Fail | SKILL.md never mentions comments; the run actioned two only because the README promises it. A literal Step 1 run renders the comment text (fix 1) | Fail | Same; the run also had to decide alone that a request to add a government quality mark must be flagged, not drawn (fix 1) |
| R5 | Works for any market | Pass | Seoul built from research; no East Africa term in A | Pass | Tanzania from the module's Languages by country, Swahili first, no Sheng |
| R6 | Builds casting, places, language, channels, prices and cultural dates from the market | Fail | Casting, places, language and prices are built; channels and cultural dates are not, and SKILL.md has no step for them. The promise is copied from the campaign packs and is wrong for a deck tool (fix 9) | Fail | Same |
| R7 | Market module template; East Africa included as a worked example | Pass | No module for Korea; TEMPLATE.md is present and fit to fill | Pass | Module loaded; its Tanzania language rule drove the copy order |
| R8 | Prompts tuned for leading models, adapt to others | Pass | Model named generically in Step 4 and in the run | Pass | Same |

Not testable in a one pass run: "attach whatever you have, the skill reads them" (no files attached), "push back and it reworks".

### From SKILL.md

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market established first; module loaded or built from research | Pass | Market layer table before any design; Hangul, environmental claim rules and complex vernacular researched | Pass | Module loaded; Dar es Salaam texture researched because the module's street texture is Nairobi's and it says to check other cities |
| S2 | Home and audience market both named | Pass | Same market, stated | Pass | Same market, stated |
| S3 | Every slide's text extracted; broken lines corrected and listed as copy flags | Pass | 2 typos corrected and flagged; everything else verbatim (fidelity script: every source line found or accounted for) | Pass | 2 typos and the swapped digit corrected and flagged |
| S4 | Numbers proofread first | Pass | All figures in the HEAVY repair orders lead with numbers | Pass | The 250 ml margin (TSh 3,400 for 4,300) was caught only because the run checked the sums; Step 1 does not ask for it (fix 3) |
| S5 | Brand Sheet: hexes, logo as attached asset, product, type in image language, brand world | Pass | All from the brief | Pass | Hexes proposed and labelled because none were supplied; SKILL.md has no rule for a missing palette when working unattended (fix 5) |
| S6 | Named language, 2 or 3 options, one recommended; unattended pick stated up front | Pass | 3 options, pick and reason in section 4 | Pass | Same |
| S7 | Language derived from material truth, category tension, temperament, market vernacular | Pass | Breaks the refill category's kraft and leaves code; council's own media | Pass | Breaks the golden pour code; the wholesaler's own media |
| S8 | Devices from the families; one accent family only | Pass | One coral stamp per slide | Pass | One yellow brush stroke per slide |
| S9 | Two mood system with brand specific names | Pass | Notice and Gable, 7 and 4 slides | Pass | Daftari and Ubao, 8 and 3 slides |
| S10 | Craft standards: one idea dominates, real hierarchy, content through medium | Pass | Prices on nozzle labels, table as an official notice, timeline as a lift panel, data as a building number | Pass | Margin in the ledger, offer on a carbon invoice, map in ballpoint, kit tagged on the counter |
| S11 | One round of production questions | Pass | Defaults stated; Step 4 has no unattended path, so the run borrowed Step 3's (fix 6) | Pass | Same (fix 6) |
| S12 | One prompt per slide, fully self contained | Pass | Scripted: 11 of 11 carry format, asset contract, full style DNA, layout, copy, closing bar; none refers to another | Pass | Scripted: 11 of 11 |
| S13 | Six part anatomy in order | Pass | Scripted, every prompt | Pass | Scripted, every prompt |
| S14 | Copy in double quotes, blocks short, long paragraphs broken into stacked lines | Pass | 83 blocks; two run 16 and 18 words, both under the 30 word line where rendering breaks | Pass | 80 blocks, longest 13 words |
| S15 | Rationale line per slide | Pass | 11 of 11 | Pass | 11 of 11 |
| S16 | HEAVY slides marked with a zone by zone fix strategy | Pass | 5 HEAVY, each with an order and an edit line | Pass | 5 HEAVY, same |
| S17 | Treatment matched to slide type | Pass | Cover, data, big idea, close loud; close is one word and one object | Pass | Same |
| S18 | HTML library: masthead, palette chips, assets card, copy flags card, acts, copy buttons, badges, rationale, fix notes, footer | Pass | `brief-a.html`, 11 copy buttons | Pass | `brief-b.html`, 11 copy buttons |
| S19 | Library page usable on a phone and in dark mode | Pass | 390 px wide at 390 px, light and dark, 0 script errors. The first build set slide numbers in Foam on white and was fixed in the run; SKILL.md gives no template and no rule (fix 8) | Pass | Same; first build put white text on the yellow HEAVY badge, fixed in the run (fix 8) |
| S20 | Style consistency workflow in the delivery | Pass | Section 7 | Pass | Section 7 |
| S21 | Rescue edit for renders that drift generic | Fail | SKILL.md hands every deck the same rescue line, "Add heavy film grain, rougher textures". Danji Bulletin is clean steel and matte paper; the line would push it toward grunge, the opposite of the language (fix 7) | Pass | Grain and rough texture suit a ledger and a Kariakoo lane, by luck rather than by rule |
| S22 | No two libraries could be mistaken for siblings | Pass | Against B and the skill's own example: different ground, type, accent and medium | Pass | Avoids the example's till receipt and stamp |
| S23 | Claims and regulatory notes observed | Pass | Bottle statistic, pilot figures and "zero waste" flagged under Korea's environmental claim rules | Pass | Fortification and "cholesterol free" flagged; quality mark not drawn; consent for the quote flagged |
| S24 | Casting by context | Pass | Lobby of building 102, late morning, silver bob, cardigan | Pass | Temeke duka at 07:00, kitenge headwrap, pouch in hand |
| S25 | Local language rendered and proofed correctly | Pass | Hangul lines kept short, each in its own zone, native proof on every render; all of it the run's own, since SKILL.md says nothing about a non Latin script (fix 2) | Pass | Swahili first per the module, given width, under 15 words, Swahili proof in the repair rules |

**Pass count: Brief A 30 of 33. Brief B 31 of 33.**

A fails: R4 comments, R6 channels and cultural dates, S21 rescue edit. B fails: R4 comments, R6 channels and cultural dates.

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| Prompts are full standalone prompts | Pass | Pass | Script: each of 22 prompts opens with the format line, carries the asset contract, a full style DNA paragraph with hex, its own layout and copy, and ends on the closing bar; none says "as above", "same as" or names another slide. |
| No hyphens and no em dashes in rendered slide copy | Fail | Fail | Script over every quoted block: A renders "Three steps — no new plastic.", "A zero-waste corner residents can see." and "— Ms Park". B renders "Pre-order kwa simu." and "— Mama Rehema". All are the client's own words; Step 1 keeps them verbatim and nothing tells the run to rewrite them (fix 1). |
| No hyphens and no em dashes in the run's own text | Pass | Pass | Script over the Markdown from section 1 down with quoted client copy removed: 0. |
| No real brand names | Pass | Pass | Script for about 80 household, oil, retail, payment, platform, image model and certification names over both runs: 0 (one false hit on the word "Line"). |
| East Africa is a module, not the default, for Brief A | Pass | n/a | Script for Swahili, Sheng, Nairobi, Kenya, matatu, shilling, duka, kadogo and similar: 0 in A. |
| Source copy reaches the slides | Pass | Pass | Fidelity script: every source line found verbatim in the quoted copy, or accounted for by a copy flag, a table split into cells or a paragraph split into lines. |
| No hyphens or em dashes in the pack's own copy | Fail | Fail | Script over the pack: SKILL.md 50 hyphenated words in prose ("self-contained", "content-through-medium", "two-mood"), TEMPLATE.md 7, east-africa.md 1 ("on-slide"). README 0. Rule 4 covers the pack's user facing copy (fix 10). |

## 3. Verdicts

**Brief A: No, narrowly.** The idea is the best thing in it. Danji Bulletin turns a residents' council's own notice board and the painted numbers on their buildings into the deck, and "1,240" painted on a gable wall is the slide a council will remember. Three things stop it going out unchanged: three slides render a dash or a hyphen the house style forbids; the comments were actioned only because the run read the README; and the footer's rescue edit would drag a clean, steel and paper language into grunge on the first render that drifts. The Hangul handling is right, but the run invented it.

**Brief B: No.** The creative is strong and right for the room: a margin table in the wholesaler's own ledger, the offer on a carbon invoice he will sign, the big idea painted over a Kariakoo lane. But the skill could not deliver it without improvising: no rule for missing hex codes, no rule to check the source's sums (a swapped digit in the margin table would have gone to the roadshow), no rule for team comments, including one asking for a real government mark, and two dashes left in rendered copy.

## 4. Fix list for the skill files

Ordered by buyer impact. Replacements avoid hyphens so they can ship as written.

1. **SKILL.md, Step 1: comments and dashes.** After "Everything else stays word for word, this is the client's approved copy, not raw material." add: "Read every comment, note and tracked change in the source and action each one before design starts; list each under the copy flags with what changed, and never render comment text on a slide. A comment you cannot action safely, such as adding a third party mark you do not hold the file for, is flagged and left out. Rewrite hyphens, em dashes and en dashes out of rendered copy with a comma, full stop, line break or a closed or open compound, and list each as a copy flag so the user can revert."

2. **SKILL.md, Step 5: non Latin scripts.** After item 5 add: "For a script other than Latin (Hangul, Arabic, Devanagari, Chinese, Thai and others), keep every rendered line short, give it its own zone so it can be repaired alone, describe the type in that script's own terms, and require a native reader to proof every render. Right to left scripts need the layout mirrored where the copy leads. If a line keeps failing, leave its panel empty and set it as live text."

3. **SKILL.md, Step 1: sums.** Append to Step 1: "Check every figure, sum and total in the source against the others. A figure that does not add up is a copy flag: show the sum, apply the correct figure, and ask the user to confirm it."

4. **SKILL.md, Step 5 item 3: type lock.** Replace "The style DNA: 2 to 3 sentences of this deck's language, ground, textures, type behaviour, photo treatment, accent, with brand hexes inline." with: "The style DNA: 2 to 3 sentences of this deck's language, ground, textures, type behaviour, photo treatment, accent, with brand hexes inline. Write it once per mood and paste it word for word into every prompt of that mood. Its type sentence is the type lock: identical in both moods and on every slide, so typography never drifts."

5. **SKILL.md, Step 2: missing palette.** After "Ask the user only about genuine gaps" sentence, add: "Working unattended, or when the user cannot supply them, propose hexes from the brand's description, mark them proposed in the Brand Sheet and on the library's palette chips, and ask for the real codes in the delivery."

6. **SKILL.md, Step 4: unattended.** Append: "Give each question a default. Working unattended, or when the brief arrives as one message to run, proceed on the defaults and state them up front."

7. **SKILL.md, Step 6: rescue edit.** Replace "and a one-line rescue edit for renders that drift generic ("Add heavy film grain, rougher textures. Change no text.")" with: "and a one line rescue edit for renders that drift generic, written from this language's own devices: a rough, analogue language pushes grain and texture, a clean language pushes crisper paper, harder light and stricter alignment. End it with \"Change no text.\""

8. **SKILL.md, Step 6: page quality.** After the library page sentence add: "The page works at phone width with no sideways scroll, in light and dark, and any brand colour used for text or badges is readable on its ground."

9. **README.md, Markets: wrong promise.** Replace "Name the market in your request and the skill builds everything local from it: casting, places, language, channels, prices and cultural dates." with: "Name the market in your request and the skill builds everything local from it: textures, street and retail references, casting, places, prices, how local language copy renders, and the claim rules on slide copy." Replace "Consistent typography across every slide, comments actioned before design starts." with "One locked type system across every slide. Comments and copy fixes actioned before design starts." so the promise names what fixes 1 and 4 now guarantee.

10. **SKILL.md, TEMPLATE.md, east-africa.md: hyphens in the pack's own copy.** Rewrite every hyphenated word in prose (for example "self-contained" to "self contained", "two-mood" to "two mood", "on-slide" to "on slide"); keep file names and paths.

11. **references/markets/east-africa.md: Tanzania's street words.** The Media section names only Kenya's matatu and boda boda. Append: "In Tanzania the shared minibus is the daladala and the three wheeler the bajaji; Dar es Salaam's wholesale texture centres on Kariakoo, not on any Nairobi reference."
