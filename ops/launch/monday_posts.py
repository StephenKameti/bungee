#!/usr/bin/env python3
"""Draft the Monday moment posts from the Moments 2027 data.

Every Monday from 9 Nov 2026, post the moments eight weeks ahead, so a
planner who reads it on Monday still has time to brief, make and book.

    python3 ops/launch/monday_posts.py            # writes ops/launch/monday-posts/
    python3 ops/launch/monday_posts.py --check    # checks only, writes nothing

Trademarked event names never appear in posts (standing rule 2): they are
swapped for plain descriptions below, and the check fails if one slips through.
"""
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "products/moments-2027/out/moments-2027.json"
OUT = ROOT / "ops/launch/monday-posts"

FIRST_MONDAY = dt.date(2026, 11, 9)
LAST_MONDAY = dt.date(2027, 4, 26)
LEAD_WEEKS = 8

# Trademarked or organiser owned names, and what the posts say instead.
PLAIN = {
    "Australian Open": "the first tennis major of the year",
    "Super Bowl LXI": "the biggest American football final",
    "NFL Draft": "American football's draft night",
    "French Open": "the clay court tennis major",
    "Champions League final": "Europe's club football final",
    "Africa Cup of Nations": "Africa's football championship",
    "FIFA Women's World Cup": "the women's football world championship",
    "Wimbledon": "the grass court tennis major",
    "Tour de France": "cycling's biggest race",
    "The Open Championship": "golf's oldest major",
    "Pan American Games": "the multi sport games of the Americas",
    "Men's Rugby World Cup": "the men's rugby world championship",
    "Men's Cricket World Cup": "the men's cricket world championship",
    "World Snooker Championship centenary": "a century of snooker's world championship",
    "Oktoberfest": "Munich's beer festival season",
    "Movember": "the moustache month for men's health",
    "Dry January and Veganuary": "the sober and plant based January",
    "Singles' Day": "the 11.11 shopping day",
    "Black Friday to Cyber Monday": "Black Friday weekend",
}
BANNED = [
    "Australian Open", "Super Bowl", "NFL", "French Open", "Roland", "Champions League",
    "AFCON", "Africa Cup of Nations", "FIFA", "World Cup", "Wimbledon", "Tour de France",
    "Open Championship", "Pan American", "Snooker Championship", "Oktoberfest", "Movember",
    "Veganuary", "Dry January", "Singles' Day", "Cyber Monday", "Olympic",
]
# Trademarked names inside angle and hook text.
TEXT_SWAP = {
    "Super Bowl Sunday in the United States": "the biggest American football final in the United States",
    "e-commerce": "online shopping",
}
LEAD_ORDER = {"Holiday": 0, "Cultural": 1, "Commercial": 2, "Religious": 3, "Seasonal": 4, "Sport": 5}


def clean(text):
    for old, new in TEXT_SWAP.items():
        text = text.replace(old, new)
    return text


def name(m):
    return PLAIN.get(m["title"], m["title"])


def day(d):
    return f"{d.day} {d:%b}"


def week_posts(moments):
    posts = []
    monday = FIRST_MONDAY
    while monday <= LAST_MONDAY:
        start = monday + dt.timedelta(weeks=LEAD_WEEKS)
        end = start + dt.timedelta(days=6)
        week = [m for m in moments if start <= dt.date.fromisoformat(m["start"]) <= end]
        posts.append((monday, start, week))
        monday += dt.timedelta(weeks=1)
    return posts


def pick_lead(week):
    # Global first (East Africa is a module, never the default), English hooks, never a sensitive date.
    pool = [m for m in week if m["category"] != "Sensitive" and m["pack"] == "Global"]
    if not pool:
        pool = [m for m in week if m["category"] != "Sensitive"]
    if not pool:
        return None
    return sorted(pool, key=lambda m: (LEAD_ORDER.get(m["category"], 9), m["start"]))[0]


def render(monday, start, week):
    d = dt.date.fromisoformat
    lead = pick_lead(week)
    lines = [f"# Monday {day(monday)} {monday.year}", "", f"Moments for the week of {day(start)} {start.year}.", ""]
    if lead is None:
        lines += ["A quiet week. Post a reminder instead:", "", "> Eight weeks out and nothing on the calendar. That is a gift. Book the next big moment early. [link]", ""]
        return "\n".join(lines)
    when = day(d(lead["start"]))
    if lead["end"] != lead["start"]:
        when += f" to {day(d(lead['end']))}"
    seen = {lead["id"]}
    also, quiet, east = [], [], []
    for m in sorted(week, key=lambda m: m["start"]):
        if m["id"] in seen:
            continue
        label = f"{name(m)} on {day(d(m['start']))}"
        if m["category"] == "Sensitive":
            quiet.append(label)
        elif m["pack"] == "East Africa":
            # Skip the regional twin of a global moment (same name, or same day and kind).
            if not any(m["title"] == x["title"] or (m["start"] == x["start"] and m["category"] == x["category"])
                       for x in week if x["pack"] == "Global"):
                east.append(label)
        else:
            also.append(label)
        seen.add(m["id"])
    title = name(lead)
    title = title[0].upper() + title[1:]
    if lead["pack"] != "Global":
        title += f" in {lead['pack']}"
    post = [
        "Eight weeks out. Brief it now.",
        "",
        f"{title}, {when}.",
        f"The angle: {clean(lead['angle'])}",
        f"The hook: \"{clean(lead['hook'])}\"",
    ]
    if also:
        post.append("Also that week: " + ", ".join(also) + ".")
    if east:
        post.append("In East Africa: " + ", ".join(east) + ".")
    if quiet:
        post.append("Go quiet: " + ", ".join(quiet) + ".")
    post += ["", "160 moments like this, dated and angled, in Moments 2027. [link]"]
    lines += ["Paste as is. Swap in the store link.", ""] + ["> " + p if p else ">" for p in post] + [""]
    if lead["pack"] != "Global":
        lines += ["Note: the hook may be in a local language. Post it only after the native speaker check on the almanac hooks comes back.", ""]
    if lead["status"] != "fixed":
        lines += [f"Note: this date is marked {lead['status']} in the almanac. Check the official announcement before posting.", ""]
    return "\n".join(lines)


def check(text, where):
    problems = []
    text = re.sub(r"\(\d{4}-\d\d-\d\d\.md\)", "", text)
    for word in BANNED:
        if word.lower() in text.lower():
            problems.append(f"{where}: trademarked name '{word}'")
    if re.search(r"\w-\w|–|—", text):
        problems.append(f"{where}: hyphen or dash")
    return problems


def main():
    moments = json.loads(DATA.read_text())["moments"]
    posts = week_posts(moments)
    problems, files = [], {}
    for monday, start, week in posts:
        text = render(monday, start, week)
        problems += check(text, monday.isoformat())
        files[f"{monday.isoformat()}.md"] = text
    index = ["# Monday moment posts", "", "Every Monday from 9 Nov 2026, post the moments eight weeks ahead. One file per Monday. Built by `ops/launch/monday_posts.py` from the almanac data; rerun it if the data changes.", "", "| Monday | Moments for the week of | Lead |", "| --- | --- | --- |"]
    for monday, start, week in posts:
        lead = pick_lead(week)
        index.append(f"| [{day(monday)} {monday.year}]({monday.isoformat()}.md) | {day(start)} {start.year} | {name(lead) if lead else 'quiet week'} |")
    files["README.md"] = "\n".join(index) + "\n"
    problems += check(files["README.md"], "README")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    if "--check" not in sys.argv:
        OUT.mkdir(parents=True, exist_ok=True)
        for f, text in files.items():
            (OUT / f).write_text(text)
    print(f"checks: pass ({len(posts)} posts)")


if __name__ == "__main__":
    main()
