# DESIGN.md (starter)

Replace this file with the DESIGN.md exported from your Google Stitch project once the screens are final. Until then this is the source of truth.

## Concept
Darkroom and Lightbox. Warm dark app chrome so imagery glows. Every finished output sits on warm paper, like a print on a lit table.

## Colour tokens
| Token | Hex | Use |
|---|---|---|
| darkroom | #0F0E0D | app background |
| panel | #1A1816 | sidebar, panels |
| raised | #24211E | cards on dark, modals |
| hairline | #34302B | borders on dark |
| paper | #F4EFE7 | lightbox output surfaces |
| paper-line | #E2DACE | borders on paper |
| ink | #15130F | text on paper |
| text | #EFE9DF | text on dark |
| muted | #A39A8F | secondary text |
| clay | #E2572B | primary accent, focus |
| clay-tint | #3A2118 | accent backgrounds |
| safe | #2A9D8F | register tag, success |
| strong | #E9A23B | register tag, warnings |
| wild | #7A5AF8 | register tag |
| danger | #D64545 | errors |
| horizon | gradient #E2572B to #E9A23B to #2A9D8F | 3px signature line only |

## Type
| Role | Family | Sizes |
|---|---|---|
| Display | Instrument Serif (regular, italic) | 40, 56, 72, 96 |
| Interface | Hanken Grotesk 400, 500, 600 | 13 labels, 15 body, 17 lead |
| Technical | JetBrains Mono 400 | 13 |
Never all caps. Tight tracking on display sizes.

## Shape and space
8pt grid. Radius 10 inputs and buttons, 16 cards, 22 large panels. Hairlines instead of shadows; soft shadow only on popovers and drawers.

## Motion
Standard 180ms, easing cubic-bezier(0.2, 0.8, 0.2, 1). Page enter: fade plus 8px rise. Hover lift on cards: 2px. Streaming caret blinks at 1s. Everything off under prefers-reduced-motion.

## Voice
Short, confident, warm. Plain words in empty and success states ("Done." "Welcome."), switchable per workspace language. No brand names. No hyphens or em dashes.

## Bungee logo
Files in brand/. Colours sampled from the logo: slate #3F414B, lime #BEFD50. The supplied logo is slate on light, so it only sits on Lightbox paper surfaces. The darkroom chrome needs a reversed logo file (white with the lime tick) before the logo can appear there; until then the app shell uses the "Bungee Studio" wordmark in Instrument Serif. Never recolour, stretch or redraw the logo.
