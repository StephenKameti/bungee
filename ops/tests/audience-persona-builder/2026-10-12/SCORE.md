# Audience and Persona Builder: test score, 12 October 2026

Skill tested: `products/skills/audience-persona-builder/skill/` as checked out on 12 October 2026 (SKILL.md, references/markets/east-africa.md, references/markets/TEMPLATE.md) and the pack README. Two invented briefs, run once each exactly as SKILL.md instructs, as if sent in one message.

| Run | Files | Tiers | Day in the life moments | Variant |
|---|---|---|---|---|
| Brief A, Nuri Table weekly side dish box, Seoul | `brief-a.md`, `brief-a.html` | 3 (Seo Jiwon, Lee Mihwa, Kang Doyun) | 8, 7, 6 | FMCG / Mass Market emphasis; no variant fits subscription food |
| Brief B, Shema Smile toothpaste, Kigali | `brief-b.md`, `brief-b.html` | 3 (Ineza, Mukamana Claudine, Gisa) | 8, 7, 6 | Youth / Teen |

How the checks were made: rule checks were scripted over the Markdown from section 1 down (links and file paths removed) and all visible HTML text: hyphens, em and en dashes, about 70 platform, retail, telecom, payment, FMCG and oral care brand names, and East Africa terms in Brief A. The widgets were opened headless at 390 px and 1280 px in light and dark: page width, elements past the edge, script errors, and whether tapping a ring opens its tier. Pass means the output meets the promise. Where it only passes because the run went beyond what the skill tells it to do, the evidence says so and points to the fix.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | Audience definitions and personas for any market | Pass | Korea built from research, no module; quintiles, officetels, the walk home | Pass | Rwanda built from research on top of the East Africa module's language line |
| R2 | Rooted in real local life: named neighbourhoods | Pass | Sillim, Bongcheon, Guro Digital Complex, Suseong (Daegu), Mangwon | Pass | Kimironko, Remera, Nyamirambo, Kimironko market, the moto stage |
| R3 | Income tiers read against the market's own distribution | Pass | Statistics Korea household income quintiles, with housing tenure as the visible marker | Fail | The module has nothing for Rwanda and the skill has no rule for a market whose known classification is a welfare tool. The run used Ubudehe, put all three personas in category C, and the tier tells a planner nothing (fixes 6, 7) |
| R4 | Purchase channels | Pass | Station exit convenience store, pickup lockers, dawn delivery, the gift shop | Pass | Butike, Kimironko market stalls, the kiosk by the moto stage |
| R5 | Media habits | Pass | Platform type, time and content in every tier | Pass | Same; radio by time of day |
| R6 | A day in the life a creative team can brief from | Pass | Present tense, time stamped, one brand moment each | Pass | Same |
| R7 | Builds casting, places, language, channels, prices and cultural dates from the market | Fail | SKILL.md never asks for cultural dates; the run added Seollal and Chuseok on its own (fix 4) | Fail | Same; the run added term dates, Umuganda, Kwibuka on its own (fix 4) |
| R8 | Copy TEMPLATE.md to make a market permanent | Fail | Desk check: TEMPLATE.md has no media or calendar section, so a filled module cannot carry two of the promised layers (fix 8) | Fail | Same |
| R9 | "Image prompts are tuned for the leading image models" | Fail | The pack writes no image prompts; the line was copied from another pack (fix 9) | Fail | Same |

Not testable in a one pass run: "attach whatever you have", "push back and it reworks".

### From SKILL.md (quality check and step rules)

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market read first; module loaded or researched | Pass | No Korea module; layer researched before any persona | Pass | East Africa module loaded; Rwanda researched |
| S2 | No generic global default; East Africa never the default | Pass | Script: 0 East Africa terms in A | Pass | Rwanda kept apart from Kenyan terms: no Sheng, LSM or estate table |
| S3 | Step 1 inputs extracted, missing ones asked | Pass | Two questions, each with a working assumption; SKILL.md says only "ask", nothing about a one message brief (fix 3) | Pass | Same |
| S4 | Three tier model, never flattened | Pass | Primary, Secondary, Amplifier | Pass | Same |
| S5 | All six components per tier | Pass | Every tier | Pass | Every tier |
| S6 | Tier assigned in the market's own system | Pass | Quintile per persona | Pass | Ubudehe labels are local, but see R3 |
| S7 | Day in the life, 6 to 8 time stamped moments, present tense | Pass | 8, 7, 6 | Pass | 8, 7, 6 |
| S8 | Named places, media types, cultural references, the brand moment | Pass | Every day | Pass | Every day |
| S9 | Psychographic profile, six fields | Pass | Every tier | Pass | Every tier |
| S10 | Price signals in local currency | Pass | KRW per lunchbox and per week; marked estimates by the run's own choice (fix 5) | Pass | RWF per tube; marked estimates (fix 5) |
| S11 | Brand relationship and barrier | Pass | Fear of waste, pride, sounding like an ad | Pass | Not her decision, trust, being scripted |
| S12 | Strategic implication as brief input, not summary | Pass | Four lines per tier | Pass | Four lines per tier; Tier 3's are terse |
| S13 | Audience type variant applied | Pass | No variant fits subscription or direct to consumer; nearest one used and said so | Pass | Youth / Teen: teen as Tier 1, mother as Tier 2 |
| S14 | Part 1: interactive widget, expandable card per tier, five surfaces | Pass | `brief-a.html`. SKILL.md gives no format, file, layout or design bar; the run chose a single HTML file (fix 6) | Pass | `brief-b.html`, same |
| S15 | Widget works on a phone, light and dark | Pass | 390 px: page 390 px wide, 0 elements past the edge, 0 script errors, ring tap opens its tier; same at 1280 px and in dark | Pass | Same |
| S16 | Part 2 written in the template's structure | Pass | All four blocks | Pass | All four blocks |
| S17 | Tier 3 profile | Pass | Part 2 says "adapted profile"; the quality check asks every tier for 6+ moments; the run gave all six components (fix 10) | Pass | Same |
| S18 | Named persona, name matched to area and tier | Pass | Jiwon (1990s Seoul), Mihwa (1960s Daegu), Doyun | Pass | Ineza, Mukamana Claudine (surname first, as used), Gisa |
| S19 | Internal voice quote in the local register | Pass | Korean, with an English gloss the skill does not ask for (fix 5) | Pass | Kinyarwanda, glossed and flagged for a native check, neither asked for (fix 5) |
| S20 | Bold strategic line per tier | Pass | Three | Pass | Three |
| S21 | No generic marketing language | Pass | Script: 0 hits for urban millennial, digitally savvy, values quality, Gen Z, on the go | Pass | Same |
| S22 | Cross tier read, 3 to 4 sentences | Pass | 4 | Pass | 4 |

**Pass count: Brief A 28 of 31. Brief B 27 of 31.**

A fails: R7 cultural dates, R8 template, R9 image prompt promise. B fails: R3 tier reading, R7, R8, R9.

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| No hyphens and no em dashes in client facing copy | Fail | Fail | Script over the deliverable and visible HTML. A: 23 hyphenated words (Markdown 17, HTML 6), 0 em or en dashes. B: 6 (Markdown 5, HTML 1). Two come straight from the skill's own templates: the field label "Self-image" and the heading "CROSS-TIER STRATEGIC READ". The rest follow the skill's own prose, which has about 40 hyphenated words (decision-maker, day-in-the-life, single-use, mid-tier), and Korean romanisation (Gwanak-gu, Suseong-gu). SKILL.md has no hyphen rule at all (fixes 1, 2) |
| No real brand names anywhere | Fail | Pass | Script for about 70 names. A: "webtoon" on the commute, a genre word in Korea but also a registered platform trademark. SKILL.md names platforms by type in its examples but never says to (fix 1). B: 0 hits |
| Figures sourced or flagged | Pass | Pass | Every figure not from the brief or a cited source is marked as an estimate or illustrative, by the run's own choice; SKILL.md says nothing (fix 5) |
| Claims a client would question | Pass | Fail | B Tier 1: "girls drive the brushing talk in class" is stated as fact with no source. Same root as the figures rule (fix 5) |
| East Africa is a module, not the default, for Brief A | Pass | n/a | The module was not loaded for A. Script for Swahili, Sheng, Nairobi, Kenya, matatu, shilling, chama, duka, LSM and similar: 0 hits |
| Widget design | Pass | Pass | Headline written as the audience insight, a serif display face with a grotesk, three ring architecture in a palette set per brief, dark mode tokens. All the run's own choices; the skill sets no design bar (fix 6) |

## 3. Verdicts

**Brief A: No.** The thinking is strong: the mother's Seollal parcel as both competitor and ally is the insight a Seoul planner would want, and the walk home from Sillim station gives media a real place to stand. But it cannot go to a client as written. It carries 23 hyphens, two of them forced by the skill's own template labels, and it names a platform trademark. The skill gives no rule for either, so every buyer's output will repeat them. Cultural dates, a README promise, appear only because the run added them.

**Brief B: No.** The personas are vivid and the Kimironko geography is right, but the tier reading fails a planner: all three personas sit in Ubudehe C, a welfare category, so the tier does not separate them or guide media weight. The module sells itself as East Africa but holds nothing for Rwanda beyond the language order. One claim is stated as fact without a source, and the copy carries 6 hyphens from the skill's own templates.

## 4. Fix list for the skill files

Ordered by buyer impact. Replacements avoid hyphens so they can ship as written.

1. **SKILL.md: no writing rules for the deliverable.** Add a "House rules for every output" section after the Core Mandate: no hyphens or em dashes anywhere in the deliverable, including labels and romanised names (write "Gwanak district", "Jiwon"; where a language's spelling needs a hyphen, rewrite around the word); name platforms, apps, retailers and competitors by type, never by trademark, unless the brief names them; figures and claims rule (fix 5); gloss and native check rule (fix 5).
2. **SKILL.md, references: the skill's own text models hyphens.** Rewrite every hyphenated word in SKILL.md, TEMPLATE.md and east-africa.md (about 45, including the "Self-image" label, the "CROSS-TIER STRATEGIC READ" heading, decision-maker, day-in-the-life, single-use, code-switch, sari-sari).
3. **SKILL.md, Step 1: questions stall a one message brief.** After the inputs, add: give each missing input a working assumption; if the brief came as one message or the user wants the work now, proceed on the assumptions and list them with the read back.
4. **SKILL.md, Component 4 and the market layer: no cultural dates.** Add a "Moments that matter" field to Component 4 (the dates and seasons that change this persona's behaviour, from the module or research, with the live year to confirm), and add the cultural calendar to the list of things that derive from the market. Makes README R7 true.
5. **SKILL.md: no discipline on figures, claims and local language lines.** Add to the house rules: every figure or claim not from the brief or a cited source is marked as an estimate or a hypothesis to verify; any quote in a language the reader may not read carries an English gloss; any line in a language the writer cannot verify is flagged for a native check.
6. **SKILL.md, Step 6: the widget has no specification.** Specify it: one self contained HTML file; the architecture drawn (rings or layers, not a table); an expandable card per tier with the five surfaces, the quote with its gloss and the bold line; the cross tier read; a headline written as the audience insight; type and colour with a point of view, from the brand if supplied; works at phone width with no sideways scroll, in light and dark.
7. **SKILL.md, Component 1 tier reference: no rule for markets without a marketing tier scale.** Add: where the market's best known classification is an official or welfare one, use it as the shared reference, say what it is, and add visible markers (housing, schooling, transport, phone) so each persona's tier is distinct and useful for media weight.
8. **TEMPLATE.md and east-africa.md: no media or calendar section; wider East Africa empty.** Add "Media landscape" and "Cultural calendar" sections to TEMPLATE.md and to the East Africa module. In the module, fix the front matter (it says the tier system applies loosely to the wider region; the body says never reuse it) and add per country pointers for Uganda, Tanzania and Rwanda: tier reference, peer networks, purchase formats, currency.
9. **README.md: a promise from another pack.** Replace "Image prompts are tuned for the leading image models and adapt to others with light edits." with a line about what this pack does deliver.
10. **SKILL.md, Step 6 Part 2: Tier 3 contradicts the quality check.** Replace "[Adapted profile, focus on role, reach, trust mechanism]" with all six components plus role, reach and trust mechanism, and make the quality check match.
