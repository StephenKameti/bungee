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

Two choices at the Sat 31 Oct go or no go. Pick one in the Decisions table.

1. **Move launch one week, to Tue 10 Nov.** Same plan, every date shifts seven days. Already done on the branch `launch/plan-b-10-nov`: merge it and every page, message and date moves. The launch price runs 10 to 16 Nov. Black Friday and the Moments early bird stay where they are. Lowest risk, costs a week of almanac season.
2. **Launch on Gumroad on Tue 3 Nov.** Same copy, same files, same prices. Its fee is higher (10 percent plus USD 0.50 on direct sales), but it opens fast. Check during sign up that it pays out to your Kenyan bank or PayPal before you build anything there. Steps in `GUMROAD.md`.

Tell me in the roadmap or the repo and I will switch every link, page and post date.
