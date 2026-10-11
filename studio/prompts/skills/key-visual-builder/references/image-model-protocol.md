# Image Model Protocol

Everything in this file exists because a refusal or a wrong pack render costs a working day. Follow it exactly. It is written for the default photoreal image model this skill assumes, but the four fixes and the refusal ladder hold for any current generation image model.

---

## 1. The four fixes

These four are the difference between a working set and a set that gets refused.

**1. Never upload a reference with visible brand marks.** Competitor caps, sleeve logos, branded club heads, a rival pack in the background of a shot. Most image model providers block generation that appears to reproduce trademarks, and separately block image to image on identifiable real people. Either one fires alone. Crop the marks out, or describe the direction in text only.

**2. Delete every negative clause.** Most current image models have no reliable negative prompting. Writing "no logos, no watermarks, no brand marks" puts those exact tokens into the request, and some safety layers read that as an attempt to strip attribution. Write what is present instead.

| Instead of | Write |
|---|---|
| No logos on the shirt | Plain solid colour apparel in a smooth unprinted cotton |
| No text in the image | Surfaces are clean and unmarked |
| No other brands visible | The shelf behind holds plain unlabelled containers |
| Don't render the label | The label face is a smooth blank panel in flat cream |

**3. Never stack race plus gender plus age.** "A Black Kenyan woman, late 20s" is the exact pattern most person generation policies watch, and the same is true of the equivalent stacked description for any other market. Use context instead of category.

> A woman with deep brown skin and short natural hair, photographed in a Nairobi apartment kitchen in morning light.

Same casting outcome. Clean pass. The market changes, the discipline does not, for example:

> A woman with straight dark hair, photographed in a Mexico City apartment kitchen in morning light.

**4. Never describe likeness duplication.** "Ghosted echo of the same woman", "the same man repeated", "clone" all read as deepfake adjacent. Write "a multiple exposure photograph capturing several phases of a single movement."

---

## 2. Pack and logo fidelity

**The rule: generate the form, place the art in post.**

Generative models cannot render your client's pack artwork correctly. Not the wordmark, not the variant name, not the weight declaration, not the barcode. A deck with a wrong pack in it loses the room.

How to write the pack into a prompt:

> A rectangular 250g cheese wedge in a tight vacuum film wrap, the top face angled to the light. The label panel across the front is a smooth blank rectangle in flat cream, occupying the centre third of the pack face, held clean and evenly lit.

That gives the designer a lit, correctly angled, correctly proportioned blank plate to drop the real artwork onto. Note it in the build sheet with the coordinates.

For a tub, a sachet, a bottle, a tube, describe: form, material finish, how light behaves on it, the angle, and the blank panel with its position and proportion.

---

## 3. Image to image, and evolving an approved KV

Image to image mode on the default photoreal model is the strongest route for this. It is how you get from one approved master to a whole campaign.

**Workflow:**

1. Start from the approved master, cropped so no brand mark, no readable type and no identifiable third party face is visible
2. Change one thing per pass. Ratio, or casting, or background, or time of day. Never three at once
3. State what is held constant explicitly: "keep the lighting direction, the colour grade and the composition unchanged"
4. State the change in the present tense: "the background becomes a softly blurred bathroom with steam on the mirror"

**For a male and female pair of the same KV,** generate the two independently from the same base prompt with the subject clause swapped, rather than asking for a modification of the first. Modification passes drift the grade and the crop, and the pair stops matching.

**For an adaptation set,** reprompt vertically rather than crop. A 9:16 story built by cropping a 4:5 master always loses the mechanism.

---

## 4. The refusal ladder

If it refuses, do not rewrite the whole prompt. Strip to bones and add clauses back one at a time until you find the trigger. Four or five attempts finds it.

**Base:**

> Editorial photograph of a woman preparing food in a bright kitchen, warm morning light through a window, 85mm, shallow depth of field.

Then add, in this order, testing after each:

1. The mechanism clause
2. The pack clause
3. The casting context clause
4. The palette and hex clause
5. The styling and wardrobe clause

**Most common triggers, in order of likelihood:** a negative clause, a stacked category casting description, a named real person or place that reads as a public figure, a described brand mark, an implied minor in a commercial context.

**Fallback when a technique will not generate:** produce the clean component frames separately from an identical base prompt and composite in an image editor. Multiple exposure, ghost trails, split screens and before and after pairs are all better controlled in post anyway, and it is what a retoucher would do regardless.

---

## 5. Children in frame

Any KV with children present. Conservative framing, parent or teacher present in or implied by the scene, school or community or home context, fully clothed, no close crop on a single child's face, activity led rather than portrait led. Describe the setting before you describe the child.

---

## 6. Prompt hygiene checklist

- [ ] Zero negative clauses, or one short one at the very end
- [ ] Casting by context, never stacked category
- [ ] Every colour carries a hex
- [ ] Pack label face described as a blank panel
- [ ] Text zone as a percentage with a named position
- [ ] Action written in present tense
- [ ] Lens and depth of field stated
- [ ] Craft tags appended
- [ ] No named real people, no named competitor brands
