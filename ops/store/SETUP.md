# Store setup, in order

Your 45 minutes, step by step. Everything to paste is already written in this folder. Stop at any step that asks for money, ID or terms: those are yours anyway, and nothing here does them for you.

Checked Thu 22 Oct 2026: Lemon Squeezy still takes new sign ups. Its move to Stripe Managed Payments has no forced date yet. Stripe Managed Payments does not list Kenya as a seller country so far, so keep Gumroad as the fallback (see the end).

## The clock (checked Mon 26 Oct 2026)

Lemon Squeezy reviews every new store before it can sell. Its help page says approval typically takes 2 to 3 business days, sometimes longer. A store in test mode cannot take real money.

| Submit step 1 by | Approval likely by | Launch Tue 3 Nov |
| --- | --- | --- |
| Tue 27 Oct | Fri 30 Oct | Safe, with a weekend spare |
| Wed 28 Oct | Mon 2 Nov | Tight |
| Thu 29 Oct or later | Tue 3 Nov or later | At risk |

Build the nine products in test mode while you wait. Each one has a Copy to Live Mode button, so nothing is built twice.

Go or no go: **Sat 31 Oct, 18:00 Nairobi**. If the store is not approved by then, see the end of this page.

Rechecked Thu 29 Oct 2026: the review still typically takes 2 to 3 business days. Submitted today means approval around Mon 2 or Tue 3 Nov, which leaves no room for a slow review. Submit anyway: it is the first step of both choices below.

**Mon 2 Nov 2026: the go or no go passed with no store and no pick.** No checkout links exist, so nothing can sell on Tue 3 Nov. Do not post the launch films or send the 50 messages until a checkout link works: a launch with no way to pay burns the list. The new clock for Plan B:

| Submit step 1 by | Approval likely by | Launch Tue 10 Nov |
| --- | --- | --- |
| Tue 3 Nov | Fri 6 Nov | Safe |
| Wed 4 Nov | Mon 9 Nov | Tight |
| Thu 5 Nov or later | Tue 10 Nov or later | At risk: Gumroad, or Tue 17 Nov |

**Thu 5 Nov 2026: still no store, so Lemon Squeezy cannot make Tue 10 Nov safely.** Two launches are left before the launch price week runs into Black Friday. Both are ready on their own branch; merge one and every date, page and message moves.

| Launch | Store | Your last step | Branch to merge |
| --- | --- | --- | --- |
| Tue 10 Nov | Gumroad, no review wait | Gumroad set up by Fri 6 Nov, payouts to Kenya confirmed | `launch/gumroad-10-nov` |
| Tue 17 Nov | Lemon Squeezy | Store submitted by Tue 10 Nov, approval likely Fri 13 Nov | `launch/lemon-17-nov` |

After Tue 17 Nov the launch price week overlaps Black Friday (27 to 30 Nov), so a later launch needs a fresh call on prices first.

**Mon 9 Nov 2026: no pick by Fri 6 Nov, so Gumroad on Tue 10 Nov is off.** Tue 17 Nov is the last launch with its own price week. It now works with either store, each on its own branch:

| Launch Tue 17 Nov | Your last step | Go or no go | Branch to merge |
| --- | --- | --- | --- |
| Lemon Squeezy | Store submitted by **Tue 10 Nov** (tomorrow), approval likely Fri 13 Nov | Sat 14 Nov, 18:00 | `launch/lemon-17-nov` |
| Gumroad, no review wait | Gumroad set up by **Fri 13 Nov**, payouts to Kenya confirmed | Sat 14 Nov, 18:00 | `launch/gumroad-17-nov` |

Gumroad buys three more days. Lemon Squeezy only if you submit tomorrow. Do not merge `launch/gumroad-10-nov` or `launch/plan-b-10-nov`: both are out of date.

If neither is ready by Sat 14 Nov, one idea for you to approve, not a plan yet: skip a separate launch week and open on Fri 27 Nov with the Black Friday offer as the launch. One price story, one burst of posts, and the Moments early bird still ends 30 Nov. It needs your yes on prices before I move any dates.

**Thu 12 Nov 2026: no Lemon Squeezy store by Tue 10 Nov, so `launch/lemon-17-nov` is off.** Gumroad on Tue 17 Nov is still open until **Fri 13 Nov** (tomorrow): set up Gumroad, merge `launch/gumroad-17-nov`, go or no go Sat 14 Nov, 18:00.

If Tue 17 Nov is missed, the Black Friday launch is now ready on its own branch, `launch/black-friday-27-nov`. Merge it only once you say yes to Everything at USD 99, Fri 27 to Mon 30 Nov. Either store works:

| Launch Fri 27 Nov | Your last step | Go or no go | Branch to merge |
| --- | --- | --- | --- |
| Lemon Squeezy | Store submitted by **Thu 19 Nov**, approval likely Tue 24 Nov | Tue 24 Nov, 18:00 | `launch/black-friday-27-nov` |
| Gumroad, no review wait | Gumroad set up by **Mon 23 Nov**, payouts to Kenya confirmed | Tue 24 Nov, 18:00 | `launch/black-friday-27-nov` |

After 27 Nov the early bird and the offer are gone, and December is a slow month for buying. Treat 27 Nov as the last good launch of the year.

## 1. Lemon Squeezy account (15 minutes, you)

1. Sign up at https://www.lemonsqueezy.com with the Bungee email address once it exists (use your own email for now if the domain is not ready; you can change it later).
2. Create the store. Name: **Bungee**. Currency: **USD**.
3. Complete the identity check and add your Kenyan bank account for payouts.
4. Accept the seller terms. This is the step only you can do.

The store will be placed under review. Carry on with step 2 anyway: build the products in test mode while it waits, then copy each one to live mode once approved.

## 2. The nine products (20 minutes, you or me with you)

Make one product per file below. Pricing: single payment. Upload the zip from `dist/` (I rebuild these every check in; run `python3 scripts/build_products.py` for a fresh set).

| Product | Copy | Price | File to upload |
| --- | --- | --- | --- |
| Key Visual Builder | `key-visual-builder.md` | USD 29 | `key-visual-builder.zip` |
| Retail Display Theatre | `fsu-display-units.md` | USD 29 | `fsu-display-units.zip` |
| Designed Deck Builder | `designed-deck-builder.md` | USD 29 | `designed-deck-builder.zip` |
| Social Content Calendar Builder | `social-content-calendar-builder.md` | USD 29 | `social-content-calendar-builder.zip` |
| Audience and Persona Builder | `audience-persona-builder.md` | USD 29 | `audience-persona-builder.zip` |
| Campaign Strategy Builder | `campaign-strategy-builder.md` | USD 29 | `campaign-strategy-builder.zip` |
| Moments 2027 | `moments-2027.md` | USD 29 now, USD 39 from 1 Dec | `Bungee-Moments-2027.zip` |
| All six skill packs | `bundle-all-six.md` | USD 129 | all six pack zips |
| Everything | `bundle-everything.md` | USD 149 | all six pack zips and the Moments zip |

For each one: paste the name, the description (everything under "Product description"), the price, the poster as the cover image, then the file. Add the licence line from the copy file. Publish the product only when you are ready; drafts are fine until then.

Then copy each product's checkout link into `ops/store/checkout-links.csv` (you can edit it on GitHub in the browser). I wire them into the website with one command.

## 3. Email list (5 minutes, you)

Turn on the store's email list or newsletter signup. Copy its form or subscribe URL into the `email-list` row of `checkout-links.csv`.

## 4. Test purchase (5 minutes, you)

Buy one pack with your own card, check the download arrives and installs in Claude, then refund it. This is the "done when" test for the store.

## 5. Paystack, after the store works (15 minutes, you)

Make one payment page per product in your existing Paystack account, priced in KES from the table in `README.md`. If a payment page cannot deliver a file, set its success redirect to a thank you page and I will build that page on the site. Send me the page links the same way, in a new column of `checkout-links.csv`.

## If Lemon Squeezy refuses or stalls

Pick one in the Decisions table, or just merge its branch.

1. **Gumroad, launch Tue 10 Nov.** Same copy, same files, same prices. Higher fee (10 percent plus USD 0.50 on direct sales), but no review wait. Check during sign up that it pays out to your Kenyan bank or PayPal before you build anything. Steps in `GUMROAD.md`. Branch: `launch/gumroad-10-nov`.
2. **Lemon Squeezy, launch Tue 17 Nov.** Submit the store by Tue 10 Nov. The launch price runs 17 to 23 Nov; Black Friday and the Moments early bird stay where they are. Costs two weeks of almanac season. Branch: `launch/lemon-17-nov`.

The older branch `launch/plan-b-10-nov` (Lemon Squeezy on 10 Nov) is out of date: do not merge it.

Any other Tuesday up to 17 Nov is one command: `python3 ops/launch/set_launch.py 2026-11-17 --store lemon` (or `--store gumroad`). It moves every launch week date in the plan, the messages, the store notes, the site and CLAUDE.md, and changes nothing else.
