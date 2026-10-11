# Key Visual

Engine: prompts/skills/key-visual-builder (SKILL.md plus references). Stitch screens: S8, S9, S15.

## Stages
| # | Stage | Input | Output schema | Checkpoint |
|---|---|---|---|---|
| 1 | Spine | Brief read back, brand kit | KVSpine | User confirms read back |
| 2 | Route axes | Spine | RouteAxes: archetype, humanisation, register, pack presence, adaptation load per planned route | Optional |
| 3 | Routes | Spine, axes, references | Route[] (6 to 8) with a real spread | User shortlists |
| 4 | Elevation pass | Routes | Route[] revised, kill list applied | None |
| 5 | Copy suites | Routes | CopySuite per route | None |
| 6 | Adaptation and build | Chosen routes | Adaptation[], BuildSheet | On demand per route |
| 7 | Motion briefs | Shortlisted routes when a moving channel is in the spine | MotionBrief per film (bumper, animated KV, short vertical video, end frame) | On demand per route |
| 8 | Close | All | Close: fire first (3), disruptive alternate, still open | None |

## Schemas (packages/shared)
```ts
Route = { id, number, name, register: "safe"|"strong"|"wild", archetype, humanisation, idea, why, layout, prompt: { text, aspect: "4:5" }, copy: CopySuite, adaptations: Adaptation[], build: BuildSheet, motion?: MotionBrief[], version }
CopySuite = { headlineA, headlineB, headlineC, subline, endline, proof, cta, localLine, localLanguage }
Adaptation = { format, ratio, call: "crop"|"reprompt", change, prompt? }
BuildSheet = { headlineZone, endlineLockup, logoPlate, packLockup, safeArea, doNot }
Close = { fireFirst: {routeId, why}[3], alternate: {routeId, why}, stillOpen: string[] }
MotionBrief = { filmLine, lengthS, ratios: string[], bpm, route: "code"|"image_to_video"|"live_action"|"hybrid", assets: string[], shots: MotionShot[], sound, posterS, buildFirst, checkBeforeFinal: string[] }
MotionShot = { barBeat, timeS, onScreen, change, camera, sound, text, holdS }
```
The motion brief method lives in prompts/skills/key-visual-builder/references/motion-brief.md. Validate in code: every hold meets the readability law (0.8 s for a label, 0.3 s per word with a 1.2 s minimum), the logo lands on a downbeat, and the shot list covers the full length.

## Direct chips map to the skill's feedback table
Make it simpler, Make it clearer, Warmer light, Pack bigger, Too serious, More local, Give me options, Closer to the reference.

## Exports
Route book (templates/route-book.html, motion brief panel included for routes that have one), PDF, prompt pack text, image zip, motion brief as Markdown or CSV for an editor or motion designer.

## Acceptance
Six to eight routes with at least two Safe, two Strong and one Wild. No two routes share an archetype and register pair. Every copy field free of hyphens and em dashes.
