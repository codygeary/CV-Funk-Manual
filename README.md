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
- Module data/text: `src/data/modules.json`
- Panel images:
  - `public/panels/free/<slug>.png`
  - `public/panels/modulations/<slug>.png`
  - `public/panels/pro/<slug>.png`

### Dark panel variants
If a `-dark` image exists it will be used automatically when the site theme is dark.

Example:
- `public/panels/free/syncro.png`
- `public/panels/free/syncro-dark.png`

## Deploy (GitHub Pages)
This project is preconfigured for a repo named `cvfunk-manual`:
- `site`: https://codygeary.github.io/cvfunk-manual
- `base`: /cvfunk-manual

If you use a different repo name, update `astro.config.mjs`.
