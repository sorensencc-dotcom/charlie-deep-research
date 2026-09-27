# CIC Industrial Design System — Enforcement Checklist

For Copywriters, authors, diagram operators, and anyone publishing **Cast Iron Charlie** external-facing artifacts (docs, GitHub wiki pages, treatment visuals, diagram/master-sheet outputs, preview UIs).

**Source of truth:** [`../cic_design_system.md`](../cic_design_system.md)  
**Scope:** Charlie / CIC branded publishing surfaces in and around `charlie-deep-research`.  
**Out of scope:** RewriteLabs / rewrite-mcp / rewrite-docs product UI unless it is clearly Charlie-branded by mistake.

## Quick palette (do not invent)

| Name | Hex | Use |
| --- | --- | --- |
| BACKGROUND (forge black) | `#1A1410` | Industrial canvas / non-wiki boards; **ink-only on wiki diagrams** (see readability MUST) |
| GRID | `#2C2420` | Brass grid lines |
| STROKES (brass) | `#B8922A` | Box outlines, connectors, accents |
| EMBER | `#C4501A` | Connection nodes / emphasis |
| TEXT_PRIMARY | `#E8E0D4` | Titles / primary text on forge canvases; on wiki paper use INK `#1A1410` |
| TEXT_SECONDARY | `#9A9088` | Labels / muted text on forge canvases |
| PAPER / PARCHMENT | `#F2ECE2` | **Wiki diagrams:** board + default node fills |
| PAPER_ALT | `#FAF6F0` | **Wiki diagrams:** optional light node fill |

## Typography

- Titles: **Playfair Display**
- Labels: **Barlow Condensed**
- Subtext: **Libre Baskerville**

## Hard aesthetic rules

### Wiki diagram readability (MUST — curated CIC wiki embeds)

Industrial forge-black BACKGROUND remains valid for master sheets / dark preview UIs. **Curated CIC wiki diagrams MUST use paper field mode** (see `cic_design_system.md` → Wiki diagram readability):

- [ ] Board / canvas fill is parchment/paper (`#F2ECE2` or approved paper alt `#FAF6F0`) — not `#1A1410` / `#2C2420`
- [ ] Default node fills are parchment/paper (light/off-white) — not forge-filled / near-black
- [ ] Forge black / near-black used for ink, borders, labels, chrome only
- [ ] Brass (`#B8922A`) and ember (`#C4501A`) used as accents only (accent stages, dashed feedback) — not default node fills
- [ ] No dark-on-dark: dark text on near-black nodes, or low-contrast labels on forge boards, is a publish blocker
- [ ] Visual exemplar followed: parchment/cream board, light nodes, black ink, ember only on accent/feedback (Chris's reference); coded contrast twin `sigil/docs/wiki/architecture.html` paper/ink/ember vars

### Shared industrial rules (all CIC diagram surfaces)


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
2. **Palette audit** — search the artifact (SVG/CSS/HTML/markdown embeds) for hex colors outside the approved tokens (industrial six + wiki paper tokens). Common drift: `#0a0806`, `#8B3A1A`, `#d45a23`, `#D98324`, `#C9A24B`, invented whites. For **wiki** diagrams, `#1A1410`/`#2C2420` as node or board fills is a fail — those are ink/chrome only.
3. **Effect audit** — search for `box-shadow`, `drop-shadow`, `linear-gradient`, `radial-gradient`, `border-radius`, SVG `rx=` / `ry=`.
4. **Font audit** — only Playfair Display, Barlow Condensed, Libre Baskerville (system fallbacks `serif` / `sans-serif` OK).
5. **Watermark** — master sheets and regenerated diagrams include CIC crest/mark bottom-right @ 0.22 opacity.
6. **Generators** — prefer `generate_diagrams.py` / `generate_master_sheet.py` over hand-styled one-offs; preview via `streamlit_master_sheet_ui.py`. Wiki-bound outputs MUST emit paper-field fills (update generator defaults before mass regen).
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
