# BOB_CIC_MASTER_SHEET_V1

**BOB_NAME:** CIC_MASTER_SHEET_V1  
**BOB_KIND:** GENERATOR_SPEC  
**BOB_ROLE:** Defines how to generate the CIC Master Sheet in two variants (A and B) without invoking tasks unless explicitly commanded.

## Intent
Produce two master-sheet outputs:
- **A.** Raster-Embedded Master Sheet (Docs-Ready)
- **B.** Full-SVG Master Sheet (Infinite-Resolution)

Both using the Industrial CIC aesthetic and Option 1 (section headers only).

## Scope
This BOB defines:
- Layout geometry
- Row structure
- Scaling rules
- Labeling rules
- Aesthetic constraints
- Output expectations

It does NOT execute generation. It only defines the spec.

## Outputs
Two artifacts when invoked:
- **A. MASTER_SHEET_RASTER** (3840×2160 SVG embedding rasterized diagrams)
- **B. MASTER_SHEET_SVG** (3840×2160 SVG with inline vector diagrams)

## Layout
**Canvas:** 3840×2160

### ROW_1_GLOBAL
- Multi-Region Architecture
- Region Registry & Proxy Logic

### ROW_2_PIPELINE
- Harvester Pipeline
- Orchestrator Flow
- Queue & DLQ Management

### ROW_3_SYSTEM_WIDE
- Reverse Image Search Workflow
- Control Plane Internal Routing
- Telemetry & Observability

### Row Labels
- GLOBAL
- PIPELINE
- SYSTEM-WIDE

Centered above each row. No dividers.

## Aesthetic
- Industrial background (#1A1410)
- Brass grid (#2C2420)
- Brass strokes (#B8922A)
- Ember nodes (#C4501A)
- Playfair Display for titles
- Barlow Condensed for labels
- Libre Baskerville for subtext
- CIC crest watermark bottom-right (opacity 0.22)

## Scaling Rules
- Each diagram scaled to same visual weight
- Maintain aspect ratio
- Uniform horizontal spacing
- 200px top margin, 160px between rows

## Variant Rules

### A. RASTER
- Each diagram embedded as `<image href="...">` at 1200×800 resolution
- No inline SVG groups
- Lightweight, docs-ready

### B. FULL_SVG
- Each diagram inlined as `<g>` containing its full SVG content
- Infinite resolution
- Heavy but archival-grade

## Execution Rules
- This BOB never triggers tasks
- Only executes when explicitly invoked with:
  - `RUN BOB_CIC_MASTER_SHEET_V1 A`
  - `RUN BOB_CIC_MASTER_SHEET_V1 B`
- If invoked without A or B, return: "Specify A or B."

## Validation
- All eight diagrams must be present
- All labels must be present
- Canvas must be exactly 3840×2160
- No missing fonts, no missing strokes
- Crest must be present
