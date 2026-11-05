#!/usr/bin/env python3
"""Move launch week to any Tuesday in one command.

Every date tied to launch day (store live, go or no go, launch price window,
one skill film a day, the waitlist line on the site, the key dates in
CLAUDE.md) is worked out from the launch date and rewritten in place.
Black Friday (27 to 30 Nov) and the Moments early bird (to 30 Nov) never move:
they are Stephen's decisions, not launch week dates.

    python3 ops/launch/set_launch.py 2026-11-17              # Lemon Squeezy
    python3 ops/launch/set_launch.py 2026-11-10 --store gumroad
    python3 ops/launch/set_launch.py 2026-11-17 --check      # show, write nothing

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

FILMS = [
    ("Key Visual Builder", "kv"),
    ("Campaign Strategy Builder", "strat"),
    ("Designed Deck Builder", "deck"),
    ("Content Calendar Builder", "cal"),
    ("Audience Persona Builder", "persona"),
    ("Retail Display Theatre", "fsu"),
]

D = r"(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) \d{1,2} (?:Oct|Nov|Dec)"


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
    if early_mondays:
        names = " and ".join(short(x) for x in early_mondays)
        posts = "post goes" if len(early_mondays) == 1 else "posts go"
        tail = "Out tomorrow." if early_mondays[-1] == day(-1) and len(early_mondays) == 1 else f"Out {L}."
        monday += f" The {names} {posts} out before launch, so end {'it' if len(early_mondays) == 1 else 'them'} with \"{tail}\" in place of the link."

    head = f"Products launch {L} 2026"
    if moved:
        head += f", moved from {short(ORIGINAL)} because the store was not ready"
    key = f"Key dates: store live {short(day(-2))} 2026. Products launch {L} 2026"
    if moved:
        key += f" (moved from {ORIGINAL.day} Nov)"

    return {
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
            (r"\| Launch, \d{1,2} to \d{1,2} (?:Oct|Nov|Dec) \|", f"| Launch, {launch.day} to {day(6).day} {day(6):%b} |"),
            (rf"Set them as sale prices in [A-Za-z ]+? and Paystack on {D}, and set them back on {D}\.",
             f"Set them as sale prices in {shop} and Paystack on {short(day(-1))}, and set them back on {short(day(7))}."),
            (r"^Every Monday from 9 Nov, post the moments eight weeks ahead, ready drafted in `monday-posts/`\."
             r"(?: The [^\"\n]*\"[^\"\n]*\" in place of the link\.)?", monday),
        ],
        "ops/launch/MESSAGES.md": [
            (r"Send on launch day, [^,]+ \d{4}, from", f"Send on launch day, {L} 2026, from"),
        ],
        "ops/launch/README.md": [
            (rf"Products launch {D} 2026\.", f"Products launch {L} 2026."),
        ],
        "ops/store/POLICIES.md": [
            (rf"goes live on {D} 2026", f"goes live on {short(day(-2))} 2026"),
        ],
        "ops/store/README.md": [
            (rf"Store goes live {D} 2026; products launch {D} 2026\.",
             f"Store goes live {short(day(-2))} 2026; products launch {L} 2026."),
        ],
        "site/README.md": [
            (rf"^## Before it goes live \({D}\)$", f"## Before it goes live ({short(day(-2))})"),
        ],
        "site/index.html": [
            (r"Check back on \d{1,2} (?:October|November|December)\.", f"Check back on {launch.day} {launch:%B}."),
        ],
        "CLAUDE.md": [
            (rf"Key dates: store live {D} 2026\. Products launch {D} 2026(?: \([^)]*\))?", key),
        ],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("date", help="launch day, a Tuesday, YYYY-MM-DD")
    ap.add_argument("--store", choices=["lemon", "gumroad"], default="lemon")
    ap.add_argument("--check", action="store_true", help="print the changes, write nothing")
    a = ap.parse_args()

    launch = dt.date.fromisoformat(a.date)
    if launch.weekday() != 1:
        sys.exit(f"{a.date} is a {launch:%A}. Launch day is a Tuesday.")
    if not ORIGINAL <= launch <= LATEST:
        sys.exit(f"Pick a Tuesday from {ORIGINAL} to {LATEST}. Later, the launch price week runs into Black Friday: that needs Stephen's call first.")

    errors, changes, new_text = [], [], {}
    for rel, subs in plan(launch, a.store).items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for pat, rep in subs:
            found = re.findall(pat, text, flags=re.M)
            if len(found) != 1:
                errors.append(f"{rel}: pattern matched {len(found)} times: {pat[:70]}")
                continue
            bare = re.sub(r"`[^`]*`|\w+_\w+\.mp4", "", rep)
            if "—" in bare or "–" in bare or re.search(r"\w-\w", bare):
                errors.append(f"{rel}: a dash slipped into: {rep[:70]}")
            old = re.search(pat, text, flags=re.M).group(0)
            if old != rep:
                changes.append((rel, old, rep))
            text = re.sub(pat, lambda _m: rep, text, count=1, flags=re.M)
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
        print(f"\n{len(changes)} lines changed. Launch day: {short(launch)} 2026, store: {a.store}.")


if __name__ == "__main__":
    main()
