# CIC Industrial Design System — Enforcement Checklist

For Copywriters, authors, diagram operators, and anyone publishing **Cast Iron Charlie** external-facing artifacts (docs, GitHub wiki pages, treatment visuals, diagram/master-sheet outputs, preview UIs).

**Source of truth:** [`../cic_design_system.md`](../cic_design_system.md)  
**Scope:** Charlie / CIC branded publishing surfaces in and around `charlie-deep-research`.  
**Out of scope:** RewriteLabs / rewrite-mcp / rewrite-docs product UI unless it is clearly Charlie-branded by mistake.

## Quick palette (do not invent)

| Name | Hex | Use |
| --- | --- | --- |
| BACKGROUND (forge black) | `#1A1410` | Canvas / page background |
| GRID | `#2C2420` | Brass grid lines |
| STROKES (brass) | `#B8922A` | Box outlines, connectors, accents |
| EMBER | `#C4501A` | Connection nodes / emphasis |
| TEXT_PRIMARY | `#E8E0D4` | Titles / primary text |
| TEXT_SECONDARY | `#9A9088` | Labels / muted text |

## Typography

- Titles: **Playfair Display**
- Labels: **Barlow Condensed**
- Subtext: **Libre Baskerville**

## Hard aesthetic rules

- [ ] Brass grid across the canvas where diagrams/master sheets are used
- [ ] Brass stroke outlines on diagram boxes
- [ ] Ember nodes at connection points
- [ ] CIC crest watermark bottom-right at opacity **0.22**
- [ ] **No** drop shadows
- [ ] **No** gradients
- [ ] **No** rounded corners (`border-radius` / `rx` / `ry` must be 0 / absent)
- [ ] No new colors, fonts, or styles beyond this checklist

## Canvas sizes

- Standard diagram: **1200×800**
- Master sheet: **3840×2160**

## Before you publish (author checklist)

1. **Point authors here** — README / Home / operator notes should link `cic_design_system.md` and this checklist.
2. **Palette audit** — search the artifact (SVG/CSS/HTML/markdown embeds) for hex colors outside the six approved tokens. Common drift: `#0a0806`, `#8B3A1A`, `#d45a23`, `#D98324`, `#C9A24B`, paper/white invents.
3. **Effect audit** — search for `box-shadow`, `drop-shadow`, `linear-gradient`, `radial-gradient`, `border-radius`, SVG `rx=` / `ry=`.
4. **Font audit** — only Playfair Display, Barlow Condensed, Libre Baskerville (system fallbacks `serif` / `sans-serif` OK).
5. **Watermark** — master sheets and regenerated diagrams include CIC crest/mark bottom-right @ 0.22 opacity.
6. **Generators** — prefer `generate_diagrams.py` / `generate_master_sheet.py` over hand-styled one-offs; preview via `streamlit_master_sheet_ui.py`.
7. **Docs** — treatment drafts and wiki pages that embed diagrams should cite this design system rather than describing ad-hoc styling.

## Operator regenerate notes

- Do **not** mass-regenerate every diagram for cosmetic drift unless Chris asks; fix generator defaults first, then regenerate selectively.
- Raster master sheet (docs-ready): `python generate_master_sheet.py A`
- Full-SVG master sheet (archival): `python generate_master_sheet.py B`
- Outputs: `master_sheets/`

## Related files

| File | Role |
| --- | --- |
| `cic_design_system.md` | Spec (canonical) |
| `bob_master_sheet_v1.md` | Master-sheet generation BOB |
| `generate_diagrams.py` | Per-diagram templates |
| `generate_master_sheet.py` | A/B master sheets |
| `streamlit_master_sheet_ui.py` | Preview UI |
| `diagrams/` | Canonical SVG outputs |
| `master_sheets/` | Generated master sheets |

## Known nearby drift (report; do not silently redesign product UI)

- `C:\dev\assets\cic-dashboard.css` — Toolforge dashboard claiming CIC branding; invents `--black/#0a0806`, `--rust/#8B3A1A`, paper/white tokens, severity ramp colors, and a `linear-gradient` divider. Treat as a separate product-UI pass if Chris wants it brought on-spec.
