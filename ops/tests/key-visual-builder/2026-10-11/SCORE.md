# Key Visual Builder: test score, 11 October 2026

Skill tested: `products/skills/key-visual-builder/skill/` at commit d915ac5 (SKILL.md, all six reference files, the HTML template). Two invented briefs, run once each exactly as SKILL.md instructs, as if sent in one message.

| Run | Files | Routes | Prompts | Motion briefs |
|---|---|---|---|---|
| Brief A, Alba coffee sachets, Lisbon and Porto | `brief-a.md`, `brief-a.html` | 7 (2 safe, 3 strong, 2 wild) | 39: 7 masters, 4 variants, 28 reprompts | 3 (fire routes) |
| Brief B, Siku Bright laundry bar, Kenya and Uganda | `brief-b.md`, `brief-b.html` | 7 (2 safe, 3 strong, 2 wild) | 29: 7 masters, 1 variant, 21 reprompts | 0 (no moving channel) |

How the checks were made: rule checks were scripted over the rendered files (every prompt, all visible HTML text, the Markdown from section 1 down); the HTML was opened headless at 1280 px and 390 px. Pass means the output meets the promise. Where it only passes because the run went beyond what the skill tells it to do, the evidence says so and points to the fix.

## 1. Promises and acceptance rules

### From README.md

| # | Promise | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| R1 | 6 to 8 distinct routes | Pass | 7 routes on 7 different archetypes | Pass | 7 routes on 7 different archetypes |
| R2 | Works for any market | Pass | Portugal built from research; no East Africa term anywhere in A | Pass | Kenya and Uganda placed separately (Kayole, Umoja, Ntinda, Mukono) |
| R3 | A copy ready image prompt per route | Pass | 7 masters, 250 to 388 words each, pasteable as is | Pass | 7 masters, 242 to 404 words each |
| R4 | A full copy suite | Pass | 3 PT headlines with EN lines, subline, endline, proof, 2 CTAs, Lisbon and Porto lines per route | Pass | Same set in Swahili and English, plus a 15 s radio read per route |
| R5 | A channel adaptation kit | Pass | 7 formats per route, each called crop or reprompt | Pass | 9 formats per route, but radio and activation rows were invented by the run (fix 5) |
| R6 | A designer build sheet | Pass | 7 items per route with coordinates | Pass | 8 items per route; price plate added by the run (fix 4) |
| R7 | Motion brief when the campaign moves | Pass | 3 briefs on the beat grid for the fire routes | Pass | Correctly not triggered; flagged under What is missing |
| R8 | Interactive route book with copy buttons | Pass | 112 copy buttons, index builds itself | Pass | 109 copy buttons |
| R9 | With a market module, every route is cast, placed and worded for the market | Pass | No module; researched layer drives every prompt and line | Fail | Module calls Uganda Swahili speaking; Kampala routes carry Swahili and the only Luganda line is unverified (fix 8) |
| R10 | Builds casting, places, language, channels and cultural dates from the market | Pass | February first light, PT outdoor sizes, bica and cimbalino, clock change | Pass | January back to school, painted shop walls, market day, radio reach |
| R11 | Builds prices from the market | Fail | SKILL.md never mentions price; gondola end plates had no guidance | Fail | Price mandatory; the run invented the price plate and per market currency (fix 4) |
| R12 | Prompts tuned for leading models, adapt to others | Pass | Tools named generically; type route sent to a type model | Pass | Same; Siku Saba offered as a real drone shoot |

Not testable in a one pass run: "push back and it reworks", "attach whatever you have".

### From SKILL.md (quality check, standing rules and step rules)

| # | Rule | A | Evidence, A | B | Evidence, B |
|---|---|---|---|---|---|
| S1 | Market confirmed, module loaded or researched first | Pass | Sunrise tables, outdoor formats and city coffee words researched before any prompt | Pass | East Africa module loaded |
| S2 | KV spine shown back before prompts | Pass | Section 2 of brief-a.md | Pass | Section 2 of brief-b.md |
| S3 | At most three questions, only on axes that change the work | Pass | Format, palette, launch month, each with an assumption | Pass | Bar size, price, Uganda language |
| S4 | All five routing axes resolved | Pass | Routing table plus one held register | Pass | Same |
| S5 | Reference law table only if references | Pass | None supplied, correctly omitted | Pass | Same |
| S6 | Spread: two safe, three strong, one or more wild | Pass | 2, 3, 2 | Pass | 2, 3, 2 |
| S7 | No two routes in one sentence | Pass | 7 archetypes, 7 laws | Pass | 7 archetypes, 7 laws |
| S8 | Every route on rung three or four | Pass | 4 on rung four; One Window is the weakest rung three | Pass | 5 on rung four |
| S9 | Eight part card anatomy in order | Pass | Every route | Pass | Every route |
| S10 | Name of two or three words, idea in one sentence | Pass | Do Not Disturb is the longest name | Pass | Wednesday renamed By Wednesday to meet the rule |
| S11 | Hex on every colour, percent text zone, craft tags | Pass | Scripted over 39 prompts; 2 hex gaps fixed during the run | Pass | Scripted over 29 prompts; 4 hex gaps and 1 missing percent fixed during the run |
| S12 | Zero negative clauses, zero stacked casting | Pass | No negation words in any prompt | Pass | Same |
| S13 | Pack label face clean wherever the pack appears | Pass | Every sachet a smooth blank panel | Pass | Every wrapper a smooth blank panel |
| S14 | Brief mandates on every KV (pack; bilingual; price) | Pass | Pack in scene or on a clean plate in all 7; PT and EN on every headline | Pass | Pack in all 7; Swahili and English; price plate on all 7 (placeholder) |
| S15 | Copy suite complete with local line | Pass | Lisbon and Porto register lines | Pass | Kenya carried by the headline; Uganda line proposed and flagged |
| S16 | Three endlines when the brief has none | Pass | Written once for the set, each route pairs; SKILL.md asks per route (fix 3) | Pass | Same |
| S17 | No hyphens or em dashes in client copy | Pass | 0 in deliverable text; Portuguese written around hyphenated words (fix 9) | Pass | 0 |
| S18 | Claims flagged, never invented | Pass | Only format facts used; "sem máquina" flagged | Pass | Week claim and the comparison suspended pending a wear test |
| S19 | Kit marks every format crop or reprompt | Pass | Every row called | Pass | Every row called, plus Designer build and Script |
| S20 | Reprompts are full standalone prompts | Pass | 28 full prompts; template has no slot for them (fix 1) | Pass | 21 full prompts |
| S21 | Kit formats come from the skill's own tables | Fail | 8x3 m roadside and the bus shelter panel are missing (fix 6) | Fail | Radio and market activation are missing (fix 5) |
| S22 | Build sheet per route, all seven items | Pass | Every route | Pass | Every route |
| S23 | Motion brief: beat grid, readability law, logo on a downbeat | Pass | One card held 1.7 s for 1.8 s needed, fixed in the run | Pass | Not triggered |
| S24 | Fire three, disruptive alternate, what is missing | Pass | Section 8 and the close | Pass | Same |
| S25 | Single interactive HTML with copy buttons | Pass | brief-a.html | Pass | brief-b.html |
| S26 | Route book from the template works on a phone | Fail | Template as shipped is 758 px wide on a 390 px screen; patched in the run (fix 10) | Fail | Same |
| S27 | No readable text in images except type as terrain on a type model | Pass | Clear Glass routed, with a composite fallback | Pass | Siku Saba routed, or shot for real |
| S28 | Kill list avoided | Pass | Checked per route | Pass | Checked; no child in frame |
| S29 | Casting by context | Pass | Neighbourhood, moment and light | Pass | Same |
| S30 | Place, light and season named in every prompt | Pass | District, clock time and February in all 39 | Pass | District and January sun in all 29 |
| S31 | Variant pairs where the effect is optional | Pass | Porto variants for two routes; headline swaps for the type route | Pass | Uganda variant for Wash Day |
| S32 | Palette as hex, never left to the model | Pass | Proposed and labelled; the skill says nothing about an unsupplied palette (fix 4) | Pass | Same |

**Pass count: Brief A 41 of 44. Brief B 40 of 44.**

A fails: R11 prices, S21 kit tables, S26 template on a phone. B fails: R9 Uganda wording, R11 prices, S21 kit tables, S26 template on a phone.

## 2. Rule checks

| Check | A | B | How it was checked |
|---|---|---|---|
| No hyphens and no em dashes in client facing copy | Pass | Pass | Script over the Markdown from section 1 down and all visible HTML text: 0 hyphens, 0 em dashes, 0 en dashes. The only hyphens in the files are file paths in the test header and CSS. |
| No real brand names anywhere | Pass | Pass | Script for about 60 coffee, laundry, retail, platform, image model and agency names: 0 hits. Social platforms and image models are named generically. The only third party names are CSS font stacks inherited from the template, not visible copy. |
| Prompts are full standalone prompts | Pass | Pass | Every one of the 68 prompts carries its own framing with the ratio in words, subject, setting, light, palette lock with hex, pack treatment, percent text zone and craft tags. None says "as above" or depends on another. |
| East Africa is a module, not the default, for Brief A | Pass | n/a | The East Africa module was not loaded for A. Script for Swahili, Sheng, Nairobi, Kenya, matatu, shilling and similar: 0 hits in A. |

## 3. Verdicts

**Brief A: Yes.** A senior creative director would send this as the first route presentation. Seven genuinely different ideas with a real spread; three of them (Second Coffee, Long Shadow, Do Not Disturb) are ownable and could only be this brand. The local truth is specific rather than postcard (the shuttered café at 7:05, bica against cimbalino, enclosed balconies in Cedofeita, Atlantic mist over granite). The open items it lists (pack format, palette, launch month, a native read) are the right client questions, not defects. One Window is the weakest route and could be cut, but leaving it in does no harm.

**Brief B: No.** Three things stop it. Uganda is mishandled because the market module says Uganda is Swahili speaking: two routes are set in Kampala with Swahili headlines, and the only Luganda line is unverified, so a Kampala client would send it straight back. Radio is a named channel, and the skill has nothing for it; the radio reads are the run's own invention, with no format, length or station language. Price is mandatory, and the skill has no price discipline; the run had to invent the price plate, and the per day route depends on it. The creative is strong (The Line, Per Day and Siku Saba are good ideas), but the skill could not deliver this brief without improvising.

## 4. Fix list for the skill files

Ordered by buyer impact. Quotes are the current text; replacements avoid hyphens so they can ship as written.

1. **SKILL.md, Step 7 and Step 5: reprompts are left as change notes.** Current line 268: "For each route, give the reprompt or the crop instruction for every channel in the spine." Replace with: "For each route, give a crop instruction for every format marked Crop, and a full standalone prompt, built to the Step 5 architecture for that ratio, for every format marked Reprompt. Never write a reprompt as a change note against the master prompt; the user must be able to paste it on its own." Current line 217 ends "Offer both rather than choosing for the user." Append: "Write each variant as its own full prompt."

2. **SKILL.md, Step 6: headlines assume English, and the local line breaks when the market's own language is the working language.** Current line 247: "**Headline.** Three options, ranged. One straight, one warm, one that earns a smile". Replace with: "**Headline.** Three options, ranged. One straight, one warm, one that earns a smile. Write them in the language the market and the brief call for, never English by default. When the brief mandates two languages, every option carries both lines, and any line the reviewer may not read gets an English gloss". Current line 252 ends "say so and skip it rather than force one". Append: ". When the headlines are already in the local language, use this line for the street or city register instead, for example a second city's own word for the same habit, or say that the headline carries it".

3. **SKILL.md, Step 6: three endlines per route.** Current line 249: "**Endline or campaign line.** If the brief has one, use it verbatim and do not improve it. If it does not, give three". Replace the last sentence with: "If it does not, write three once for the whole set, ranged elegant, plain and shareable, show them with the spine, and have each route name the one it pairs with. Never write a different endline per route". Seven routes times three endlines is 21 candidate lines for a three year commitment.

4. **SKILL.md, Step 1 and Step 8: no budget, no price, no rule for a missing palette.** Current line 50: "| Palette | Hex values. Pull from a supplied logo, guideline, or packshot. Never leave colour to the model |". Replace with: "| Palette | Hex values. Pull from a supplied logo, guideline, or packshot. If none is supplied, propose four or five, mark them proposed, and list the real palette under What is missing. Never leave colour to the model |". After line 55 add: "| Budget | Low budgets get six routes, the minimum viable kit first, and routes that build from one plate or one cheap real shoot |" and "| Price and currency | Shelf price and currency per market, if price must show. Never invent one; use a marked placeholder such as KSh XX |". After line 298 add the build sheet item: "**Price plate.** When price is mandatory: position, size, currency per market, the recommended retail price line, and a placeholder until the client confirms the figure". This also makes the README's "prices" promise true.

5. **references/adaptation-kit.md, references/copy-craft.md, SKILL.md Step 7: radio and live activations do not exist.** In adaptation-kit.md, before "## 7. The minimum viable kit", add "## 7. Audio": "Radio is not a crop or a reprompt. Per route, write a 15 s script in the market's spoken language: the mechanism as a sound effect, the line said twice, the endline, the price said once, about 2.5 words a second. Note the station language; regional and vernacular stations often carry the reach." Then "## 8. Activation and sampling", a table with: gazebo or canopy valance (designer build, two colours, the endline), stall A board 2:3 (crop), demo backdrop or roll up 1:2.5 (reprompt, bottom 400 mm hidden by the table), promoter apron or shirt (designer build), bunting (one icon, nothing photographic), take home sampler card (designer build). Renumber the minimum viable kit to 9. In copy-craft.md section 5, after line 81 add: "| Radio | Said, never read. The mechanism as a sound, the line twice, the price once, 15 or 30 s |". In SKILL.md Step 7, after the "When the campaign moves" paragraph add: "**When the spine lists radio or live activations,** add them from references/adaptation-kit.md sections 7 and 8."

6. **references/adaptation-kit.md, section 3, and SKILL.md line 278: no street furniture format, one billboard size for the world.** After line 46 add: "| Street furniture 6 sheet (bus shelter, metro, mall) | about 2:3 portrait, 1185 x 1750 mm visible | Backlit, read on foot at 2 to 5 m. Usually a crop of the 4:5 master; lift the grade one stop for the lightbox |". Under the table add: "Standard sizes vary by market; confirm them with the media owner. 8x3 m is the roadside standard in some European markets; 12x3 m and 40x10 ft are common in parts of Africa and Asia." In SKILL.md line 278 change "| Billboard 6x3 | 2:1 |" to "| Billboard, the market's standard size (6x3 m is 2:1) | 2:1 or as specified |".

7. **SKILL.md, Market layer: no rule for briefs that span two markets or cities.** After line 15 add: "When the brief names two or more markets or cities, set each route in one named place and spread the set across them, give each fire immediately route a full variant prompt for the other place, and give the local line per market. Never let one market's casting, language or currency stand in for another's."

8. **references/markets/east-africa.md: Uganda language is wrong for household briefs.** Current line 53 begins: "Regional note: Uganda and Tanzania are also Swahili speaking, but local slang, emphasis and code switch differ from Kenyan Sheng. Do not reuse a Kenyan Sheng line unchanged for a Ugandan or Tanzanian brief." Replace those two sentences with: "Regional note: Tanzania is Swahili first, with its own slang and emphasis, so never reuse a Kenyan Sheng line unchanged. Uganda is different: English carries most advertising, and in Kampala and the central region Luganda is the everyday household language; Swahili is official but is not the home register for most Ugandan mothers. For a Ugandan household audience, propose a Luganda local line written or checked by a native writer, and flag a Swahili only mandate as a client decision." Current line 68: "Radio remains a strong reach medium outside major urban centres, relevant when a line needs to work read aloud, not just seen". Append: ", and much of it runs in local languages, Luganda across central Uganda among them".

9. **references/copy-craft.md line 9 and SKILL.md line 256: the hyphen rule collides with languages whose spelling needs one.** Current: "**No hyphens. No em dashes. Anywhere in client facing copy.** Rewrite the sentence". Append: ". Where a language's correct spelling needs a hyphen, such as the European Portuguese word for breakfast or a verb with an attached pronoun, rewrite around the word; never drop the hyphen and leave a misspelling". Add the same sentence to SKILL.md line 256.

10. **assets/kv-library-template.html: breaks on phones and has no home for half of what SKILL.md asks for.** (a) Phone overflow: add `.route>div,.grid>*{min-width:0}` and `.panel{overflow-x:auto}` to the stylesheet; without them the bare template is 758 px wide on a 390 px screen. (b) Adaptation rows: replace the five fixed rows (feed, story, video end frame, billboard, shelf talker) with one example row and the comment `<!-- one row per format in the spine; delete what the spine does not list -->`, and add `.call.build` and `.call.script` styles for Designer build and Script rows. (c) Reprompts: add a `<details>` block per Reprompt row holding a `.prompt` with its own copy button, so full reprompts have somewhere to live. (d) Endline options: add a wide block in "The brief, read back" for the three set level endlines. (e) Dark brand colours: line 97 `.btn.on-plate{background:var(--accent);...}` makes the copy button vanish on the dark prompt plate when the client primary is navy or black; change it to `.btn.on-plate{background:var(--plate-ink);color:var(--plate);border-color:transparent}`, and add an `--accent-dark` token used inside both dark mode blocks so route numbers stay readable. (f) Footer: SKILL.md Step 9 asks for tool routing in the footer; add a fifth paragraph after line 316 for it.

11. **SKILL.md line 315 and the template motion panel: the panel drops half the motion brief.** Current: "**Motion brief panel,** inside the route article, only for routes that have one: the spec line, the shot list table on the beat grid, the sound line and the poster frame." Replace with: "**Motion brief panel,** inside the route article, only for routes that have one: the film line, the spec line, the build route, the assets, the shot list table on the beat grid, the sound line, the text on screen, the lockup and poster frame, and the build first and check before final notes." Add a `<dl>` for those rows under the sound line in the template panel.

12. **SKILL.md line 57: questions stall a one message brief.** Current: "If nothing is missing, do not ask. Proceed." Append: "Give each question a working assumption. If the user wants the work now, or sent the brief as one message to run, proceed on the assumptions, mark them in the spine, and list them under What is missing."
