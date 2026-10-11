---
name: audience-persona-builder
description: |
  Build precise, strategically actionable audience definitions and consumer personas for campaigns, briefs, and pitches in any market in the world, localised to the brief's stated market via an optional market module. Trigger this skill whenever the user asks to define an audience, build personas, describe a target market, or create a "day in the life", including phrases like "define the audience for...", "who is our target for...", "give me a day in the life of...", "build personas for...", "who are we talking to?", "describe the consumer for...", or when a campaign brief needs an audience architecture. Also trigger when the user uploads a brief and asks to identify who the brand should target. Always use this skill for any audience or consumer profiling task, even if the word "persona" is not used.
---

# Audience Definition & Persona Builder

## Market layer (do this first)

Before building anything, read the brief for the market or markets the audience work is for. Everything local, language and code switching, neighbourhoods and their socioeconomic reading, the local income/social tier system, retail and purchase channels, and the peer networks that shape decisions, derives from the stated market. Never fall back to a generic global default.

If the brief does not state a market, ask one question to confirm it, unless the user has already stated their own home market earlier in the conversation, in which case use that without asking again.

Once the market is known, look for `references/markets/<market>.md`. If a file exists, load it and use it as the source of geography, tier definitions, purchase channels and cultural touchpoints for that market. If no file exists, do not fall back to generic filler. Build local specificity directly from the brief and from research: real neighbourhoods or districts, the market's own established tier system, the actual retail formats and channels people use there, real language patterns. Casting and persona detail are always specific to the stated market and described by context, what someone does, wears, where they are, how they speak, never by stacking category words.

`references/markets/east-africa.md` is supplied as a worked market module. `references/markets/TEMPLATE.md` is a blank copy for building a new one.

---

## Core Mandate

Produce a board-ready, campaign-actionable audience architecture. The standard: hyper-specific, grounded in the stated market's own real places and real tiers, no generic marketing personas. Every output should make a planner, creative director, or client say "that's exactly who we're talking to", not "yes, that could be anyone."

No stock-photo descriptions. No generic "urban millennial" language. Real neighbourhoods, real media habits, real purchase triggers, real cultural tension.

---

## Step 1: Intelligence Gathering

Read the brief carefully before asking. Extract what you can, then ask for what's missing.

### Required Inputs
1. **Brand / product**, what it is, what it does, what tier (premium / mass / value)
2. **Campaign objective**, awareness, trial, loyalty, behaviour change, launch
3. **Market**, city/region and country, neighbourhood or district tier if specified
4. **Any existing audience assumption**, what the client already thinks they know about their consumer
5. **Category context**, who else is in this space and who they target

### Inferred Defaults (apply unless overridden)
- **Geography**: the stated market's main metro area, with neighbourhood or district-level specificity, refined by the market module where one exists
- **Language**: the market's primary language, plus any code-switch or slang register the market module or brief calls for
- **Tier model**: 3 tiers, Primary (buyer/decision-maker), Secondary (influencer/aspirant), Amplifier (cultural force)
- **Cultural context**: this market's own savings or trading networks, group chats, informal commerce patterns, and social gathering points, from the market module or research
- **Output format**: Visualised audience architecture widget + written strategic read per tier

---

## Step 2: The 3-Tier Audience Architecture

Every audience definition uses this model. Never flatten to a single audience. Never go beyond 4 tiers without a compelling reason.

### Tier 1: Primary Audience
**The buyer, user, and decision-maker.**
This is the person whose behaviour the campaign must change. All media planning, copy tone, and channel selection is anchored here.

### Tier 2: Secondary Audience
**The influencer, aspirant, or co-decision-maker.**
This person shapes Tier 1's choices. They may be a peer, a child, a younger sibling, a member of the same savings or social group, or a social media voice. They don't always buy, but they determine what Tier 1 buys.

### Tier 3: Amplifier Audience
**The cultural force.**
The person, community, or platform that legitimises the brand in this market. Influencers, community gatekeepers, trade channels, informal retailers, or opinion leaders. They are not the consumer, they are the permission-giver.

---

## Step 3: Per-Tier Profile Architecture

For each tier, build all six components:

### Component 1: WHO THEY ARE (Demographics)
```
Age range:
Gender:
Income / social tier: [defined by the market's own tier system]
Location: [Specific named neighbourhoods, districts, or towns]
Household composition:
Employment / income source:
Language dominance:
```

**Income / social tier reference:**
Use the tier system typical of the market (for example LSM bands, socioeconomic level, social grade, SEC). Load the market module for the mapped local definition; do not invent a universal scale where the market already has its own established system and name for it. If no module exists, research the local system and label tiers using the market's own terminology rather than importing another market's labels.

### Component 2: A DAY IN THEIR LIFE
Chronological. Neighbourhood-specific. Real cultural texture. 6 to 8 time-stamped moments, minimum.

**Format:**
```
[TIME], [What they're doing and where. What brand/media/social interaction happens here.
What decision or trigger occurs. What they're feeling.]
```

**Requirements:**
- Name specific locations, not "a shop", but the actual local retail format and a plausible street or area name. For example, "the supermarket on Mombasa Road" in Nairobi, or "the corner store on Avenida Insurgentes" in Mexico City.
- Name specific media, not "social media", but the actual platform type and moment, for example "the short video platform at 10pm while the kids are asleep"
- Name specific cultural references (savings-group meetings, school gate, commute routine), sourced from the market module or research
- Include the exact moment where the brand has an opportunity to appear

### Component 3: PSYCHOGRAPHIC PROFILE
The internal world, motivations, fears, aspirations, tensions.

```
Core motivation: [The deep why behind their behaviour]
Primary tension: [The unresolved conflict the brand can speak to]
Self-image: [How they see themselves vs. how they want to be seen]
Status signals: [What they use to communicate success or belonging]
Fear / shame trigger: [What keeps them up, what they won't admit publicly]
Aspiration anchor: [The version of themselves they're working toward]
```

### Component 4: MEDIA & PURCHASE BEHAVIOUR
Where they consume, what they trust, how they buy.

```
Primary media: [Platform type + time of day + content type]
Secondary media: [Platform type + context]
Trusted voices: [Who influences their decisions, family, influencer, faith
                 leader, savings-group member]
Purchase channel: [Local corner shop, local supermarket chain, large
                    format retail, online, group buy, etc.]
Purchase trigger: [What tips them from consideration to purchase]
Price sensitivity: [Small-format/single-use economy vs. value-size vs.
                     premium, with specific local price signals in
                     local currency]
Brand loyalty pattern: [Switcher / loyalist / trial-driven]
```

### Component 5: BRAND RELATIONSHIP
Where they are with this brand right now, and what needs to shift.

```
Current awareness: [Know it / use it / lapsed / never tried]
Current perception: [What they think/feel about the brand today]
Barrier to trial/loyalty: [The specific thing stopping them]
What would change their mind: [The trigger or message that would shift behaviour]
What they need to believe: [The single most important thing the brand must prove]
```

### Component 6: STRATEGIC IMPLICATION FOR THE BRIEF
The "so what", written as a direct brief input, not a summary.

```
What this means for CREATIVE: [1 to 2 sentences, tone, casting, visual world]
What this means for MEDIA: [1 to 2 sentences, channels, time of day, context]
What this means for COPY: [1 to 2 sentences, language register, code-switch
                            decision, message priority]
What this means for ACTIVATION: [1 to 2 sentences, where to show up physically]
```

---

## Step 4: Audience Type Variants

Different campaign types require emphasis on different components. Adjust depth accordingly:

### FMCG / Mass Market (detergents, seasonings, oral care, deodorants)
- Deep Tier 1 and Tier 2 profiles
- Heavy emphasis on purchase channel, price sensitivity, and the small-format/single-use economy
- The market's own primary peer influence networks (savings groups, school gate, workplace networks, from the market module) as the main channel
- Tier 3 = grassroots influencers, neighbourhood opinion leaders, broadcast personalities (named specifically per market)

### Youth / Teen Campaigns (ice lollies, toothpaste, snacks, ice cream)
- Tier 1 = the child/teen (the user)
- Tier 2 = the parent (the buyer), especially the mother
- Tier 3 = peer group, short-video and video-platform creators, school gate social currency
- Day-in-the-life anchored to school routine, tuck shop or nearest equivalent, after-school moment

### Premium / Aspirational (regional airlines, members clubs, premium services)
- Upper income tiers as primary audience
- Day-in-the-life anchored to weekend routines, neighbourhood social dynamics, travel aspirations
- Media: photo and stories feed platform, professional or private messaging groups, podcasts, weekend print/news
- Tier 3 = aspirational community figures, private club or professional networks, the market's own business community hub (named specifically per market)

### Behaviour Change / Health (hygiene, recycling, public health)
- Add a BARRIER ANALYSIS block per tier (cognitive / social / practical barriers)
- Day-in-the-life includes the specific risky behaviour moment
- Tier 3 = community health workers, school teachers, faith leaders
- Frame aspirations around family safety and community dignity, not just individual health

### B2B / Trade (Agency pitches, SaaS tools, institutional)
- Tier 1 = decision-maker (CMO, brand manager, procurement)
- Tier 2 = internal influencer (creative team, marketing ops)
- Tier 3 = industry opinion leaders, awards bodies, peer agencies
- Day-in-the-life anchored to work calendar, approval chains, budget cycles

---

## Step 5: Market Geography & Tier Reference

Use this to ground personas in specific, named places and an accurate local tier system. Never use generic "urban area" descriptions.

Load `references/markets/<market>.md` for this market's own geography and tier tables, neighbourhood-level social profiles, local purchase channels, and key cultural touchpoints. If no module exists for the stated market, build the equivalent from the brief and research: name real neighbourhoods or districts, map them to the market's own established income/social tier system, and identify the actual local venues (markets, malls, transit, community institutions) that anchor daily life there. Never substitute one market's structure for another it was not built for.

### Example: East Africa (Kenya)
See `references/markets/east-africa.md` for the full estate-level social profile table, LSM bands, and key Nairobi cultural touchpoints (savings groups, neighbourhood group chats, school gate, informal transit culture, the corner kiosk, church, football ground).

### Example: a second market
The same structure applies elsewhere. In Metro Manila, the equivalent table would map barangays and districts (Makati, BGC, Quezon City, Tondo, Caloocan) to local social class bands, with touchpoints like sari-sari stores, jeepney routes, parish life, and barangay associations replacing the savings groups and informal transit culture used in the Kenya module. The mechanism repeats, the content is entirely local.

---

## Step 6: Output Format

### Deliver as a layered output

**Part 1: Audience Architecture Visual**
Build an interactive widget showing the 3-tier model with expandable cards per tier. Each card surfaces: Who they are, Day-in-the-life highlight, Key psychographic, Brand relationship, and Strategic implication.

**Part 2: Written Strategic Brief Input**
After the visual, deliver a clean written document structured for direct insertion into a campaign brief:

```
AUDIENCE ARCHITECTURE, [Brand] / [Campaign]

PRIMARY AUDIENCE (Tier 1)
[Full 6-component profile]

SECONDARY AUDIENCE (Tier 2)
[Full 6-component profile]

AMPLIFIER AUDIENCE (Tier 3)
[Adapted profile, focus on role, reach, trust mechanism]

CROSS-TIER STRATEGIC READ
[3 to 4 sentences synthesising what the three tiers mean together, the
overarching audience insight that should anchor the brief]
```

### Tone standards for persona writing
- Write the day-in-the-life in present tense, "She wakes up at 5:45am..." not "The primary consumer would wake up..."
- Give each persona a name, never "the consumer" or "Target Audience A"
- Names should be authentic to the market and matched to the local area and tier. See the market module for worked examples. For instance, in Kenya: Zawadi for Lavington (an upper-middle estate), Atieno for Kayole (a working-class estate), Wanjiru for South B (a middle-class estate); in Mexico City: Fernanda for Polanco (an upscale district), Itzel for Iztapalapa (a working-class district).
- Quote their internal voice once per persona, in italics, in their actual local language register
- End each tier profile with one bold strategic line, the sentence a creative director would read out in the briefing room

---

## Quality Check Before Delivering

Before finalising, verify each tier profile has:
- [ ] Named persona (not "Target A")
- [ ] Specific local neighbourhood(s) named, sourced from the market module or research
- [ ] Income/social tier assigned, using the market's own tier system
- [ ] Day-in-the-life with 6+ time-stamped moments
- [ ] Specific named locations, media platforms, and cultural touchpoints
- [ ] Psychographic tension and aspiration clearly stated
- [ ] Brand relationship / barrier identified
- [ ] Strategic implication written as brief input (not summary)
- [ ] Internal voice quote included
- [ ] No generic marketing language ("urban millennial", "digitally savvy", "values quality")

---

## Reference Files

- `references/markets/east-africa.md`, a worked market module for Kenya and wider East Africa: the Nairobi geography and estate profile table, LSM tier bands, local purchase channels, and key cultural touchpoints.
- `references/markets/TEMPLATE.md`, a blank copy for building a new market module.
