"""Clean Rack renders with the live displays from the current panel images.

Rack's screenshot mode (scripts/capture-panels.sh) gives exact crops, but its
displays show the preview state. The current images in public/panels have live
displays, but rough crops. For each panel this lines the current image up with
the render, finds the displays (big dark shapes on the light render), and copies
in each display whose live content differs from the preview. Everything else,
edges, knobs, labels and lights, comes from the render, so old panel art in the
hand capture doesn't come back.

  python3 scripts/merge-live-displays.py              every module
  python3 scripts/merge-live-displays.py mala twang   just these
Writes panel-captures/final/<collection>/<slug>(-dark).png for place-panels.py.
A module with no current image just uses the render. To bring in a new live
screen, drop a fresh screenshot into public/panels and run this again.
Needs Pillow, numpy and scipy.
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "panel-captures")
# Panels whose current image shows today's panel art and whose lights or buttons
# read better live than in Rack's preview: everything inside the edge band
# comes from the current image, not just the displays.
WHOLE = {"picus", "vega", "fuzzy", "arrange-xl", "arcs"}
PLUGIN = {"free": "CVfunk", "modulations": "CVfunkModulations",
          "chord-caster": "CVfunkChordCaster", "sands": "CVfunkSands"}


def warp(img, size, p):
    sx, sy, dx, dy = p
    return img.transform(size, Image.AFFINE, (sx, 0, dx, 0, sy, dy), Image.BILINEAR)


def align(hand, render):
    """(sx, sy, dx, dy) such that render pixel (x, y) is hand pixel (sx*x+dx, sy*y+dy)."""
    hg = hand.convert("L").filter(ImageFilter.GaussianBlur(1))
    rg = render.convert("L").filter(ImageFilter.GaussianBlur(1))

    def score(ref, q, scale):
        w = np.asarray(warp(hg, (ref.shape[1], ref.shape[0]), (q[0] / scale, q[1] / scale, q[2], q[3])), np.float32)
        m = 6   # skip the outer band, where the hand crop is off by definition
        return np.abs(w[m:-m, m:-m] - ref[m:-m, m:-m]).mean()

    p = [hand.width / render.width, hand.height / render.height, 0.0, 0.0]
    for scale, steps in ((0.5, [0.01, 0.01, 8, 8]), (1.0, [0.002, 0.002, 2, 2])):
        ref = np.asarray(rg.resize((round(rg.width * scale), round(rg.height * scale))), np.float32)
        best = score(ref, p, scale)
        for _ in range(6):
            improved = True
            while improved:
                improved = False
                for i in range(4):
                    for d in (-steps[i], steps[i]):
                        t = list(p); t[i] += d
                        s = score(ref, t, scale)
                        if s < best - 1e-4: best, p, improved = s, t, True
            steps = [v / 2 for v in steps]
    return p, best


def display_regions(light_render):
    """Rectangles around the displays: big or nearly solid dark shapes on the light render."""
    g = np.asarray(light_render.convert("L"))
    lab, _ = ndimage.label(ndimage.binary_opening(g < 50, iterations=2))
    boxes = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        a = (lab[sl] == i).sum(); h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
        fill = a / (w * h)
        if a >= 10000 or (a >= 2500 and fill >= 0.85) or (a >= 1500 and w * h >= 8000 and fill >= 0.7):
            boxes.append([sl[0].start, sl[1].start, sl[0].stop, sl[1].stop])
    # Preview drawing can split one display into pieces: merge boxes that touch.
    merged = True
    while merged:
        merged = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if a[0] <= b[2] + 4 and b[0] <= a[2] + 4 and a[1] <= b[3] + 4 and b[1] <= a[3] + 4:
                    boxes[i] = [min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])]
                    del boxes[j]; merged = True; break
            if merged: break
    regions = []
    for y0, x0, y1, x1 in boxes:
        m = np.zeros(g.shape, bool); m[max(0, y0 - 3):y1 + 3, max(0, x0 - 3):x1 + 3] = True
        regions.append(m)
    return regions


def merge(hand, render, regions, whole=False, thresh=45, min_pixels=300):
    hand, render = hand.convert("RGB"), render.convert("RGB")
    p, err = align(hand, render)
    W = warp(hand, render.size, p)
    if whole:
        keep = np.zeros((render.height, render.width), bool); keep[8:-8, 8:-8] = True
        alpha = Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1))
        out = render.copy(); out.paste(W, (0, 0), alpha)
        return out, len(regions), err
    d = np.abs(np.asarray(W, np.int16) - np.asarray(render, np.int16)).max(axis=2).astype(np.uint8)
    d = np.asarray(Image.fromarray(d).filter(ImageFilter.GaussianBlur(1.5))) > thresh
    keep = np.zeros(d.shape, bool); used = 0
    for r in regions:
        if (d & r).sum() >= min_pixels: keep |= r; used += 1
    alpha = Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1))
    out = render.copy(); out.paste(W, (0, 0), alpha)
    return out, used, err


only = sys.argv[1:]
for m in json.load(open(os.path.join(ROOT, "src/data/modules.json"))):
    if only and m["slug"] not in only: continue
    coll, plugin = m["collection"], PLUGIN[m["collection"]]
    light = os.path.join(WORK, "light", plugin, m["vcvSlug"] + ".png")
    if not os.path.exists(light): print(m["slug"], ": no render"); continue
    regions = display_regions(Image.open(light))
    note = [m["slug"]]
    for theme, suffix in (("light", ""), ("dark", "-dark")):
        render = Image.open(os.path.join(WORK, theme, plugin, m["vcvSlug"] + ".png")).convert("RGB")
        current = os.path.join(ROOT, "public/panels", coll, m["slug"] + suffix + ".png")
        whole = m["slug"] in WHOLE
        if os.path.exists(current) and (regions or whole):
            out, used, err = merge(Image.open(current), render, regions, whole)
            note.append(f"{theme}: " + ("whole panel live" if whole else f"{used}/{len(regions)} live")
                        + ("  (check: poor match)" if err > 15 and not whole else ""))
        else:
            out = render; note.append(f"{theme}: render")
        dst = os.path.join(WORK, "final", coll, m["slug"] + suffix + ".png")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        out.save(dst, optimize=True)
    print("  ".join(note))
