# CLAUDE.md - Project Context

## Project: charlie-deep-research

Strategic tool for **Cast Iron Charlie** with integrated CIC architectural visualization system.

## 📊 Current Focus: CIC Master Sheet Generator

Builds industrial-styled architectural master sheets for CIC platform documentation.

### Architecture

- **Design System:** Industrial CIC aesthetic (forge black, brass, ember)
- **Generator:** Produces two variants (A: raster-embedded, B: full-SVG)
- **Diagrams:** 8 SVG templates covering global, pipeline, and system-wide architectures
- **Output Canvas:** 3840×2160px master sheets

### Key Files

- `generate_master_sheet.py` — Main generator (variants A & B)
- `generate_diagrams.py` — Diagram template generator
- `cic_design_system.md` — Design system specification
- `bob_master_sheet_v1.md` — BOB specification (BOB execution mode)
- `diagrams/` — 8 architecture diagram templates (1200×800 SVG)

### BOB Execution Mode

When user provides BOB specs with explicit RUN commands:

- Only executes on `RUN BOB_CIC_MASTER_SHEET_V1 A` or `RUN BOB_CIC_MASTER_SHEET_V1 B`
- No inference, no validation, no commentary
- Returns "Specify A or B" if invoked without variant selection

## ⚠️ Quota Management (March 2026)

- **Token Trimming:** Always slice scraped text to `[:1800]` chars.
- **Error 429:** Implement exponential backoff if rate-limited.

## 🎨 Design System

- **Primary Theme:** Industrial CIC (#1A1410 forge black)
- **Accent Palette:**
  - Brass: #B8922A (strokes, grid)
  - Ember: #C4501A (nodes, highlights)
  - Text Primary: #E8E0D4 (warm light)
  - Text Secondary: #9A9088 (muted steel)
- **Typography:**
  - Titles: Playfair Display
  - Labels: Barlow Condensed
  - Subtext: Libre Baskerville
