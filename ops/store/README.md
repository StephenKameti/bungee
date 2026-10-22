# Store copy

Everything for the Lemon Squeezy store, ready to paste. One file per product, two bundles, and the policies. Store goes live Sun 1 Nov 2026; products launch Tue 3 Nov 2026.

## Files

| File | Product | Price (USD) | Paystack (KES) | Headline |
| --- | --- | --- | --- | --- |
| `key-visual-builder.md` | Key Visual Builder | 29 | 3,800 | The client wants options. By tomorrow. |
| `fsu-display-units.md` | Retail Display Theatre | 29 | 3,800 | Plain shelves sell nothing. |
| `designed-deck-builder.md` | Designed Deck Builder | 29 | 3,800 | Your deck looks like a template. |
| `social-content-calendar-builder.md` | Social Content Calendar Builder | 29 | 3,800 | Thirty days. Nothing planned. |
| `audience-persona-builder.md` | Audience and Persona Builder | 29 | 3,800 | "Women, 25 to 45" is not a person. |
| `campaign-strategy-builder.md` | Campaign Strategy Builder | 29 | 3,800 | Board meeting. Monday. |
| `moments-2027.md` | Moments 2027 | 39 (early bird 29 to 30 Nov) | 5,000 (early bird 3,800) | 2027 is already booked. |
| `bundle-all-six.md` | All six skill packs | 129 | 16,500 | Brief at six. Pitch at nine. |
| `bundle-everything.md` | Everything (six packs plus Moments 2027) | 149 | 19,500 | Brief at six. Pitch at nine. |
| `POLICIES.md` | Refund policy, terms of sale, privacy notice | | | Draft, not legal advice, Stephen to approve |

Each product file has the store fields (name, price, SEO title, meta description, film, poster, delivery file), the description to paste, and three FAQ items.

## Paystack prices in Kenyan shillings

Rate used: **1 USD = 129.75 KES**, mid market, checked Mon 12 Oct 2026 (allratestoday.com live converter). Prices are rounded to friendly figures, slightly under the straight conversion on the bundles so they still feel like the deal.

| USD | Straight conversion | KES price |
| --- | --- | --- |
| 29 | 3,763 | 3,800 |
| 39 | 5,060 | 5,000 |
| 129 | 16,738 | 16,500 |
| 149 | 19,333 | 19,500 |

Rechecked Thu 22 Oct 2026: **1 USD = 129.86 KES** (exchange-rates.org, 05:00 UTC). That is a 0.1 percent move, so the KES prices stand.

Rule: if the shilling moves more than 3 percent, reprice.

## Films and posters

Every page attaches its 16:9 film and its poster. Renders are kept out of git: rebuild them with `films/README.md`, then take them from each film's `out/` folder (the packaged set also lands in the films outputs folder via `films/package.sh`).

| Product | Film | Poster |
| --- | --- | --- |
| Key Visual Builder | `kv_16x9.mp4` | `kv_poster.png` |
| Retail Display Theatre | `fsu_16x9.mp4` | `fsu_poster.png` |
| Designed Deck Builder | `deck_16x9.mp4` | `deck_poster.png` |
| Social Content Calendar Builder | `cal_16x9.mp4` | `cal_poster.png` |
| Audience and Persona Builder | `persona_16x9.mp4` | `persona_poster.png` |
| Campaign Strategy Builder | `strat_16x9.mp4` | `strat_poster.png` |
| Moments 2027 | `moments_16x9.mp4` | `moments_poster.png` |
| Both bundles | `suite_16x9.mp4` | `suite_poster.png` |

If the store's media slot takes images only, use the poster as the cover image and host the film on the site.

## Delivery files

Build with `python3 scripts/build_products.py`. Each pack downloads as `dist/<slug>.zip` (guide, licence and the inner skill zip buyers upload to Claude). Moments 2027 downloads as `dist/Bungee-Moments-2027.zip`. Bundles attach every zip they include.

## Copy rules applied

* No employer, client or third party brand names. Claude is named because it is the platform.
* No trademarked event names. Moments 2027 is described generically ("the biggest football final in the United States"); the almanac file itself keeps the real names.
* Every product sold for any market. East Africa appears only as an included regional module.
* No hyphens or dashes in the copy.

## Open points for Stephen

1. **Install wording.** Resolved 12 Oct: the pack READMEs now match the store pages (any plan, Free included).
2. **Refund rule.** `POLICIES.md` proposes a 14 day refund when a product will not install or open, and no refund for a change of mind after download.
3. **Paystack prices.** Approve the KES figures above.
4. **Policies.** Fill in the bracketed details (address, contact email, governing law) and have the drafts checked.
