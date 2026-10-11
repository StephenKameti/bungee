---
name: key-visual-builder
description: |
  Build campaign Key Visuals for any market from a brief, deck or typed request. Produces 6 to 8 named KV routes, each with a copyable image model prompt, copy suite, channel adaptation kit, designer build sheet and, when the campaign moves, a motion brief for bumpers, animated KVs and short vertical video, localised through an optional market module. Trigger whenever the user asks for a key visual, KV, master visual, campaign visual or hero visual, including "build the KV for...", "give me key visuals for this brief", "develop the KV routes", "give me image prompts for the key visual", or when a brief, deck, PDF or chat screenshot is uploaded for that purpose. Also trigger on KV revisions and adaptations: "make the KV simpler", "rework the KV", "adapt the KV for OOH, POS or social", "animate the KV", "give me a bumper for this route". Use it when the deliverable is the campaign master image and its adaptations, not slide backgrounds or a one off event poster.
---

# Key Visual Builder

## Market layer (do this first)

Before anything else, read the brief for the market or markets the work is for. Everything local, casting, places, light, language for local lines, retail environment, media, currency, cultural calendar, derives from the stated market. Never invent it from a generic "international" or "African" default.

If the brief does not state a market, ask one question to confirm it, unless the user has already stated their own home market earlier in the conversation, in which case use that without asking again.

Once the market is known, look for `references/markets/<market>.md`. If a file exists for that market, load it and use it as the source of casting, place, light, language and retail detail for every route. If no file exists for that market, build the local specificity directly from the brief and from research into that market's places, retail environment, media and cultural calendar. Either way, casting is always specific to the named market and described by context, for example a named neighbourhood and the light there at a stated time of year, never by stacking category words like race, gender and age.

`references/markets/east-africa.md` is supplied as a worked market module. `references/markets/TEMPLATE.md` is a blank copy for building a new one.

## Core Mandate

A Key Visual is not a nice picture. It is the single image that carries the campaign proposition, survives being cropped to a shelf talker, and still means something to a driver going past at speed. This skill turns a brief into a spread of KV routes, each one already laid out as a working artwork with the copy written and the crops planned.

For example, a KV built for Nairobi has to still mean something at 80kph on the main road out of the city; a KV built for Mexico City has to still mean something to a pedestrian on a crowded Reforma pavement. The test is the same, the place changes with the market.

The generated image is a **base plate**. It carries no readable text and no logos. The wordmark, endline, pack lockup and legal go on in post by the designer. Everything this skill produces is built around that division of labour.

Three things ship together for every route. A prompt without copy is half a job. Copy without crops is a KV that dies at adaptation.

1. The master KV prompt
2. The copy suite
3. The adaptation kit and designer build sheet

**Standard is top tier international advertising award craft.** Not stock. Not "a family smiling in a kitchen" with the region as the only variable.

---

## Step 1: Extract the KV Spine

Read the whole input before writing anything. Brief, deck, PDF, chat screenshot, or typed request. Then fill this table and show it back to the user before any prompts. If the input is a deck, read every slide. If it is a formal brief, the spine is usually already in it and asking for it again is a waste of the user's time.

| Spine element | What to pull |
|---|---|
| Client and brand | Company, brand, sub brand, agency the work is presented under |
| Product hero | The exact SKU, pack format, size, variant that must appear |
| Business problem | The commercial friction in one line. Basket size, penetration, switching, price per gram, category entry |
| Single minded proposition | Verbatim from the brief if it exists. Never paraphrase a signed SMP |
| Insight | The human truth underneath. If the brief has none, write one and mark it as proposed |
| Campaign line or lockup | Existing line, existing lockup file, or "to be written" |
| Audience | Who, age band, role in the household or kitchen or trade, in their own language |
| Palette | Hex values. Pull from a supplied logo, guideline, or packshot. Never leave colour to the model |
| Channels | Every place the KV must land. This sets the adaptation kit |
| Mandatories | Client non negotiables. Pack visible, underarms bare, no smiling, WHO six step, dress code |
| No gos | Category conflicts, competitor cues, banned claims, tournament and flag rules |
| Reference material | Global KV to evolve, past campaign, reference wall, competitor work |
| Due date | Drives how many routes get built out in full |

**Then ask, at most, three questions.** Only on axes that would change the work and that the brief genuinely does not answer. Never ask about anything already in the input. If nothing is missing, do not ask. Proceed.

### When there is a global or regional KV to evolve

This is the most common live situation. The instruction "evolve the existing KV, do not build new routes" changes the whole job.

- Deconstruct the reference into its **devices** first. The split screen. The magnifier. The before and after. The colour coded halves. State them in a table
- Keep the devices, change the world. Casting, context and light specific to the market layer, never the reference's original market carried over unchanged
- Every route in the set must be traceably the same campaign as the reference
- The spread rule below still applies, but the spread is across executions of the device, not across unrelated ideas

---

## Step 2: Route the KV on Five Axes

Resolve all five before writing a prompt.

### Axis 1: KV Archetype

Pick the archetype the proposition demands, not the one that is easiest to render.

| Archetype | What it is | When it is right |
|---|---|---|
| Demonstration split | Frame divided. Without the brand versus with it. Colour coded halves, a clarity device inside each | Hygiene, efficacy, protection, education. Any proposition that is an argument |
| Product truth | The product doing the thing, shot as evidence. Macro, cross section, texture, cut, melt, pour | Food, taste, quality, heritage, craft. Any proposition that is a claim about the thing itself |
| Occasion tableau | The moment the brand belongs to, staged as one composed frame | Festive, family, hosting, ritual, togetherness. Any proposition about an occasion |
| Hero portrait | One person, one look, one truth. Environmental or studio | Confidence, transformation, identity, aspiration, category entry |
| World build | A constructed or heightened environment the brand owns | Brand platform work, umbrella campaigns, "the wonderful world of" territory |
| Object poetry | One object, isolated, treated with total seriousness. Surreal scale, impossible perspective, frozen physics | Premium, halo, prestige, luxury, cut through in a cluttered category |
| Type as terrain | The line built as physical environment. Mown, poured, laid, carved, stacked | When the line is the idea and it is strong enough to be the picture |

### Axis 2: Humanisation

| Level | Use |
|---|---|
| No people | Product truth, object poetry, type as terrain. Zero casting risk, fastest to approve |
| Hands and body, face away | Cooking, using, pouring, applying. All the humanity, none of the casting debate |
| One figure, face present | Hero portrait, demonstration split. Highest impact, highest revision risk. Expect notes on expression |
| Group | Occasion tableau only. Three or four figures maximum. Groups of six read as stock |

### Axis 3: Register

Pick one and hold it across the whole set. Mixing registers reads as indecision.

| Register | Signature | Fits |
|---|---|---|
| High key clean | White or ivory ground, soft even light, no shadow drama, generous air | FMCG shopper, hygiene, health, education, anything for a lightbox or shelf |
| Warm documentary | Real light, real rooms, telephoto compression, no gloss, slight grain | Behaviour change, community, banking, NGO, government |
| Editorial luxury | Marble, chrome, silk, shallow depth, controlled specular highlights | Premium tiers, halo SKUs, hospitality, spirits, skincare |
| Cinematic dark | Deep ground, rim light, wet surfaces, single hard key | Flagship, sport, launch moments, gin and grill, night occasions |
| Graphic flat | Bold blocks of brand colour, hard shadow, poster logic, no photographic realism | Youth, telco, disruptor, price led shopper, anything that must scream at 3 metres |

### Axis 4: Pack Presence

The most common client note in almost any market is "make the pack bigger." Decide upfront so the revision does not break the composition.

| Mode | Consequence for the prompt |
|---|---|
| Pack in scene | Describe the pack physically by shape, colour and finish. Never ask the model to render the label. Leave the label face as a clean blank plate for the designer to place the real artwork |
| Pack on clean plate | Generate the scene with a defined empty area sized for the packshot. State it as a percentage of frame |
| Pack as hero | Object poetry archetype. The pack is the subject. Still leave the label face clean |
| No pack | Brand platform and teaser work only. Confirm with the user before assuming this |

**Standing rule: never ask a generative model to render your client's pack artwork or logo.** It will get it wrong, and wrong pack art in a client deck is a credibility loss you cannot recover in the same meeting. Generate the form, place the real art in post.

### Axis 5: Adaptation Load

List every channel from the spine. This decides the crop set. See `references/adaptation-kit.md` for the full ratio and channel table.

---

## Step 3: The Elevation Pass

This is the step that separates this skill from a prompt generator. Run it before writing any prompt. Full laws library and anti pattern list in `references/elevation.md`.

### The elevation ladder

Every idea sits on one of four rungs. Only rung three and four ship.

1. **Literal.** The words of the brief, pictured. "Family enjoying a festive meal." Delete on sight
2. **Staged.** Literal, but art directed. Better light, better casting, better props. Still not an idea
3. **Devised.** There is a mechanism. A device, a tension, a reveal, a wrong thing that turns out to be right. The image does work the headline does not have to
4. **Devised with a law.** The mechanism is expressed through a borrowed visual law. Impossible perspective. Frozen physics. Surreal isolation. Language as terrain. Absurdist seriousness. Scale inversion

### The seven elevation rules

1. **Find the law, not the look.** When the user supplies references, extract the rule that makes them work and state it back in a three column table: reference, what it said, what I did with it. Never imitate the surface
2. **The image must hold alone.** Cover the headline. If the picture stops meaning anything, it is not a KV, it is an illustration
3. **One idea per frame.** Two ideas in a prompt is two routes. Split it
4. **Tension before release.** The strongest KVs show the problem and the answer in the same frame. Split, before and after, magnifier, cross section, empty versus full
5. **Culture specific, never a continent wide stereotype.** A named district of one city is not a named district of another, and neither is a generic stand in for the whole region or continent. Name the district, the neighbourhood, the market, the light, all pulled from the market layer. As an example, a Nairobi estate in January light is not a Nairobi estate in July light. The same discipline applies anywhere, a Jakarta kampung in the dry season is not a Jakarta kampung in the wet season
6. **The pack earns its place.** If the pack is in frame it is doing something. Being held near a face is not doing something
7. **Escalate the idea, never the adjectives.** "More creative" is never answered by adding "hyper detailed, ultra realistic, stunning" to the same prompt. It is answered by a new mechanism

### The kill list

Do not ship any of these unless the brief explicitly demands it and even then argue first.

Smiling family around a table. Hands presenting a product to camera. Generic golden hour sunset. Ingredients exploding in midair without a reason. A woman laughing alone with food. A gradient background with a floating pack. A single iconic natural or architectural landmark used as lazy shorthand for an entire region or continent, for example a baobab tree standing in for all of Africa or a rickshaw standing in for all of South Asia. Sunburst rays behind a hero. Anyone pointing at anything.

---

## Step 4: Build the Option Set

### How many

**Six to eight routes.** Never four. The user will ask for more.

### The spread rule

The set must span. **Two safe, three strong, one that should not work but does**, plus one or two wildcards if the brief has room. Eight variations on one idea is one route, not eight. If two cards could be described in the same sentence, one of them is not a route.

Safe means the client will nod. Strong means the client will lean forward. The one that should not work is the reason the meeting is memorable, and it must still be legitimately buildable.

### Card anatomy

Every route is a card with these eight parts, in this order.

1. **Number and name.** Two or three words. Nameable, memorable, quotable in a client meeting. Low Tide. The Second Half. Full Table. Morning Light. Steam Rising
2. **The idea.** One sentence. What the image is doing conceptually. Two sentences means the idea is not sharp yet
3. **Why it wins.** One line linking the mechanism back to the single minded proposition. Naming the archetype and register in brackets
4. **Layout logic.** Where the concept sits in frame, where the copy lives, why the crop set will survive
5. **Master KV prompt.** Full prose block, tool tagged, copyable, built to the architecture in Step 5
6. **Copy suite.** Per Step 6
7. **Adaptation kit.** Per Step 7
8. **Designer build sheet.** Per Step 8

---

## Step 5: Prompt Architecture

Written for the default photoreal image model. Prose quality drives the output. No parameter strings. Full protocol, refusal ladder and image to image workflow in `references/image-model-protocol.md`.

```
[SHOT TYPE AND FRAMING, with aspect ratio stated in words]
+ [HERO SUBJECT, described physically, action in the present tense]
+ [SECONDARY ELEMENTS and props, each earning its place]
+ [ENVIRONMENT AND GROUND, with hex]
+ [LIGHTING DIRECTION, named source and quality]
+ [PALETTE LOCK, hex on every coloured element]
+ [PACK TREATMENT, form described, label face left clean]
+ [TEXT ZONE, as a percentage of frame and a named position]
+ [STYLE AND CRAFT TAGS]
+ [one short closing absence clause, if needed at all]
```

### The rules that make these work

**Text zones as percentages.** Not "leave space at the top." Write "the upper 38 percent of the frame above the pack is unbroken warm ivory #F8F5F0, held clean as the headline zone."

**Hex on every coloured element.** Turquoise #12B7C9. Not "turquoise."

**Physical description beats adjective stacking.** "Back of the hand tilted so the light catches the rim of the wedge, crumb structure open at the cut face" beats "delicious appetising cheese."

**Present tense action.** The model renders verbs better than nouns. "Steam lifting off the surface" not "with steam."

**Positive construction only.** Most current image models have no reliable negative prompting. Writing "no logos, no text" pushes those tokens into the request and some safety layers read it as an attempt to strip attribution. Write what is present. "Plain unprinted apparel in solid colour." "The label face is a smooth blank panel." One short absence clause maximum, at the very end, only if unavoidable.

**Casting by context, never by category.** Do not stack race plus gender plus age. Write "a woman with deep brown skin and short natural hair, photographed in a Nairobi kitchen" for a Kenyan market brief, or "a woman with straight dark hair, photographed in a Mexico City apartment kitchen" for a Mexican one. Same casting outcome, clean pass, no policy trip, and the description is doing the market's work instead of a label.

**Variant pairs where the effect is optional.** With steam and without. Day and night. Pack in scene and pack on plate. Offer both rather than choosing for the user.

### Standing craft tags

```
4K. Advertising grade. Top tier international award show craft.
Editorial food photography / studio product photography / documentary portrait / photorealistic composite.
Shot on 85mm, shallow depth of field.
```

### Tool routing

Name tools generically unless the user has already told you which image model, image editor or type renderer they use, in which case route to their named stack.

| Need | Tool | Note |
|---|---|---|
| Photoreal scenes, people, food, composites, pack in scene | The default photoreal image model | Default. Prose driven, hex inline, no parameter strings |
| Readable type in the image, mown lettering, foil, engraved lines | A dedicated type rendering image model | The only reliable choice for legible type. Use for type as terrain routes |
| Surreal, conceptual, editorial abstraction, object poetry | A stylised or editorial image model | Use its raw or photographic style setting and pin the version so the whole set matches |
| Clean studio packshot on white | An isolated product image model | Strongest on isolated product |
| Adapting or extending an approved KV, changing one element | The default photoreal image model, image to image mode | Crop all visible brand marks out of the reference first. See references |

---

## Step 6: Copy Suite

Every route ships with copy. Not placeholder copy. Copy the client could run.

Per route, produce:

- **Headline.** Three options, ranged. One straight, one warm, one that earns a smile
- **Subline.** One line, the proposition made plain
- **Endline or campaign line.** If the brief has one, use it verbatim and do not improve it. If it does not, give three
- **Pack or proof callout.** The short line that sits by the pack. Since 1979. 8 month cave aged. Kills 99.9 percent of germs
- **CTA.** Channel appropriate. Different for POS and for social
- **Local line.** At least the headline, written in the market's dominant local language or its natural street register, with an English gloss alongside it. Natural blend, never translated English, never forced. If the market's brief is already English first with no local vernacular in play, say so and skip it rather than force one

### Copy rules

- **No hyphens and no em dashes anywhere in client facing copy.** Rewrite the sentence instead
- Short, punchy, emotive. If a line needs a comma to survive, cut it
- Local language inflection must be how people actually speak, not how a brand thinks people speak. Test it out loud
- Comprehension in three to five seconds at the fixture. That is the real brief for shopper work
- Never write a claim the brief has not cleared. Flag suspended claims in the card

Full craft notes, headline patterns and endline patterns in `references/copy-craft.md`.

---

## Step 7: Adaptation Kit

The master KV is a 4:5 or 1:1 plate. The KV only earns its money when it crops. For each route, give the reprompt or the crop instruction for every channel in the spine.

Default set unless the spine says otherwise:

| Format | Ratio | What changes |
|---|---|---|
| Master KV | 4:5 | The full composition. Everything else derives from this |
| Feed post | 1:1 | Tighten to the mechanism. Drop the widest environment |
| Story and short vertical video | 9:16 | Rebuild vertically. Move the text zone to the upper third, subject to the lower two thirds |
| OLV end frame | 16:9 | Widen. Text zone moves to a clean side third |
| Billboard 6x3 | 2:1 | One element only. The mechanism at scale, endline on a clean third. Nothing survives at speed except one idea |
| Shelf talker | 3:4 tall narrow | Pack plus one visual cue. No environment |
| Gondola end | 1:2 tall | Vertical world, pack repeated, headline at eye height |
| Dangler | 1:1 double sided | The mechanism, both faces, no small type |

Say plainly which formats need a **reprompt** and which are a **crop**. A vertical story is almost never a crop of a horizontal master, and pretending it is costs a day.

Full channel table with pixel sizes, bleed and safe area in `references/adaptation-kit.md`.

**When the campaign moves.** If the spine lists any moving channel (bumper, animated KV, short vertical video, video end frame, cutdowns), write a **motion brief** for the fire immediately routes, or for the routes the user shortlists. Never for all eight by default. Follow `references/motion-brief.md`: film line, spec, build route, assets, a shot list on the beat grid, sound, on screen text and the poster frame. The motion brief uses the route's own copy suite and local line, so the film and the still say the same thing.

---

## Step 8: Designer Build Sheet

The handover to the artworker. Per route, exact and unambiguous:

- **Text zones.** Percentage of frame and named position for headline, subline, endline
- **Logo plate.** Where the wordmark sits, clear space, positive or reversed version
- **Pack lockup.** Coordinates and scale for dropping the real pack artwork onto the blank label face
- **Endline lockup.** Position, and whether it sits on the image or on a colour block
- **Safe area and bleed.** For print and OOH formats
- **Colour build.** Hex list, and the CMYK note if the route goes to print
- **Do not.** The two or three things that will break this composition if changed

---

## Step 9: Output

**Deliver as a single self contained interactive HTML file.** This is the house deliverable. Template and pattern in `assets/kv-library-template.html`.

Structure:

- **Cover.** Client, brand, job, campaign line, date, image model ({{IMAGE_MODEL}}), decision date
- **Spine strip.** The Step 1 table, condensed. So the client sees the brief was read
- **Reference law table.** Three columns, only if references were supplied
- **One route article per route** with the full eight part anatomy and a copy button on every prompt and every copy line. Set data-register (safe, strong or wild) and data-name on each article; the sticky route index, numbering and register tags build themselves
- **Motion brief panel,** inside the route article, only for routes that have one: the spec line, the shot list table on the beat grid, the sound line and the poster frame. Delete the panel from routes without a brief
- **Footer.** Palette hex swatches, standing rules, tool routing, casting note

**Close every delivery with:**

- **Fire immediately.** The three routes to generate first, named, one line each on why
- **The disruptive alternate.** The one route to put on the table beside the safe pick, so there are two clearly different directions in the room
- **What is missing.** Anything the brief did not answer that will need a client decision before artwork

---

## Step 10: Reading Feedback

Feedback arrives short and direct. Read it correctly the first time.

| What they say | What it means | What to do |
|---|---|---|
| Make it simpler | Too many elements competing. Not a colour problem | Strip to one mechanism and one subject. Rebuild, do not tweak |
| Make it clearer | The device is not reading in three seconds | Add a clarity device inside the frame. Magnifier, ring, arrow of light, hard split |
| Not impressed | The routes are descriptions, not ideas | Throw the set out. Go find a law and build from it |
| More creative | Same as above | New mechanism. Never new adjectives |
| Make it lighter or airier | Register is wrong | Switch register entirely to high key clean. Do not brighten the existing set |
| Make the pack bigger | Usually correct. The pack is the ad | Move to pack on clean plate or pack as hero. Recompose, do not scale up |
| Too serious | Register is wrong in the other direction | Switch register. Do not add a smile to the existing set |
| Give me options | The spread was too narrow | Widen the spread, not the count |
| Keep it closer to the global | Stop inventing | Return to the reference devices. Change only world, casting and light |

**The failure mode to avoid:** answering "more creative" by adding words to the same prompt. Adjective inflation is not creative escalation. A new route is a new idea.

---

## Standing Rules

- The generated image never contains readable text or logos. The only exception is a type as terrain route, and that goes to a dedicated type rendering image model
- Never render the client's pack artwork or logo generatively. Generate the form, leave the label face clean, place the real art in post
- Hex on every coloured element in every prompt. Colour is never left to the model
- Text zone stated as a percentage and a named position, or the prompt is not finished
- Positive construction only. No stacked negative clauses
- Casting described by context, never by stacked category
- Market specificity is not optional. Name the place, the light, the season, all pulled from the market layer for the brief's stated market
- No hyphens and no em dashes in any client facing copy
- Every route ships with prompt, copy and crops together. Never a prompt alone
- Six to eight routes with a real spread

---

## Quality Check Before Delivering

- [ ] Market confirmed and the matching market module loaded or researched before any prompt
- [ ] KV spine extracted and shown back before any prompt
- [ ] All five routing axes resolved
- [ ] Reference laws stated in a three column table, if references were supplied
- [ ] Six to eight routes with a genuine spread, not variations on one idea
- [ ] Every route sits on rung three or four of the elevation ladder
- [ ] Every route has a nameable title and a one sentence idea
- [ ] Every prompt has hex on every colour, a percentage text zone, and craft tags
- [ ] Zero negative clause stacking, zero stacked category casting
- [ ] Pack label face left clean in every prompt that includes the pack
- [ ] Copy suite complete per route including a local line in the market's language where one applies
- [ ] Adaptation kit marks each format as crop or reprompt
- [ ] Designer build sheet present per route
- [ ] Motion brief written for the shortlisted routes whenever a moving channel is in the spine, with the shot list on the beat grid, holds that meet the readability law, and the logo on a downbeat
- [ ] No hyphens or em dashes in any client facing copy
- [ ] Fire immediately picks and the disruptive alternate named at the close
- [ ] Delivered as a single interactive HTML file with copy buttons
