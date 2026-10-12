# Retail Display Theatre: rerun score, Briefs A and B, 12 October 2026

Skill tested: `products/skills/fsu-display-units/skill/` after the SCORE.md fix list (fixes 1 to 9 applied to SKILL.md, device-library.md, example-prompts.md, markets/TEMPLATE.md and markets/east-africa.md; README.md unchanged). Both briefs run once more, exactly as the updated SKILL.md instructs, as if sent in one message. Both are rerun because both had fails: A's came from the skill (price, category rules, the pack itself), B's from the skill and from the output.

| Run | File | Prompts | Tiers |
|---|---|---|---|
| Brief A rerun, Kalinowa mead, Warsaw | `brief-a-rerun.md` | 9: 2 floor, 3 medium, 2 counter, 1 tray, 1 context shot | All four |
| Brief B rerun, Mhogo Kali crisps, Dar es Salaam | `brief-b-rerun.md` | 8: 2 floor, 2 medium, 2 counter, 1 smallest tier (duka hanger), 1 context shot | All four |

How the checks were made: the same 41 checks as SCORE.md, with the same script over every prompt, the deliverable text and every pack file. Pass means the output meets the promise because the skill told it how, not because the run improvised.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | B | Evidence |
|---|---|---|---|---|
| R1 | Premium prompts for FSUs, gondolas, counter units, glorifiers and in store theatre | Pass | Pass | As the first run |
| R2 | Any retail environment in any market | Pass | Pass | Warsaw researched, no East Africa term in A; Dar es Salaam from the module plus researched gap |
| R3 | One theatrical device per unit | Pass | Pass | B3 is now the step ramp alone (was Fail); A7 and B5 are the one permitted whisper Step 2 now names |
| R4 | A family that shares one material language | Pass | Pass | Unchanged |
| R5 | Clean plates, type added in post | Pass | Pass | Every prompt carries the skill's new lockdown wording: wordmark from the logo file, real labels from the pack shots, everything else blank |
| R6 | Builds casting, places and language from the market | Pass | Pass | Unchanged |
| R7 | Builds prices from the market | Pass | Pass | Step 1 item 8: złoty strips sized for the price per litre, placeholder XX,XX zł; TSh plate on duka units, placeholder TSh XXX (was Fail) |
| R8 | Builds channels and cultural dates | Pass | Pass | Unchanged |
| R9 | Make a market permanent by filling TEMPLATE.md | Pass | Pass | TEMPLATE's language section now stands alone: language order, register, who checks the line (was Fail) |
| R10 | East Africa module as a worked example | Pass | Pass | A: correctly not loaded. B: the module's Outside Kenya note gives the Dar es Salaam grille window, power cuts and Swahili first; the market layer now asks for the rest of the gap to be researched; no pointer to another pack (was Fail) |
| R11 | Prompts tuned for leading models, adapt to others | Pass | Pass | Unchanged |

### From SKILL.md (step rules)

| # | Rule | A | B | Evidence |
|---|---|---|---|---|
| S1 | Market confirmed, module loaded or researched first | Pass | Pass | B researches the gap because the market layer now says to |
| S2 | Brand inputs collected | Pass | Pass | Materials proposed as a marked assumption and listed under What is missing, now as Step 1 says; price and logo file collected under the new items |
| S3 | Palette in hex with a loudness rule | Pass | Pass | Unchanged |
| S4 | One register phrase | Pass | Pass | Unchanged |
| S5 | Four to six materials plus banned list | Pass | Pass | Unchanged |
| S6 | Pack shots required, fidelity block | Pass | Pass | Scripted: 17 of 17 |
| S7 | Campaign device built | Pass | Pass | Unchanged |
| S8 | Casting explicit, by context | Pass | Pass | Scripted: 17 of 17 |
| S9 | Exactly one device per unit | Pass | Pass | B3 chillies removed (was Fail) |
| S10 | No device repeated except the permitted whisper | Pass | Pass | A7 whispers A1, B5 whispers B1; A9 and B8 carry no new device, as Step 2 now says |
| S11 | Device matched to size | Pass | Pass | Unchanged |
| S12 | Descending family across all four tiers | Pass | Pass | B5 Grille Snap is the smallest tier, the duka's own rugged format Step 3 now names (was Fail) |
| S13 | Six to nine prompts | Pass | Pass | 9 and 8 |
| S14 | One paragraph, four blocks in order | Pass | Pass | Scripted |
| S15 | Preamble the same text, pasted in full, changed only where a unit cannot carry a clause | Pass | Pass | A2 and B2 drop the wordmark clause (the case Step 4 now names); the unlit duka units drop the lighting clause |
| S16 | Text lockdown in every prompt | Pass | Pass | Scripted: 17 of 17, all in the skill's wording |
| S17 | Block 3 complete | Pass | Pass | Unchanged |
| S18 | Block 4 complete | Pass | Pass | Scripted |
| S19 | Tool, aspect, attachments and why | Pass | Pass | Logo file in the attachments, now as Step 5 lists it |
| S20 | Why line is commercial | Pass | Pass | Unchanged |
| S21 | Generation order, hero first | Pass | Pass | B order now ends with B5 after B1 is approved |
| S22 | Production honesty flags | Pass | Pass | Now including the category rules flag from Step 5 |
| S23 | Restrained variant for a conservative register | Pass | Pass | Not triggered |
| S24 | Never a generic international retail look | Pass | Pass | Unchanged |

### The pack itself and the standing rules

| # | Check | A | B | Evidence |
|---|---|---|---|---|
| P1 | No hyphens or em dashes in the pack's own copy | Pass | Pass | Script over README, SKILL.md and every reference: 0 hyphenated words outside file paths, 0 em dashes (was 16) |
| P2 | No real brand names in the pack | Pass | Pass | 0 hits |
| P3 | Worked examples teach full standalone prompts | Pass | Pass | Example 2 now 320 words and passes all 10 prompt checks (was 148 words, 7 fails) |
| P4 | Pack is self contained | Pass | Pass | 0 pointers to another pack |
| P5 | Regulated category flagged | Pass | Pass | A: the Polish alcohol flag now comes from Step 5's category rules line. B: the same line, answered for snacks |
| P6 | East Africa is a module, never the default | Pass | Pass | 0 East Africa terms in A |

**Pass count: Brief A 41 of 41 (first run 35). Brief B 41 of 41 (first run 32).**

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| No hyphens and no em dashes in the deliverable | Pass | Pass | 0 hyphenated words, 0 em dashes, 0 en dashes from section 1 down |
| No hyphens in the pack | Pass | Pass | 0 outside file paths |
| No real brand names | Pass | Pass | About 100 names over both reruns and every pack file: 0 hits |
| Every prompt fully standalone | Pass | Pass | 17 prompts, 423 to 488 words, each passing all 10 checks; 0 abbreviations |
| Worked examples standalone | Pass | Pass | Both examples pass all 10 checks |
| East Africa is a module, not the default, for Brief A | Pass | n/a | 0 hits |

## 3. Verdicts

**Brief A rerun: Yes.** A creative director would send this unchanged. The work is the same strong family, and the two things the first run had to invent now come from the skill: the alcohol law flag, which sends the client to legal before any supermarket unit is priced, and the złoty price strip with the price per litre.

**Brief B rerun: Yes.** A creative director would send this unchanged. Heat Ladder is now one idea. Three hundred dukas get their own tier, the grille hanger that whispers the hero's snap, built for sun and power cuts. The Dar es Salaam texture now has a starting point in the module and an instruction to research the rest. The price plate is in the skill. Every open item under What is missing is a client question, not a gap in the work.

## 4. Notes for the next pass (not defects)

* The East Africa module's Outside Kenya note is a starting point for two cities only. A filled Tanzania or Uganda module, written from a real brief, would give Dar es Salaam and Kampala the depth Nairobi has.
* The category rules flag names categories, not laws. That is right for a global pack, but a buyer in a regulated category should expect the flag to send them to legal, not answer for them.
* Prompts run 420 to 490 words because the preamble is pasted in full. That is the standing rule; if a generator truncates long prompts, the fix is a shorter preamble, never a shared one.
* Not testable here: rebuilding the sellable zip. Run `python3 scripts/build_products.py` once these files are committed.
