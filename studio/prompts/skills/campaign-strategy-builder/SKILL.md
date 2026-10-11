---
name: campaign-strategy-builder
description: |
  Build complete, board ready campaign strategy documents for brands in any market, across FMCG, behaviour change, sports and lifestyle categories, localised through an optional market module, with motion briefs for hero films and short video executions. Trigger whenever the user asks to build a strategy, develop a campaign platform, write a creative brief, develop creative territories or produce a full campaign document, including "build a strategy for...", "give me a campaign platform for...", "develop creative territories for...", "write the insight for...", "create a creative brief for...", or when a brief, deck or research document is uploaded and campaign development is the goal. Also trigger for copy suites, campaign names or execution plans as part of a larger strategy. Use it any time the deliverable is a campaign strategy document or creative brief, even if only part of it is being built.
---

# Campaign Strategy Document Builder

## Market layer (do this first)

Before Step 1, establish the market or markets this campaign is for. Everything local, audience reading, media landscape and channel weights, retail reality, price points and currency, language for the copy suite, casting and photography direction, the cultural calendar, and regulatory notes such as alcohol or health claim rules, derives from the stated market. Never default to a generic international placeholder.

If the brief does not state a market, ask one question to confirm it, unless the user has already stated their own home market earlier in the conversation, in which case use that without asking again.

Once the market is known, look for `references/markets/<market>.md`. If a file exists, load it and use it as the source of audience, language, media, retail, casting and regulatory detail for the whole document. If no file exists, build the local specificity directly from the brief and from research into that market's audience, media landscape, retail environment, regulatory environment and cultural calendar, never generic filler.

`references/markets/east-africa.md` is supplied as a worked market module, written from Kenya as its fullest reference. `references/markets/TEMPLATE.md` is a blank copy for building a new one.

## Core Mandate

Produce a complete, client-ready campaign strategy document at the standard of a senior creative director and planner with 15+ years of experience working across the world's markets. Every output must earn the room, specific, culturally precise, commercially grounded, and creatively ambitious, for whichever market the brief names. No strategy-speak filler. No globally generic frameworks copy-pasted without localisation.

The full document runs 9 sections. They always appear in this order. Individual sections can be built standalone when the user requests it.

---

## Step 1: Intelligence Gathering

Read everything provided before asking. Extract from any uploaded brief, deck, research doc, or previous conversation output. Ask only for what is genuinely missing.

### Required Inputs
1. **Brand / product**, name, category, specific variants if relevant
2. **Campaign objective**, what behaviour must change and in whom
3. **Target audience**, or instruct the Audience Persona Builder skill to run first
4. **Market**, country, city, language context, resolved in the market layer above before continuing
5. **Mandatories**, legal, regulatory, brand guidelines, claims restrictions
6. **Budget tier**, production level (ATL-capable / digital-first / activation-led)
7. **Campaign window**, seasonal, always-on, event-linked (e.g. a major sporting tournament, a national holiday, a religious observance)

### Inferred Defaults (apply once the market is known, unless overridden)
- **Market**: as resolved in the market layer, never defaulted to any single region
- **Languages**: English or the market's business language, master, plus a local language adaptation and a youth or street register variant for youth where the market has one, per the market module
- **Media mix**: TV + OOH + Digital Social + Radio + Activation (adjust for budget tier and the market's actual media landscape)
- **Campaign architecture**: Single platform with 3 to 4 creative territories
- **Copy standard**: Award-submission quality, global award show level ambition
- **Casting**: Talent and setting authentic to the stated market, non-stock-photo aesthetic, cast by context per the market module
- **Document format**: Board-ready, suitable for client presentation, EXCOM pitch, or award submission

---

## Step 2: Campaign Type Classification

Identify the campaign type before writing. This determines which sections need deepest development.

| Campaign Type | Core Emphasis | Key Sections |
|---|---|---|
| **FMCG / Mass Market** | Insight → Platform → Copy suite | Strong Sections 3, 4, 5, 6 |
| **Behaviour Change** | Tension → Barrier analysis → Channel | Strong Sections 2, 3, 7 |
| **Product Launch** | Proposition → Proof → Visibility | Strong Sections 4, 5, 8 |
| **Event / Seasonal** | Cultural moment → Speed → Earned media | Strong Sections 3, 5, 7 |
| **Sports Sponsorship** | Fan insight → Integration → Merch | Strong Sections 2, 5, 7, 8 |
| **Institutional / Pitch** | Problem → Solution → Impact | Strong Sections 1, 2, 4, 8 |

---

## The 9-Section Campaign Strategy Architecture

---

### SECTION 1: SITUATION ANALYSIS
*What is the honest current state of this brand, category, and market?*

**Deliver:**
- Category truth: what is the category actually selling vs. what the consumer is buying
- Brand current position: awareness level, usage rate, perception gap
- Competitive landscape: who owns what territory, and what is the unclaimed space
- Cultural moment: what is happening in the stated market right now that changes the context for this brief

**Format:** 4 focused paragraphs. No bullet lists. Each paragraph makes one sharp observation.

**Standard:** The situation analysis should contain at least one observation the client does not already know: something that reframes the brief.

---

### SECTION 2: AUDIENCE ARCHITECTURE
*Precisely who are we talking to, influencing, and activating?*

Apply the 3-tier model:
- **Tier 1**, Primary: the buyer/user/decision-maker. All creative is anchored here.
- **Tier 2**, Secondary: the influencer, peer, or co-decision-maker. Creative should reach them through Tier 1.
- **Tier 3**, Amplifier: the cultural permission-giver (influencer, community gatekeeper, trade partner).

For each tier: demographics, local neighbourhood or regional context from the market layer, media behaviour, purchase trigger, and brand relationship.

**If the Audience Persona Builder skill has already been run**, pull from its output and synthesise: do not repeat in full. Write the 2-sentence strategic read per tier and move on.

**If no audience has been defined**, run a condensed version: Who / Where in the market / What moves them / What the brand must prove to them.

---

### SECTION 3: THE INSIGHT
*The single human truth that makes the strategy inevitable.*

**The insight is not:**
- A research finding, for example "67% of mothers in Nairobi wash clothes three times a week" for a Kenyan brief, or "58% of mothers in Jakarta hand-wash despite owning a machine" for an Indonesian one
- A category fact ("Bleach kills 99.9% of germs")
- A brand statement ("Our brand has been trusted for 40 years")

**The insight is:**
- A tension in human behaviour, something people feel but don't say
- A contradiction between how the consumer presents themselves and how they feel inside
- A cultural truth specific to the stated market that a global brief would miss

**Format:**
```
INSIGHT: [2 to 3 sentences. Present tense. Written as if the consumer said it themselves, their inner voice, not a planner's voice.]

ONE-LINE BRIEF INSIGHT: "[Single sentence. Quotable. Creatively triggering. This is what goes into the brief header.]"

WHY THIS INSIGHT WORKS: [2 to 3 sentences. Strategic rationale, why this truth is true for Tier 1, relevant for Tier 2, and exploitable across media.]
```

**Standard:** The one-line brief insight should be able to generate 10 different creative executions. If it only unlocks one, it is not the insight: it is the idea.

---

### SECTION 4: CAMPAIGN PLATFORM
*The strategic and creative territory the brand will own.*

**Deliver:**
```
CAMPAIGN NAME: [The platform name, 2 to 5 words. Can be in the market's local language, English, or both.]

CAMPAIGN LINE (ENDLINE): [The master copy line. Should function as the brand's voice 
for the duration of this campaign. Not a tagline, a statement of intent.]

PLATFORM RATIONALE: [3 to 4 sentences. Why this platform name and line are the right answer 
to the insight. What territory it claims. Why no competitor can credibly stand here.]

CAMPAIGN PROPOSITION: [One sentence. What the brand is promising to the consumer. 
Format: "[Brand] gives [Tier 1 audience] [functional and emotional benefit] 
because [reason to believe]".]

TONE OF VOICE: [3 descriptive words. Then one sentence expanding each. 
Not generic (not "warm, friendly, trustworthy"). Specific to this brand, this market, 
this moment.]
```

---

### SECTION 5: CREATIVE TERRITORIES
*3 to 4 distinct executional directions off the single platform.*

Each territory is a different way to tell the same truth. They should feel like siblings, same DNA, different personality.

**Per territory, deliver:**

```
TERRITORY [N], [TERRITORY NAME]
[One sentence establishing the creative idea.]

THE IDEA: [2 to 3 sentences. What this territory does. What it shows, says, or makes the 
consumer feel. Be specific, describe an actual execution, not just a concept direction.]

HERO EXECUTION: [Describe the single strongest piece of creative in this territory, 
TVC, OOH, activation, or social. Include scene/visual direction, copy line, and cast note.]

COPY LINE(S): [1 to 3 lines. In English. Then local language adaptation. Youth or street register variant if youth-targeted, where the market has one.]

BEST FOR: [Which media channel and which audience tier this territory is strongest in.]

WHY IT WORKS: [1 to 2 sentences. Psychological or cultural mechanism. What makes this 
land in the stated market that it might not land elsewhere.]
```

**Standard:** Each territory must generate a different emotional response. If two territories feel the same, one of them is a sub-execution, not a territory.

---

### SECTION 6: COPY SUITE
*The full language system for the campaign.*

**Master campaign copy:**
```
CAMPAIGN LINE: [English or the market's business language]
LOCAL LANGUAGE ADAPTATION: [not a translation, a cultural rewrite into the market's dominant local language]
YOUTH OR STREET REGISTER VARIANT: [youth-register version, where the market has one]
```

**Per medium: standard copy elements:**

**OOH / Billboard:**
```
Headline: [Max 7 words. Works as a standalone sentence in a 2-second read.]
Body copy: [Optional. Max 10 words if present.]
Super/lockup: [Product name + campaign line]
Local language adaptation of headline:
```

**TVC (30s structure):**
```
SCENE DIRECTION: [Opening shot, what the viewer sees in seconds 0 to 5]
NARRATIVE ARC: [What happens, told in 4 beats]
VO / DIALOGUE: [Key spoken lines, local language and business language as appropriate]
SUPER: [On-screen text at close]
END FRAME: [Product shot + campaign line + logo]
CAST NOTE: [Who is in this ad and why]
```
When the hero film is chosen for production, expand it into a full motion brief (`references/motion-brief.md`): the 30 s structure becomes a 15 bar shot list on a 120 BPM beat grid, with the end frame on a downbeat.

**Radio (30s):**
```
OPEN: [First 5 seconds, the hook that stops the dial from turning]
BODY: [10 to 15 seconds, story or argument]
CTA: [5 seconds, what to do now]
SIGN-OFF: [Brand name + campaign line read as VO]
```

**Social (channel-type specific):**
```
IMAGE FEED CAPTION: [Conversational, 2 to 3 lines, hashtag at end]
SHORT VIDEO HOOK: [First 3 words of the caption, the scroll-stopper]
SHORT VIDEO FILM: [10 to 15 s. Hook on screen in the first 2 s, two beats of value, call to action. Brief it with the short vertical post preset in references/motion-brief.md]
COMMUNITY FEED CAPTION: [Slightly longer, community-oriented, question or call to action]
MESSAGING APP SHARE: [For group buy / community group share, brief, direct, shareable]
```

**Copy tone rules:**
- Never open with the brand name
- Never use "We are proud to..." or "We are excited to..."
- Every line should work spoken aloud, if it reads awkwardly spoken, rewrite it
- Local language copy is a cultural rewrite, not a translation, the feeling must be the same, the words need not be
- Youth or street register copy requires authentic register, not tokenistic, not condescending

---

### SECTION 7: CHANNEL & TOUCHPOINT MAP
*Where the campaign lives and what it does at each touchpoint.*

**Format: per channel:**
```
[CHANNEL NAME]
Role in the campaign: [What job does this channel do, build awareness / drive trial / 
create conversation / close the sale]
Audience tier served: [Tier 1 / 2 / 3]
Key message: [The one thing this channel must communicate]
Format / spec: [Duration, dimensions, production notes]
Timing: [When in the campaign window]
KPI: [What does success look like here]
```

**Standard channel set for FMCG, adjust to the market's actual media landscape from the market layer:**
- TV (free-to-air channels, name the market's actual broadcasters)
- Radio (business-language adult contemporary, mass-market local-language stations, youth and vernacular stations, per the market module)
- OOH (the market's major arterial roads, city centre, and neighbourhood-level boards, named from the market layer)
- Digital Social (short video platforms, image-led platforms, community platforms, by audience tier)
- Messaging app (group seeding, community group networks)
- Activation / BTL (neighbourhood, supermarket, market, school)
- Influencer / earned media partnership

**Adjust channel set for:**
- Youth campaigns: add the market's leading short video and video-sharing platforms, neighbourhood activations, school gate
- Premium/luxury: replace mass radio with podcast, add experiential
- Behaviour change: add community health workers, relevant religious or civic institutions, school curriculum

---

### SECTION 8: CAMPAIGN EXECUTIONS OVERVIEW
*The full picture of what gets made.*

**Hero executions (must-produce):**
List 3 to 5 flagship pieces across media. Per execution:
- Title
- Format and spec
- Which territory it lives in
- Key visual / scene description (2 to 3 sentences)
- Production complexity: Low / Medium / High
- Award potential: Yes / No, and which category

**Support executions:**
List the supporting content, social cutdowns, radio scripts, POS materials, activation collateral.

**Motion briefs (for every hero execution that moves):**
For each hero film, bumper, kinetic social or short vertical video, attach a motion brief from `references/motion-brief.md`: film line, spec and build route, assets, the shot list on the beat grid, sound, on screen text in the market's language, and the poster frame. Keep the brief to the hero pieces; cutdowns inherit the hero's grid and are listed as formats, not rebriefed.

**Production mandatories:**
```
CASTING DIRECTION: [Who is in this campaign, demographics, tone, authenticity notes]
LOCATION: [Named locations from the stated market, not "urban setting"]
PALETTE: [Brand colours, hex codes]
PHOTOGRAPHY STYLE: [Photorealistic / editorial / documentary / stylised]
CAMPAIGN CONSTRAINT FLAGS:
  - [ ] No national flags / jerseys if a sports tournament applies
  - [ ] Claims compliance (check with legal before lockup)
  - [ ] Child safety protocols if minors featured
  - [ ] Supers / disclaimers required
```

---

### SECTION 9: STRATEGIC SIGN-OFF
*The closing statement that anchors everything.*

**Deliver:**
```
THE CAMPAIGN IN ONE PARAGRAPH:
[5 to 6 sentences. What this campaign is. Who it speaks to. What it says. 
How it says it. What behaviour it changes. Written as the opening paragraph 
of an award submission, compelling, specific, proud.]

THE BRIEF INSIGHT (REPEATED):
["[One-line insight]"]

THE CAMPAIGN LINE (REPEATED):
["[Campaign endline]"]

NEXT STEPS:
1. [First action, usually: Audience/insight validation / consumer qual]
2. [Second action, concept development / creative brief to team]
3. [Third action, production briefing / budget allocation]
4. [Fourth action, media plan / channel booking]
```

---

## Output Format

### Full document delivery
When building the complete strategy:
1. Title page: Brand / Campaign name / Date / Prepared by [Agency or author name, ask the user if unknown]
2. All 9 sections in sequence, each with a clear heading
3. Strategic sign-off as the final page
4. Append: Deck conversion note, how many slides this strategy translates to and which sections map to which slides
5. Append: Motion briefs for the moving hero executions, one per film, after the sign off

### Partial delivery
When the user requests a single section (e.g. "write the insight" or "give me the creative territories"):
- Deliver that section in full, at full depth
- Add a one-line bridge note: what section it connects to next
- Offer to continue to the next section

### Board-ready formatting rules
- Each section starts on its own clear heading
- No bullet lists in narrative sections (Situation Analysis, Insight, Platform Rationale, Sign-Off)
- Bullet/structured format only for Copy Suite, Channel Map, and Mandatories
- Copy lines always presented as: `Business language / Local language adaptation / Youth or street register (if applicable)`
- Bold the one-line brief insight and the campaign line, always
- Every section ends with a one-line strategic implication for the creative team

---

## Quality Check Before Delivering

Before finalising, verify:
- [ ] Situation analysis contains one observation the client doesn't already know
- [ ] Insight is a human tension, not a category fact or research statistic
- [ ] One-line brief insight can unlock 10 different executions
- [ ] Campaign platform name and line are distinct, not interchangeable
- [ ] 3 to 4 creative territories feel like siblings, not duplicates
- [ ] Every copy line works spoken aloud
- [ ] Local language copy is a cultural rewrite, not a word-for-word translation
- [ ] Youth or street register variant is authentic to the market's own register, where the market has one
- [ ] Channel map assigns a specific role and KPI to each channel
- [ ] Hero executions include production complexity and award potential notes
- [ ] Every moving hero execution has a motion brief with a beat grid shot list, readable holds and the end frame on a downbeat
- [ ] Strategic sign-off reads like an award submission opener
- [ ] No generic strategy-speak ("leverage synergies", "holistic approach", "360-degree campaign")
- [ ] No stock-photo casting divorced from the stated market in any visual direction note
