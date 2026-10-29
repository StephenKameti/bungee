# Fallback store: Gumroad

Use this only if you pick choice 2 at the Sat 31 Oct go or no go (see the end of `SETUP.md`). Same copy, same files, same prices. About 30 minutes, all yours: sign up, payouts and terms.

Checked Thu 29 Oct 2026. Gumroad charges 10 percent plus USD 0.50 on direct sales and handles sales tax and VAT. Payouts go out weekly, every Friday, for sales at least 7 days old, with a USD 10 minimum. Gumroad pays to a bank account where it can and falls back to PayPal elsewhere. One payments guide lists Kenya for direct bank payouts, but Gumroad's own help page does not list countries, so **check the payout settings during sign up before you build anything**. If Kenya is not offered for bank or PayPal, stop and take choice 1 (launch Tue 10 Nov).

## 1. Account (10 minutes, you)

1. Sign up at https://gumroad.com with the Bungee email address, or your own for now.
2. Open Settings, then Payments. Confirm your Kenyan bank account or PayPal is accepted. This is the go or no go for Gumroad.
3. Accept the terms. Only you can do this.

## 2. The nine products (15 minutes, you)

New product, type Digital product. Use the same table as step 2 of `SETUP.md`: name, description from the copy file, price, the poster as the cover, the zip from `dist/`. Bundles: make each bundle its own product with all its zips attached, priced as in the table.

Launch price: set it as a temporary price drop or an offer code on each product, using the figures in `ops/launch/LAUNCH-PLAN.md`. Set it back on the day the plan says.

## 3. Links, list and test (5 minutes, you)

1. Copy each product's link into `checkout-links.csv`. The site build accepts any plain https link, so nothing else changes.
2. Gumroad collects buyer emails by default. For leads, turn on its follow form and paste that link in the `email-list` row.
3. Buy one pack yourself, install it in Claude, then refund it.

Paystack stays exactly as in step 5 of `SETUP.md`.

## If you later move to Lemon Squeezy

Keep the Gumroad products live until the Lemon Squeezy ones are approved, then swap the links in `checkout-links.csv`. I rebuild the site in one command.
