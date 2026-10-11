# Bungee films

Eight films made with the motion studio skill. Each one comes in 16:9, 1:1 and 9:16 at 60 fps (H.264, AAC stereo), mixed to −14 LUFS with true peak at or below −1.5 dBFS. Frame 0 of every file is its poster frame, so feeds and players show the right thumbnail before anyone presses play.

| Film | Length | Files | Poster frame |
|---|---|---|---|
| Bungee suite launch | 21 s | suite_16x9.mp4, suite_1x1.mp4, suite_9x16.mp4 | 20.2 s, the Bungee lockup |
| Moments 2027 promo | 21 s | moments_16x9.mp4, moments_1x1.mp4, moments_9x16.mp4 | 3.6 s, "2027 is already booked." over the year ribbon |
| Key Visual Builder | 15 s | kv_16x9.mp4, kv_1x1.mp4, kv_9x16.mp4 | 3.3 s, the lime name card |
| Retail Display Theatre | 15 s | fsu_16x9.mp4, fsu_1x1.mp4, fsu_9x16.mp4 | 3.3 s, the lime name card |
| Designed Deck Builder | 15 s | deck_16x9.mp4, deck_1x1.mp4, deck_9x16.mp4 | 3.3 s, the lime name card |
| Content Calendar Builder | 15 s | cal_16x9.mp4, cal_1x1.mp4, cal_9x16.mp4 | 3.3 s, the lime name card |
| Audience Persona Builder | 15 s | persona_16x9.mp4, persona_1x1.mp4, persona_9x16.mp4 | 3.3 s, the lime name card |
| Campaign Strategy Builder | 15 s | strat_16x9.mp4, strat_1x1.mp4, strat_9x16.mp4 | 3.3 s, the lime name card |

The Bungee Studio launch film is planned for after the app is built: prompt CC19 in the Studio starter pack (claude-code/BUILD-PROMPTS.md) makes it inside the app's own repo, in week 12 of the build plan.

## What is on screen

Every claim in the skill films comes from that pack's README or SKILL.md. Every date, count and card in the Moments film comes from the shipped almanac data: 160 moments, 88 in the global pack, 8 regions, Ramadan and Lent together from 10 February to 9 March, 20 moments in October, Remembrance and Veterans Day on the same date as Singles' Day, Hanukkah from 24 December beside Christmas Day. Trademarked event names are kept off screen. No brand other than Bungee appears.

Type: Instrument Serif and Hanken Grotesk for the Bungee system; Fraunces and Manrope inside the Moments film, because that film shows the almanac itself. Logo: the supplied PNG, with the lime tick split into its own layer so it lands on its own beat. Sound: original scores and effects synthesized in code (suite and skill series in A minor, Moments in D minor). No voiceover, no licensed music.

## Rebuild or change a film

You need Node 18 or later, ffmpeg, Python 3 with numpy, and Playwright's Chromium.

```
cd films/engine && npm install          # Playwright and the font packages, once
cd ../suite   && ./finalize.sh 20.2 A "" suite
cd ../moments && ./finalize.sh 3.6 D "" moments
cd ../skills  && ./finalize.sh 3.3 A skill=kv kv      # then fsu, deck, cal, persona, strat
```

Run the skill films one at a time, because they share one cues file. `finalize.sh` renders the poster, builds the sound effects from the film's cues, mixes them with the score, renders the three formats at 60 fps with motion blur and muxes the audio. A 15 second film takes about 20 minutes on two CPU cores.

Faster checks while editing:

```
node render.mjs --stills 7.5 --q skill=deck                      # one frame, full size
node render.mjs --contact 2 --sheet review/contact.png           # one frame per bar
node render.mjs --w 960 --h 540 --fps 30 --sub 1 --format jpeg   # quick silent animatic
```

Where the words live: the skill series copy is in the `FILMS` object at the top of `skills/index.html`; the Moments sections are in `SEC` and the card data above it in `moments/index.html`; the suite copy is in `suite/index.html`. Change a line, render a still to check the fit, then run `finalize.sh` again.

New score: `python3 music.py --bpm 120 --bars 11 --style clean --key A --out audio/music.wav`, then `python3 beats.py audio/music.wav beats.json --bpm 120 --phase 0` so every cue stays on the grid.

## Folder map

```
films/
  brand/        the logo PNGs and the split tick layer
  engine/       shared kit, fonts, render.mjs, music.py, beats.py, sfx.py, finalize.sh
  suite/        index.html, docs/shotlist.md, review/REVIEW_LOG.md, audio/, beats.json
  moments/      the same
  skills/       one template for all six skill films, switched with ?skill=kv|fsu|deck|cal|persona|strat
  docs/         brand notes, decisions log, the approved shot lists
```
