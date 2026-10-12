---
name: social-content-calendar-builder
description: |
  Build complete monthly social media content calendars for brands in any market, across FMCG, hospitality, lifestyle and institutional categories, localised through an optional market module, with a compact motion brief for every short video, story or animated post. Trigger whenever the user asks to build a content calendar, plan social posts, create a posting schedule, write caption suites or develop platform specific content, including "build me a content calendar for...", "give me social posts for this month", "I need captions for...", "what should we post this month?", or when a brief or campaign strategy is uploaded and social execution is the goal. Also trigger for seasonal or cultural moment requests like "give me Easter posts for...", "April Fools ideas for..." or "what should we post for a national holiday?" Use it for any social content planning task, even if the word calendar is not used.
---

# Social Content Calendar Builder

## Market layer (do this first)

Before building anything, read the brief for the market or markets the calendar is for. Everything local, language and code switching, casting, places and neighbourhoods and their socioeconomic reading, retail channels, platforms that matter locally, posting rhythms, cultural calendar, currency and price points, derives from the stated market. Never fall back to a generic global default.

If the brief does not state a market, ask one question to confirm it, unless the user has already stated their own home market earlier in the conversation, in which case use that without asking again.

Once the market is known, look for `references/markets/<market>.md`. If a file exists, load it and use it as the source of local specificity: language, platforms, posting rhythms, fixed annual moments, sporting anchors, hashtag sets and caption register for that market. If no file exists, do not fall back to generic filler. Build local specificity directly from the brief and from research: real neighbourhoods, real retail channels, real platforms in use, real language patterns, real price points in local currency. Casting is always specific to the stated market and described by context, what someone does, wears, where they are, how they speak, never by stacking category words.

`references/markets/east-africa.md` and `references/markets/east-africa-calendar.md` are supplied as a worked market module. `references/markets/TEMPLATE.md` is a blank copy for building a new one.

---

## Core Mandate

Produce a complete, production-ready monthly content calendar, every post planned, captioned, image-directed, and scheduled. The standard: a social media manager local to the target market should be able to hand this directly to a designer and scheduler with zero additional briefing. No vague content ideas. Real captions. Real image direction. Real times.

All content is grounded in the target market's own cultural context by default, established in the market layer above. Posts acknowledge real moments in that market, commute patterns, salary or pay-cycle dates, school term rhythms, local sporting fixtures, not generic global social templates.

---

## Step 1: Intelligence Gathering

Read the brief or conversation before asking. Extract what you can, then request only what is genuinely missing.

### Required Inputs
1. **Brand / account**, name, category, what it sells, tone of voice
2. **Target month**, which month, any campaign window or seasonal anchor
3. **Primary platform(s)**, by type: short video platform, photo and stories feed platform, community feed platform, messaging broadcast, professional network, plus any platform the market module flags as locally dominant
4. **Audience**, who follows this account (default: the target market's urban adults 22 to 40, refined by the market module)
5. **Campaign or content theme**, any active campaign the calendar should serve
6. **Posting frequency**, how many posts per week (default: 3 per week on anchor days)
7. **Mandatories**, any legal, brand, or product claims restrictions
8. **Prices, offers and brand facts**, prices in local currency, offer dates, stock, history, prizes and service promises. Use only what the brief gives. Where a post needs one that is missing, write a marked placeholder such as TSh [price, to confirm] and list it under Open items. Never invent a sell out, an anniversary, a delivery time or a prize.

### Inferred Defaults (apply unless overridden)
- **Anchor posting days**: Monday, Wednesday, Friday
- **Optimal posting times**: morning commute, lunch break, evening commute or post-work scroll, timed to the market's own working day (the market module gives specific local times where one exists)
- **Language**: the market's primary language, plus any code-switch or slang register the market module or brief calls for
- **Cultural context**: this market's public holidays, sporting events, and neighbourhood-level or community-level social rhythms, baked in
- **Image generation approach**: use an image model suited to photorealistic people and lifestyle scenes, a separate one suited to product and flat-lay work, and a separate one suited to cinematic or editorial imagery, matched to what the user's own stack supports
- **Hashtag strategy**: the count set per platform in Step 5, a mix of brand hashtag, category hashtag, and this market's own cultural hashtags

---

## Step 2: Content Architecture

Every calendar is built on the 4-Pillar model. Assign each post a pillar before writing. No more than 40% of posts in any single pillar.

Weeks run Monday to Sunday. A part week of three days or fewer at either end of the month joins the week next to it.

### The 4 Pillars

**Pillar 1: Brand / Product**
The commercial content. Product features, campaigns, promotions, launches, offers. This is what the brand wants to say. Keep it to maximum 30% of total posts, more than this and the account feels like an ad feed.

**Pillar 2: Lifestyle & Aspiration**
The brand living in the consumer's world. Not product-first, world-first. The food they eat, the places they go, the feelings they have, with the brand woven in naturally. This earns the right to post Pillar 1.

**Pillar 3: Community & Engagement**
Questions, polls, challenges, user-generated content reposts, reactions to this market's cultural moments. This is where the brand shows up as a participant in the conversation, not a broadcaster. Required minimum: 1 community post per week.

**Pillar 4: Education & Value**
Tips, how-tos, explanations, behind-the-scenes, "did you know" content. Builds trust. Makes the brand useful, not just visible. Especially important for FMCG and health brands.

### Pillar assignment by brand type
| Brand Type | P1 Brand | P2 Lifestyle | P3 Community | P4 Education |
|---|---|---|---|---|
| FMCG mass market | 30% | 35% | 20% | 15% |
| Hospitality / restaurant | 30% | 35% | 25% | 10% |
| Lifestyle / fashion | 25% | 40% | 25% | 10% |
| Health / behaviour change | 20% | 25% | 25% | 30% |
| B2B / institutional | 30% | 15% | 20% | 35% |

---

## Step 3: Cultural Moment Calendar

Apply this every month before writing any posts. Cultural moments are mandatory anchors, brands that ignore them feel irrelevant.

Load the moments file for the markets in the brief: global moments plus the market's own moments. Start from `references/global-cultural-moments.md` for the moments that recur across many markets in some form (new year, a romantic or gifting occasion, international women's day, a major spring holiday period, a labour or workers day, a mother's or father's day equivalent, a major national day, a major faith or harvest calendar date, a year-end shopping event, the year-end holiday season). Then layer in `references/markets/<market>.md` for that market's own fixed dates, sporting anchors, monthly rhythms and weekly moments. Where a market module exists, its dates and framing take precedence over the generic dataset, since exact dates, moveable dates, and local weight all vary by market. A module never lists every date: always check the target month for the moveable faith and lunar dates in the global file, and for the country's own dates when the module covers it only in outline.

Sensitive moments, remembrance days, disaster anniversaries, election dates, protest anniversaries, are always a rule, not a suggestion: no promotional content on those dates in that market. Check the market module and the brief for these dates before scheduling, and when in doubt, ask or research rather than guess.

**Quiet days.** On a sensitive date, or a day of worship the market keeps solemn (Good Friday, a remembrance day, a national day of mourning), post nothing promotional and pause paid posts. Either leave the day silent or post one plain line with no product, no CTA and no hashtags, and move the anchor slot to the nearest suitable day. The anchor day and CTA rules do not apply to a quiet day. Show it in the calendar as a quiet day, so nobody fills the gap.

### Example: East Africa (Kenya)
See `references/markets/east-africa.md` for the full fixed annual moments list, monthly social rhythms, sporting anchors and hashtag sets, and `references/markets/east-africa-calendar.md` for the month-by-month content angles and arcs.

### Example: a second market
The same mechanism applies everywhere the content changes. In Mexico City, fixed annual moments would include Independence Day (Sep 16), Day of the Dead (Nov 1 to 2), a Christmas-to-Epiphany season running through Jan 6, and Mother's Day on a fixed date (May 10) rather than a moveable Sunday. In Manila, they would include a different independence date, a strong pre-Christmas season starting as early as September, and typhoon-season sensitivities that a Nairobi or Mexico City calendar would never need to flag. Fixed dates, moveable dates, monthly rhythm, sporting anchors, and sensitive dates repeat as a structure in every market; only the content is local.

---

## Step 4: Per-Post Architecture

Every post in the calendar must include all six components. No exceptions.

```
POST [N], [DATE], [DAY], [PILLAR]

THEME: [One sentence, what this post is about and why now]
PLATFORM: [Which platform(s), format may differ per platform]

CAPTION:
[Full caption as it will appear, not a summary, not "write about X".
The actual words, in the brand's voice, in the right language register.
Written to work on this specific day, referencing the market's own
cultural moment if relevant.]
[Hashtags on a separate line at the end: #Brand #Category #Market #Cultural]

VISUAL DIRECTION:
[A full standalone image prompt, pasteable on its own: ratio in words,
shot type, subject, place, season and time of day, light, the feed
look palette written out with hex, the text zone as a percent of the
frame, and the tool. Never "as post 3" or "same scene".]
[Specify: with text overlay OR no text overlay, both options if relevant]
[The real pack and logo are placed in design. In the prompt a pack is
a plain shape in the brand colours with a smooth blank label panel
and no lettering.]

POSTING TIME: [Specific, e.g. "Friday 5:30 PM"]
FORMAT: [Feed post / Short video / Story / Carousel, with specs if short video/Carousel]
CTA: [What action the post drives, comment / share / visit link / message / tag]
```

**Every short video, story or animated post also carries a compact motion brief** (the full method is in `references/motion-brief.md`):

```
MOTION: [length] s · [9:16 master, other ratios] · [tempo] BPM · route [code drawn / image to video / live action / edit]
HOOK ON SCREEN (0 to 2 s): [the words or image that stop the scroll]
BEATS: 4 to 8 rows of  bar.beat | what changes | text on screen and hold
SOUND: [trending audio slot, original track or voiceover line] + the key sound effect
SOUND OFF TEST: [what a muted viewer understands]
POSTER FRAME: [time in seconds]
```

---

## Step 5: Platform-Specific Caption Standards

Apply these format rules per platform type. Never write the same caption for every platform. If the market module names a locally dominant platform not covered below, follow the closest matching format type and note the local platform explicitly.

Word counts are English words. Languages that fold more meaning into a word or are written without spaces (Korean, Japanese, Chinese, Thai, Swahili and others) match the length of the English gloss, not the literal count. Short, punchy and emotive beats long: every caption earns each line.

### Photo and stories feed platform
```
Length: 40 to 120 words for feed posts. One storytelling post a
        week may run to 200. The first line carries the post.
        Stories: 3 to 5 words max visible text.
Opener: First line must be a scroll-stopper, no "We are excited to..."
Structure: Hook → Story or context → CTA → Hashtags (last line)
Hashtag count: 8 to 12. Mix: brand (1), campaign (1 to 2), category (2 to 3),
               market cultural (2 to 4)
Language: Match brand register, formal for upper income tiers,
          the market's mass-market inflected language for broad reach,
          youth code-switch register for youth-first brands
Short video caption: Shorter, 30 to 80 words. Hook in first 3 words
              (visible before the "more" cut)
```

### Short video platform
```
Length: 30 to 80 words
Opener: First 3 words = the hook. This determines if they watch.
Tone: Direct, unpolished, real. Less brand voice, more human voice.
Hashtags: 4 to 6. Include trending local hashtags for this market's
          short video platform + 1 to 2 brand tags
Sound direction: Always note suggested audio, trending sound OR
                 specific music genre
Text overlay on video: Short. 3 to 6 words max per card.
```

### Community feed platform
```
Length: 100 to 200 words. Slightly longer than the photo feed platform
        is acceptable.
Tone: Community-first. In many markets this platform carries a
      "neighbourhood group" energy: warmer, more conversational,
      more directly receptive to the market's own colloquial
      register than the photo feed platform. For example, in Kenya
      this is more directly Swahili-friendly; in Mexico this is more
      comfortable in casual regional Spanish.
CTA: This platform typically rewards link clicks less than the photo
     feed platform, focus on comment and share CTAs
Hashtags: 3 to 5 only. Hashtags underperform here, don't over-tag.
Best post types: Carousel, single image, short native video
```

### Messaging broadcast (channel or group)
```
Length: 80 words max. Should read like a message from a person,
        not a brand broadcast.
Format: Plain text + image attached separately. No hashtags.
Tone: Most conversational of all platforms. "Hey, just wanted to let
      you know..." energy.
CTA: Direct, "Reply to order", "Tap the link", "Call us on..."
Timing: Send in the market's own morning or early-evening window,
        tied to local work rhythms. Never send late evening.
```

### Professional network (for B2B / institutional clients)
```
Length: 200 to 400 words. This platform rewards longer thoughtful posts.
Structure: Observation → Insight → Implication → CTA
Tone: Professional but human. First-person where appropriate.
Hashtags: 3 to 5. Industry + professional + this market's business tags.
No: Hard product sell, casual slang or code-switch register,
    entertainment content.
```

---

## Step 6: Caption Voice Standards

These rules apply across all platforms and all brands:

**Never open with:**
- The brand name
- "We are excited / proud / pleased to..."
- "It's [Day] and we're..."
- "Did you know?" as the literal first words
- A hashtag

**Always:**
- Write the caption aloud before finalising, if it sounds like a press release, rewrite it
- Include one specific local reference per week (a neighbourhood, a food, a cultural habit, a known moment), sourced from the market module or research, never invented
- End every caption with a clear CTA, even soft ones ("Drop your answer below" counts), except on a quiet day (Step 3)
- Use the correct language register for the market: formal use of the market's official or business language for premium and B2B, the market's own mass-market colloquial blend for FMCG, and the market's youth code-switch register for youth-first brands. For example, in Kenya this is formal English for premium, Swahili-inflected English for FMCG mass market, and Sheng for youth brands; in the Philippines the equivalent pattern is formal English for premium, Taglish for FMCG mass market, and youth-coined slang for youth brands.

**Local-language caption rules:**
- Local-language captions (where the market's brief calls for them) are cultural rewrites, not translations, the feeling must land, the words need not be literal
- Example, Kenya (Swahili): common openers that work: "Saa hii...", "Ukweli ni...", "Mama anajua...", "Wakati wa..."
- Example, a different market, Mexico City (Mexican Spanish): common openers that work: "La neta es...", "Aquí entre nos...", "Ya sabes que..."
- Never mix languages mid-sentence unless the brand is explicitly built on a code-switch register

---

## Step 7: Output Format

### Deliver as a full monthly calendar

Structure:
1. **Calendar overview**, brand, month, platform(s), total post count, pillar split, key cultural moments flagged, quiet days, dates still to confirm, and the feed look: four or five hex colours (from the brand, or proposed and marked proposed), one light and grade, one type zone rule. Every visual prompt writes the feed look out in full, so the month hangs together as one grid
2. **Week-by-week breakdown**, each week as a section with its cultural context note
3. **Per-post entries**, all six components, every post
4. **Hashtag master list**, brand hashtags + category hashtags + this market's own cultural hashtags to rotate
5. **Image production priority**, which 5 posts to brief to the designer first (usually the highest-reach moments: end-of-week posts, cultural moment posts, campaign hero posts)
6. **Open items**, every placeholder price, unconfirmed date, prize or claim the client must confirm

### Visual format
Deliver one self contained HTML file:
- Tabs for the overview, each week, the hashtag list, image priority and open items
- Per-post card carrying every component: number, date and day, pillar badge, theme, platform, format, posting time, CTA, caption, visual direction, motion brief where there is one, and any messaging broadcast
- Copy button on every caption, broadcast, visual prompt and motion brief
- Cultural moment flags highlighted in a distinct colour; quiet days shown as their own card
- Readable at 390 px phone width with no sideways scroll, in light and dark mode

### When building a single post or small set
- Deliver full per-post architecture for each requested post
- Include 2 caption variants (one in the market's dominant business language, one led by the market's local-language register) where platform allows
- Always include the visual direction as a pasteable prompt

---

## Quality Check Before Delivering

Before finalising, verify every post has:
- [ ] Pillar assigned, and pillar split is within range
- [ ] Caption written in full, not a summary or placeholder
- [ ] Caption does not open with brand name, "We are excited", or a hashtag
- [ ] Local-language captions are a cultural rewrite, not a translation
- [ ] Visual direction is a full standalone prompt with the feed look hex palette, and any pack has a blank label panel
- [ ] No invented price, offer, history, prize or promise; placeholders listed under Open items
- [ ] Posting time specified
- [ ] CTA included, except on a quiet day
- [ ] This market's cultural moment anchors used for all relevant dates, moveable faith dates checked, sensitive dates avoided and quiet days marked
- [ ] Platform-specific format applied (short video vs feed, length, hashtag count)
- [ ] Every short video, story or animated post has a compact motion brief, with the hook on screen in the first 2 seconds and a sound off test
- [ ] At least 1 community post per week
- [ ] No more than 30% of posts in Pillar 1

---

## Reference Files

- `references/global-cultural-moments.md`, the base layer of moments that recur across many markets, to be combined with a market module, never used alone.
- `references/markets/east-africa.md` and `references/markets/east-africa-calendar.md`, a worked market module for Kenya and wider East Africa: fixed annual moments, monthly social rhythms, weekly moments, sporting anchors, hashtag sets, local-language caption rules, and month-by-month content angles.
- `references/markets/TEMPLATE.md`, a blank copy for building a new market module.
- `references/motion-brief.md`, the motion brief method for short video, story and animated posts: beat grid shot list, readability law, format presets.
