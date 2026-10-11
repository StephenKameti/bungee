# Google Stitch prompts

One Stitch project. Paste the design system first, then one screen per prompt, in order.

## Design system (paste first)

```
BUNGEE STUDIO DESIGN SYSTEM. Use this for every screen that follows.

Product: Bungee Studio, a creative production suite for agencies and brand teams anywhere in the world. Five tools share one shell: Key Visual, Retail Theatre, Deck Designer, Content Calendar and Campaign Strategy. Users are creative directors, designers, strategists and social managers. They judge taste in seconds, so the interface must feel like a premium creative tool, never a generic SaaS dashboard.

Concept: Darkroom and Lightbox. The app chrome is a warm dark darkroom so imagery glows. Every finished output (a route, a slide, a strategy page, a calendar) sits on a warm paper lightbox surface, like a print pinned to a lit table. Dark tools, light work.

Colour
Darkroom background #0F0E0D. Panel #1A1816. Raised panel #24211E. Hairline #34302B.
Lightbox paper #F4EFE7. Paper line #E2DACE. Ink on paper #15130F.
Text on dark #EFE9DF. Muted text #A39A8F.
Primary accent Clay #E2572B (buttons, focus rings, active states). Clay tint #3A2118.
Register colours used on tags only: Safe Lake #2A9D8F, Strong Saffron #E9A23B, Wild Violet #7A5AF8. Danger #D64545.
Signature: a 3px "horizon" line, a horizontal gradient from Clay #E2572B through Saffron #E9A23B to Lake #2A9D8F. Use it sparingly: top edge of the app shell, top edge of exported documents, loading bars. Never as a background.

Type
Display: Instrument Serif, regular and italic, for page titles, route names, slide names and big numerals. Tight tracking, large sizes (40 to 96px).
Interface: Hanken Grotesk 400, 500, 600 for everything else. Body 15px, labels 13px, never all caps.
Prompts and technical strings: JetBrains Mono 13px on dark plates.

Shape and space
8pt grid. Radius 10px for inputs and buttons, 16px for cards, 22px for large panels. 1px hairlines instead of shadows. Only popovers and drawers get a soft shadow. Generous padding: cards 20 to 28px.

Components
Primary button: Clay fill, dark text #15130F, 40px high. Secondary: transparent with hairline border. Ghost: text only.
Tags: small rounded rectangles, 12px Hanken Grotesk 600, register colours as fills with white text.
Copy button: sits top right of every prompt plate and every copy line. Changes to "Copied" in Lake for 1.4 seconds.
Command palette: centred, 640px wide, raised panel, search at top, grouped results.
Step tracker: horizontal row of five steps (Brief, Read back, Explore, Refine, Deliver) with the active step in Clay.
Streaming state: text appears word by word with a thin Clay caret. A small plan list on the side ticks off stages as they complete.

Imagery
Real, warm photography of real people in real places, drawn from the markets the workspace serves: a rotation across cities such as São Paulo, Lagos, Jakarta, Warsaw, Nairobi, Mexico City and Seoul. Natural light, editorial framing, never a single "global" look. No stock handshakes, no robots, no glowing brains, no sparkles icon for AI.

Voice
Short, confident, warm. Empty and success states use plain words ("Done." "Welcome."); a workspace can switch these to its own language in settings. No brand names anywhere. No hyphens or em dashes in any interface copy.

Accessibility
Text contrast at least 4.5:1. Visible focus rings in Clay. Every interactive element reachable by keyboard.
```

## S1 Marketing landing page (Desktop web)

```
Screen: public landing page for Bungee Studio. Apply the Bungee Studio design system.

Top: thin horizon gradient line across the full width, then a slim nav on the darkroom background: wordmark "Bungee Studio" in Instrument Serif at left, links Tools, Pricing, Examples, Sign in at right, and a Clay "Start free" button.

Hero: left two thirds holds a huge Instrument Serif headline on two lines: "From brief to board ready. In one sitting." Below it one line in Hanken Grotesk muted: "Key visuals, retail theatre, designed decks, content calendars and campaign strategy, built for every market you work in." Two buttons: Clay "Start free" and a secondary "Watch the film" with a small play icon and a "0:20" label; it opens the launch film in a dark lightbox modal with captions on. The right third shows a tilted stack of three lightbox paper cards overlapping: a key visual route card with a warm photo of a Lisbon café at sunrise, a slide thumbnail, and a calendar month fragment.

Below the hero: a horizontal strip titled "One brief. Five tools." showing a single brief card on the far left with five thin lines flowing right into five tool tiles (Key Visual, Retail Theatre, Deck Designer, Content Calendar, Campaign Strategy), each tile with a small photo, the tool name in Instrument Serif and a one line promise.

Then a proof section on lightbox paper: a large before and after. Left a plain text brief pasted from a chat. Right the finished route book page with six route cards.

Then a "Built for every market" band: three short statements with photos from three different cities: "Copy in the market's own language, not translation." "Casting and places that look like there, not anywhere." "A cultural calendar that knows when to go quiet."

Footer on darkroom: small links, the horizon line, a language switcher, "Made for every market".
```

## S2 Pricing (Desktop web)

```
Screen: pricing page. Apply the Bungee Studio design system.

Title in Instrument Serif: "Pick your studio." Subtitle muted: "Prices in your currency. Cancel any time."

A currency menu top right, auto detected from location: USD, EUR, GBP, INR, BRL, NGN, KES and more.

Three plan cards side by side on raised panels, the middle one outlined in Clay with a small tag "Most teams":
Solo, one tool of your choice, USD 19 a month. Studio, all five tools, USD 59 a month. Agency, all five tools for five seats plus shared brand kits, USD 199 a month. Show local currency equivalents beneath.
Each card lists five short benefits with small check marks, the number of image preview credits per month, and a full width button.

Below: a compact credits explainer row showing that image previews use credits and text generation is unlimited within fair use, with a small calculator slider "How many key visual routes a month?" updating an estimate.

Then an FAQ accordion on lightbox paper with six questions. Payment row at the bottom shows neutral card, bank transfer and local wallet icons without any brand logos.
```

## S3 Sign up and onboarding (Desktop web)

```
Screen: three step onboarding after sign up. Apply the Bungee Studio design system.

Left half: a full height warm editorial photo of a young creative team reviewing prints on a table in a sunlit studio, with the horizon line along the top edge.

Right half on darkroom: a step tracker with three dots. Step 1 "What do you do?" shows four large selectable tiles: Creative director, Designer, Strategist, Social manager. Step 2 "Where do you work?" shows a searchable country picker with multi select (any country in the world, recent picks as chips), and a language preference for local lines that fills from the chosen countries. Step 3 "Create your first brand kit" shows a drop zone for a logo, three colour swatch pickers and a tone slider from Playful to Premium.

Show Step 2 as the active state. Bottom right: Back as ghost button, Continue as Clay button. Top right: "Skip for now" ghost link.
```

## S4 Home and project library (Desktop web)

```
Screen: signed in home. Apply the Bungee Studio design system.

Left sidebar 248px on panel colour: wordmark at top, a Clay "New brief" button, then navigation: Home, Projects, Brand kits, Moments, then a divider and the five tools each with a small line icon: Key Visual, Retail Theatre, Deck Designer, Content Calendar, Campaign Strategy. At the bottom: credits meter (a thin bar with "142 of 200 image credits"), settings, and the user avatar.

Main area: greeting in Instrument Serif "Good morning, Amara." with a muted line "Three projects moved this week."

A wide "Start from a brief" composer: a large text area with placeholder "Paste the brief, drop a PDF or deck, or describe the job", an attachment button, a row of tool chips to choose which tools to run, and a Clay "Read the brief" button.

Below: "Upcoming moments" as a horizontal scroll of small date cards from the cultural calendar (for example 27 Oct Diwali, 31 Oct Halloween, 1 Nov Día de los Muertos) with a red striped card for a sensitive date.

Then "Recent projects" as a grid of lightbox paper cards, three per row. Each card shows a cover image from the project output, the project name in Instrument Serif, client name, small tool badges used in the project, and last edited time. Hovering a card lifts it slightly.

Top bar: search field with the hint "Search or press Cmd K".
```

## S5 Brand kit editor (Desktop web)

```
Screen: brand kit editor. Apply the Bungee Studio design system.

Header: brand name "Northwind Coffee" in Instrument Serif with an edit icon, a muted line "Used in 4 projects", and a Save button.

Two columns. Left column 60 percent on lightbox paper, arranged like a brand book spread: logo tile with light and dark versions, colour swatches with hex values and roles (Primary, Secondary, Accent, Neutral), typography specimen showing a headline and body sample, a pack shot gallery of four product images on neutral backgrounds, and a "Do and don't" strip of four small image examples.

Right column 40 percent on darkroom panels: Voice settings with sliders (Playful to Premium, Local to Global, Warm to Bold), language mix chips filled from the brand's markets (for example English, Portuguese), "Always say" and "Never say" word lists as editable chips, markets served, and a "Casting notes" text field.

At the bottom right a small preview card titled "How we will sound" showing one sample headline generated from the settings.
```

## S6 New brief intake (Desktop web)

```
Screen: new brief intake, the shared entry for all five tools. Apply the Bungee Studio design system.

Step tracker at top with five steps: Brief, Read back, Explore, Refine, Deliver. Brief is active.

Centre column 760px wide. A large drop zone on raised panel with a dashed hairline: "Drop the brief. PDF, deck, Word, a screenshot of a chat, or a voice note." Below it a tab row: Paste text, Upload, Voice note. Paste text is active with a long pasted brief visible.

Under the drop zone: "Brand kit" selector showing the selected kit with its logo and colours, and "References" with three small reference image thumbnails and an add tile.

Then "What should we make?" with five large tool toggles in a row, each a card with the tool name in Instrument Serif and a one line output description. Key Visual and Content Calendar are toggled on with Clay outlines.

Right margin: a slim "What we still need" checklist that fills as the brief is read: Product, Audience, Proposition, Mandatories, Deadline. Two are ticked.

Bottom: Clay button "Read the brief" and a muted note "About 40 seconds".
```

## S7 Brief read back and plan (Desktop web)

```
Screen: brief read back with a visible plan. Apply the Bungee Studio design system.

Step tracker with Read back active.

Main area: a lightbox paper sheet titled in Instrument Serif "The brief, read back." It shows an editable two column table: Product hero, Business problem, Single minded proposition (large italic serif line spanning the width), Insight, Audience, Channels, Mandatories, No gos. Each row has a small pencil icon on hover. Two rows carry a Saffron tag "Assumed" to show where the AI filled a gap.

Right panel on darkroom 340px: "The plan" listing what will happen next, with times: Route the spread across five axes, Write eight routes, Elevation pass, Copy suites, Adaptation kits. A small toggle "Ask me before each step".

A question card between the sheet and the panel: "Is the pack the hero, or the moment?" with two answer buttons, showing the AI asks one sharp question instead of many.

Bottom bar: Back, and a Clay "Looks right. Build it." button.
```

## S8 Key Visual route spread (Desktop web)

```
Screen: key visual route spread. Apply the Bungee Studio design system.

Step tracker with Explore active. Header: project "Northwind Coffee, Lisbon launch" and campaign line in serif italic "The first cup is yours."

Filter row: All, Safe, Strong, Wild tags with counts, a sort menu, and a view switch between Grid and Wall.

Main: a grid of eight route cards, four per row, on lightbox paper. Each card: a 4:5 preview image area (three show generated warm photographic previews, the rest show an elegant empty state with the route name and a small "Preview" button), big serif route number in Clay (01 to 08), route name in Instrument Serif (Morning Light, Full Table, Low Tide, Steam Rising, The Second Half, Kettle Choir, First Light Commute, Mama's Hour), register tag, and a one line idea. Card footer: star to shortlist, a compare checkbox and a menu.

Floating bottom bar appears because two cards are selected: "Compare 2", "Generate previews (2 credits)", "Shortlist".

Right edge: a collapsible "Fire these first" panel listing three recommended routes with one line reasons, and the disruptive alternate highlighted in Clay.
```

## S9 Key Visual route detail (Desktop web)

```
Screen: single route detail. Apply the Bungee Studio design system.

Left 45 percent: large 4:5 image preview on a lightbox mat with a thin paper border, below it a filmstrip of four variations with the second selected, and buttons: Vary, Upscale, Edit area (brush icon), Download.

Right 55 percent scrolling panel on darkroom:
Route header: number 03 in large Clay serif, name "Low Tide" in Instrument Serif, Wild tag, the one sentence idea, and "Why it wins" in muted text.
Master prompt on a near black plate in JetBrains Mono with a Clay "Copy prompt" button and a small label "Image model, 4:5".
Copy suite: rows for Headline A, B, C in serif, Subline, Endline, Call to action, and a Local line in Clay italic reading "O primeiro café é teu." with a small English gloss beneath. Each row has a small Copy link.
Adaptation kit: a compact table with Feed 1:1, Vertical story 9:16, Video end frame 16:9, Billboard 2:1, Shelf talker 3:4, each with Crop or Reprompt pills and a Generate link.
Designer build sheet: headline zone, logo plate, pack lockup, safe area, and a red "Do not" line.
Motion brief: a tab beside the build sheet showing spec chips (6 s, 9:16 plus 1:1, 120 BPM, poster 5.0 s), a compact shot list table with bar.beat in Clay mono, what changes, and the on screen text in serif, a sound line beneath, and a "Copy brief" button.

Top right: a chat style "Direct this route" input: "Make it simpler", "Warmer light", "Pack bigger" suggestion chips.
```

## S10 Retail Theatre family planner (Desktop web)

```
Screen: retail display family planner. Apply the Bungee Studio design system.

Header: "Retail Theatre" in Instrument Serif, the brand kit chip, and an environment selector showing Pharmacy with alternatives Supermarket, Beauty store, Liquor store.

Top section: "The family" shown as a descending size lineup on a lightbox paper floor: a tall floor unit silhouette, a gondola end, a shelf strip and a small counter unit, left to right, each outlined, labelled and connected by a single shared material swatch row beneath them (matte lacquer ivory, light oak, brushed brass, pale stone).

Middle: "Choose one device per unit" as a horizontal library of device cards with small illustrations: Oversized pack as architecture, Glorifier and dome, Frozen motion, Campaign device in 3D, Texture wall, Light as material. The floor unit slot shows Oversized pack selected; the counter slot shows Glorifier selected.

Bottom: unit cards in a row, each with a render preview area, the unit prompt collapsed with a Copy button, dimensions, and a Saffron "Production note" flag such as "Dome needs anti glare acrylic, check pharmacy lighting".

Right drawer: "Honesty check" listing what is buildable locally, what costs more and what to fake in post.
```

## S11 Deck Designer, design language picker (Desktop web)

```
Screen: choose a design language for a deck. Apply the Bungee Studio design system.

Step tracker with Explore active. Header: "Deck Designer" and the deck name "Investor Update, 14 slides".

Three large proposal columns, each a lightbox paper panel:
1. "Ledger and Neon": deep navy and signal green swatches, a condensed grotesk headline specimen, a thin rule grid, a sample slide thumbnail.
2. "Night Harvest": warm black and harvest gold swatches, a high contrast serif specimen, full bleed photography rule, sample slide thumbnail.
3. "Editorial Storm": paper white and storm grey with one red accent, an editorial serif and mono pairing, asymmetric grid, sample slide thumbnail.
Each column lists its rules in short lines: Type, Colour, Grid, Photography, Signature move. A Clay "Use this language" button at the bottom of each.

Above the columns a slim notice: "Type is locked across every slide once you choose: same font, weight, size and styling."

Right side a narrow panel "From your deck" showing extracted slide titles 1 to 14 with a small comment bubble icon on slides 4 and 9, meaning client comments were found and will be actioned.
```

## S12 Deck Designer, storyboard (Desktop web)

```
Screen: deck storyboard and slide editor. Apply the Bungee Studio design system.

Top: a storyboard strip of 14 slide thumbnails in 16:9 on a darkroom rail, numbered, with the current slide outlined in Clay and two slides marked with a small Saffron dot "Needs review".

Main: the selected slide large on a lightbox mat, a fully designed slide with a serif headline and a warm photograph of a woman running a corner shop, cast for the deck's market.

Right panel: tabs Copy, Prompt, Comments. Copy tab active: Headline, Body, Footnote fields exactly as they appear on the slide, a locked typography spec line "Headline: Night Harvest Serif 64, Body: Grotesk 20", and a Regenerate button. The Prompt tab label shows a count of characters.

Bottom bar: Generate all slides (14 credits), Export as PDF, Export slides, Copy prompt pack.
```

## S13 Content Calendar month view (Desktop web)

```
Screen: social content calendar, month view. Apply the Bungee Studio design system.

Header: "October 2027" in large Instrument Serif with arrows, the brand chip, market chips Portugal and Brazil, and platform chips with neutral icons for short video, photo feed, messaging broadcast and professional network.

Left rail: "Pillars" with four coloured pills and their weekly share (Culture 30 percent, Product 30 percent, Community 25 percent, Value 15 percent), and "Moments this month" listing Golden Week 1 Oct, Rosh Hashanah 2 Oct, Diwali 29 Oct, Halloween 31 Oct, and a remembrance date with red striped styling marked "Go quiet".

Main: a seven column month grid on lightbox paper. Each day cell shows post chips with a pillar colour edge, platform icon, and a two word title. Moment days carry a small label strip at the top of the cell. The 20th is richly filled.

Right drawer open for one post: format, a vertical 9:16 visual thumbnail, caption tabs for each of the brand's market languages (for example English, Portuguese, Brazilian Portuguese) with the second tab active, hashtags, best time to post, a compact motion brief block for this short video post (hook on screen, five beat rows with times and on screen text, sound line, sound off test), and Approve and Regenerate buttons.

Top right: Export menu (Spreadsheet, Calendar file, PDF).
```

## S14 Campaign Strategy builder (Desktop web)

```
Screen: campaign strategy document builder. Apply the Bungee Studio design system.

Left outline rail on darkroom listing the nine sections: Situation, Audience, Insight, Platform, Territories, Copy suite, Channels, Executions, Sign off. Completed sections show a Lake tick, the current section Insight is highlighted in Clay, later ones are muted.

Centre: a lightbox paper document page with generous margins, section title "03 The insight" in Instrument Serif. Three insight option cards stacked, each with a bold one line human truth in serif italic, a short "Why it works" paragraph and a "Choose this" button. The second card is selected with a Clay outline.

Right panel: "Evidence" showing short bullet notes from the uploaded research and the brief, each with a small source chip.

Top bar: document title, a Deep mode toggle labelled "Deep thinking for board papers", share and export (Word, PDF, Deck outline).

Show text streaming into the Platform section preview at the bottom of the page with a Clay caret.
```

## S15 Export and share (Desktop web)

```
Screen: export and share dialog over a dimmed route spread. Apply the Bungee Studio design system.

Centred modal 720px on raised panel. Title in Instrument Serif "Send it out."

Left column: format choices as selectable rows with small icons: Route book (interactive web page), PDF, Slides, Prompt pack (text), Spreadsheet. Route book is selected.

Right column: a live thumbnail of the route book cover on lightbox paper, and options: include previews, include copy, include build sheets, client logo on cover, watermark drafts.

Bottom: a share link field with Copy, an access selector (Anyone with link, Only my team), and a Clay "Export" button. A small success toast example in the corner reading "Done. Route book ready."
```

## S16 Settings and billing (Desktop web)

```
Screen: settings, billing tab. Apply the Bungee Studio design system.

Left settings nav: Profile, Team, Brand kits, Billing, Usage, Data and privacy.

Billing content: current plan card "Studio" with next payment date and amount in the workspace currency, a Change plan button, and the payment method shown as a neutral card icon with last four digits and a local payment option (bank transfer or wallet) where the country supports it.

Usage card: this month's image credits as a bar (142 of 200), text generations count, and a small bar chart of usage by tool.

Invoices table: date, amount, status pill, download link.

Data and privacy note at the bottom: "Your briefs and brand files are private to your workspace and are never used to train models." with a link to delete workspace data.
```

## S17 Mobile review (Mobile 390px)

```
Screen: mobile review flow for approving work on the move. Apply the Bungee Studio design system.

Top: horizon line, project name "Northwind Coffee, Lisbon launch" and a back arrow.

A full width swipeable route card on lightbox paper: 4:5 preview image, route number and name in Instrument Serif, register tag, one line idea.

Below the card: three large thumb friendly buttons in a row: Reject (ghost), Comment (secondary), Shortlist (Clay).

Under that a collapsible "Copy" section showing Headline A and the local line with copy icons.

Bottom tab bar: Home, Projects, New brief (Clay circle), Moments, Profile.
```
