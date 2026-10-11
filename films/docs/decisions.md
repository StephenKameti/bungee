# Decisions log

- 2026-10-05 Route A (code drawn, one index.html per film, headless Chrome capture, ffmpeg). No framework needed; the films show Bungee's own pages and outputs, which are already HTML.
- Brand: logo supplied as PNG (transparent and white background versions). Colours sampled from the file: slate #3F414B, lime #BEFD50. No brand fonts supplied, so the films use the Bungee Studio pairing (Instrument Serif, Hanken Grotesk). Logged for the person to confirm.
- The lime tick is split from the real logo PNG as its own layer (pixel exact, verified by recomposite) so it can land on its own beat.
- Music: original scores synthesized in code at 120 BPM. Suite and skill series in A minor, Moments in D minor. No voiceover.
- Lengths: suite 21 s and Moments 21 s (10 bars plus held lockup), skill films 15 s (7 bars plus held lockup).
- Six skill films share one template, one score and one index.html, switched by a query parameter, so the series reads as one.
- Trademarked event names are kept off screen in the films.
- Shot lists sent for approval before any animation code (gate G5).
- 2026-10-05 Shot lists approved by the person. End cards: skill name and "Skill pack", no URL. Skill name cards carry "A skill for Claude" in small type. Type stays Instrument Serif and Hanken Grotesk.
- Pillar and status colours in the films stay inside the brand: slate, lime, sand #D9D5C7, steel #8C93A8. The one exception is a muted red #C8463D used only to mean "sensitive, go quiet", as in the almanac.
- 2026-10-05 Skill films: poster frame moved from the lockup (about 14.2 s) to the lime name card at 3.3 s. The six lockups are identical apart from a small endline, so the name card is what tells the six apart at thumbnail size.
- 2026-10-05 Moments: poster frame moved from the lockup (about 20.0 s) to 3.6 s, "2027 is already booked." over the full year ribbon. It reads as the almanac at thumbnail size.
- 2026-10-05 Moments "go quiet" beat uses Remembrance and Veterans Day (11 November), which shares its date with Singles' Day in the almanac. Chosen over remembrance days for tragedies so the film never uses a tragedy to sell. The red here is the almanac's own sensitive colour, #8E1D1D.
- 2026-10-05 Kit fix: place() now scales about its anchor (left or top), so low resolution previews match the full size render. Full size renders were unaffected, since S is 1 at 1080 based sizes.
- 2026-10-05 Skill series copy set with hand placed line breaks (one fitted size per film) so no headline ends on a single word.
