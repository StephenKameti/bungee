# Retail Theatre

Engine: prompts/skills/fsu-display-units. Stitch screen: S10.

## Stages
| # | Stage | Input | Output schema | Checkpoint |
|---|---|---|---|---|
| 1 | Ingest | Brand kit, pack shots, environment, unit list, register | RetailBrief | Confirm |
| 2 | Devices | RetailBrief | DevicePlan: one device per unit from the library | User swaps devices |
| 3 | Family | DevicePlan | Family: shared material language, size ladder floor to counter | None |
| 4 | Prompts | Family | Unit[] with prompt, dimensions, blank panels rule | None |
| 5 | Honesty | Units | Honesty: buildable locally, costs more, fake in post | None |

## Schemas
```ts
Unit = { id, type: "floor"|"gondola"|"shelf"|"counter"|"glorifier"|"testing", device, name, why, prompt: { text, aspect: "4:5" }, dimensions, materials: string[], productionNote }
Family = { materials: string[], palette: {name, hex}[], lighting, units: Unit[] }
Honesty = { buildable: string[], costsMore: string[], fakeInPost: string[] }
```

## Rules enforced in code
Exactly one theatrical device per unit. Every panel blank for type in post. Pack fidelity line present in every prompt.

## Exports
Spec sheet PDF, prompt pack, render zip.
