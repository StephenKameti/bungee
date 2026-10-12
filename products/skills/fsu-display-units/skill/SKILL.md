---
name: fsu-display-units
description: Generate premium, high impact AI image prompts for retail display units for any brand, in any market. FSUs (free standing units), gondolas, POS/POSM displays, glorifiers, counter top units, shelf displays, testing stations, and in store theatre for pharmacies, beauty stores, supermarkets, liquor stores and any retail environment, localised to the brief's stated market via an optional market module. Use this skill whenever the user asks for display unit prompts, FSU designs, POS or POSM visuals, retail display mockups, counter units, shelf displays, in store units, merchandising units, or brand theatre in retail, including "give me FSU prompts for...", "I need display units for...", "design a POS unit for...", "retail display mockups for...", or when a brand brief is shared and retail visibility materials are the deliverable. Also use it when reworking existing display unit prompts that were judged too plain, too simple or not eye catching enough.
---

# Retail Display Theatre

## Market layer (do this first)

Read the brief for the market or markets the display units are for. Casting, the retail environment, local retail chains described generically, light and any local line on the unit all derive from that market. Never fall back to a generic "international" retail look.

If the brief does not state a market, ask one question to confirm it, unless the user has already stated their own home market earlier in the conversation, in which case use that without asking again.

Once the market is known, look for `references/markets/<market>.md`. If a file exists, load it and use it for casting, retail environment and local detail. A regional module is often written from one city; where it does not cover the named country or city, use what it says for the region and research the gap for that place. If none exists, build the local specificity from the brief and from research into that market's retail landscape. Casting is always specific to the named market and described by context, never by stacking category words.

`references/markets/east-africa.md` is supplied as a worked market module. `references/markets/TEMPLATE.md` is a blank copy for building a new one.

Build image generation prompts for retail display units that stop traffic. The standard this skill encodes: every unit gets exactly one theatrical device, every unit in a family shares one material language, and every prompt generates a clean plate that survives client feedback because the type goes on in post.

The output of this skill is a set of copyable image prompts organized as a descending size family, each with a tool recommendation, aspect ratio, reference attachment instructions, and a one line rationale. It is not a fabrication spec, but it must never promise something unbuildable, so production honesty rules are part of the standard.

## Step 1 · Ingest the brand

Never write a prompt from a brand name alone. Collect, from the conversation, uploaded files, memory, or by asking:

1. **Palette with hex codes.** Exact values, and a rule for how loudly each colour may be used (e.g. "accent only, never a field"). If the user has no codes, propose them and confirm.
2. **Register.** One phrase that governs everything: clinical and restrained, luxury flagship, playful FMCG, craft premium, mass market energy. The register decides whether impact comes from light and form or from colour and character.
3. **Materials vocabulary.** 4 to 6 named materials and finishes (e.g. warm ivory matte panels, light oak, brushed brass, pale stone). Also name the banned materials, the cheap tells the register must never show (chrome, gloss acrylic, visible LED strips, gold foil, adjust per brand).
4. **The product set.** Which SKUs go on the unit, which one is the hero, and whether pack reference images exist. If packs will appear, the user must attach pack shots; the prompt then carries the exact reproduction block (Step 4). Ask for the logo file too; the wordmark is reproduced from it, never typed by the generator.
5. **A campaign device to own.** The single best FSU is usually the brand's existing campaign idea translated into three dimensions, a mirror, a sun, a drop, a mascot, a ritual. Ask what the campaign device is. If there is none, the product's own form or its usage moment becomes the device.
6. **Retail environment(s).** Pharmacy, beauty store, supermarket, duty free, liquor store. The environment sets lighting, adjacency and how loud the unit may be, and it is read off the market layer, since what a supermarket looks and feels like changes market to market.
7. **Casting.** Where people appear in renders, match the market layer and be explicit in every prompt, described by context rather than stacked category words. As an example, "shoppers with deep brown skin in a Nairobi supermarket" for a Kenyan brief, or "shoppers in a Ho Chi Minh City pharmacy" for a Vietnamese one. Never leave casting to the generator's defaults.
8. **Price and currency.** If price must show (common for small trade and promotions), it is never rendered: the unit carries a blank price plate or strip sized for the market's currency and price format, including any unit price the market requires by law, and the delivery notes a marked placeholder such as TSh XXX for post.

If the brief arrives as one message to run, do not stall on questions: propose any missing input as a marked assumption, proceed, and list every assumption under What is missing at the end of the delivery.

## Step 2 · Choose one theatrical device per unit

This is the law that separates impactful units from shelving with good manners. Each unit gets exactly ONE device, executed completely. Two devices on one unit reads as effort rather than confidence. Across a family, do not repeat a device, with one exception: a counter or tray miniature of the floor hero's device, the same idea whispered. In aisle context shots show an approved unit in place and carry no new device.

Pick from the device library (read `references/device-library.md` for the full library with usage notes and worked examples). The seven families:

1. **Oversized pack as architecture**: a giant, exactly faithful replica of the pack IS the unit structure. Highest stopping power, highest fabrication cost.
2. **Product in frozen motion**: a pour, a drop, a lather, a crumble, suspended mid air on hidden mounts. The moment of use made permanent.
3. **Campaign device in 3D**: the campaign's key visual idea built as an object (mirror, halo, doorway, mascot moment).
4. **Light as material**: internal glow, halo rings, a lit horizon. Concealed sources only; visible LED strips kill premium instantly.
5. **Narrative structure**: the unit's form draws the product story in space: a ritual sequence on ascending platforms, a ribbon connecting steps, a journey from left to right.
6. **Glorifier elevation**: one hero product raised, encased, or spotlit like an artifact; the rest of the range in attendance. Luxury grammar, works at every size.
7. **Sculpted texture wall**: the product's sensory signature (lather, foam, grain, petals, bubbles) rendered as dimensional relief on the unit's surfaces.

Match device to size: architecture and motion suit floor units; glorifiers and mini versions of the family device suit counters. Counter units stay in the family: one may whisper the floor hero's device at small scale (the only permitted repeat), and the rest carry their own device in the same uniform.

## Step 3 · Build the family, not a unit

Deliver a descending size family so the client can match ambition to each door:

- **Floor / full FSU** (1.6 to 2.0 m), the hero, flagship doors only
- **Medium** (1.1 to 1.4 m), the negotiation unit chains actually accept
- **Counter top** (0.3 to 0.5 m), the volume placement
- **Tray / glorifier** (smallest), fits any counter, still unmistakably the brand

Where the market's trade runs through kiosks, dukas, warungs, bodegas or other small independents, the smallest tier is their own rugged format: a clip strip, a grille or shelf hanger, a counter dispenser. Unpowered, built for sun, dust and weeks between visits, never a shrunk mall unit.

All sizes share the material language, palette rules and one visual signature so the family reads as one brand at every scale. Group prompts under size headers. 6 to 9 prompts is the sweet spot; below 5 feels thin, above 10 dilutes.

## Step 4 · Write each prompt to the standard

Every prompt is one paragraph of continuous prose with four blocks in order. Read `references/example-prompts.md` for two full worked examples before writing your first prompt in a session.

**Block 1, the fixed preamble** (the same text across the whole family; write it once, then paste it in full at the start of every prompt. Never abbreviate it or write "same preamble as above": every prompt must work pasted on its own. Change a clause only when a unit cannot carry it, for example the wordmark clause on a replica whose own label carries the logo):
- "Photorealistic retail display mockup photography" plus the register phrase
- The full palette with hex codes and loudness rules
- The materials vocabulary and the banned materials
- Casting instruction
- The text lockdown: the wordmark only where specified, reproduced from the attached logo file; the real pack labels reproduced from the pack shots; apart from those, every printed panel, price strip and shelf talker completely blank for artwork in post, no straplines, no small print, no other readable text rendered in the image. With no logo file, leave the wordmark panel blank too

The text lockdown is not negotiable. Generators misspell, and burned in type means a full regeneration on every copy change. Clean plates plus typesetting in post is the only workflow that survives client feedback rounds.

**Block 2, the pack fidelity block** (only when real packs appear, including oversized replicas):
"Use the attached [brand] pack references as the exact source of truth for all products, including any oversized sculptural replicas, which must reproduce label design, logo, typography, colours and proportions exactly at scale. Do not redesign, translate, paraphrase or respell any label text."

**Block 3, the unit itself:**
- Approximate dimensions in centimetres and the unit's footprint
- The one device, described completely: what it is, what it is made of, how it is lit, where the product sits relative to it
- Where the wordmark sits (once), and which panel stays blank for post
- Product facing: which SKUs, which shelf, naked product beside carton details where relevant

**Block 4, scene and camera:**
- The retail environment and what falls out of focus behind
- A human figure for scale where useful (cast per Step 1), doing something believable, reading a carton, glancing in the mirror, never posing
- Lens, aperture, lighting mood, and one line making the unit the brightest or warmest object in frame

## Step 5 · Deliver with metadata and honesty

Present the set grouped by size, each prompt carrying:
- **Tool** (e.g. the default photoreal image model for environments and structures, an isolated product image model for close human moments, adjust to the user's stack)
- **Aspect ratio** (4:5 for single units, 16:9 for in aisle context shots)
- **Reference attachments**: exactly which pack shots, logo file or prior generations to attach, and which reference is critical
- **A one line "why"**: what the device does commercially, not what it looks like

Recommend a generation order: the hero unit first, because the family inherits its material language, and one flagship render becomes the reference attachment for the rest.

Close every delivery with production honesty. Flag, unprompted, whichever apply:
- Custom fabrication with internal lighting costs several times flat pack shelving and needs mains power at the bay. Present hero units as a 3 to 5 door tier, not the volume unit, or procurement prices the hero against fifty doors and kills the family
- Retail estate is negotiated: chains have fixture specs and paid listings; the deck should show the unit the buyer will actually accept alongside the ambition unit
- Nothing plumbed, nothing structurally impossible: water features become decorative basins with hidden reservoirs; floating elements get "on hidden mounts" in the prompt and a rigging note in the flag
- Restocking is a budget line: a premium unit with gaps looks worse than no unit; fewer units plus funded merchandising visits beats wide placement that decays
- Category rules: alcohol, tobacco and nicotine, medicines, infant formula and some foods carry promotion and display rules that vary by market (where a unit may stand, gifts with purchase, price promotion, human figures). Name the category and market, say which rules may bite, and send the client to their legal team before any unit is priced
- If the brand register is conservative (medical, financial, clinical benchmark brands), keep one restrained variant in the appendix so the client can choose the register rather than reject the theatre

End with **What is missing**: every assumption made, the attachments still needed, and any price or legal sign off the units wait on.

## Reworking a rejected set

When the user says a previous set is too simple or not eye catching (a trigger for this skill), diagnose before rewriting: the failure is almost always that the units are shelving, product rows in a branded box, with zero devices. The fix is Step 2, not louder colour. Palette and register stay; impact comes from form and light. Say so explicitly when delivering the rework, and name the device each unit now carries.
