# Designed Deck Builder: rerun score, Briefs A and B, 12 October 2026

Skill tested: `products/skills/designed-deck-builder/skill/` and `README.md` after the SCORE.md fix list (fixes 1 to 8 and 10 in SKILL.md, fix 9 in README.md, fix 10 in TEMPLATE.md and east-africa.md, fix 11 in east-africa.md). Both briefs failed the first pass mark, so both were run once more, exactly as the updated SKILL.md instructs, as if sent in one message.

| Run | Files | Language | Slides | HEAVY | Rendered copy blocks |
|---|---|---|---|---|---|
| Brief A rerun, Mulgyeol Refill, Seoul | `brief-a-rerun.md`, `brief-a-rerun.html` | Danji Bulletin (Notice, Gable) | 11 | 5 | 85 |
| Brief B rerun, Kipaji Alizeti, Dar es Salaam | `brief-b-rerun.md`, `brief-b-rerun.html` | Kariakoo Ledger (Daftari, Ubao) | 11 | 5 | 81 |

How the checks were made: the same 33 checks and the same scripts as SCORE.md, over every prompt, every quoted copy block, the Markdown from section 1 down and every file in the pack. The HTML was opened headless at 390 px and 1280 px in light and dark. Pass means the output meets the promise because the skill told it how, not because the run improvised.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | Plain deck in, designed slide prompts out, copy included | Pass | 11 prompts | Pass | 11 prompts |
| R2 | A design language invented for that brand and its market | Pass | Danji Bulletin, unchanged | Pass | Kariakoo Ledger, unchanged |
| R3 | One locked type system across every slide | Pass | Script: the type lock sentence appears word for word in 11 of 11 prompts, both moods (was improvised) | Pass | Same, 11 of 11 |
| R4 | Comments and copy fixes actioned before design starts | Pass | Both comments actioned under Step 1's comments pass; no comment text on any slide (was Fail) | Pass | Mbezi added; the quality mark flagged and left out, as Step 1 now says for a third party mark (was Fail) |
| R5 | Works for any market | Pass | Seoul from research; 0 East Africa terms | Pass | Tanzania from the module |
| R6 | Builds textures, street and retail references, casting, places, prices, local language rendering and claim rules from the market | Pass | Every item present in the market layer and the prompts; the promise now matches what SKILL.md does (was Fail) | Pass | Same (was Fail) |
| R7 | Market module template; East Africa as a worked example | Pass | TEMPLATE.md now free of hyphens, fit to fill | Pass | Module now carries Tanzania's own street words |
| R8 | Prompts tuned for leading models, adapt to others | Pass | Model named generically | Pass | Same |

Not testable in a one pass run: "attach whatever you have", "push back and it reworks".

### From SKILL.md

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market first; module loaded or built from research | Pass | Market layer before design | Pass | Module loaded, including its new Tanzania line |
| S2 | Home and audience market both named | Pass | Stated | Pass | Stated |
| S3 | Verbatim extraction, copy flags for every correction | Pass | 2 typos, 2 comments, 3 dash rewrites, all listed with a revert path | Pass | 2 typos, 1 sum, 2 comments, 2 dash rewrites, all listed |
| S4 | Numbers proofread first; sums checked | Pass | Sums pass run and recorded: nothing to flag | Pass | Sums pass caught TSh 3,400 for 4,300 by rule (was improvised) |
| S5 | Brand Sheet complete | Pass | From the brief | Pass | Hexes proposed, marked on the Brand Sheet and on the palette chips, real codes asked for in the footer, as Step 2 now says (was improvised) |
| S6 | Named language, options, recommendation, unattended pick stated | Pass | Section 4 | Pass | Section 4 |
| S7 | Language derived from the brand's world and the market | Pass | Unchanged | Pass | Unchanged |
| S8 | One accent family | Pass | Coral stamp only | Pass | Yellow stroke only |
| S9 | Two mood system | Pass | Notice and Gable | Pass | Daftari and Ubao |
| S10 | Craft standards, content through medium | Pass | Unchanged | Pass | Unchanged |
| S11 | Production questions with defaults | Pass | Defaults stated up front because the brief came as one message, as Step 4 now says (was improvised) | Pass | Same |
| S12 | One self contained prompt per slide | Pass | Script, 11 of 11 | Pass | Script, 11 of 11 |
| S13 | Six part anatomy in order | Pass | Script, 11 of 11 | Pass | Script, 11 of 11 |
| S14 | Copy blocks short, long paragraphs stacked | Pass | 85 blocks, longest 11 words (was 18) | Pass | 81 blocks, longest 13 words |
| S15 | Rationale line per slide | Pass | 11 of 11 | Pass | 11 of 11 |
| S16 | HEAVY slides with zone by zone fixes | Pass | 5, numbers first | Pass | 5, numbers first |
| S17 | Treatment matched to slide type | Pass | Unchanged | Pass | Unchanged |
| S18 | HTML library with every element Step 6 lists | Pass | `brief-a-rerun.html`, 11 copy buttons | Pass | `brief-b-rerun.html`, 11 copy buttons, chips marked proposed |
| S19 | Page works on a phone and in dark mode, brand colours readable | Pass | 390 px wide at 390 px in light and dark, 0 script errors; slide numbers in Deep Teal on light, Signal Coral on dark | Pass | Same; Ink on the yellow HEAVY badge |
| S20 | Style consistency workflow | Pass | Section 7 | Pass | Section 7 |
| S21 | Rescue edit written from the language's own devices | Pass | "Crisper matte paper, harder flat daylight, sheets squared to the board, building numerals sharper and larger. Change no text." (was Fail) | Pass | "Heavier film grain, more worn wood and ruled paper, deeper carbon blue, harder early light. Change no text." |
| S22 | No two libraries siblings | Pass | Unchanged | Pass | Unchanged |
| S23 | Claims and regulatory notes observed | Pass | Unchanged | Pass | Unchanged |
| S24 | Casting by context | Pass | Unchanged | Pass | Unchanged |
| S25 | Local language rendered and proofed | Pass | Step 5's rule for scripts other than Latin applied: short lines, own zones, Hangul gothic, native proof, live text fallback in the repair rules (was improvised) | Pass | Swahili first, Swahili proof |

**Pass count: Brief A 33 of 33 (first run 30). Brief B 33 of 33 (first run 31).**

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| Prompts are full standalone prompts | Pass | Pass | Script over 22 prompts: format line, asset contract, full style DNA with hex, own layout and copy, closing bar; none refers to another. |
| No hyphens and no em dashes in rendered slide copy | Pass | Pass | Script over every quoted block: 0 (first run: 3 in A, 2 in B). |
| No hyphens and no em dashes in the run's own text | Pass | Pass | 0. |
| No real brand names | Pass | Pass | Same 80 name script over both reruns and the pack: 0. |
| East Africa is a module, not the default, for Brief A | Pass | n/a | 0 East Africa terms in A. |
| Source copy reaches the slides | Pass | Pass | Fidelity script: every source line found verbatim or accounted for by a copy flag, a table split into cells or a paragraph split into lines. |
| No hyphens or em dashes in the pack's own copy | Pass | Pass | SKILL.md, TEMPLATE.md, east-africa.md and README.md: 0 in prose (first run: 58). File paths and the skill's own name are kept. |

## 3. Verdicts

**Brief A rerun: Yes.** A creative director would send this to the client as it stands. The council sees its own notice board and its own painted building numbers, with the pilot's 1,240 bottles at the scale of a building. The copy now meets the house style without losing a word of meaning, every change is listed with a way back, the Hangul is set up to be proofed and repaired line by line, and the rescue edit keeps the language clean instead of roughening it.

**Brief B rerun: Yes.** The margin table is right before anyone presents it, because the skill now checks sums. The palette is clearly marked as proposed with the real codes asked for, the government mark is held back until the real file exists, and the deck reads Swahili first with no dash in the rendered copy. The ideas are unchanged and strong: margin in the ledger, offer on the carbon invoice, the big idea painted over a Kariakoo lane.

## 4. Notes for the next pass (not defects)

* The pack has no HTML template, so each run builds its own library page. Step 6 now sets the quality bar (phone, light and dark, readable colours), and both pages meet it, but a shipped template, as the Key Visual Builder has, would make every buyer's page look as good as these.
* Not yet tested: a right to left script deck, a deck supplied as a file with real tracked changes, and a rework of rejected prompts. Worth a brief each in the next round.
* `python3 scripts/build_products.py` was not run here, as this pass was limited to the pack and its test folder; rebuild the zip before release.
