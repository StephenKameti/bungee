# Designed Deck Builder test, Brief B: Kipaji Alizeti trade roadshow deck, Dar es Salaam

Test record. Skill: `products/skills/designed-deck-builder/skill/` as shipped (SKILL.md, `references/markets/TEMPLATE.md`, `references/markets/east-africa.md`). Run once on 12 October 2026, exactly as SKILL.md instructs, as if a user had sent the brief and deck below in one message. Everything from section 1 down is the deliverable; the prompt library page built from it is saved beside this file as `brief-b.html`.

**Brief as sent:** Make our trade roadshow deck look designed, as slide images with the copy in them. Brand: Kipaji Foods, launching Kipaji Alizeti sunflower cooking oil in Dar es Salaam in four sizes, including small kadogo pouches. Audience: wholesalers and duka owners at roadshow stops across the city. Colours are a sunflower yellow and a deep green; we do not have the codes to hand. Logo: the word "Kipaji" in a bold rounded serif with a small sunflower over the i. I will attach the logo and a photo of the four packs. Copy below, Swahili first as it will be presented. Two comments from the team are still in it.

**Source deck as sent (verbatim):**

1. Cover. Kipaji Alizeti / Mafuta ya kupikia ya kila siku. / Everyday cooking oil. / Roadshow ya Wauzaji, Dar es Salaam, Januari 2027 / Trade Roadshow, Dar es Salaam, January 2027
2. Soko. Mteja ananunua kidogo, kila siku. / Shoppers buy small, every day. / Mama lishe, familia na wanafunzi wananunua mafuta kwa kipimo kidogo kila siku kwa sababu pesa inaingia kidogo kidogo, na duka lenye kipimo sahihi ndilo linalompata mteja huyo kila asubuhi bila kukosa.
3. Vipimo. Vipimo vinne. Kila mfuko, kila mteja. / Four sizes for every pocket. / Kipaji Alizetti 100 ml pakiti TSh 500 / 250 ml pakiti TSh 1,200 / Lita 1 chupa TSh 4,500 / Lita 3 dumu TSh 13,000
4. Ubora. Yameongezwa Vitamini A na D. Hayana kolesteroli. / Fortified with Vitamins A and D. Cholesterol free. [Maoni, Neema: weka alama ya ubora ya serikali hapa]
5. Faida. Faida yako kwa kila katoni. / Your margin per carton. / Table, columns: Kipimo / Size; Bei ya jumla / Wholeseller price; Bei ya rejareja / Retail value; Faida / Margin. Rows: 100 ml (vipande 48) TSh 20,400, TSh 24,000, TSh 3,600 / 250 ml (vipande 24) TSh 24,500, TSh 28,800, TSh 3,400 / Lita 1 (chupa 12) TSh 47,000, TSh 54,000, TSh 7,000 / Lita 3 (dumu 4) TSh 45,600, TSh 52,000, TSh 6,400
6. Ofa. Nunua katoni 10, pata 1 bure. / Buy 10 cartons, get 1 free. / Lipa kwa simu, pokea mzigo kesho. / Pay by mobile money, delivery next day. / Pre-order kwa simu. / Ofa inaisha 28 Februari 2027.
7. Msaada. Tunakusaidia kuuza. / We help you sell. / Mwavuli wa kibanda / Stika za rafu / Bango la bei / Sampuli 20 za 100 ml kwa kila duka jipya
8. Wasambazaji. Wasambazaji wetu Dar es Salaam. / Our distributors across Dar es Salaam. / Kariakoo, Ilala, Kinondoni, Temeke, Ubungo, Mbagala [Comment, Baraka: add Mbezi, the new depot opens in January]
9. Sauti ya duka. "Pakiti ya 100 ml imeleta wateja wapya kila asubuhi." / "The 100 ml pack brings new customers every morning." — Mama Rehema, Duka la Rehema, Temeke
10. Wazo kuu. Kila tone lina kazi. / Every drop earns its place.
11. Mwisho. Tuanze leo. / Let's start today. / Simu: +255 700 000 000

**Where the run had to interpret the skill** (scored in SCORE.md):

* No hex codes. Step 2 says research the real hexes and ask only about genuine gaps. The brand is not findable and the run is unattended, so the run proposed hexes and marked them proposed. SKILL.md has no rule for this.
* The two team comments. SKILL.md is silent on comments; the README promises they are actioned before design. The run actioned the Mbezi comment and flagged, rather than actioned, the government quality mark comment, because a real certification mark must come from the authority's own file.
* The margin table. The 250 ml margin reads TSh 3,400, but TSh 28,800 less TSh 24,500 is TSh 4,300: two digits swapped. Step 1 asks for broken lines to be corrected and flagged; it does not ask for sums to be checked. The run checked every row because Step 5 says numbers come first.
* Hyphen and em dash in the client's copy. "Pre-order" (slide 6) and the dash on slide 9 are rendered as sent; SKILL.md has no rule for them.
* Market texture. The East Africa module's texture is Nairobi's and it says not to reuse it for Dar es Salaam without checking, but gives no Dar es Salaam texture. The run researched it.
* Production questions. As in Brief A, Step 4 has no unattended path; the run used Step 3's rule and proceeded on the defaults.
* Typography consistency. One style DNA per mood, pasted verbatim, as in Brief A.

---

## 1. Market layer

| Area | What the market layer sets |
|---|---|
| Market | Dar es Salaam, Tanzania, for brand and audience. East Africa module loaded. Its Languages by country section sets the order: Swahili leads daily life, media, business and advertising, so Swahili first and English second, as the deck already does. No Sheng: this is a trade audience, and Sheng is a Kenyan register. |
| Texture | Researched, since the module's street texture is Nairobi's. Kariakoo, the city's wholesale heart: narrow lanes of stacked cartons, porters pulling loaded handcarts, hand painted wooden shop signs, carbon copy invoice books on wooden counters. Daladala minibuses and bajaji three wheelers carry the street colour. Dukas with painted fronts in every ward. |
| Retail and price | Wholesale by the carton, retail by the piece. Kadogo packs drive daily buying; mama lishe food vendors buy small every morning. Mobile money is the default way to pay a supplier and at the till. Prices in Tanzanian shillings, written TSh 4,500. |
| Typography | Swahili sets like English in a display face: no diacritics, but long agglutinated words (linalompata, wanafunzi) break badly at narrow widths, so give Swahili lines width and keep each under about 15 words. |
| Casting and light | By context: a woman in her forties in a printed kitenge headwrap behind her duka counter in Temeke at 07:00. January is the short dry season: hot, humid, hard white coastal light, haze off the harbour by midday. |
| Regulatory | Module: health and nutrition claims need a cleared substantiation line before they are rendered. "Fortified with Vitamins A and D" needs the fortification certificate behind it. "Cholesterol free" is true of every plant oil, and a claim that implies a rival lacks it is often ruled misleading; flag it. A government quality mark is placed only from the authority's own file, with permission. |

## 2. Copy flags

Every change below is already applied in the prompts. Revert any of them by editing the quoted text in that slide's prompt.

| Slide | As sent | In the prompts | Why |
|---|---|---|---|
| 03 | "Kipaji Alizetti" | "Kipaji Alizeti" | Brand name misspelled. |
| 05 | "Wholeseller price" | "Wholesale price" | Typo. |
| 05 | 250 ml margin "TSh 3,400" | "TSh 4,300" | Two digits swapped: TSh 28,800 less TSh 24,500 is TSh 4,300. Confirm with finance before the roadshow. |
| 08 | Comment from Baraka | "Mbezi" added as a seventh pin | Comment actioned; the comment text is removed from the slide. |
| 04 | Comment from Neema, add the government quality mark | Not added | Flagged, not actioned: a real certification mark must come from the authority's own file and be cleared for use. Attach it as an extra image when you have it. |

**Claims to clear before the roadshow:**

* Slide 04: "Yameongezwa Vitamini A na D." needs the fortification certificate. "Hayana kolesteroli." / "Cholesterol free." is a claim regulators often treat as misleading on a plant oil; legal to confirm or cut. Rendered as sent.
* Slide 09: the quote needs Mama Rehema's written consent to be used. Rendered as sent.

## 3. Brand Sheet

| Item | What the prompts use |
|---|---|
| Colours | Proposed, none supplied: Kipaji Sun #F2A900, Deep Green #0E4D2E, Cream #FFF6E0, Ink #1A1A17. Replace with the real codes when they arrive; the prompts change in one place per mood. |
| Logo | The word "Kipaji" in a bold rounded serif with a small sunflower over the i. Image 1 in every prompt, placed as provided, never redrawn. |
| Product | The four packs: 100 ml and 250 ml pouches, a 1 litre bottle and a 3 litre jerrycan, sunflower yellow labels with green. Image 2 in every prompt that shows them. |
| Typography | Brand face not supplied. Described in image language: a heavy rounded slab serif for headlines, echoing the logo and the precision of a good sign painter; a clean typewriter mono for figures and body. |
| Brand world | Everyday, dependable, proud of small sizes. Category convention for cooking oil: golden pour shots, smiling families at the table, sunflower fields. Worth breaking for a trade audience who care about margin and stock that moves. |

## 4. Design language

Three languages were considered. Working unattended, the run picks the strongest and states it here.

| Language | One sentence |
|---|---|
| **Kariakoo Ledger** (picked) | The deck speaks the wholesaler's own media: ruled order books and carbon copy invoices for the numbers, hand painted Kariakoo shop signs for the big moments. |
| Mama Lishe Gold | Flash lit dawn documentary of food vendors frying in big pans, oil catching the light, the copy set in the steam. |
| Ubao Pure | Every slide a hand painted shop board, the whole deck as a street of signs. |

**Why Kariakoo Ledger.** A wholesaler judges a supplier by the numbers and by whether stock moves. The ledger is where he does that sum every evening; the painted sign is where Kariakoo announces anything worth knowing. Mama Lishe Gold is the consumer's story and belongs in the consumer launch. Ubao Pure is loud on every slide and has nowhere quiet for the margin table.

**Devices:** ruled ledger pages with faint blue lines and a sheet of blue carbon paper (texture); heavy rounded slab serif for headlines, typewriter mono for figures (type behaviour); flat early light documentary of Kariakoo lanes with fine grain (photo treatment); hand painted wooden signboards carrying the loud lines (structure); one hand painted Kipaji Sun brush stroke per slide under the key line, the only accent.

**Two moods:**

* **Daftari** (quiet, content slides 02, 03, 04, 05, 06, 07, 08, 09): the order book on a wooden shop counter.
* **Ubao** (loud, slides 01, 10, 11): Kariakoo itself, full bleed, with the line painted on a shop signboard.

**Content through medium:** the margin table is the ledger page (05); the offer is a filled carbon copy invoice slip (06); the support kit is laid out on the counter, each item with a paper tag (07); the distributor map is drawn in ballpoint across a ledger double page (08).

## 5. Production questions

Asked as one round; working unattended, the run proceeds on the defaults.

| Question | Default used |
|---|---|
| Target image model | The image model with the strongest text rendering and the best preservation of attached brand assets. |
| Copy handling | Verbatim everything, with the copy flags in section 2. The 31 word Swahili body on slide 02 is broken into three stacked lines, word for word. |
| Pure table slide (05) | Rendered in image as the ledger page: four short rows. |
| Aspect | 16:9. |

## 6. Prompt library

**Attach these every time:** Image 1, the Kipaji logo file. Image 2, the photo of the four packs. After the cover is approved, Image 3, the approved cover render, and add this line to every later prompt: "Image 3 is the approved style reference; match its design system."

### Act 1: The market and the range

#### 01 Cover [Ubao]

Rationale: the roadshow opens in the place every wholesaler in the room buys from, with the brand announced the way Kariakoo announces everything, on a painted board.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo and Image 2 is the Kipaji Alizeti pack family. Place both exactly as provided, never redrawn.

Style: Kariakoo Ledger, Ubao mood. A full bleed documentary photograph of a narrow Kariakoo wholesale lane in Dar es Salaam at 06:30 in January, walls of stacked cartons, a porter's handcart, hard white early light with long shadows, warm grade, fine film grain. Type is a heavy rounded slab serif for headlines, hand painted onto wooden shop signboards in Deep Green #0E4D2E on Cream #FFF6E0, with a clean typewriter mono for small lines, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: the lane runs from the bottom right into depth at the left. Across the upper half, fixed above a shop front, a long wooden signboard painted Cream with the headline "Kipaji Alizeti" huge in Deep Green, and beneath it on the same board "Mafuta ya kupikia ya kila siku." with "Everyday cooking oil." smaller under that. The Kipaji Sun stroke runs under "Kipaji Alizeti". On a stack of cartons at bottom right, the four packs from Image 2 lined up. Bottom left, two small typewriter lines in Cream on a dark strip of shadow: "Roadshow ya Wauzaji, Dar es Salaam, Januari 2027" and "Trade Roadshow, Dar es Salaam, January 2027". The logo from Image 1 is small at the top left corner of the slide.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 02 Soko [Daftari] [HEAVY]

Rationale: the market shift written up as the first page of a wholesaler's order book, his own habit of noting what moved today.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo. Place it exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: the book fills the frame, slightly rotated. Left page, top: the headline "Mteja ananunua kidogo, kila siku." large in slab serif, and beneath it "Shoppers buy small, every day." smaller; the Kipaji Sun stroke runs under the Swahili headline. Right page, three typewriter lines on three ruled lines with space between them: "Mama lishe, familia na wanafunzi wananunua mafuta kwa kipimo kidogo kila siku" then "kwa sababu pesa inaingia kidogo kidogo," then "na duka lenye kipimo sahihi ndilo linalompata mteja huyo kila asubuhi bila kukosa." In the lower right of the right page, a small square photograph clipped to the book: a mama lishe pouring oil into a wide pan at a roadside stall at dawn. The logo is small at the bottom left of the left page.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): one body line per edit, top to bottom, then the headline: "Keep everything identical. On the right page, the third line must read exactly: 'na duka lenye kipimo sahihi ndilo linalompata mteja huyo kila asubuhi bila kukosa.'"

#### 03 Vipimo [Daftari] [HEAVY]

Rationale: four sizes, four price tags tied on the real packs; the shopkeeper reads the price where his customer will.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo and Image 2 is the Kipaji Alizeti pack family. Place both exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: top third, across the open book, the headline "Vipimo vinne. Kila mfuko, kila mteja." in slab serif, and beneath it "Four sizes for every pocket." smaller, the Kipaji Sun stroke under the Swahili line. Under that, small in typewriter mono: "Kipaji Alizeti". Bottom two thirds, the four packs from Image 2 standing in a row on the counter in front of the book, smallest at the left, each with a Cream paper price tag tied on with string, the tag in typewriter mono, two lines each, the price in bold. Tag 1: "100 ml pakiti" "TSh 500". Tag 2: "250 ml pakiti" "TSh 1,200". Tag 3: "Lita 1 chupa" "TSh 4,500". Tag 4: "Lita 3 dumu" "TSh 13,000". The logo is small at the top right of the book.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): prices first, tag by tag, one tag per edit: "Keep everything identical. Tag 4 must read exactly: 'Lita 3 dumu' 'TSh 13,000'." Then the headline.

#### 04 Ubora [Daftari]

Rationale: one bottle and two short lines; quality claims read strongest when nothing competes with them.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo and Image 2 is the Kipaji Alizeti pack family. Place both exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: right half, the 1 litre bottle from Image 2 standing on the counter, close, light catching the oil. Left half, the open book with two lines in slab serif, generous space between them: "Yameongezwa Vitamini A na D." and "Hayana kolesteroli." Beneath each, its English line in typewriter mono: "Fortified with Vitamins A and D." and "Cholesterol free." The Kipaji Sun stroke runs under "Yameongezwa Vitamini A na D." The logo is small at the bottom left of the book.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

### Act 2: The money

#### 05 Faida [Daftari] [HEAVY]

Rationale: the margin is written where a wholesaler writes margins, in his own ruled book, column by column.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo. Place it exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: the book is seen straight from above, filling the frame. Across the top of both pages, the headline "Faida yako kwa kila katoni." in slab serif and "Your margin per carton." smaller beneath. Below, a ruled ledger table across both pages in typewriter mono, four columns and a header row. Header: "Kipimo / Size" | "Bei ya jumla / Wholesale price" | "Bei ya rejareja / Retail value" | "Faida / Margin". Row 1: "100 ml (vipande 48)" | "TSh 20,400" | "TSh 24,000" | "TSh 3,600". Row 2: "250 ml (vipande 24)" | "TSh 24,500" | "TSh 28,800" | "TSh 4,300". Row 3: "Lita 1 (chupa 12)" | "TSh 47,000" | "TSh 54,000" | "TSh 7,000". Row 4: "Lita 3 (dumu 4)" | "TSh 45,600" | "TSh 52,000" | "TSh 6,400". The Faida column is in bold and the Kipaji Sun stroke runs under "TSh 7,000". The logo is small at the bottom right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): every figure first, row by row, one row per edit: "Keep everything identical. In row 2 the four cells must read exactly: '250 ml (vipande 24)' 'TSh 24,500' 'TSh 28,800' 'TSh 4,300'." Then the header row. Fallback: regenerate with the ruled table empty and set the figures as live text.

#### 06 Ofa [Daftari] [HEAVY]

Rationale: the offer arrives as the invoice he will actually sign, the carbon copy still in the book.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo. Place it exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: centre, a carbon copy invoice slip torn half out of the book, slightly lifted, the blue carbon sheet visible beneath. On the slip, the headline "Nunua katoni 10, pata 1 bure." large in slab serif, and "Buy 10 cartons, get 1 free." beneath; the Kipaji Sun stroke runs under the Swahili line. Below on the slip, two lines in typewriter mono: "Lipa kwa simu, pokea mzigo kesho." and "Pay by mobile money, delivery next day." Right of the slip, a phone lying face up on the counter, its screen showing one large green tick. Bottom left on the book page, two small typewriter lines: "Pre-order kwa simu." and "Ofa inaisha 28 Februari 2027." The logo is small at the top left.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): numbers first ("10", "1", "28", "2027"), then the slip lines top to bottom, then the two small lines, one per edit.

#### 07 Msaada [Daftari]

Rationale: the support kit laid out on the counter like a delivery being checked in, each piece tagged.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo and Image 2 is the Kipaji Alizeti pack family. Place both exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: top left on the open book, the headline "Tunakusaidia kuuza." in slab serif and "We help you sell." beneath; the Kipaji Sun stroke runs under the Swahili line. The rest of the counter, seen from above, holds four items laid out neatly in a grid, each with a Cream paper tag in typewriter mono: a folded Deep Green and Kipaji Sun kiosk umbrella, tag "Mwavuli wa kibanda"; a roll of plain Kipaji Sun shelf strips, tag "Stika za rafu"; a blank Cream price board with a Deep Green frame, tag "Bango la bei"; a neat bundle of twenty 100 ml pouches from Image 2 tied with string, tag "Sampuli 20 za 100 ml kwa kila duka jipya". The logo is small at the bottom right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 08 Wasambazaji [Daftari] [HEAVY]

Rationale: the route to market drawn the way a sales rep draws it for a new customer, in ballpoint across the book.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo. Place it exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: top left, the headline "Wasambazaji wetu Dar es Salaam." in slab serif and "Our distributors across Dar es Salaam." beneath; the Kipaji Sun stroke runs under the Swahili line. Across both pages, a simple map of Dar es Salaam drawn in blue ballpoint over the ruled lines: the coastline on the right, the harbour inlet, a few main roads as single lines. Seven Deep Green round pins, each with a small typewriter label: "Kariakoo" at the centre near the harbour, "Ilala" just south west of it, "Kinondoni" to the north, "Mbezi" further north west, "Ubungo" to the west, "Temeke" to the south, "Mbagala" furthest south. The logo is small at the bottom right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

Fix strategy (HEAVY): one pin label per edit, starting with "Mbezi", the new one: "Keep everything identical. The label on the north western pin must read exactly: 'Mbezi'."

### Act 3: Proof and close

#### 09 Sauti ya duka [Daftari]

Rationale: a shopkeeper the room knows by type, in her own duka, saying the one thing they all want to hear.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo and Image 2 is the Kipaji Alizeti pack family. Place both exactly as provided, never redrawn.

Style: Kariakoo Ledger, Daftari mood. The slide is an open wholesale order book lying on a worn wooden shop counter, ruled pages in Cream #FFF6E0 with faint blue lines and a red margin, a sheet of blue carbon paper peeking from under one page, flat even early light, fine film grain. Type is a heavy rounded slab serif for headlines in Deep Green #0E4D2E and a clean typewriter mono for body and figures in Ink #1A1A17, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: left half, a photograph clipped to the book: a woman in her forties in a printed kitenge headwrap behind her duka counter in Temeke at 07:00, shelves of small packs behind her, the 100 ml pouch from Image 2 in her hand, a direct, easy look. Right half, the open book with the quote in slab serif over two lines: "Pakiti ya 100 ml imeleta wateja wapya kila asubuhi." and beneath it in typewriter mono "The 100 ml pack brings new customers every morning." Below, small: "— Mama Rehema, Duka la Rehema, Temeke". The Kipaji Sun stroke runs under "wateja wapya". The logo is small at the bottom right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 10 Wazo kuu [Ubao]

Rationale: the big idea painted high over a Kariakoo lane, where the room will picture it on the way home.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo. Place it exactly as provided, never redrawn.

Style: Kariakoo Ledger, Ubao mood. A full bleed documentary photograph of a narrow Kariakoo wholesale lane in Dar es Salaam at 06:30 in January, walls of stacked cartons, a porter's handcart, hard white early light with long shadows, warm grade, fine film grain. Type is a heavy rounded slab serif for headlines, hand painted onto wooden shop signboards in Deep Green #0E4D2E on Cream #FFF6E0, with a clean typewriter mono for small lines, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: looking up the lane from low down, one huge Cream signboard spans the lane between two buildings in the upper half, painted with "Kila tone lina kazi." in Deep Green, enormous, and beneath it on the same board "Every drop earns its place." at a third of the size. The Kipaji Sun stroke runs under "Kila tone lina kazi." Below, the lane busy and soft with movement, a porter crossing. The logo is small at the bottom right.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

#### 11 Mwisho [Ubao]

Rationale: one word and one object: a duka shutter going up at dawn and a single bottle on the counter, the first sale of the day.

```text
Design a 16:9 presentation slide in Kariakoo Ledger style. Image 1 is the Kipaji logo and Image 2 is the Kipaji Alizeti pack family. Place both exactly as provided, never redrawn.

Style: Kariakoo Ledger, Ubao mood. A full bleed documentary photograph of a narrow Kariakoo wholesale lane in Dar es Salaam at 06:30 in January, walls of stacked cartons, a porter's handcart, hard white early light with long shadows, warm grade, fine film grain. Type is a heavy rounded slab serif for headlines, hand painted onto wooden shop signboards in Deep Green #0E4D2E on Cream #FFF6E0, with a clean typewriter mono for small lines, the same two families on every slide. The single accent is one hand painted brush stroke in Kipaji Sun #F2A900 under the key line, the only yellow stroke on the slide.

Layout: a duka front in the lane, its metal shutter half rolled up, early light spilling onto the wooden counter where the 1 litre bottle from Image 2 stands alone. Above the shutter, a Cream signboard painted with "Tuanze leo." huge in Deep Green, with the Kipaji Sun stroke beneath, and "Let's start today." smaller under it. Bottom left, small typewriter line in Cream on the shadowed wall: "Simu: +255 700 000 000". The logo sits at the right end of the signboard, small.

Editorial print quality, 2K, all text spelled exactly as quoted, no other text, no watermarks.
```

## 7. Run order and repair rules

**Run order:** lock the look with the cover first and generate it until it is loved. Then the light slides (04, 07, 09, 10, 11, 02). Heavy slides last (03, 05, 06, 08).

**Style consistency:** run one image model chat session per act so the conversation holds the style. Attach the approved cover as Image 3 on every later prompt and add "Image 3 is the approved style reference; match its design system." Keep the same attachments on every message, edits included.

**Repair rules:** repair beats regeneration. One zone per edit: "Keep everything identical. In [zone] the text must read exactly: '…'". Numbers get proofread first. After 5 to 7 edit rounds, restart from the best frame. A Swahili reader proofs every line on every render.

**Rescue edit** for a render that drifts generic: "Add heavy film grain, rougher textures. Change no text."
