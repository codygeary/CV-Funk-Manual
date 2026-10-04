"""Make the web-sized panel images the site uses.

Reads public/panels/<collection>/<slug>.png (and -dark.png), writes
public/panels-web/<slug>.jpg at 600px tall, and records each panel's
width/height ratio in src/data/panel-ratios.json for the rack layout.

Run after adding or recapturing panels:  python3 scripts/make-web-panels.py
Needs Pillow (pip install pillow).
"""
import glob, json, os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, DST = os.path.join(ROOT, "public/panels"), os.path.join(ROOT, "public/panels-web")
os.makedirs(DST, exist_ok=True)
ratios = {}
for path in sorted(glob.glob(os.path.join(SRC, "*", "*.png"))):
    name = os.path.basename(path)[:-4]
    im = Image.open(path).convert("RGB")
    if not name.endswith("-dark"):
        ratios[name] = round(im.width / im.height, 4)
    im = im.resize((round(im.width * 600 / im.height), 600), Image.LANCZOS)
    im.save(os.path.join(DST, name + ".jpg"), quality=78, optimize=True, progressive=True)
json.dump(ratios, open(os.path.join(ROOT, "src/data/panel-ratios.json"), "w"), indent=1, sort_keys=True)
print(len(ratios), "panels")
