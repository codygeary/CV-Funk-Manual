"""Copy the finished panels into public/panels.

Takes panel-captures/final/<collection>/<slug>(-dark).png from
merge-live-displays.py. Without a final image it falls back to the raw render
from capture-panels.sh, matched by the module's vcvSlug.

  python3 scripts/place-panels.py              copy everything
  python3 scripts/place-panels.py vega fuzzy   copy only these slugs
  python3 scripts/place-panels.py --dry-run    list what would be copied
Then run scripts/make-web-panels.py.
"""
import json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "panel-captures")
PLUGIN = {"free": "CVfunk", "modulations": "CVfunkModulations",
          "chord-caster": "CVfunkChordCaster", "sands": "CVfunkSands"}

only = [a for a in sys.argv[1:] if not a.startswith("--")]
dry = "--dry-run" in sys.argv
copied, missing = 0, []
for m in json.load(open(os.path.join(ROOT, "src/data/modules.json"))):
    if only and m["slug"] not in only: continue
    coll = m["collection"]
    for theme, suffix in (("light", ""), ("dark", "-dark")):
        src = os.path.join(WORK, "final", coll, m["slug"] + suffix + ".png")
        if not os.path.exists(src):
            src = os.path.join(WORK, theme, PLUGIN[coll], m["vcvSlug"] + ".png")
        if not os.path.exists(src):
            missing.append(m["slug"] + suffix); continue
        dst = os.path.join(ROOT, "public/panels", coll, m["slug"] + suffix + ".png")
        if dry: print(os.path.relpath(src, ROOT), "->", os.path.relpath(dst, ROOT))
        else: shutil.copyfile(src, dst)
        copied += 1
print(("Would copy" if dry else "Copied"), copied, "panels")
if missing: print("No capture for:", ", ".join(missing))
