# Content Calendar

Engine: prompts/skills/social-content-calendar-builder plus data/moments-2027.json (global moments and regional packs). Stitch screen: S13.

## Stages
| # | Stage | Input | Output schema | Checkpoint |
|---|---|---|---|---|
| 1 | Setup | Brand kit, markets, month, platforms, campaign | CalendarBrief | Confirm |
| 2 | Pillars and rhythm | CalendarBrief | Pillar[] with target share, weekly rhythm | User adjusts shares |
| 3 | Month plan | Pillars, moments for markets and month | Post[] skeleton on dates | User drags posts |
| 4 | Posts | Skeleton | Post[] full | Per post approve |

## Schemas
```ts
Post = { id, date, time, platform, format, pillar, title, captions: Record<languageCode, string>, hashtags: string[], visualDirection, motion?: CompactMotionBrief, momentId?, status: "draft"|"approved" }
CompactMotionBrief = { lengthS, ratios: string[], bpm, route, hookOnScreen, beats: { barBeat, change, text, holdS }[], sound, soundOffTest, posterS }
Pillar = { name, colour, targetShare, description }
```

## Rules enforced in code
Every short video, story or animated post carries a CompactMotionBrief. No promotional post on a moment with category Sensitive. Pillar drift warning above 10 points. Moments filtered by selected markets.

## Exports
XLSX, CSV, ICS, PDF month view. Motion briefs export in the spreadsheet as their own tab, one row per beat.
