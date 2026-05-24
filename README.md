# CIC Deep Research Toolkit

Operator‑grade assets, generators, and specifications for producing CIC's
Industrial‑style system diagrams and master sheets.

## Master Sheets (v1.0)

Two variants are available:

### Variant A — Raster‑Embedded (Docs‑Ready)

- 3840×2160 Industrial canvas
- Brass grid, ember nodes, crest watermark
- GLOBAL / PIPELINE / SYSTEM‑WIDE rows
- Diagrams embedded as raster images
- Lightweight, ideal for README and web surfaces

Generated via:

```bash
python generate_master_sheet.py A
```

### Variant B — Full‑SVG (Archival)

- Same layout and styling as Variant A
- All diagrams inlined as full SVG `<g>` groups
- Infinite resolution, archival‑grade

Generated via:

```bash
python generate_master_sheet.py B
```

Output files are written to:

```bash
./master_sheets/
```

## Diagram Sources

All eight CIC Industrial diagrams live in:

```bash
diagrams/
```

## Specs

- `cic_design_system.md` — CIC Industrial Design System
- `bob_master_sheet_v1.md` — BOB spec for master sheet generation
- `CLAUDE.md` — BOB execution wrapper for Claude

## Tools

- `generate_master_sheet.py` — Produces A/B master sheet variants
- `generate_diagrams.py` — Builds individual diagram templates
- `streamlit_app.py` — CIC‑styled viewer for diagrams and master sheets
