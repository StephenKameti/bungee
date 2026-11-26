# If Fri 27 Nov is missed

Written Thu 19 Nov 2026. A proposal, not a plan. Nothing moves until you pick.

Go or no go for 27 Nov is still **Tue 24 Nov, 18:00 Nairobi**. Lemon Squeezy works only if submitted today, with approval Tue 24 Nov at best. Gumroad set up by Mon 23 Nov is the safer route.

If 27 Nov is missed, the Black Friday offer and the Moments early bird (to 30 Nov) both lapse. Two ways to go after that.

| | A. Tue 8 Dec | B. Tue 12 Jan |
| --- | --- | --- |
| Why | Planners lock 2027 in December. Moments 2027 is most useful now | Clean start after the holiday pause, one week before Studio |
| Store step | Gumroad set up by Fri 4 Dec | Gumroad set up by Fri 8 Jan |
| Launch price | Moments 2027 at USD 29 for launch week, 8 to 14 Dec | Moments 2027 at USD 29 for launch week, 12 to 18 Jan |
| Clashes | Ends a week before the holiday pause | Studio beta runs 4 to 10 Jan; Studio launch 19 Jan shares the list of 50 |
| Risk | Short runway before the pause | Two asks of the same 50 people in eight days |

My pick: **A, Tue 8 Dec.** The almanac sells on timing, and December is when teams plan the year. Studio keeps January to itself.

Either way the prices you set on 11 Oct stand; only the Moments launch week price is new. Say A or B and the price, and I will build the branch the same day.

**Mon 23 Nov 2026: ready.** `ops/launch/set_launch.py` now takes late dates (1 to 15 Dec, 5 to 12 Jan). It moves every launch date, turns the Moments early bird lines into the USD 29 launch week price on the site, store pages and messages, and swaps the Black Friday section for a short note. Option A is built on branch `launch/dec-8` (Gumroad), not merged. Say A and the price, and merge it: https://github.com/StephenKameti/bungee/compare/main...launch/dec-8

**Thu 26 Nov 2026: 27 Nov is off.** No store by the Tue 24 Nov go or no go. Option B is now built too, on branch `launch/jan-12` (Gumroad set up by Fri 8 Jan, go or no go Sat 9 Jan, 18:00), not merged. Both branches merge cleanly into today's main and pass the site and posts checks. A: https://github.com/StephenKameti/bungee/compare/main...launch/dec-8 . B: https://github.com/StephenKameti/bungee/compare/main...launch/jan-12 . My pick is still A, and A needs Gumroad by Fri 4 Dec.
