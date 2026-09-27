# Gang Sheet Builder — working demo

A browser-based DTF gang sheet builder: the customer uploads their artwork, arranges it on a
22" roll, and the price updates live with the sheet length.

**Live demo:** https://anirudhatalmale6-alt.github.io/gang-sheet-builder-demo/

## What it does

- **Upload** PNG / JPG / WebP, or drag-and-drop straight onto the sheet. Artwork is sized from
  its pixel dimensions at 300 DPI, so a 1200×900 px file lands as a 4" × 3" print.
- **Arrange** — drag to move, corner handles resize with the aspect ratio locked, rotate handle
  (snaps to 15°, hold Shift for free rotation), arrow keys nudge, Shift+arrow nudges 1".
- **Auto-nest** packs every design with a 0.125" gutter using shelf packing.
  **Fit sheet to art** nests and then drops to the smallest length tier that fits.
- **Live pricing** by length tier (12" / 24" / 36" / 48" / 60" / 120"), with a usage meter
  showing how much of the sheet the customer is actually paying for.
- **Pre-flight checks**, live, before they can order:
  - overlapping designs (can't be cut apart after printing)
  - anything outside the 0.25" safe margin (gets trimmed)
  - effective DPI per design, flagged red under 150 DPI
- **Export** — PNG proof, plus the layout as JSON for the production queue.

## Notes

- The proof renders at 100 DPI in-browser to keep memory sane. In production the print-ready
  300 DPI file (6600 px wide) is rendered server-side from the JSON layout when the order is
  placed — that keeps the customer's browser out of it entirely.
- Length tiers and prices live in the `TIERS` array at the top of the script — a shop plugs
  in their own numbers there.
- No build step, no dependencies. Open `index.html`.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole builder — markup, styles, logic |
| `samples/` | Placeholder transfer artwork used by "Load sample designs" |
| `make_samples.py` | Regenerates the sample PNGs (Pillow) |
| `shots/` | Screenshots of the builder under test |
