# Audience and Persona Builder test run, Brief A: Nuri Table, Seoul

Test record. Skill: `products/skills/audience-persona-builder/skill/` at the commit checked out on 12 October 2026, run exactly as SKILL.md instructs, as if a user had sent the brief below in one message. Everything from section 1 down is the deliverable as the skill specifies it: Part 1, the interactive audience architecture widget, is saved beside this file as `brief-a.html`; Part 2, the written brief input, is section 4 below.

**Brief as sent:** Nuri Table is a new weekly box of home style side dishes and two soups, delivered chilled every Sunday night across Seoul. KRW 29,000 a week, no contract, pause any week. Objective: trial among people who live alone. Launch: February 2027. Channels: social video, the national messaging app's gift shop, subway, convenience store pickup lockers. Who are we talking to?

**Where the run had to interpret the skill** (scored in SCORE.md):
* Step 1 says "extract what you can, then ask for what's missing". A one message brief cannot answer, so the two missing inputs (existing audience assumption, category context) carry stated working assumptions and the run proceeds.
* No market module for Korea exists, so the market layer is built from the brief and research, as SKILL.md says. The skill gives no rule for marking unverified figures; the run marks every number that is not from the brief or a source as an estimate.
* Step 4 has no variant for subscription or direct to consumer food. The run uses FMCG / Mass Market emphasis (purchase channel, price) with the Premium variant's weekend routine.
* The skill asks for the internal voice "in their actual local language register" but says nothing about a gloss. The run adds an English gloss after each Korean quote so a non Korean reviewer can read it.
* Part 2's template says Tier 3 gets an "adapted profile", but the quality check asks every tier for a 6+ moment day in the life. The run gives Tier 3 all six components to satisfy both.
* The skill names platforms generically in its own examples but never says to. The run names every platform, retailer and app by type.
* The widget has no specification (format, file, layout). The run builds a single HTML file.

---

## 1. Market layer

No `references/markets/korea.md` exists. Built from the brief and research.

| Area | What the market layer sets |
|---|---|
| Language | Korean. Peers speak in banmal (casual speech); brands that want closeness borrow it carefully. The solo living vocabulary is the register this brief lives in: honbap (eating alone), jachwi (living on your own and cooking for yourself), naengpa (clearing out the fridge). English loan words are common in product talk, not in feelings. |
| Income / social tier | Korea's own reference is Statistics Korea's household income quintiles (1st, lowest, to 5th, highest). For single person households, housing tenure is the visible signal everyone reads: owned apartment, jeonse (large lump sum deposit), wolse (monthly rent) officetel or one-room, gosiwon (a tiny exam room). |
| Geography | See the area table below. Gwanak-gu (Sillim, Bongcheon) has one of Seoul's highest concentrations of people living alone. |
| Purchase channels | Convenience stores on every corner (the default solo dinner), large discount marts, traditional markets (Sinwon market in Sillim, Mangwon market), dawn delivery grocery apps, food delivery apps, the messaging app's gift shop for sending food and coupons to others. |
| Media | The national messaging app (chat, gift shop, open chat rooms), short video and long video platforms, the portal site's news and blogs, webtoons on the commute, subway screens and platform walls. |
| Currency | KRW. Convenience store lunchbox about KRW 4,500 to 6,000; a delivered single meal with fee about KRW 15,000 to 20,000 (estimates, confirm with a shelf and app check). |
| Calendar | Seollal (Lunar New Year) falls around 6 February 2027, confirm the holiday dates. Children go home and return to Seoul with their mother's food in plastic containers; by the second week those containers are empty or forgotten in the freezer. March brings new hires and new leases. |

Context fact: about four in ten Seoul households are one person, and the share among young adults is far higher ([Asia News Network](https://asianews.network/?p=227045), [Asia Economy, June 2025](https://view.asiae.co.kr/en/article/2025062508162476670)).

**Seoul area social profiles**

| Area | Tier (household income quintile) | Cultural character | Key touchpoints |
|---|---|---|---|
| Gangnam / Seocho / Songpa | 5th | Owned apartments, high spend, hagwon economy | Department store food halls, dawn delivery, private gyms |
| Mapo / Seongdong (Mangwon, Yeonnam, Seongsu) | 4th | Young professionals, café culture, design studios | Mangwon market, independent cafés, pop up stores |
| Yeongdeungpo (Yeouido, Mullae) | 4th | Finance workers, long hours | Office tower food courts, late convenience stores |
| Gwanak / Dongjak (Sillim, Bongcheon, Noryangjin) | 2nd to 3rd | Young singles, students, exam takers, one-rooms, gosiwon | Sinwon market, Sillim station convenience stores, cheap set meal restaurants |
| Guro / Geumcheon (Guro Digital Complex) | 3rd | IT and back office workers, commuters | Office canteens, Line 2 and Line 7 transfer, delivery |
| Nowon / Dobong / Gangbuk | 2nd to 3rd | Family apartment complexes, older residents | Complex community chats, traditional markets, church |

## 2. The brief, read back

| Input | From the brief |
|---|---|
| Brand / product | Nuri Table: a weekly chilled box of home style side dishes (banchan) and two soups. Mass premium: KRW 29,000 a week, about KRW 4,100 a day. |
| Campaign objective | Trial. |
| Market | Seoul, Korea. Launch February 2027. |
| Existing audience assumption | Not stated. Working assumption: the client thinks "busy young professionals". |
| Category context | Not stated. Working assumption: the real competition is not another box but the convenience store lunchbox, the delivery app, and mum's food parcel. |

**Questions** (one message brief: working assumptions used until answered)

| Question | Why it matters | Working assumption |
|---|---|---|
| Who does the client think the buyer is today? | It tells us which assumption to break. | "Busy young professionals" in Gangnam and Yeouido. |
| What does the brand compete with in the client's mind? | It sets Tier 2 and the barrier. | Convenience store meals and delivery; mum's parcel is not on the client's list. |

## 3. Part 1: Audience architecture visual

Built as an interactive widget: `brief-a.html`. Three rings, one per tier; tap a ring or a card to open it. Each card surfaces who they are, a day in the life highlight, the key psychographic, the brand relationship and the strategic implication.

## 4. Part 2: Written strategic brief input

### AUDIENCE ARCHITECTURE, Nuri Table / Launch, February 2027

---

### PRIMARY AUDIENCE (Tier 1): Seo Jiwon, 31, Sillim

**WHO THEY ARE**
```
Age range: 27 to 36
Gender: Women lead (Jiwon); men living alone are a strong second
Income / social tier: 3rd household income quintile; wolse officetel, the visible marker
Location: Sillim and Bongcheon (Gwanak-gu), Guro Digital Complex for work
Household composition: Lives alone, 23 square metre officetel, 7th floor
Employment / income source: Payroll accountant at a mid-size logistics firm, salaried
Language dominance: Korean; solo living slang with friends
```

**A DAY IN THEIR LIFE (a Wednesday in late February)**

```
06:50, Wakes to the alarm in the officetel. Opens the fridge: a container of
her mother's braised lotus root from Seollal, now two weeks old. Closes it.
Drinks a carton of soy milk standing at the counter.

07:40, Line 2 from Sillim station toward Guro Digital Complex. Reads a
webtoon episode, then a short video of a solo living creator cooking dinner
in a one-room. Saves it. She will not make it.

12:10, Office canteen with two colleagues. The talk turns to what everyone
ate last night. Two of three say convenience store. Laughter, a small wince.

15:30, The team chat room on the messaging app. A colleague sends a coffee
coupon from the gift shop for her birthday next week. She notices how easy
gifting food has become.

19:20, Sillim station exit. The convenience store by the exit has a lunchbox
promotion at KRW 4,900. She buys one with a cup of instant soup.
BRAND MOMENT: the pickup locker beside the door. A chilled box that is
already hers would beat the lunchbox on the same walk home.

20:10, Eats at her small table while a long video plays on the laptop. The
plastic tray goes in the recycling bag, which is already full.

22:30, Her mother calls from Daegu. "Did you eat?" "I ate." She does not say
what.

23:15, Scrolls a dawn delivery app, fills a basket with vegetables for a
proper weekend cook, then empties it. Last time half went in the food
waste bin.
```

**PSYCHOGRAPHIC PROFILE**
```
Core motivation: To live alone well, not just alone
Primary tension: She wants to eat like someone looks after her, but cooking
                 for one wastes food, money and the evening
Self-image: Capable and independent / wants to be seen as someone who has
            her life in order
Status signals: A tidy officetel on camera, home cooked dinners posted
                on her stories, a gatsaeng (productive life) routine
Fear / shame trigger: That her mother is right: she is not eating properly
Aspiration anchor: A small, ordered life where dinner is never the
                   problem
```

**MEDIA & PURCHASE BEHAVIOUR**
```
Primary media: Short video on the commute and in bed; solo living cooking
               creators, 22:00 to 00:00
Secondary media: The messaging app all day (chats, gift shop); webtoons on
                 Line 2; subway platform walls at Sillim and Guro
Trusted voices: Her mother on food, colleagues on value, solo living creators
                on what is worth trying
Purchase channel: Convenience store by the station exit (four nights a week),
                  dawn delivery app (weekend intentions), food delivery app
                  (Friday)
Purchase trigger: A cheap first week, and proof it will not go to waste
Price sensitivity: Spends roughly KRW 25,000 to 35,000 a week on solo dinners
                   already (estimate); KRW 29,000 is the same money, not new money
Brand loyalty pattern: Trial driven; loyal once a routine forms
```

**BRAND RELATIONSHIP**
```
Current awareness: Never heard of it (new brand)
Current perception: "Meal box" means a commitment and a fridge full of guilt
Barrier to trial/loyalty: Fear of waste: one person cannot finish a box
What would change their mind: Portions sized for one, a pause button, and
                              seeing it fit the walk home
What they need to believe: This is enough for one, and none of it ends up
                           in the bin
```

**STRATEGIC IMPLICATION FOR THE BRIEF**
```
What this means for CREATIVE: Cast her alone and content, never lonely. The
    visual world is the small table, the one bowl, the light of the officetel
    at 20:00.
What this means for MEDIA: Own the walk home: Sillim and Guro station walls,
    pickup lockers, and short video between 22:00 and midnight.
What this means for COPY: Casual Korean with solo living words she uses
    herself. Lead with "enough for one", then the price per day.
What this means for ACTIVATION: Convenience store pickup lockers at Gwanak
    and Guro station exits, with a free first week code on the locker door.
```

*"편의점 도시락 세 번이면 일주일 끝. 엄마 반찬은 냉동실에서 잠자고."*
(Three convenience store lunchboxes and the week is over. Mum's side dishes sleep in the freezer.)

**She is not lonely at dinner. She is tired of eating like nobody cares.**

---

### SECONDARY AUDIENCE (Tier 2): Lee Mihwa, 58, Daegu

**WHO THEY ARE**
```
Age range: 52 to 65
Gender: Women (mothers of children living alone in Seoul)
Income / social tier: 3rd to 4th household income quintile; owns an apartment
                      in a 1990s complex
Location: Suseong-gu, Daegu (also Gwangju, Daejeon, Busan, the Gyeonggi
          satellite cities)
Household composition: Lives with her husband; two adult children in Seoul
Employment / income source: Part time at a pharmacy counter; husband near
                            retirement
Language dominance: Korean, Gyeongsang dialect
```

**A DAY IN THEIR LIFE (the Sunday after Seollal)**

```
07:00, Kitchen. Portions the leftover Seollal food into containers for
Jiwon: japchae, jeon, braised beef. Labels each with a marker.

09:30, Church in Suseong-gu. After the service, the women talk about their
children in Seoul. One says her son eats ramen every night. Nods all round.

11:30, Courier counter at the apartment complex. Pays for a chilled parcel
to Sillim. The box weighs 6 kilograms. She worries it is too much and not
enough at the same time.

14:00, The family chat room on the messaging app. Sends a photo of the
parcel. Jiwon replies with a heart and nothing else.

17:00, Watches a long video about health after 50, then a short clip of a
young woman eating alone in a one-room. Thinks of her daughter.

19:30, Her friend shows her the messaging app's gift shop: you can send a
meal to someone's phone. BRAND MOMENT: a gift option that sends a week
of home style food without a 6 kilogram box.

21:30, Calls Jiwon. "Did you eat?"
```

**PSYCHOGRAPHIC PROFILE**
```
Core motivation: To keep feeding her child from 240 km away
Primary tension: She wants to care for Jiwon, but the parcels arrive too big,
                 and she knows half goes uneaten
Self-image: The family's cook and keeper / wants to be seen as a mother
            whose children are well
Status signals: Children with good jobs in Seoul, food that tastes like
                hers
Fear / shame trigger: That her daughter is thin, tired and too proud to say
Aspiration anchor: Knowing Jiwon eats well on a Wednesday, not just at
                   Seollal
```

**MEDIA & PURCHASE BEHAVIOUR**
```
Primary media: The messaging app (family chat, friends' group, gift shop),
               all day
Secondary media: Long video health and cooking channels, evening TV dramas
Trusted voices: Church friends, her sister, pharmacy colleagues
Purchase channel: Traditional market and the large discount mart for her own
                  kitchen; the gift shop for sending
Purchase trigger: A friend who already sends it; a gift that looks like care,
                  not a shortcut
Price sensitivity: Spends more than KRW 29,000 on one parcel's ingredients and
                   courier (estimate); price is not the barrier, pride is
Brand loyalty pattern: Loyal once trusted
```

**BRAND RELATIONSHIP**
```
Current awareness: Never heard of it
Current perception: Bought food for her child feels like giving up
Barrier to trial/loyalty: Taste and pride: it must taste like home
What would change their mind: Hearing it is made the home way, and being the
                              one who sends it
What they need to believe: Sending Nuri Table is still her cooking for Jiwon,
                           just on the weekdays
```

**STRATEGIC IMPLICATION FOR THE BRIEF**
```
What this means for CREATIVE: Frame Nuri Table as mum's weekday kitchen, a
    gift she sends, never a replacement for her cooking.
What this means for MEDIA: The messaging app's gift shop as a media channel in
    the two weeks after Seollal and before Chuseok.
What this means for COPY: Warm, respectful Korean; "send" and "for your
    child" lead; never imply her parcels are too much.
What this means for ACTIVATION: A Seollal return gift card in the courier
    parcel, so her next box can be a Nuri Table week.
```

*"반찬 보내도 반은 버린다는 거, 나도 알아."*
(I know half the side dishes I send get thrown away.)

**Let mum send the weekdays. She already sends the holidays.**

---

### AMPLIFIER AUDIENCE (Tier 3): Kang Doyun, 27, Mangwon dong

**WHO THEY ARE**
```
Age range: 24 to 34
Gender: Mixed; Doyun represents the solo living creators
Income / social tier: 4th quintile income, 2nd quintile housing: a semi
                      basement one-room he has made famous
Location: Mangwon dong (Mapo-gu); films at Mangwon market
Household composition: Lives alone
Employment / income source: Video editor by day; solo living cooking channel,
                            about 180,000 followers (illustrative)
Language dominance: Korean; fast, funny, self mocking
```

**Role, reach, trust mechanism:** Doyun's audience trusts him because his kitchen is as small as theirs and he shows the failures. When he says something is worth it for one person, it is permission to stop feeling guilty about not cooking.

**A DAY IN THEIR LIFE (a filming Saturday)**
```
10:00, Mangwon market for ingredients, filming the prices on a small camera.
12:00, Cooks one dish in the one-room on a single induction ring.
15:00, Edits; the comments ask "how do you not waste food?"
18:00, Posts a 60 second short. BRAND MOMENT: a "one week, one fridge shelf"
       challenge with a Nuri Table box.
21:00, Live chat with viewers about food waste and electricity bills.
23:30, Answers DMs from viewers who live alone and are tired.
```

**PSYCHOGRAPHIC PROFILE**
```
Core motivation: To make living alone feel like a choice worth showing
Primary tension: Paid partnerships could break the trust he built
Self-image: Honest, scrappy / wants to be seen as the friend who has it figured out
Status signals: Comments, not followers
Fear / shame trigger: Being called out as an ad
Aspiration anchor: A book, a show, a small kitchen brand of his own
```

**MEDIA & PURCHASE BEHAVIOUR**
```
Primary media: Short video and long video platforms, his own channel
Secondary media: Open chat rooms of his fans on the messaging app
Trusted voices: Other creators, his comment section
Purchase channel: Traditional market, dawn delivery
Purchase trigger: A product that makes good content and is honest
Price sensitivity: Counts every won on camera
Brand loyalty pattern: Loyal to what his audience accepts
```

**BRAND RELATIONSHIP**
```
Current awareness: Never heard of it
Current perception: Meal boxes are for people who can afford not to care
Barrier to trial/loyalty: Fear of sounding like an ad
What would change their mind: Freedom to test it badly on camera
What they need to believe: The box survives his honesty
```

**STRATEGIC IMPLICATION FOR THE BRIEF**
```
What this means for CREATIVE: Let creators test it on camera with no script.
What this means for MEDIA: Seed 15 solo living creators in the two weeks after Seollal.
What this means for COPY: Their words, not ours.
What this means for ACTIVATION: A Mangwon market pop up with Doyun cooking from the box.
```

*"혼자 사는 게 문제가 아니라, 혼자 먹는 게 귀찮은 거지."*
(Living alone isn't the problem. Eating alone is just a hassle.)

**If Doyun can't break it on camera, it's real.**

---

### CROSS-TIER STRATEGIC READ

Jiwon does not need saving; she needs dinner to stop being a daily negotiation she loses at the convenience store door. Her mother already solves this four times a year with a 6 kilogram parcel, which is the real competitor and the real ally. Nuri Table wins by becoming the weekday version of mum's box: sized for one, sent or bought, and vouched for by creators who live in rooms as small as Jiwon's. The anchor insight: **in Seoul, living alone is fine; eating like nobody cares is not.**

---

## 5. Quality check (as the skill lists it)

| Check | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Named persona | Seo Jiwon | Lee Mihwa | Kang Doyun |
| Specific local neighbourhoods | Sillim, Bongcheon, Guro Digital Complex | Suseong-gu, Daegu | Mangwon dong, Mangwon market |
| Tier assigned in the market's own system | 3rd quintile, wolse officetel | 3rd to 4th quintile | 4th income, 2nd housing |
| Day in the life, 6+ moments | 8 | 7 | 6 |
| Named locations, media, touchpoints | Yes | Yes | Yes |
| Tension and aspiration | Yes | Yes | Yes |
| Brand relationship / barrier | Fear of waste | Pride | Sounding like an ad |
| Strategic implication as brief input | Yes | Yes | Yes |
| Internal voice quote | Yes, with gloss | Yes, with gloss | Yes, with gloss |
| No generic marketing language | Checked | Checked | Checked |
