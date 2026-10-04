# CV funk Manual (Astro)

Static manual site generated from the PDF (`CV_funk_Manual.pdf`).

## Run locally
```bash
npm install
npm run dev
```

## Build
```bash
npm run build
npm run preview
```

## Content
- Module data/text: `src/data/modules.json`; collections: `src/data/collections.json`
- Panel images: `public/panels/<collection>/<slug>.png`, plus `<slug>-dark.png` for the dark theme.
  The site shows web-sized copies from `public/panels-web/`. After adding or recapturing panels, run
  `python3 scripts/make-web-panels.py` (needs Pillow) to regenerate them and `src/data/panel-ratios.json`.

## Layout
- `src/pages/index.astro`: the whole manual. The rack, filters and module pages are rendered in the
  browser by `src/scripts/site.js` from the data embedded at build time.
- `src/styles/site.css`: styles. Panel-style text uses Menlo, with DejaVu Sans Mono (`public/fonts/`) as the fallback.
- `src/pages/{free,modulations,chord-caster,sands}.astro`: redirect old links to `/#c-<collection>`.
- Deep links: `#<slug>` opens a module (`#twang`), `#c-<collection>` opens a collection (`#c-sands`).

## Deploy (GitHub Pages)
This project is preconfigured for a repo named `cvfunk-manual`:
- `site`: https://codygeary.github.io/cvfunk-manual
- `base`: /cvfunk-manual

If you use a different repo name, update `astro.config.mjs`.

## Figures (charts, zooms, waveforms)
Each module can list any number of figures in `src/data/modules.json`:

```json
"figures": [
  { "id": "swing", "src": "/figures/syncro/swing.png", "caption": "Swing at 50%…", "section": "panelMap" }
]
```

- Put image files in `public/figures/<slug>/`.
- `section` is `panelMap`, `basicUse` or `patching` (default `panelMap`).
- To place a figure at a specific point in the text, put `[[fig:<id>]]` on its own line in that section. Figures not placed in the text appear at the end of their section.
- Optional: `srcDark` (a dark-theme version) and `alt` (defaults to the caption).

## Rewriting text in bulk
`manual-text/b*.py` hold the current manual text, one Python dict per batch of modules. `python3 manual-text/apply_text.py` writes them into `modules.json` and copies the figures they list from `../PDF_manuals/extracted/` (mapping in `manual-text/figsrc.py`). Editing `modules.json` directly is fine too; just don't run `apply_text.py` afterwards or it will overwrite those edits.

## Videos
Modules and collections can list YouTube videos (`videos` in `modules.json` and `collections.json`):

```json
"videos": [{ "id": "LT-7bXAbz20", "title": "…", "by": "Omri Cohen", "start": 0,
             "chapters": [[11, "Basic functionality"], [238, "Beats and shapes"]] }]
```

`start` and chapter times are in seconds. The current list is kept in `manual-text/videos.py`.
