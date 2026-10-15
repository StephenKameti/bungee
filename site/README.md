# Bungee website

One static page plus three policy pages. No framework, no build step beyond `build.py`. Fonts are self hosted (Instrument Serif and Hanken Grotesk, OFL), so the page loads nothing from third parties.

## Files

| File | What |
| --- | --- |
| `index.html` | The landing page: hero, the six packs, Moments 2027, bundles, install steps, markets, FAQ, email signup |
| `build.py` | Writes `refunds.html`, `terms.html` and `privacy.html` from `ops/store/POLICIES.md`, then checks the site |
| `assets/` | Logo, favicon, share image (`og.png`, 1200 x 630), fonts |

## Build and check

```
python3 site/build.py
```

It fails on any hyphen or dash in visible copy, or a missing asset. It also lists what still blocks going live ("NOT READY TO DEPLOY"): blanks in the policies, empty checkout links, no email list endpoint.

Preview locally: `cd site && python3 -m http.server 8765`, then open http://localhost:8765.

## Before it goes live (Sun 1 Nov)

1. Stephen approves `ops/store/POLICIES.md` and fills the blanks. Rerun `build.py`.
2. Create the nine products in Lemon Squeezy, then paste each checkout URL into `CHECKOUT` at the top of the script in `index.html`. Empty links fall back to the bundles section.
3. Paste the email list form URL into `JOIN_ENDPOINT`. Until then the form says the list opens on launch day.
4. Deploy the `site/` folder to any static host and point the domain at it.
5. On 1 Dec, change the Moments 2027 block from the early bird price (USD 29, was 39) to USD 39.

## Copy rules

Short, punchy, no hyphens or dashes, no third party brands (Claude is named as the platform), no trademarked event names, any market first with East Africa as a module. The almanac chart data comes from `products/moments-2027/out/moments-2027.json` (count of moments per month by category); refresh the `YEAR` array if the almanac changes.
