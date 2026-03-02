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
- Extracted panel-page images: `public/panels/*.png`

## Deploy (GitHub Pages)
This project is preconfigured for a repo named `cvfunk-manual`:
- `site`: https://codygeary.github.io/cvfunk-manual
- `base`: /cvfunk-manual

If you use a different repo name, update `astro.config.mjs`.
