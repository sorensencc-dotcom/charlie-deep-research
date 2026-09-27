# CIC Design System — Industrial Style

## Palette
- **BACKGROUND:** #1A1410 (forge black)
- **GRID:** #2C2420 (dark brass)
- **STROKES:** #B8922A (brass)
- **EMBER:** #C4501A (ember orange)
- **TEXT_PRIMARY:** #E8E0D4 (warm light)
- **TEXT_SECONDARY:** #9A9088 (muted steel)

## Typography
- **TITLES:** Playfair Display
- **LABELS:** Barlow Condensed
- **SUBTEXT:** Libre Baskerville

## Aesthetic Rules
- Brass grid lines across the canvas
- Brass stroke outlines on all diagram boxes
- Ember nodes marking connection points
- CIC crest watermark bottom-right, opacity 0.22
- No drop shadows, no gradients, no rounded corners
- Strict geometric alignment
- Consistent spacing and margins

## Canvas Sizes
- **Standard diagram:** 1200×800
- **Master sheet:** 3840×2160

## Layout Principles
- Three rows: GLOBAL, PIPELINE, SYSTEM-WIDE
- Centered row labels
- Even horizontal spacing
- Maintain aspect ratio of embedded diagrams
- No dividers unless specified

## Behavior Rules
- Do not invent new colors, fonts, or styles
- Use only the palette and rules above
- Follow exact geometry and spacing instructions when provided

## Wiki diagram readability (CIC-facing wiki embeds) — MUST

Industrial forge-black canvases (BACKGROUND `#1A1410` above) remain valid for **non-wiki** CIC artifacts (master sheets, dark preview UIs, treatment boards explicitly specified as forge).

For **curated CIC wiki diagrams** (GitHub wiki HTML/SVG/PNG and Mermaid `classDef` on `brand: cic` pages), authors MUST use **paper field** mode instead:

| Name | Hex | Use on wiki diagrams |
| --- | --- | --- |
| PAPER / PARCHMENT (board + default node fill) | `#F5F0E6` | Diagram board/background and default node fills |
| PAPER_ALT (optional node fill) | `#FAF6F0` | Alternate light/off-white node fill |
| INK (forge black as ink) | `#1A1410` | Text, borders, labels, chrome only — NEVER node/board fill on wiki diagrams |
| INK_SECONDARY | `#2C2420` | Secondary ink / muted chrome — NEVER default node fill on wiki diagrams |
| STROKES (brass) | `#B8922A` | Box outlines, connectors |
| EMBER | `#C4501A` | Accent stages, emphasis nodes, dashed feedback loops only |
| TEXT_ON_PAPER | `#1A1410` | Primary label text on parchment (dark on light) |
| TEXT_MUTED_ON_PAPER | `#5C5349` | Secondary labels on parchment |

### Wiki-diagram hard rules

- MUST use parchment/paper field for board + default node fills.
- MUST use forge black / near-black for ink and borders only.
- MUST use brass/ember as accents only (not default fills).
- MUST NOT ship dark-on-dark (near-black node fills with dark text, or forge-black boards with low-contrast labels) on CIC wiki diagrams.
- Visual exemplar: Chris's parchment/cream board reference (light/off-white node fills, black ink, ember/orange only on accent stages and dashed feedback).
- Coded contrast twin (pattern only): `C:\dev\sigil\docs\wiki\architecture.html` (`--color-paper`, `--color-ink`, `--color-accent`).

See also: `docs/CIC_DESIGN_SYSTEM_ENFORCEMENT.md` readability checklist and Toolforge `docs/meta/governance/wiki-style-and-structure.md` §8 / W13.
