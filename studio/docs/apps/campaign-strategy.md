# Campaign Strategy

Engine: prompts/skills/campaign-strategy-builder. Stitch screen: S14.

## Stages
The nine sections, in order: Situation, Audience, Insight, Platform, Territories, Copy suite, Channels, Executions, Sign off.
Checkpoints: Insight (three options, user chooses) and Territories (three, user chooses or merges). Changing a checkpoint choice regenerates every later section.

## Schemas
```ts
Section = { key, title, blocks: Block[], sources: {label, origin: "brief"|"upload"|"assumed"}[] }
Block = { kind: "paragraph"|"bullets"|"table"|"quote"|"callout", content }
InsightOption = { truth, why, tension }
Territory = { name, idea, lines: string[], visualCue, risk }
Execution = { title, format, territory, scene, complexity, awardPotential, motion?: MotionBrief }
```
MotionBrief is shared with Key Visual (see docs/apps/key-visual.md). Every moving hero execution gets one after the sign off; cutdowns inherit its grid.

## Deep mode
Uses claude-opus-5 for board papers. Shown as a toggle with its extra cost.

## Exports
DOCX, PDF, deck outline that opens in Deck Designer, motion briefs as an appendix and as Markdown for an editor.
