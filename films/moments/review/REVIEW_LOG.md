# Moments 2027 promo review log

| Round | Hook | Readability | Motion | Variety | Composition | Brand | Sound | Three biggest problems | Fixes |
|---|---|---|---|---|---|---|---|---|---|
| 1 (contact 16:9) | 8 | 7 | 6 | 8 | 7 | 8 | 7 | Ribbon labels floated at different heights (bars hung from the top); the counter slammed in while the year was still in the centre; story chart too small with its label sitting on the ticks | Fixed height bar wells so bars grow up from one baseline, as on the page; sub line and ribbon clear before the year moves and the count starts 0.2 s later; chart rebuilt with taller bars, a bracket and a "Together, 10 Feb to 9 Mar" label |
| 2 (contact 9:16 and 1:1, transition strips) | 8 | 8 | 7 | 8 | 8 | 9 | 8 | Ribbon never shown complete before it left (both times); "October" said three times on one screen; cursor and file chip off target at preview scale | Ribbon builds in 0.06 s per month and holds 0.4 s; second ribbon starts with "Every date." so it completes; kicker becomes "Month by month"; cursor geometry measured in CSS px |
| 3 (full res stills all formats, animatic audio) | 9 | 8 | 8 | 8 | 8 | 9 | 8 | File chip covered the Diwali card in 1:1 | Taller tray for the picks beat in 1:1 so the chip lands below the list |

Animatic: −14.3 LUFS integrated, true peak −2.0 dBFS.
Poster frame: 3.6 s ("2027 is already booked." over the full year ribbon). This replaces the lockup frame in the approved list because it reads as the almanac at thumbnail size.
Final: `./finalize.sh 3.6 D "" moments`.
