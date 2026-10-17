"""Apply rewritten manual text (manual-text/b*.py) to src/data/modules.json
and copy the figures each entry lists into public/figures/<slug>/.

Run from the repo root:  python3 manual-text/apply_text.py
"""
import glob, importlib.util, json, os, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXTRACTED = os.path.join(os.path.dirname(ROOT), "PDF_manuals", "extracted")
sys.path.insert(0, HERE)
from figsrc import FROM

def render_page_figures(pdf, page):
    """Union of all figure boxes on a PDF page, rendered as one image."""
    import fitz
    pdf_dir = os.path.join(os.path.dirname(ROOT), "PDF_manuals")
    sys.path.insert(0, pdf_dir)
    from extract_figures import figure_boxes
    pg = fitz.open(os.path.join(pdf_dir, pdf))[int(page) - 1]
    boxes = figure_boxes(pg)
    clip = boxes[0]
    for b in boxes[1:]: clip |= b
    clip = (clip + (-6, -6, 6, 6)) & pg.rect
    pix = pg.get_pixmap(dpi=220, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod.MODULES

data_path = os.path.join(ROOT, "src/data/modules.json")
mods = json.load(open(data_path))
by = {m["slug"]: m for m in mods}
done = []
for path in sorted(glob.glob(os.path.join(HERE, "b*.py"))):
    for slug, new in load(path).items():
        m = by[slug]
        if "tagline" in new: m["tagline"] = new["tagline"]
        for key in ("panelMap", "basicUse", "patching"):
            if key in new: m["sections"][key] = new[key].strip()
        if "figures" in new:
            m["figures"] = new["figures"]
            for f in new["figures"]:
                key = f["src"].split("/figures/")[1].rsplit(".", 1)[0]
                dst = os.path.join(ROOT, "public", f["src"].lstrip("/"))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if key in FROM and not os.path.isdir(EXTRACTED) and os.path.exists(dst):
                    continue   # PDF sources not in this checkout: keep the figure already built
                if key in FROM and FROM[key].startswith("pdf:"):
                    # "pdf:<file>:<page>": every figure on that page as one image
                    im = render_page_figures(*FROM[key][4:].split(":"))
                elif key in FROM:
                    im = Image.open(os.path.join(EXTRACTED, FROM[key])).convert("RGB")
                if key in FROM:
                    im.thumbnail((1400, 1400))
                    # 256-colour palette: these are diagrams and screenshots, and it cuts size ~4x
                    im = im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
                    im.save(dst, optimize=True)
                elif not os.path.exists(dst):
                    sys.exit(f"{slug}: figure {f['src']} has no source and no file")
            # every [[fig:id]] in the text must name a listed figure
            ids = {f["id"] for f in new["figures"]}
            for key2, text in m["sections"].items():
                for line in text.split("\n"):
                    t = line.strip()
                    if t.startswith("[[fig:") and t[6:-2] not in ids:
                        sys.exit(f"{slug}.{key2}: unknown figure {t}")
        done.append(slug)
# Videos (manual-text/videos.py) for modules and collections
import videos as V
for m in mods:
    if m["slug"] in V.MODULES: m["videos"] = V.MODULES[m["slug"]]
    else: m.pop("videos", None)
cpath = os.path.join(ROOT, "src/data/collections.json")
cols = json.load(open(cpath))
for c in cols:
    if c["id"] in V.COLLECTIONS: c["videos"] = V.COLLECTIONS[c["id"]]
json.dump(cols, open(cpath, "w"), indent=2, ensure_ascii=False); open(cpath, "a").write("\n")
json.dump(mods, open(data_path, "w"), indent=2, ensure_ascii=True)
open(data_path, "a").write("\n")
print("updated", len(done), "modules:", ", ".join(done))
