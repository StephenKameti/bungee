#!/usr/bin/env python3
"""Move launch week to any Tuesday in one command.

Every date tied to launch day (store live, go or no go, launch price window,
one skill film a day, the waitlist line on the site, the key dates in
CLAUDE.md) is worked out from the launch date and rewritten in place.
Black Friday (27 to 30 Nov) and the Moments early bird (to 30 Nov) never move:
they are Stephen's decisions, not launch week dates.

A launch after 30 Nov (1 to 15 Dec, or 5 to 12 Jan 2027) is a late launch: the
Black Friday offer and the early bird have lapsed, so the Moments early bird
lines become a USD 29 launch week price and the Black Friday section becomes a
short note. A late launch is one way: to go back to a November date, use git.

    python3 ops/launch/set_launch.py 2026-11-17              # Lemon Squeezy
    python3 ops/launch/set_launch.py 2026-11-10 --store gumroad
    python3 ops/launch/set_launch.py 2026-11-17 --check      # show, write nothing
    python3 ops/launch/set_launch.py 2026-12-08 --store gumroad   # late launch, option A

Running it with the date already set changes nothing. Every pattern must match
exactly once, or nothing is written.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ORIGINAL = dt.date(2026, 11, 3)
FIRST_MONDAY_POST = dt.date(2026, 11, 9)
LATEST = dt.date(2026, 11, 17)  # a later launch week runs into Black Friday
BLACK_FRIDAY_END = dt.date(2026, 11, 30)
# Late windows: after Black Friday and before the holiday pause, or after the
# pause and before the Studio launch on Tue 19 Jan 2027.
LATE_WINDOWS = [(dt.date(2026, 12, 1), dt.date(2026, 12, 15)), (dt.date(2027, 1, 5), dt.date(2027, 1, 12))]

FILMS = [
    ("Key Visual Builder", "kv"),
    ("Campaign Strategy Builder", "strat"),
    ("Designed Deck Builder", "deck"),
    ("Content Calendar Builder", "cal"),
    ("Audience Persona Builder", "persona"),
    ("Retail Display Theatre", "fsu"),
]

D = r"(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) \d{1,2} (?:Oct|Nov|Dec|Jan)"
Y = r"\d{4}"


def short(d):
    return f"{d:%a} {d.day} {d:%b}"


def plan(launch, store):
    """Return {file: [(pattern, replacement), ...]} for this launch."""
    day = lambda n: launch + dt.timedelta(days=n)
    moved = launch != ORIGINAL
    L = short(launch)
    shop = "Gumroad" if store == "gumroad" else "Lemon Squeezy"

    if store == "gumroad":
        submit = f"| By {short(day(-4))} | Gumroad store set up with `ops/store/GUMROAD.md`; no review wait | You |"
        gate = f"| {short(day(-3))}, 18:00 | Go or no go: Gumroad pays out to Kenya and a test purchase works? | You |"
    else:
        submit = f"| {short(day(-7))} | Lemon Squeezy store submitted for review (2 to 3 business days) | You |"
        gate = f"| {short(day(-3))}, 18:00 | Go or no go: store approved? If not, see the end of `ops/store/SETUP.md` | You |"

    films = []
    for i, (name, code) in enumerate(FILMS, start=1):
        label = name
        if i == 6:
            label += ", plus the first Monday moment post" if not moved else ", plus that week's Monday moment post"
        films.append((
            rf"^\| {D} \| {re.escape(name)}[^|]*\| {code}_9x16\.mp4, {code}_1x1\.mp4 \|$",
            f"| {short(day(i))} | {label} | {code}_9x16.mp4, {code}_1x1.mp4 |",
        ))

    early_mondays = []
    m = FIRST_MONDAY_POST
    while m < launch:
        early_mondays.append(m)
        m += dt.timedelta(days=7)
    monday = "Every Monday from 9 Nov, post the moments eight weeks ahead, ready drafted in `monday-posts/`."
    if len(early_mondays) > 2:
        monday += f" The Monday posts before launch end with \"Out {L}.\" in place of the link."
    elif early_mondays:
        names = " and ".join(short(x) for x in early_mondays)
        posts = "post goes" if len(early_mondays) == 1 else "posts go"
        tail = "Out tomorrow." if early_mondays[-1] == day(-1) and len(early_mondays) == 1 else f"Out {L}."
        monday += f" The {names} {posts} out before launch, so end {'it' if len(early_mondays) == 1 else 'them'} with \"{tail}\" in place of the link."

    yr = launch.year
    late = launch > BLACK_FRIDAY_END
    head = f"Products launch {L} {yr}"
    if moved:
        head += f", moved from {short(ORIGINAL)} because the store was not ready"
    key = f"Key dates: store live {short(day(-2))} {day(-2).year}. Products launch {L} {yr}"
    if moved:
        key += f" (moved from {ORIGINAL.day} Nov)"

    subs = {
        "ops/launch/LAUNCH-PLAN.md": [
            (r"^Products launch .*?\. Times are Nairobi time\.", f"{head}. Times are Nairobi time."),
            (rf"^\| (?:By )?{D} \| (?:Lemon Squeezy store submitted|Gumroad store set up)[^\n]*\| You \|$", submit),
            (rf"^\| {D}, 18:00 \| Go or no go[^\n]*\| You \|$", gate),
            (rf"^\| By {D} \| Store live, ", f"| By {short(day(-2))} | Store live, "),
            (rf"^\| By {D} \| 50 names", f"| By {short(day(-2))} | 50 names"),
            (rf"^\| {D} \| Launch price set up", f"| {short(day(-1))} | Launch price set up"),
            (rf"^\| {D} \| Checkout links in the website", f"| {short(day(-1))} | Checkout links in the website"),
            (rf"^## Launch day, {D}$", f"## Launch day, {L}"),
            *films,
            (rf"{D} is the last day of the launch price", f"{short(day(6))} is the last day of the launch price"),
            (r"\| Launch, \d{1,2} to \d{1,2} (?:Oct|Nov|Dec|Jan) \|", f"| Launch, {launch.day} to {day(6).day} {day(6):%b} |"),
            (rf"Set them as sale prices in [A-Za-z ]+? and Paystack on {D}, and set them back on {D}\.",
             f"Set them as sale prices in {shop} and Paystack on {short(day(-1))}, and set them back on {short(day(7))}."),
            (r"^Every Monday from 9 Nov, post the moments eight weeks ahead, ready drafted in `monday-posts/`\."
             r"(?: The [^\"\n]*\"[^\"\n]*\" in place of the link\.)?", monday),
        ],
        "ops/launch/MESSAGES.md": [
            (r"Send on launch day, [^,]+ \d{4}, from", f"Send on launch day, {L} {yr}, from"),
        ],
        "ops/launch/README.md": [
            (rf"Products launch {D} {Y}\.", f"Products launch {L} {yr}."),
        ],
        "ops/store/POLICIES.md": [
            (rf"goes live on {D} {Y}", f"goes live on {short(day(-2))} {day(-2).year}"),
        ],
        "ops/store/README.md": [
            (rf"Store goes live {D} {Y}; products launch {D} {Y}\.",
             f"Store goes live {short(day(-2))} {day(-2).year}; products launch {L} {yr}."),
        ],
        "site/README.md": [
            (rf"^## Before it goes live \({D}\)$", f"## Before it goes live ({short(day(-2))})"),
        ],
        "site/index.html": [
            (r"Check back on \d{1,2} (?:October|November|December|January)\.", f"Check back on {launch.day} {launch:%B}."),
        ],
        "CLAUDE.md": [
            (rf"Key dates: store live {D} {Y}\. Products launch {D} {Y}(?: \([^)]*\))?", key),
        ],
    }
    if late:
        end = day(6)
        span = f"{launch.day} to {end.day} {end:%b}" if launch.month == end.month else f"{launch.day} {launch:%b} to {end.day} {end:%b}"
        late_subs = {
            "ops/launch/LAUNCH-PLAN.md": [
                (r"^\| Moments 2027 \| USD 39 \| (?:Stays at the USD 29 early bird|USD 29 for launch week) \| KES 3,800 \|$",
                 "| Moments 2027 | USD 39 | USD 29 for launch week | KES 3,800 |"),
                (r"^## Black Friday(?:, Fri 27 to Mon 30 Nov \(your call\))?\n.*?(?=^## After launch week)",
                 "## Black Friday\n\nNo offer this year. The store was not ready by Fri 27 Nov, so the offer and the Moments early bird "
                 "(to 30 Nov) lapsed. The Moments launch week price above takes their place.\n\n", re.S),
            ],
            "ops/launch/MESSAGES.md": [
                (r"(?:Early bird is USD 29 until 30 Nov|Launch week price USD 29 until [^.\n]+)\. \[link\]",
                 f"Launch week price USD 29 until {short(end)}. [link]"),
                (r"Moments 2027 USD 29 (?:early bird, USD 39 from December|launch week, USD 39 after)\.",
                 "Moments 2027 USD 29 launch week, USD 39 after."),
            ],
            "ops/store/moments-2027.md": [
                (rf"USD 39, one time\. (?:Early bird USD 29 until Mon 30 Nov 2026|Launch week USD 29 until {D} {Y})",
                 f"USD 39, one time. Launch week USD 29 until {short(end)} {end.year}"),
                (r"\((?:early bird|launch week) KES 3,800\)", "(launch week KES 3,800)"),
                (r"USD 29 (?:early bird|launch week)\. \|", "USD 29 launch week. |"),
            ],
            "ops/store/README.md": [
                (r"\| 39 \((?:early bird 29 to 30 Nov|launch week 29, [^)]+)\) \| 5,000 \((?:early bird|launch week) 3,800\) \|",
                 f"| 39 (launch week 29, {span}) | 5,000 (launch week 3,800) |"),
            ],
            "site/index.html": [
                (r"(?:Early bird price until 30 November|Launch week price until \d{1,2} (?:December|January))\.",
                 f"Launch week price until {end.day} {end:%B}."),
            ],
            "site/README.md": [
                (r"^5\. On [^,]+, change the Moments 2027 block from the (?:early bird|launch week) price",
                 f"5. On {short(day(7))}, change the Moments 2027 block from the launch week price"),
            ],
            "CLAUDE.md": [
                (r"(?:Black Friday offer 27 to 30 Nov|No Black Friday offer this year: the store was not ready)\.",
                 "No Black Friday offer this year: the store was not ready."),
                (r"Moments 2027 USD 39 \((?:USD 29 early bird to 30 Nov|USD 29 for launch week, [^)]+)\)",
                 f"Moments 2027 USD 39 (USD 29 for launch week, {span})"),
            ],
        }
        for rel, extra in late_subs.items():
            subs.setdefault(rel, []).extend(extra)
    return subs


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("date", help="launch day, a Tuesday, YYYY-MM-DD")
    ap.add_argument("--store", choices=["lemon", "gumroad"], default="lemon")
    ap.add_argument("--check", action="store_true", help="print the changes, write nothing")
    a = ap.parse_args()

    launch = dt.date.fromisoformat(a.date)
    if launch.weekday() != 1:
        sys.exit(f"{a.date} is a {launch:%A}. Launch day is a Tuesday.")
    ok = ORIGINAL <= launch <= LATEST or any(a_ <= launch <= b_ for a_, b_ in LATE_WINDOWS)
    if not ok:
        sys.exit(f"Pick a Tuesday from {ORIGINAL} to {LATEST}, from 1 to 15 Dec, or from 5 to 12 Jan 2027. "
                 "Other weeks run into Black Friday, the holiday pause or the Studio launch.")

    errors, changes, new_text = [], [], {}
    for rel, subs in plan(launch, a.store).items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for pat, rep, *fl in subs:
            flags = re.M | (fl[0] if fl else 0)
            found = re.findall(pat, text, flags=flags)
            if len(found) != 1:
                errors.append(f"{rel}: pattern matched {len(found)} times: {pat[:70]}")
                continue
            bare = re.sub(r"`[^`]*`|\w+_\w+\.mp4", "", rep)
            if "—" in bare or "–" in bare or re.search(r"\w-\w", bare):
                errors.append(f"{rel}: a dash slipped into: {rep[:70]}")
            old = re.search(pat, text, flags=flags).group(0)
            if old != rep:
                changes.append((rel, old, rep))
            text = re.sub(pat, lambda _m: rep, text, count=1, flags=flags)
        new_text[rel] = text

    if errors:
        print("Nothing written.", *errors, sep="\n  ")
        sys.exit(1)
    for rel, old, rep in changes:
        print(f"{rel}\n  - {old}\n  + {rep}")
    if not changes:
        print(f"Launch is already set to {short(launch)} ({a.store}). Nothing to change.")
    if not a.check:
        for rel, text in new_text.items():
            (ROOT / rel).write_text(text, encoding="utf-8")
        print(f"\n{len(changes)} lines changed. Launch day: {short(launch)} {launch.year}, store: {a.store}.")


if __name__ == "__main__":
    main()
