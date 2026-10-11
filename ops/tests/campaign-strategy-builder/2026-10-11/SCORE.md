# Campaign Strategy Builder: test score, 11 Oct 2026

**Skill tested:** `products/skills/campaign-strategy-builder/` at commit `34d1c90` (SKILL.md, references/motion-brief.md, references/markets/east-africa.md, references/markets/TEMPLATE.md, README.md).

**How the runs were made:** each brief was treated as the user's whole first message and run through SKILL.md in order: market layer, Step 1 inputs, Step 2 classification, Sections 1 to 9, then the Output Format appendices (deck conversion note, motion briefs after the sign off). No user was available to answer follow ups, so the inputs the skill would have asked for (author name, licence, claims list, brand palette, window for B) were carried as an "Assumptions to confirm" box on each title page.

* **Brief A (Mexico City):** no `references/markets/mexico.md` exists, so per SKILL.md L15 the local layer was built from the brief plus desk research: the IMSS platform worker pilot figures ([Xataka México, 16 Jan 2026](https://www.xataka.com.mx/legislacion-y-derechos/nueva-ley-para-uber-didi-rappi-no-freno-trabajo-206-mil-repartidores-tienen-imss)) and the rule that e-money institutions may not open savings accounts or promise returns ([IDC Online on CONDUSEF, Aug 2022](https://idconline.mx/corporativo/2022/08/25/fintech-no-pueden-ofrecer-ahorros-creditos-y-rendimientos-condusef)).
* **Brief B (Nairobi and Dar es Salaam):** `east-africa.md` loaded. Kenya's 2027 election dates checked ([The Star, 24 Jun 2026](https://www.the-star.co.ke/news/2026-06-24-iebc-unveils-key-dates-ahead-of-2027-general-election/)): poll 10 Aug 2027, campaign period from 29 May 2027.

**Outputs:** `brief-a.md` (about 8,000 words, 4 territories, 3 motion briefs) and `brief-b.md` (about 7,500 words, 3 territories, 2 motion briefs). The skill asks for no other files.

**QA corrections made during the run (logged for honesty):** both INSIGHT blocks and two Brief A territory ideas first ran to 4 sentences against the skill's 2 to 3; tightened. Brief B first used "bajaji", the Tanzanian everyday word for a three wheeler, which comes from a manufacturer's trademark; replaced with "three wheeler taxi". Brief B's own brief names a messaging platform; the run renders it generically throughout.

## 1. Promises and rules

P = Pass, F = Fail. "Desk" means checked against the skill files because a single run cannot exercise it.

| # | Source | Promise or rule | A | B | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | README L3, L22 | Board ready strategy for any market | P | P | Mexico built with no module; Kenya and Tanzania built from the module with separate city lines |
| 2 | README L3 | Situation analysis | P | P | Section 1 in both, four paragraphs |
| 3 | README L3 | Audience | P | P | Three tiers in both; B adds suppliers as a directly reached Tier 2 |
| 4 | README L3 | Insight | P | P | "Saving waits for a normal day..." / "My name is my real capital..." |
| 5 | README L3 | Platform | P | P | El Día Bueno + Lo que guardas, te guarda / Jina Ni Mtaji + Jina jema hung'aa gizani |
| 6 | README L3 | Creative territories | P | P | A: 4 territories; B: 3 |
| 7 | README L3 | Copy suites with local language adaptation | P | P | A: Spanish master plus Mexico City street register; B: Swahili, English, Sheng and Dar street variants |
| 8 | README L3 | Channel map | P | P | Every opened channel mapped with role, tier, message, spec, timing, KPI |
| 9 | README L3 | Executions with motion briefs for the hero films | P | P | A: 4 heroes, 3 motion briefs; B: 4 heroes, 2 motion briefs |
| 10 | README L3 | Senior planner standard | P | P | Each Section 1 reframes the brief (A: USD 8 per saver; B: the lever is a supplier number) |
| 11 | README L22 | Market builds casting, places, language, channels, prices, cultural dates | P | P | Named streets and markets, MXN, KSh and TSh amounts, dated 2027 moments in both |
| 12 | README L22 | Permanent markets via TEMPLATE saved as `<your-market>.md` | P | P | A fell back to research correctly; B found `east-africa.md` only because L17 names it, not via the L15 lookup (Fix 7) |
| 13 | README L16 | Try it: motion brief for the 30 second hero film | P | P | Both 30 s films briefed as 15 bars at 120 BPM, end frame on 14.1 |
| 14 | README L18 | Try it: insight and three territories | P | P | Section 3 plus 3 to 4 territories in both |
| 15 | README L19 | Try it: turn a research deck into a creative brief | F | F | Desk: SKILL.md has no creative brief format, only the 9 section document (Fix 8) |
| 16 | README L25 | Attach brief, deck, logo, pack shots; the skill reads them | P | P | Desk: Step 1 L29 "Read everything provided before asking" |
| 17 | README L26 | Push back and it reworks rather than restarts | F | F | Desk: SKILL.md has no revision instruction; behaviour rests on the model, not the skill (Fix 10) |
| 18 | README L27 | Image prompts tuned for leading image models | F | F | Desk: the skill makes no image prompts; neither run contains one (Fix 9) |
| 19 | README L13 | Switches on by itself when the request matches | P | P | Desk: description covers briefs "uploaded" with campaign development as the goal; bare pasted briefs like these are the weakest case (Fix 14) |
| 20 | SKILL L9 to 13 | Market established first; ask only if unstated | P | P | Market stated in both briefs; no question needed |
| 21 | SKILL L15, L17 | Load the module, or research when none exists | P | P | A: research with sources above; B: east-africa.md loaded |
| 22 | SKILL L11, L21 | Never a generic placeholder market | P | P | A: Álvaro Obregón, Viaducto, godínez, cuesta de enero; B: Marikiti, Mabibo, upatu, saa saba |
| 23 | SKILL L31 to 38 | Seven required inputs captured | P | P | All seven restated on each title page; B's window inferred and flagged |
| 24 | SKILL L43, L252 to 265 | Media mix and channel set fitted to the brief and market | P | P | A drops TV and radio; B drops TV and billboards and English radio |
| 25 | SKILL L51 to 62 | Campaign type classified before writing | P | P | A: Behaviour Change lead, Product Launch support; B: Behaviour Change |
| 26 | SKILL L23 | Nine sections in this order | P | P | Headings Section 1 to 9 in order in both files |
| 27 | SKILL L73 to 81 | Section 1: 4 paragraphs, no bullets, one new observation | P | P | Script check: 4 paragraphs, 0 bullets in each |
| 28 | SKILL L88 to 97 | Section 2: three tiers with context, media, trigger, relationship | P | P | All fields present per tier |
| 29 | SKILL L104 to 123 | Section 3: insight format, human tension, unlocks 10 executions | P | P | 3 sentence insight, bold one line, why; tension not a statistic |
| 30 | Test brief (not in SKILL.md) | Three insight options | F | F | SKILL.md Section 3 asks for one insight; the runs gave one, with no alternatives for the board (Fix 11) |
| 31 | SKILL L131 to 147 | Section 4: name, line, rationale 3 to 4 sentences, proposition, tone | P | P | Name 3 words each; rationale 4 sentences each; proposition in the set format |
| 32 | SKILL L152 to 176 | Section 5: 3 to 4 territories, full fields, distinct emotions | P | P | A: joy, relief, pride, wit; B: relief, laughter, pride |
| 33 | SKILL L42, L168, L185, L346 | Copy order: English or business language, then local adaptation, then youth | F | F | Rule clashes with "Spanish first" and "Swahili first"; in Mexico business and local language are the same; both runs broke the rule to obey the brief (Fix 1) |
| 34 | SKILL L192 to 198 | OOH: headline max 7 words, body max 10, lockup, local headline | P | P | A headlines 5 to 6 words, body 8; B headlines 3 to 5, body 9 |
| 35 | SKILL L201 to 209 | 30 second film structure, six fields | P | P | Written as the hero online film because neither brief opens TV |
| 36 | SKILL L212 to 217 | Radio 30 seconds: open, body, CTA, sign off | P | P | A: radio not opened, stated in the doc; B: two city spots |
| 37 | SKILL L220 to 226 | Social: five elements | P | P | All five in both, two city voice notes in B |
| 38 | SKILL L228 to 233 | Copy tone rules | P | P | No line opens with the brand; no "proud to"; Kenyan forms swapped for Tanzanian in Dar |
| 39 | SKILL L240 to 250 | Channel map: six fields per channel | P | P | Role, tier, message, spec, timing, KPI on every channel |
| 40 | SKILL L21 (no template) | Commercially grounded: budget split and funnel to the objective | P | P | Runner added budget tables, funnels and phasing; no SKILL.md template asks for them (Fix 2) |
| 41 | SKILL L271 to 281 | Section 8: 3 to 5 heroes with six fields, support list | P | P | 4 heroes each with complexity and award notes |
| 42 | SKILL L286 to 297 | Production mandatories with brand palette hex codes | F | F | No brand palette supplied and no fallback in the skill; both runs had to invent a "proposed" palette (Fix 4) |
| 43 | SKILL L304 to 322 | Section 9: 5 to 6 sentence paragraph, insight and line repeated, 4 next steps | P | P | 6 sentences each; 4 dated next steps |
| 44 | SKILL L330 | Title page: Brand, Campaign, Date, Prepared by | F | F | "Prepared by: [Agency or author name to confirm]": the skill says ask, with no fallback when unanswered (Fix 4) |
| 45 | SKILL L333 | Deck conversion note | P | P | A: 24 slides; B: 22 slides, mapped to sections |
| 46 | SKILL L284, L334 | Motion brief for every moving hero, after the sign off | P | P | Appendix B in both; cutdowns inherit the grid |
| 47 | motion-brief.md §1, §2, §6 | Anatomy in order, shot list columns, build first and check before final | P | P | All eight parts and the closing pair in every brief |
| 48 | motion-brief.md §3, §4 | 120 BPM grid, 15 bars for 30 s, downbeat end frame, hook in 2 s, readable holds | P | P | Every hold meets 0.3 s per word and 1.2 s minimum; changes every 1 to 2 s |
| 49 | SKILL L343 to 348 | Headings, no bullets in narrative sections, bold insight and line, implication per section | P | P | Script check: all 9 sections end on "For the creative team" |
| 50 | SKILL L367, L368 | No strategy speak; no stock casting | P | P | No "leverage", "holistic", "360 degree"; casting written by context |
| 51 | east-africa.md | Module guidance correct for the brief's markets | P | F | A: module rightly not loaded. B: module says English is the business language, wrong for Dar; its kanga rule bans real market work wear; run overrode both (Fixes 6, 13) |

## 2. Rule checks

| # | Check | A | B | Evidence |
| --- | --- | --- | --- | --- |
| 52 | No hyphens and no em dashes in client facing copy | P | P | Script scan: 0 em or en dashes; 0 hyphens outside markdown table delimiter rows (syntax, not copy) |
| 53 | No real brand names anywhere | P | P | Scan against a list of platforms, networks, retailers, banks and vehicle makers: 0 hits after the "bajaji" correction |
| 54 | East Africa a module, not the default, for Brief A | P | P | brief-a.md: 0 hits for Swahili, Sheng, Kenya, chama, matatu, shilling, mobile money; B uses the module with separate Nairobi and Dar lines |
| 55 | Claims stay within the mandatories | P | P | A: no ahorro, rendimiento, interés, tasa or garantizado in consumer copy; rewards routed to the approved list. B: no riba, faida, kukua, mkopo or kodi in any line; "mtaji" only as metaphor |

Judgement calls to put to each client's compliance team: in A, whether "te guarda" (it protects you) could be read as a deposit protection claim; in B, whether "Jina Ni Mtaji" (your name is capital) could be read as a financial claim. Both runs say neither is intended.

**Pass count:** Brief A 48 of 55. Brief B 47 of 55.

## 3. Verdicts

**Brief A: No.** The thinking is board grade: an insight that names the real blocker, a line that survives any licence, four distinct territories and a compliance led choice of verbs. It cannot go unchanged because the skill left it with a bracketed author placeholder and an invented palette, the copy layout breaks the skill's own language rule to honour "Spanish first", and the budget, funnel and phasing exist only because the runner added them; a strict run of this SKILL.md would have shipped no budget split against a USD 400,000 brief. Two working notes ("refresh before the board", "replace them with Fieldnote's own funnel data in week 2") also need removing. One hour of editing.

**Brief B: No.** Same placeholder and palette problems, and the same missing budget template. In addition the East Africa module's language rule (English as the business language) is wrong for Dar es Salaam, so the Tanzanian copy rests on the runner's own knowledge rather than the module the buyer paid for, and every Swahili and street line still needs the native speaker check that the module itself requires. The campaign idea, supplier led plan and radio scripts would survive a board; the document would not go out unchanged.

## 4. Fix list

1. **SKILL.md, copy language order.** L168 hard codes English first and L346 fixes the order, which breaks any "local language first" mandate and has no answer for markets where business and local language match.
   * L168 current: `COPY LINE(S): [1 to 3 lines. In English. Then local language adaptation. Youth or street register variant if youth-targeted, where the market has one.]`
   * Replace: `COPY LINE(S): [1 to 3 lines. In the master language: the brief's mandated first language, else the market's business language. Then the local language adaptation. Youth or street register variant if youth targeted, where the market has one.]`
   * L185 current: `CAMPAIGN LINE: [English or the market's business language]`. Replace: `CAMPAIGN LINE: [the master language, as set by the brief's language mandate]`
   * L346 current: ``- Copy lines always presented as: `Business language / Local language adaptation / Youth or street register (if applicable)` ``. Replace: ``- Copy lines always presented in the brief's mandated language order (for example Swahili first, English second); with no mandate, `Business language / Local language adaptation / Youth or street register (if applicable)`. Where the business and local language are the same, write the master natively, skip the adaptation, and add an English gloss when the reader needs one.``
   * Add to Inferred Defaults: `- **Document language**: the language the user writes in; consumer copy follows the brief's language mandate`

2. **SKILL.md, budget and objective maths.** No section turns the brief's budget and numeric objective into a split, a funnel or a timeline.
   * In the Section 7 format block, after `KPI: [What does success look like here]` add: `Budget: [amount and share of the total]`
   * After the channel set lists add: `Close the map with a budget table that sums to the brief's budget, a funnel from reach to the objective's number with the ratio assumed at each stage and the cost per objective unit, and a phasing plan across the campaign window with dated cultural moments.`
   * Quality Check, add: `- [ ] Budget table sums to the brief's budget and the funnel reaches the objective's number`

3. **SKILL.md, regulated claims.** Claims control is one checkbox at the very end (L294); both fintech briefs needed it from the first line of copy.
   * L36 current: `5. **Mandatories**, legal, regulatory, brand guidelines, claims restrictions`. Replace: `5. **Mandatories**, legal, regulatory, brand guidelines, claims restrictions. Before writing copy, turn them into a banned word list and an approved claims list in every language and register the copy will use (for example interest, returns, profit, loan, tax, or the word for savings where the licence forbids it), and route every rate, reward or protection claim to the approved list`
   * Quality Check, add: `- [ ] Every consumer line checked against the banned word list in every language and register used`

4. **SKILL.md, unanswered inputs.** The skill says "ask" but gives no fallback, so the title page and palette ship with placeholders.
   * L330 current: `Prepared by [Agency or author name, ask the user if unknown]`. Replace: `Prepared by [Agency or author name; ask once, in the same message as every other missing input]`
   * Under Required Inputs add: `If the user says to proceed without an answer, list each gap as a numbered line in an "Assumptions to confirm" box on the title page. Never leave bracketed placeholders or notes to self in the body.`
   * L290 current: `PALETTE: [Brand colours, hex codes]`. Replace: `PALETTE: [Brand colours, hex codes, from the client's guidelines. If none were supplied, propose a campaign palette, label it proposed, and name the category colours to avoid]`

5. **SKILL.md, channels the brief opens.** Section 6 writes TV, OOH, radio and social by default and L252 starts from a fixed FMCG set; in app, CRM, community and activation copy have no home.
   * Before `**OOH / Billboard:**` add: `Write copy only for the channels the brief opens. When TV is closed, write the 30 s structure as the hero online film. Channels with no block below (in app, CRM, messaging communities, activation signage) get the closest block and the same tone rules.`
   * L252 current: `**Standard channel set for FMCG, adjust to the market's actual media landscape from the market layer:**`. Replace: `**Channel set: use the channels the brief opens; with no list, start from this FMCG set and adjust to the market's actual media landscape:**`
   * Under "Adjust channel set for" add: `- Financial services and apps: add in app, CRM, referral, and agent or community networks`

6. **references/markets/east-africa.md, language.** Written for Kenya and wrong for Tanzania and Uganda.
   * Current (L18): `The dominant working language of business and advertising is English. The dominant local language for the local line is Swahili, often blended with Sheng,` and later `Regional note: Uganda and Tanzania are also Swahili speaking, but local slang and code switch differ from Kenyan Sheng, do not reuse a Kenyan line unchanged.`
   * Replace the first sentence pair with: `In Kenya the working language of business and advertising is English and the local line is Swahili, often blended with Sheng,` and the regional note with: `Regional note: in Tanzania Swahili is the working language of business, media and advertising and English is secondary, so the master line is Swahili; street register differs from Sheng (eti not ati, upo not uko, mshiko for money). In Uganda English leads and the local line in Kampala and the central region is Luganda, not Swahili. Never reuse a Kenyan line unchanged.`

7. **SKILL.md, module lookup.** L15 looks up `references/markets/<market>.md`, so a Kenya, Lagos or Kampala brief never finds a regional module by name.
   * L15 current: ``Once the market is known, look for `references/markets/<market>.md`.``. Replace: ``Once the market is known, look in `references/markets/` for the module whose `market` or `primary_reference` front matter covers it (for example `east-africa.md` covers Kenya, Uganda, Tanzania, Zambia and Rwanda). For a brief spanning two markets, write every local line separately for each.``

8. **SKILL.md, creative brief mode.** README L19 and the description promise a creative brief; SKILL.md has no format for one.
   * Under Output Format add: `### Creative brief (one page)` then `When the user asks for a creative brief: brand and objective; Tier 1 audience in two sentences; the one line brief insight; the proposition; campaign name and line; tone in three words; mandatories and banned claims; deliverables and channels; timing and budget. Sections 2 to 4 at full depth, everything else one line each.`

9. **README.md, image prompt promise.** The skill makes no image prompts.
   * L27 current: `* Image prompts are tuned for the leading image models and adapt to others with light edits.`. Replace: `* Motion briefs are tool agnostic: a motion designer, an editor or an image to video model can build from the same shot list.`

10. **SKILL.md, revisions.** README L26 promises rework on push back; nothing in SKILL.md backs it.
    * Under Output Format add: `### Revisions` then `When the user pushes back ("too safe", "too corporate", "more local"), keep the structure and every part not named, rework only what was named, and open with one line on what changed and why.`

11. **SKILL.md, insight options.** One insight with no alternatives gives a board nothing to choose between.
    * Under the Section 3 format block add: `Develop three candidate insights in this format, recommend one, and give one line on why each of the other two loses. Carry only the recommended insight into Sections 4 to 9.`

12. **SKILL.md, constraint flags.** Election periods and vehicle scenes are common blockers missing from the list.
    * After L293 `- [ ] No national flags / jerseys if a sports tournament applies` add: `- [ ] Election period: no party colours, candidate imagery or rally footage` and `- [ ] Vehicles: talent rides or drives legally (helmet on, no phone in hand while moving)`

13. **references/markets/east-africa.md, casting.** The kanga rule bans authentic market work wear.
    * L30 current: `kanga or kitenge patterned fabric only when the brief calls for a traditional or festive register, never as generic decoration`. Replace: `kanga or kitenge never as decoration; as everyday work wear it is accurate (a kanga tied as an apron at a market stall, a headwrap in Dar es Salaam and on the coast), so cast it as worn, not as styling`

14. **SKILL.md description, triggering.** A pasted brief with no verb relies on the word "uploaded".
    * Current: `or when a brief, deck or research document is uploaded and campaign development is the goal`. Replace: `or when a brief, deck or research document is uploaded or pasted (objective, budget, channels, mandatories) and campaign development is the goal`
