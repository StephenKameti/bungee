#!/usr/bin/env python3
"""Build the sellable zips into dist/.

Each skill pack ships as dist/<slug>.zip:
  Bungee-<Name>/README.md, LICENSE.txt and <slug>.zip (the skill folder a buyer uploads to Claude).
Moments 2027 ships as dist/Bungee-Moments-2027.zip from products/moments-2027/out.

Run from the repo root: python3 scripts/build_products.py
Rebuild Moments first if its data changed: cd products/moments-2027 && python3 build.py
"""
import io
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
PACKS = {
    "key-visual-builder": "Bungee-Key-Visual-Builder",
    "fsu-display-units": "Bungee-Retail-Display-Theatre",
    "designed-deck-builder": "Bungee-Designed-Deck-Builder",
    "social-content-calendar-builder": "Bungee-Social-Content-Calendar-Builder",
    "audience-persona-builder": "Bungee-Audience-and-Persona-Builder",
    "campaign-strategy-builder": "Bungee-Campaign-Strategy-Builder",
}


def zip_dir(src, arc_root):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for base, _, files in os.walk(src):
            for f in sorted(files):
                if f.startswith("."):
                    continue
                p = os.path.join(base, f)
                z.write(p, os.path.join(arc_root, os.path.relpath(p, src)))
    return buf.getvalue()


def main():
    os.makedirs(DIST, exist_ok=True)
    for slug, outer in PACKS.items():
        pack = os.path.join(ROOT, "products", "skills", slug)
        inner = zip_dir(os.path.join(pack, "skill"), slug)
        out = os.path.join(DIST, slug + ".zip")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in ("README.md", "LICENSE.txt"):
                z.write(os.path.join(pack, f), f"{outer}/{f}")
            z.writestr(f"{outer}/{slug}.zip", inner)
        print("built", os.path.relpath(out, ROOT))
    moments = os.path.join(ROOT, "products", "moments-2027", "out")
    out = os.path.join(DIST, "Bungee-Moments-2027.zip")
    with open(out, "wb") as fh:
        fh.write(zip_dir(moments, "Bungee-Moments-2027"))
    print("built", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
