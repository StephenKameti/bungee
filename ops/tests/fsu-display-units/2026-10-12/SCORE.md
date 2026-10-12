# Retail Display Theatre: test score, 12 October 2026

Skill tested: `products/skills/fsu-display-units/skill/` as shipped (SKILL.md, device library, worked examples, market TEMPLATE, East Africa module), sold as Retail Display Theatre. Two invented briefs, run once each exactly as SKILL.md instructs, as if sent in one message. SKILL.md specifies Markdown prompts only, no HTML.

| Run | File | Market | Register | Prompts | Tiers |
|---|---|---|---|---|---|
| Brief A, Kalinowa craft mead | `brief-a.md` | Warsaw (no module, researched) | Craft premium | 9: 2 floor, 3 medium, 2 counter, 1 tray, 1 context shot | All four |
| Brief B, Mhogo Kali cassava crisps | `brief-b.md` | Dar es Salaam (East Africa module) | Playful mass market | 8: 2 floor, 2 medium, 3 counter or duka, 1 context shot | No smallest tier |

How the checks were made: rule checks were scripted over every prompt (the lines that open with a quote marker), the deliverable text from section 1 down, and every file in the pack. Per prompt the script checks the opening frame, all five hex codes, the text lockdown, the pack fidelity block, the casting clause, dimensions, a lens line, a brightest object line, the lighting clause, and any abbreviation such as "same as above". Pass means the output meets the promise. Where it only passes because the run went beyond what the skill tells it to do, the evidence says so and points to the fix.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | Premium prompts for FSUs, gondolas, counter units, glorifiers and in store theatre | Pass | Floor monolith, floor replica, cabinet, gondola end, wall bay, counter glorifier, till unit, tray | Pass | Floor units, gondola end, petrol station wall, duka hanger, duka counter, till unit |
| R2 | Any retail environment in any market | Pass | Specialist alcohol shops and supermarket halls in Warsaw; no East Africa term anywhere in A | Pass | Supermarkets, petrol station shops and dukas in Dar es Salaam |
| R3 | One theatrical device per unit | Pass | One device each; A7 repeats the A1 sun as a whisper, read from a contradiction in Step 2 (fix 3) | Fail | B3 Heat Ladder (narrative) also carries sculpted chilli forms rising on rods: a second idea |
| R4 | A family that shares one material language | Pass | Smoked oak, amber glass, Linden Green inlay on all nine | Pass | Red gloss, yellow inner line, a crisp in the silhouette on all eight |
| R5 | Clean plates, type added in post | Pass | Every panel and price strip blank; lockdown had to be rewritten to let real labels render (fix 2) | Pass | Same; price plates blank |
| R6 | Builds casting, places and language from the market | Pass | Warsaw winter coats by moment; Mokotów and Żoliborz shops; Polish strength names on labels | Pass | Kanga and work shirt by moment; Sinza, Mwenge, Masaki; Swahili first noted |
| R7 | Builds prices from the market | Fail | SKILL.md never mentions price; the run invented złoty plus price per litre strips | Fail | Price is the duka message in the brief; the run invented the TSh price plate |
| R8 | Builds channels and cultural dates | Pass | Specialist versus supermarket; Andrzejki, Mikołajki, Wigilia | Pass | Supermarket, forecourt, duka; Saba Saba, Nane Nane, Ramadan |
| R9 | Make a market permanent by filling TEMPLATE.md | Fail | TEMPLATE's language section "defers to the matching key visual market module", a file this pack does not contain | Fail | Same file |
| R10 | East Africa module as a worked example | Pass | Correctly not loaded for Warsaw | Fail | Module's places, light and retail notes are Kenya only and it points to another pack for worked lines; Dar es Salaam came from research SKILL.md did not ask for |
| R11 | Prompts tuned for leading models, adapt to others | Pass | Tools named generically | Pass | Same |

Not testable in a one pass run: install, "push back and it reworks", "attach whatever you have".

### From SKILL.md (step rules)

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market confirmed, module loaded or researched first | Pass | Market layer table before any prompt | Pass | Module loaded; gap researched beyond the instruction (fix 7) |
| S2 | Seven brand inputs collected | Pass | Materials proposed; the skill has no rule for a one message brief (fix 8) | Pass | Same |
| S3 | Palette in hex with a loudness rule per colour | Pass | All five with rules | Pass | All five with rules |
| S4 | One register phrase | Pass | Craft premium, wine cellar confidence | Pass | Playful mass market energy |
| S5 | Four to six materials plus banned list | Pass | Six and seven banned | Pass | Six and six banned |
| S6 | Pack shots required, fidelity block when packs show | Pass | Every prompt | Pass | Every prompt |
| S7 | Campaign device asked for and built | Pass | Lato w butelce as the amber sun (A1, A7) and the kept July block (A8) | Pass | The crunch as the snap (B1, B5) |
| S8 | Casting explicit in every prompt, by context | Pass | Scripted: 9 of 9 | Pass | Scripted: 8 of 8; no children in frame |
| S9 | Exactly one device per unit | Pass | As R3 | Fail | As R3 |
| S10 | No device repeated across the family | Pass | Only the A7 whisper, which Step 2 both forbids and asks for (fix 3) | Pass | Only the B5 whisper (fix 3) |
| S11 | Device matched to size | Pass | Replica only at 200 cm | Pass | Replica only at 180 cm |
| S12 | Descending family across all four tiers | Pass | Floor, medium, counter, tray | Fail | No smallest tier; the duka formats are filed as counter units because Step 3 has no tier for small trade (fix 4) |
| S13 | Six to nine prompts | Pass | 9 | Pass | 8 |
| S14 | One paragraph, four blocks in order | Pass | Scripted | Pass | Scripted |
| S15 | Preamble identical across the family | Pass | Identical except A2 (no wordmark clause; the replica's label carries it). The skill allows no change (fix 1) | Pass | Identical except B2 (wordmark) and the unlit duka units (lighting clause). Same note |
| S16 | Text lockdown in every prompt | Pass | Scripted: 9 of 9 | Pass | Scripted: 8 of 8 |
| S17 | Block 3: dimensions, device, wordmark once, blank panel, facing | Pass | Every unit | Pass | Every unit |
| S18 | Block 4: setting, believable figure, lens, aperture, brightest object | Pass | Scripted | Pass | Scripted |
| S19 | Tool, aspect, attachments and why on every prompt | Pass | Every prompt; logo file attached by the run, not by the skill (fix 2) | Pass | Same |
| S20 | Why line is commercial, not visual | Pass | Every line names a door, a shopper moment or a sale | Pass | Same |
| S21 | Generation order, hero first | Pass | A1 first, its render attached to A7 and A9 | Pass | B1 first, its render attached to B5 |
| S22 | Production honesty flags that apply | Pass | Hero tier, accepted unit, power, rigging, restocking | Pass | Same plus duka weathering |
| S23 | Restrained variant for a conservative register | Pass | Not triggered (craft premium) | Pass | Not triggered (playful) |
| S24 | Never a generic international retail look | Pass | Corner shop window onto wet Warsaw street; excise strip on every bottle | Pass | Grille window duka, forecourt, red earth verge |

### The pack itself and the standing rules

| # | Check | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| P1 | No hyphens or em dashes in the pack's own copy | Fail | 16 hyphenated words across SKILL.md and references, including the title "FSU-Display Units" | Fail | Same pack |
| P2 | No real brand names in the pack | Pass | Script for about 100 names: 0 hits | Pass | Same |
| P3 | Worked examples teach full standalone prompts | Fail | Example 2 is "[Same preamble and pack fidelity blocks as Example 1.]" plus 148 words; Step 4 says to write the preamble "once as a constant" (fix 1) | Fail | Same pack |
| P4 | Pack is self contained | Fail | Two pointers to "the key visual builder skill", which a buyer of this pack may not own (fixes 5 and 7) | Fail | Same |
| P5 | Regulated category flagged | Fail | Alcohol in Poland: the skill has no category flag; the run added one, and it could remove the supermarket units entirely (fix 6) | Pass | Not regulated beyond labelling |
| P6 | East Africa is a module, never the default | Pass | Not loaded for Warsaw; no East Africa term in A | Pass | Loaded only because the brief names Dar es Salaam |

**Pass count: Brief A 35 of 41. Brief B 32 of 41.**

A fails: R7 prices, R9 template, P1 hyphens, P3 examples, P4 self contained, P5 category rules. B fails: R3 and S9 one device, R7 prices, R9 template, R10 module, S12 smallest tier, P1, P3, P4.

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| No hyphens and no em dashes in the deliverable | Pass | Pass | Script over the text from section 1 down: 0 hyphenated words, 0 em dashes, 0 en dashes. The only hyphens in the files are file paths in the test header |
| No hyphens in the pack | Fail | Fail | Script over README, SKILL.md and every reference: 16 hyphenated words outside file paths |
| No real brand names | Pass | Pass | Script for about 100 retail, drinks, snack, beauty, fuel, telecom, payment, image model and platform names over both outputs and every pack file: 0 hits. Chains described generically; every other product in context shots is unbranded |
| Every prompt fully standalone | Pass | Pass | All 17 open with the frame and carry all five hex codes, materials, banned list, casting, lockdown, pack block, unit, scene and lens. 0 abbreviations. 438 to 487 words each |
| Worked examples standalone | Fail | Fail | Same script over `example-prompts.md`: Example 2 fails 7 of 10 checks (no frame, no hex, no lockdown, no pack block, no casting, abbreviation) |
| East Africa is a module, not the default, for Brief A | Pass | n/a | Script for Swahili, Sheng, Nairobi, Kenya, duka, shilling, TSh and similar: 0 hits in A |

## 3. Verdicts

**Brief A: Yes.** A creative director would send this. Nine units, nine ideas in one oak and amber uniform, and the hero sun is exactly the right device for a shop that is dark by four. The local truth is specific: the excise strip over every closure, the strength names taught as colour on Three Strengths, a two line price strip for the price per litre. It passes only because the run went beyond the skill twice: it added the alcohol law flag, which decides whether the supermarket units exist at all, and it invented the Polish price format. The skill must carry both.

**Brief B: No.** Three things stop it. Heat Ladder carries two ideas (the step ramp and the sculpted chillies), the exact failure the skill warns playful brands about. Three hundred dukas are the volume of this brief and the skill's size ladder has no tier for them, so the duka formats arrive filed as counter units and the family has no smallest tier. And the module is Kenya only: the Dar es Salaam grille window, the power cuts and Swahili first came from research the skill never asked for, while the module points the buyer to a pack they may not own. The units themselves (The Snap, Grille Snap, The Throne) are strong.

## 4. Fix list for the skill files

Ordered by buyer impact. Replacements avoid hyphens so they ship as written.

1. **SKILL.md Step 4 and example-prompts.md: preamble taught as a shared constant.** Step 4 said "identical across the whole family; write it once as a constant". Replace with: "the same text across the whole family; write it once, then paste it in full at the start of every prompt. Never abbreviate it or write "same preamble as above": every prompt must work pasted on its own. Change a clause only when a unit cannot carry it, for example the wordmark clause on a replica whose own label carries the logo". Write Example 2 out in full and add a note that it is pasted again.
2. **SKILL.md Step 1, Step 4 and Step 5: the lockdown forbids the labels the pack block demands, and the wordmark is typed by the generator.** Lockdown now: "the wordmark only where specified, reproduced from the attached logo file; the real pack labels reproduced from the pack shots; apart from those, every printed panel, price strip and shelf talker completely blank... With no logo file, leave the wordmark panel blank too." Step 1 item 4 asks for the logo file; Step 5 attachments list it. Example 1 and 2 aligned.
3. **SKILL.md Step 2: "do not repeat a device" against "the counter unit is the same idea whispered".** Now: one permitted repeat, a counter or tray miniature of the floor hero's device; context shots show an approved unit and carry no new device; other counter units carry their own device in the same uniform.
4. **SKILL.md Step 3: no tier for small trade.** Added: where trade runs through kiosks, dukas, warungs, bodegas or other small independents, the smallest tier is their own rugged format (clip strip, grille or shelf hanger, counter dispenser), unpowered, built for sun, dust and weeks between visits.
5. **SKILL.md Step 1: no price rule, so the README's "prices" promise was untrue.** Added item 8, Price and currency: never rendered; a blank plate or strip sized for the market's currency and price format, including any legally required unit price; a marked placeholder such as TSh XXX.
6. **SKILL.md Step 5: no category regulation flag.** Added: alcohol, tobacco and nicotine, medicines, infant formula and some foods carry market specific promotion and display rules; name them and send the client to legal before any unit is priced.
7. **SKILL.md market layer and east-africa.md: a regional module written from one capital.** Market layer now says to research the gap when a module does not cover the named country or city. Module gains an Outside Kenya note (Dar es Salaam: grille window shops, power cuts, Swahili first; Kampala: kiosks and arcade shops, English and Luganda) and loses its pointer to another pack.
8. **SKILL.md Step 1 and Step 5: a one message brief stalls on questions.** Added: propose missing inputs as marked assumptions, proceed, and end with What is missing (assumptions, attachments, price or legal sign off).
9. **All pack files: hyphens in the pack's own copy, and a pointer to another pack.** Title renamed "Retail Display Theatre" to match the product. 16 hyphenated words rewritten (in store, eye catching, exact reproduction, not negotiable, burned in, flat pack, medium to high, walk up, full length, left to right, one device and others). TEMPLATE.md's language section no longer defers to a key visual module.

README.md needed no change: with fix 5 its "prices" promise is now true.
