# CIC Deep Research Toolkit

Operator‑grade assets, generators, and specifications for producing CIC's
Industrial‑style system diagrams and master sheets.

## CIC Industrial Design System

**Source of truth:** [`cic_design_system.md`](cic_design_system.md)

All Cast Iron Charlie **external-facing** diagrams, master sheets, preview UIs,
treatment visuals, and published wiki/docs artifacts in this repo must follow
that spec. Do not invent new colors, fonts, or styles.

| Token | Hex | Role |
| --- | --- | --- |
| Forge black | `#1A1410` | Background |
| Grid | `#2C2420` | Brass grid |
| Brass | `#B8922A` | Strokes / accents |
| Ember | `#C4501A` | Nodes / emphasis |
| Text primary | `#E8E0D4` | Titles / body |
| Text secondary | `#9A9088` | Labels / muted |

**Fonts:** Playfair Display (titles), Barlow Condensed (labels), Libre Baskerville (subtext).

**Hard rules:** no drop shadows, no gradients, no rounded corners; CIC crest watermark bottom-right at opacity `0.22`.

**Author / Copywriter checklist:** [`docs/CIC_DESIGN_SYSTEM_ENFORCEMENT.md`](docs/CIC_DESIGN_SYSTEM_ENFORCEMENT.md)

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
- `generate_diagrams.py` - Builds individual diagram templates (must emit CIC watermark)
- `streamlit_master_sheet_ui.py` - CIC-styled master sheet / diagram preview UI
- `streamlit_app.py` - CIC-branded deep-research inventory UI (palette must stay on-spec)
