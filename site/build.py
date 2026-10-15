"""Build the legal pages for the Bungee website from ops/store/POLICIES.md, then check the site.

Run from the repo root:  python3 site/build.py
Exit code 1 if any check fails. Placeholders in square brackets are reported as
"not ready to deploy" so the site cannot go live with blanks in the policies.
"""
import html, os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
POL = os.path.join(ROOT, "..", "ops", "store", "POLICIES.md")

PAGES = {"refunds.html": ("Refund policy", "Refunds"),
         "terms.html": ("Terms of sale", "Terms of sale"),
         "privacy.html": ("Privacy notice", "Privacy notice")}

SHELL = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Bungee</title><link rel="icon" href="assets/favicon.png">
<link rel="stylesheet" href="assets/fonts.css">
<style>
body{{margin:0;background:#F6F6F2;color:#3F414B;font:500 17px/1.6 "Hanken Grotesk",system-ui,sans-serif}}
.wrap{{max-width:720px;margin:0 auto;padding:40px clamp(16px,4vw,40px) 80px}}
header a img{{height:30px;width:auto}}
h1{{font:400 clamp(44px,7vw,72px)/1 "Instrument Serif",Georgia,serif;margin:56px 0 28px;letter-spacing:-.02em}}
p{{margin:0 0 18px;color:#2A2C33}} strong{{font-weight:600;color:#3F414B}}
a{{color:#3F414B}} footer{{margin-top:48px;border-top:1.5px solid #3F414B;padding-top:18px;font-size:14px;color:#6C6E77}}
</style></head><body><div class="wrap">
<header><a href="index.html"><img src="assets/bungee-logo.png" alt="Bungee home" width="96" height="30"></a></header>
<h1>{title}</h1>
{body}
<footer><a href="index.html">Back to Bungee</a> · <a href="refunds.html">Refunds</a> · <a href="terms.html">Terms</a> · <a href="privacy.html">Privacy</a></footer>
</div></body></html>
"""


def inline(t):
    t = html.escape(t, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)


def blocks():
    """Return {heading: [paragraphs]} for each > quoted block whose first line is a bold heading."""
    out, cur, para = {}, None, []
    for line in open(POL, encoding="utf-8").read().splitlines():
        if not line.startswith(">"):
            if para and cur: out[cur].append(" ".join(para)); para = []
            continue
        t = line[1:].strip()
        m = re.fullmatch(r"\*\*(.+?)\*\*", t)
        if m and m.group(1) in [v[1] for v in PAGES.values()]:
            cur = m.group(1); out[cur] = []; para = []; continue
        if cur is None: continue
        if not t:
            if para: out[cur].append(" ".join(para)); para = []
        else:
            para.append(t)
    if para and cur: out[cur].append(" ".join(para))
    return out


class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.chunks = []
    def handle_starttag(self, tag, a):
        if tag in ("script", "style"): self.skip += 1
        d = dict(a)
        for k in ("alt", "aria-label", "placeholder"):
            if d.get(k): self.chunks.append(d[k])
        if tag == "meta" and (d.get("name") == "description" or (d.get("property") or "").startswith("og:")):
            self.chunks.append(d.get("content") or "")
    def handle_endtag(self, tag):
        if tag in ("script", "style"): self.skip -= 1
    def handle_data(self, d):
        if not self.skip: self.chunks.append(d)


def visible(path):
    p = Text(); p.feed(open(path, encoding="utf-8").read()); return "\n".join(p.chunks)


def main():
    b = blocks(); errors = []; warnings = []
    for fn, (title, key) in PAGES.items():
        if key not in b: errors.append(f"{key}: not found in POLICIES.md"); continue
        body = "\n".join(f"<p>{inline(x)}</p>" for x in b[key])
        open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(SHELL.format(title=title, body=body))
        blanks = re.findall(r"\[[^\]]+\]", " ".join(b[key]))
        if blanks: warnings.append(f"{fn}: blanks to fill before deploy: {', '.join(sorted(set(blanks)))}")

    # copy rules on every page: no hyphens or dashes in visible text
    js = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    for fn in ["index.html", *PAGES]:
        txt = visible(os.path.join(ROOT, fn))
        if fn == "index.html":  # pack copy lives in the script as quoted strings; slugs are not copy
            m = re.search(r"const PACKS = \[(.*?)\];", js, re.S)
            txt += "\n" + " ".join(re.findall(r'"([^"]*)"', re.sub(r'slug:"[^"]*"', "", m.group(1))))
            txt += "\n" + " ".join(re.findall(r'(?:hook|out|chip):"([^"]*)"', js.split("const MOMENTS")[1][:300]))
        if "\u2014" in txt or "\u2013" in txt: errors.append(f"{fn}: dash character found")
        for w in sorted(set(re.findall(r"\S*\w-\w\S*", txt))): errors.append(f"{fn}: hyphen in '{w}'")

    # assets referenced must exist
    for ref in set(re.findall(r'(?:src|href)="(assets/[^"]+)"', js)):
        if not os.path.exists(os.path.join(ROOT, ref)): errors.append(f"missing asset {ref}")

    empty = re.findall(r'"([a-z0-9-]+)": ""', js)
    if empty: warnings.append(f"checkout links still empty: {len(empty)} (buttons fall back to #bundles)")
    if 'const JOIN_ENDPOINT = ""' in js: warnings.append("email list endpoint still empty")

    for w in warnings: print("NOT READY TO DEPLOY:", w)
    for e in errors: print("FAIL:", e)
    print("checks:", "pass" if not errors else "fail", f"({len(warnings)} deploy blockers)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
