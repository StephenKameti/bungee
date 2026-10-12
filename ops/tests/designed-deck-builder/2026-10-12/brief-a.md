# Designed Deck Builder test, Brief A: Mulgyeol Refill partner deck, Seoul

Test record. Skill: `products/skills/designed-deck-builder/skill/` as shipped (SKILL.md, `references/markets/TEMPLATE.md`, `references/markets/east-africa.md`). Run once on 12 October 2026, exactly as SKILL.md instructs, as if a user had sent the brief and deck below in one message. Everything from section 1 down is the deliverable; the prompt library page built from it is saved beside this file as `brief-a.html`.

**Brief as sent:** Design our partner deck so it looks studio made, as image prompts for an image model that renders the copy. Brand: Mulgyeol Refill (물결 리필), a Seoul start up that installs refill stations for laundry, kitchen and bathroom liquids in apartment complexes. Audience: apartment residents' councils and management offices in Seoul. Colours: Deep Teal #0B4F4C, Foam #EEF4EF, Signal Coral #FF5A3C, Ink #1C1F1E. Logo: lowercase rounded wordmark "mulgyeol" with three short wave lines over the u, Korean name 물결 리필 beneath. I will attach the logo and a photo of the station. Deck copy below, with two comments from my team still in it.

**Source deck as sent (verbatim):**

1. Cover. 병은 그대로, 채우기만. / Keep the bottle. Refill the rest. / Apartment Partner Programme 2027 / 아파트 파트너 프로그램 2027
2. Problem. Our recycling bins are full of bottles we could have kept. / 분리수거함은 다시 쓸 수 있던 병으로 가득합니다. / Every week, Seoul households carry bags of empty detergent, shampoo and dish soap bottles to the recycling area, and most of those bottles were perfectly good containers that only needed refilling instead of being thrown away and replaced. / A family of four empties around 9 plastic bottles of cleaning and care products a month.
3. Meet Mulgyeol. A refill station that lives where you live. / 우리 단지 안의 리필 스테이션. / Six everyday refils. Pay by the gram. Open 24 hours in your complex's shared space. [Comment, Jiwoo Han: say "common area" not "shared space", boards use 공용공간]
4. How it works. Three steps — no new plastic. / 1 Bring any clean bottle / 빈 병을 가져오세요 / 2 Fill what you need / 필요한 만큼 채우세요 / 3 Pay by weight, tap your phone / 무게만큼 결제하세요
5. On tap. Six refills. Priced by the gram. / 여섯 가지 리필, 그램 단위 가격. / Laundry liquid 세탁세제 ₩380 / 100 g / Fabric softener 섬유유연제 ₩320 / 100 g / Dish soap 주방세제 ₩290 / 100 g / Shampoo 샴푸 ₩690 / 100 g / Body wash 바디워시 ₩590 / 100 g / Multi surface cleaner 다용도 세정제 ₩260 / 100 g / Prices include VAT.
6. Pilot results. Pilot complex, Mapo District, 412 housholds, 90 days / 1,240 bottles kept out of the bin / 68% of households refilled twice or more / ₩4,100 average saving per household per month [Comment, Minseo Oh: lead with the bottles number, it's the one boards remember]
7. What your complex gets. 단지에 돌아가는 혜택 / Station and install: Free, fitted in one day / Management fee credit: 3% of station sales, credited monthly / Recycling report: Monthly, bottles and kilograms kept out of the bin / Upkeep: Cleaned and restocked twice a week / Lobby poster: A zero-waste corner residents can see / Contract: 12 months, cancel with 30 days notice
8. Timeline. From vote to first refill in 6 weeks. / 결정부터 첫 리필까지 6주. / Week 1 Council vote / Week 2 Site visit / Week 4 Install / Week 6 Launch day
9. Resident. "I stopped buying bottles in March. My recycling bag got lighter, and so did my bills." — Ms Park, Building 102, pilot complex
10. Big idea. The cleanest bottle is the one you already own. / 가장 깨끗한 병은, 이미 가진 병입니다.
11. Close. Let's fill your complex first. / 함께 채워요. / partners@mulgyeol.example

**Where the run had to interpret the skill** (scored in SCORE.md):

* The two team comments. SKILL.md says nothing about comments in a source deck; Step 1 only extracts slide text. The README promises "comments actioned before design starts", so the run actioned both and listed them with the copy flags. A run that followed Step 1 to the letter could render the comment text on the slide.
* Hyphen and em dash in the client's copy. "zero-waste" (slide 7) and the dashes on slides 4 and 9 are not broken lines, so Step 1 keeps them word for word. They are rendered as sent. SKILL.md has no rule for them.
* Korean copy. No Korea module exists and SKILL.md gives no rule for a non Latin script, so the Hangul handling below (short lines, own zone, native proof) is the run's own.
* Production questions. Step 4 asks one round and has no unattended path; Step 3 does. The run applied Step 3's unattended rule to Step 4 and proceeded on the defaults.
* Brand research. The brand is invented and the brief supplies the palette and logo, so Step 2 is built from the brief.
* Typography consistency. Step 5 asks for "2 to 3 sentences of this deck's language" per prompt but not that they repeat word for word. The run wrote one style DNA per mood and pasted it verbatim into every prompt.

---

## 1. Market layer

| Area | What the market layer sets |
|---|---|
| Market | Seoul, South Korea. Home market and audience market are the same: residents' councils (입주자대표회의) and management offices (관리사무소) of Seoul apartment complexes. No `references/markets/` file exists for Korea, so this layer is built from research into Seoul's visual culture, retail and rules. |
| Visual vernacular | The apartment complex (단지) is the world of this deck. Its own graphic language: building numbers painted huge on the white gable ends of every block; the brushed steel notice board in each lift lobby, with A4 notices held by round magnets and stamped by the management office; colour coded recycling cages in the car park on the complex's weekly sorting evening; clear volume based waste bags. |
| Retail and payment | Card and phone tap payment are standard at every till; a refill station paid by phone tap fits the habit. Prices in won with VAT included, written ₩380 style. |
| Typography | Hangul sets as square syllable blocks and reads well in a bold clean gothic (sans) with a little extra spacing. Condensing Hangul hurts it; keep Korean lines in a normal width gothic and let Latin carry any condensed or rounded display behaviour. Pair the two at matched cap and syllable height. |
| Hangul in image models | Image models render Hangul less reliably than Latin. Every Korean line stays short (under about 12 syllables where the copy allows), sits in its own zone so it can be repaired alone, and gets a native proofread on every render. |
| Casting and light | By context: a woman in her fifties with a neat silver bob and a grey cardigan in the lift lobby of building 102 at late morning. The deck is pitched in late autumn: ginkgo leaves bright yellow on complex paths, blue hour arriving before 18:00, cool clear air. |
| Regulatory | Environmental claims ("zero waste", "eco friendly", plastic saved) fall under Korea's environmental labelling and advertising rules, which have been tightened against greenwashing. Any number or green claim on a slide needs a source line or softer wording before the deck goes to a council. |

## 2. Copy flags

Every change below is already applied in the prompts. Revert any of them by editing the quoted text in that slide's prompt.

| Slide | As sent | In the prompts | Why |
|---|---|---|---|
| 03 | "Six everyday refils." | "Six everyday refills." | Typo. |
| 03 | "Open 24 hours in your complex's shared space." | "Open 24 hours in your complex's common area." | Comment from Jiwoo Han actioned; the comment text is removed from the slide. |
| 06 | "412 housholds" | "412 households" | Typo; it also appears beside a number, so a council would notice. |
| 06 | Comment from Minseo Oh | Bottles number is the hero | Comment actioned; the comment text is removed from the slide. |

**Claims to clear before the deck is presented:**

* Slide 02: "A family of four empties around 9 plastic bottles of cleaning and care products a month." Needs a source line. Rendered as sent.
* Slide 06: all three pilot figures need the pilot report behind them. Rendered as sent.
* Slide 07: "A zero-waste corner residents can see." An environmental claim under Korea's labelling rules. Rendered as sent.

## 3. Brand Sheet

| Item | What the prompts use |
|---|---|
| Colours | Deep Teal #0B4F4C (primary), Foam #EEF4EF (ground), Signal Coral #FF5A3C (accent), Ink #1C1F1E (text). All from the brief; no conflict. |
| Logo | Lowercase rounded wordmark "mulgyeol" with three short wave lines over the u, Korean name 물결 리필 beneath. Image 1 in every prompt, placed as provided, never redrawn. |
| Product | The refill station: a tall white steel cabinet with a Deep Teal front panel, six stainless nozzles in a row, a weighing plate and a small screen. Image 2 in every prompt that shows it. Residents bring their own bottles, so no branded bottle is shown. |
| Typography | Brand face not supplied. Described in image language: a heavy rounded geometric sans for Latin, a bold clean Hangul gothic with generous spacing for Korean, regular weights of the same families for body. |
| Brand world | Start up, practical, neighbourly. Category convention for refill and green brands: leaves, kraft paper, hand lettering, soft greens. That is the code worth breaking. |

## 4. Design language

Three languages were considered. Working unattended, the run picks the strongest and states it here.

| Language | One sentence |
|---|---|
| **Danji Bulletin** (picked) | The deck lives on the apartment complex's own media: A4 notices on the lift lobby's steel board for the argument, and the giant painted building numbers on the gable walls for the big moments. |
| Euljiro Proof | Risograph proofs from Seoul's old print alleys, misregistered teal and coral, crop marks and colour bars, every slide a press check. |
| Rinse Cycle | Hyper clean macro photography of liquid falling from stainless nozzles, the copy floating in the pour. |

**Why Danji Bulletin.** The audience is a residents' council. The notice board is the medium they already trust and read every day, and the painted block number is the most Seoul thing on any complex. Every refill deck in the category is leaves and kraft paper; this one looks like the building itself is talking. Euljiro Proof is beautiful but speaks to designers, not councils. Rinse Cycle is the category's own cliché with better lighting.

**Devices:** steel notice board and A4 sheets held by round magnets (structure); flat daylight documentary photography with fine film grain (photo treatment); heavy rounded Latin sans with a bold Hangul gothic (type behaviour); giant gable numerals carrying the deck's big numbers (structure, loud mode); one Signal Coral round stamp reading "채움" (fill) per slide, the only accent.

**Two moods:**

* **Notice** (quiet, content slides 02, 03, 04, 05, 07, 08, 09): the lift lobby notice board.
* **Gable** (loud, slides 01, 06, 10, 11): the complex itself at blue hour, full bleed photography, painted numerals.

**Content through medium:** prices as the label strip on the station's six nozzles (05); the partner table as an official management office notice with ruled rows (07); the timeline as a lift button panel where the floors are weeks (08); the pilot's bottle count painted as a building number on a gable wall (06).

## 5. Production questions

Asked as one round; working unattended, the run proceeds on the defaults.

| Question | Default used |
|---|---|
| Target image model | The image model with the strongest text rendering and the best preservation of attached brand assets. |
| Copy handling | Verbatim everything, with the copy flags in section 2. The 38 word body on slide 02 is broken into three stacked lines, word for word. |
| Pure table slide (07) | Rendered in image as an official notice: six short rows. |
| Aspect | 16:9. |

## 6. Prompt library

**Attach these every time:** Image 1, the Mulgyeol Refill logo file. Image 2, the photo of the refill station. After the cover is approved, Image 3, the approved cover render, and add this line to every later prompt: "Image 3 is the approved style reference; match its design system."

### Act 1: The problem and the answer

#### 01 Cover [Gable]

Rationale: the complex is the hero, and the year sits where a building number would, so the council sees their own buildings before they read a word.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo and Image 2 is the Mulgyeol refill station. Place both exactly as provided, never redrawn.

Style: Danji Bulletin, Gable mood. A full bleed documentary photograph of a Seoul apartment complex at blue hour in late November, white fifteen storey blocks, lit windows, ginkgo leaves bright yellow on the paths, a cool clean grade with fine film grain. Type is a heavy rounded geometric sans for Latin and a bold clean Hangul gothic with generous spacing for Korean, set in Foam #EEF4EF or Deep Teal #0B4F4C, the same two families on every slide. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: the white gable end of one block fills the right two thirds of the frame, shot slightly from below, with a giant numeral "2027" painted on it in Deep Teal #0B4F4C in the exact manner of a Seoul building number. The left third is a calm band of dusk sky and path. Top left, the logo from Image 1, small, in Foam. Middle left, the Korean headline "병은 그대로, 채우기만." very large, and directly beneath it the English line "Keep the bottle. Refill the rest." at half that size. Bottom left, two small lines stacked: "Apartment Partner Programme 2027" and "아파트 파트너 프로그램 2027". The Signal Coral stamp "채움" sits pressed slightly crooked over the corner of the English line.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 02 The problem [Notice] [HEAVY]

Rationale: the problem is shown where it happens, in the recycling cage, and the long body is split into three short notice lines so each one renders and repairs alone.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo. Place it exactly as provided, never redrawn.

Style: Danji Bulletin, Notice mood. The slide is a brushed steel lift lobby notice board in a Seoul apartment complex in flat daylight, holding crisp matte A4 sheets in Foam #EEF4EF fixed by round magnets in Deep Teal #0B4F4C. Type is a heavy rounded geometric sans for Latin headlines and a bold clean Hangul gothic with generous spacing for Korean, Ink #1C1F1E on paper, body in the regular weight of the same families; fine film grain, faint glare on the steel, generous empty board around every sheet. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: left half, a large landscape photograph pinned to the board with four magnets: a car park recycling cage on sorting evening, clear bags packed with empty detergent, shampoo and dish soap bottles, flat documentary light. Right half, one A4 notice. At its top the headline "Our recycling bins are full of bottles we could have kept." in heavy Ink type, and beneath it "분리수거함은 다시 쓸 수 있던 병으로 가득합니다." smaller. Below a hairline, three short stacked lines in regular weight: "Every week, Seoul households carry bags of empty detergent, shampoo and dish soap bottles to the recycling area," then "and most of those bottles were perfectly good containers" then "that only needed refilling instead of being thrown away and replaced." At the foot of the notice, set apart in bold: "A family of four empties around 9 plastic bottles of cleaning and care products a month." The coral stamp sits on the number 9. The logo is small at the bottom right of the board.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): repair in this order, one zone per edit. 1, the bold foot line, numbers first ("9"). 2, the Korean headline. 3, the three body lines, one per edit. Edit form: "Keep everything identical. On the notice, the third body line must read exactly: 'that only needed refilling instead of being thrown away and replaced.'"

#### 03 Meet Mulgyeol [Notice]

Rationale: a new notice going up on the board is exactly how a complex meets something new.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo and Image 2 is the Mulgyeol refill station. Place both exactly as provided, never redrawn.

Style: Danji Bulletin, Notice mood. The slide is a brushed steel lift lobby notice board in a Seoul apartment complex in flat daylight, holding crisp matte A4 sheets in Foam #EEF4EF fixed by round magnets in Deep Teal #0B4F4C. Type is a heavy rounded geometric sans for Latin headlines and a bold clean Hangul gothic with generous spacing for Korean, Ink #1C1F1E on paper, body in the regular weight of the same families; fine film grain, faint glare on the steel, generous empty board around every sheet. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: one fresh A4 notice sits slightly right of centre, newer and whiter than the board around it, two blank older sheets partly visible at the far left edge. On the notice, top: the logo from Image 1. Then the headline "A refill station that lives where you live." large, and beneath it "우리 단지 안의 리필 스테이션." Then three short lines stacked with generous space: "Six everyday refills." "Pay by the gram." "Open 24 hours in your complex's common area." Pinned overlapping the notice's lower left corner, a square photograph of the station from Image 2 standing in a bright lobby corner. The coral stamp sits on "Pay by the gram."

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 04 How it works [Notice]

Rationale: three steps as three notices in a row, the order you would read them waiting for the lift.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo. Place it exactly as provided, never redrawn.

Style: Danji Bulletin, Notice mood. The slide is a brushed steel lift lobby notice board in a Seoul apartment complex in flat daylight, holding crisp matte A4 sheets in Foam #EEF4EF fixed by round magnets in Deep Teal #0B4F4C. Type is a heavy rounded geometric sans for Latin headlines and a bold clean Hangul gothic with generous spacing for Korean, Ink #1C1F1E on paper, body in the regular weight of the same families; fine film grain, faint glare on the steel, generous empty board around every sheet. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: across the top of the board, the headline "Three steps — no new plastic." printed in heavy Ink type on a long strip of Foam paper. Below it, three portrait A4 notices in a row with equal gaps. Each carries a huge Deep Teal numeral at the top, a small square photograph in the middle, and two lines at the bottom. Notice one: "1", a hand holding an empty clean bottle, "Bring any clean bottle" and "빈 병을 가져오세요". Notice two: "2", a stainless nozzle filling a clear bottle, "Fill what you need" and "필요한 만큼 채우세요". Notice three: "3", a phone tapping a reader on a weighing plate, "Pay by weight, tap your phone" and "무게만큼 결제하세요". The coral stamp sits on notice three. The logo is small at the bottom right of the board.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

### Act 2: The offer

#### 05 On tap [Notice] [HEAVY]

Rationale: the price list is the station's own nozzle label strip, so the prices are read where the residents will read them.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo and Image 2 is the Mulgyeol refill station. Place both exactly as provided, never redrawn.

Style: Danji Bulletin, Notice mood. The slide is a brushed steel lift lobby notice board in a Seoul apartment complex in flat daylight, holding crisp matte A4 sheets in Foam #EEF4EF fixed by round magnets in Deep Teal #0B4F4C. Type is a heavy rounded geometric sans for Latin headlines and a bold clean Hangul gothic with generous spacing for Korean, Ink #1C1F1E on paper, body in the regular weight of the same families; fine film grain, faint glare on the steel, generous empty board around every sheet. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: top third, an A4 notice in landscape across the board with the headline "Six refills. Priced by the gram." and beneath it "여섯 가지 리필, 그램 단위 가격." Bottom two thirds, a close straight on photograph of the station's front from Image 2, the six stainless nozzles in one row, and under each nozzle a white label card in a row of six, each card holding three short lines. Card 1: "Laundry liquid" "세탁세제" "₩380 / 100 g". Card 2: "Fabric softener" "섬유유연제" "₩320 / 100 g". Card 3: "Dish soap" "주방세제" "₩290 / 100 g". Card 4: "Shampoo" "샴푸" "₩690 / 100 g". Card 5: "Body wash" "바디워시" "₩590 / 100 g". Card 6: "Multi surface cleaner" "다용도 세정제" "₩260 / 100 g". Prices in heavy type, the largest thing on each card. Bottom right corner, small: "Prices include VAT." The coral stamp sits on card 3. The logo is small at the top right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): numbers first, card by card from 1 to 6, one card per edit: "Keep everything identical. On card 4 the text must read exactly: 'Shampoo' '샴푸' '₩690 / 100 g'." Then the Korean headline, then "Prices include VAT." If a card keeps failing after three edits, regenerate with only that card's label blank and set it as live text.

#### 06 Pilot results [Gable] [HEAVY]

Rationale: the number boards remember is painted on a building, the size a building number is, which is the size this result deserves.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo. Place it exactly as provided, never redrawn.

Style: Danji Bulletin, Gable mood. A full bleed documentary photograph of a Seoul apartment complex at blue hour in late November, white fifteen storey blocks, lit windows, ginkgo leaves bright yellow on the paths, a cool clean grade with fine film grain. Type is a heavy rounded geometric sans for Latin and a bold clean Hangul gothic with generous spacing for Korean, set in Foam #EEF4EF or Deep Teal #0B4F4C, the same two families on every slide. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: one white gable end fills the centre of the frame, straight on, and the giant numeral "1,240" is painted across it in Deep Teal #0B4F4C exactly like a building number. Directly beneath the numeral, on the wall, the line "bottles kept out of the bin" in Deep Teal at a quarter of its height. Top left, small in Foam: "Pilot complex, Mapo District, 412 households, 90 days". Bottom band across the dusk path, two short facts side by side in Foam: left "68% of households refilled twice or more", right "₩4,100 average saving per household per month". The coral stamp sits beside the numeral's last digit. The logo is small at the bottom right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): numbers first: "1,240", then "68%", then "₩4,100", then "412". One zone per edit: "Keep everything identical. On the gable wall the numeral must read exactly: '1,240'."

#### 07 What your complex gets [Notice] [HEAVY]

Rationale: an offer to a council arrives as an official notice with ruled rows, the format every management office already signs.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo. Place it exactly as provided, never redrawn.

Style: Danji Bulletin, Notice mood. The slide is a brushed steel lift lobby notice board in a Seoul apartment complex in flat daylight, holding crisp matte A4 sheets in Foam #EEF4EF fixed by round magnets in Deep Teal #0B4F4C. Type is a heavy rounded geometric sans for Latin headlines and a bold clean Hangul gothic with generous spacing for Korean, Ink #1C1F1E on paper, body in the regular weight of the same families; fine film grain, faint glare on the steel, generous empty board around every sheet. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: one large landscape A4 notice, centred, an official form with fine Deep Teal hairline rules. Header: "What your complex gets." large and "단지에 돌아가는 혜택" beneath. Then a ruled table of six rows and two columns, the left column bold, the right regular. Row 1: "Station and install" | "Free, fitted in one day". Row 2: "Management fee credit" | "3% of station sales, credited monthly". Row 3: "Recycling report" | "Monthly, bottles and kilograms kept out of the bin". Row 4: "Upkeep" | "Cleaned and restocked twice a week". Row 5: "Lobby poster" | "A zero-waste corner residents can see". Row 6: "Contract" | "12 months, cancel with 30 days notice". The coral stamp is pressed over the right end of row 1, slightly crooked, like a management office approval. The logo is small at the bottom right of the notice.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): numbers first ("3%", "12", "30"), then row by row, one row per edit: "Keep everything identical. In row 2 the right column must read exactly: '3% of station sales, credited monthly'." Fallback: regenerate with the six right hand cells blank and set them as live text.

### Act 3: Proof and close

#### 08 Timeline [Notice] [HEAVY]

Rationale: the lift button panel is the complex's own timeline; each floor is a week, and the lit buttons are the milestones.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo. Place it exactly as provided, never redrawn.

Style: Danji Bulletin, Notice mood. The slide is a brushed steel lift lobby notice board in a Seoul apartment complex in flat daylight, holding crisp matte A4 sheets in Foam #EEF4EF fixed by round magnets in Deep Teal #0B4F4C. Type is a heavy rounded geometric sans for Latin headlines and a bold clean Hangul gothic with generous spacing for Korean, Ink #1C1F1E on paper, body in the regular weight of the same families; fine film grain, faint glare on the steel, generous empty board around every sheet. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: left third, an A4 notice with the headline "From vote to first refill in 6 weeks." large and "결정부터 첫 리필까지 6주." beneath. Right two thirds, a close photograph of a brushed steel lift button panel set into the board, one vertical column of six round buttons numbered 1 to 6 from the bottom up. Buttons 1, 2, 4 and 6 glow Deep Teal #0B4F4C; 3 and 5 are unlit. Beside each lit button, a small engraved steel plate: beside 1 "Week 1 Council vote", beside 2 "Week 2 Site visit", beside 4 "Week 4 Install", beside 6 "Week 6 Launch day". The coral stamp sits on the plate beside button 6. The logo is small at the bottom right of the board.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): button numerals first, then plates from 1 to 6, one plate per edit: "Keep everything identical. The plate beside button 4 must read exactly: 'Week 4 Install'."

#### 09 Resident [Notice]

Rationale: one real neighbour, in the lobby where councils meet her, says it better than any figure.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo. Place it exactly as provided, never redrawn.

Style: Danji Bulletin, Notice mood. The slide is a brushed steel lift lobby notice board in a Seoul apartment complex in flat daylight, holding crisp matte A4 sheets in Foam #EEF4EF fixed by round magnets in Deep Teal #0B4F4C. Type is a heavy rounded geometric sans for Latin headlines and a bold clean Hangul gothic with generous spacing for Korean, Ink #1C1F1E on paper, body in the regular weight of the same families; fine film grain, faint glare on the steel, generous empty board around every sheet. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: left half, a large portrait photograph pinned to the board: a woman in her fifties with a neat silver bob and a grey cardigan, in the lift lobby of building 102 at late morning, holding a clear refill bottle at her side, a calm half smile. Right half, one A4 notice carrying the quote in heavy type over three lines: "I stopped buying bottles in March." then "My recycling bag got lighter," then "and so did my bills." Beneath it, small: "— Ms Park, Building 102, pilot complex". The coral stamp sits at the end of the quote. The logo is small at the bottom right of the board.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 10 Big idea [Gable]

Rationale: the one line the council should repeat at their next meeting, given the whole sky.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo. Place it exactly as provided, never redrawn.

Style: Danji Bulletin, Gable mood. A full bleed documentary photograph of a Seoul apartment complex at blue hour in late November, white fifteen storey blocks, lit windows, ginkgo leaves bright yellow on the paths, a cool clean grade with fine film grain. Type is a heavy rounded geometric sans for Latin and a bold clean Hangul gothic with generous spacing for Korean, set in Foam #EEF4EF or Deep Teal #0B4F4C, the same two families on every slide. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: low angle from the path, the blocks in the lower third, a deep clear blue hour sky filling the upper two thirds. In the sky, the line "The cleanest bottle is the one you already own." very large in Foam, set over two lines. Beneath it, "가장 깨끗한 병은, 이미 가진 병입니다." at half the size. Centred in the foreground on the path among the ginkgo leaves, one empty clear plastic bottle, standing upright, lit by a lobby window. The coral stamp sits beside the bottle. The logo is small at the bottom right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 11 Close [Gable]

Rationale: one word and one object: the station glowing in a lobby at night, waiting.

```text
Design a 16:9 presentation slide in Danji Bulletin style. Image 1 is the Mulgyeol Refill logo and Image 2 is the Mulgyeol refill station. Place both exactly as provided, never redrawn.

Style: Danji Bulletin, Gable mood. A full bleed documentary photograph of a Seoul apartment complex at blue hour in late November, white fifteen storey blocks, lit windows, ginkgo leaves bright yellow on the paths, a cool clean grade with fine film grain. Type is a heavy rounded geometric sans for Latin and a bold clean Hangul gothic with generous spacing for Korean, set in Foam #EEF4EF or Deep Teal #0B4F4C, the same two families on every slide. The single accent is one round rubber stamp in Signal Coral #FF5A3C reading "채움", the only coral on the slide.

Layout: seen from the path outside, the glass doors of a lift lobby glowing warm at night, and inside, the station from Image 2 standing alone, lit. The left third is dark building wall. On it, very large in Foam, "함께 채워요." and beneath it "Let's fill your complex first." at half the size. Bottom left, small: "partners@mulgyeol.example". The coral stamp sits pressed on the glass door. The logo sits above the Korean line, small.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

## 7. Run order and repair rules

**Run order:** lock the look with the cover first and generate it until it is loved. Then the light slides (03, 04, 09, 10, 11, 02). Heavy slides last (05, 06, 07, 08).

**Style consistency:** run one image model chat session per act so the conversation holds the style. Attach the approved cover as Image 3 on every later prompt and add "Image 3 is the approved style reference; match its design system." Keep the same attachments on every message, edits included.

**Repair rules:** repair beats regeneration. One zone per edit: "Keep everything identical. In [zone] the text must read exactly: '…'". Numbers get proofread first. After 5 to 7 edit rounds, restart from the best frame. A native Korean reader proofs every Hangul line on every render.

**Rescue edit** for a render that drifts generic: "Add heavy film grain, rougher textures. Change no text."
