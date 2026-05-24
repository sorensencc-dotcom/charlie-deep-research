# CIC Master Sheet Generator

Industrial architectural visualization system for Cast Iron Charlie platform documentation.

## Overview

Generates high-fidelity master sheets displaying system architecture across three dimensions:
- **GLOBAL:** Multi-region and regional configuration
- **PIPELINE:** Data harvesting, orchestration, and queueing
- **SYSTEM-WIDE:** Search workflows, control plane, observability

## Quick Start

### Generate Master Sheet

```bash
python generate_master_sheet.py A  # Raster-embedded (docs-ready)
python generate_master_sheet.py B  # Full-SVG (infinite resolution)
```

### Generate Diagram Templates

```bash
python generate_diagrams.py  # Creates 8 SVG diagram templates
```

## Architecture

### Components

| File | Purpose |
|------|---------|
| `generate_master_sheet.py` | Main generator (3840×2160 SVG output) |
| `generate_diagrams.py` | Diagram template generator |
| `diagrams/` | 8 architecture diagram templates (1200×800 SVG) |
| `cic_design_system.md` | Design system specification |
| `bob_master_sheet_v1.md` | BOB specification for master sheet |

### 8 Diagrams

#### GLOBAL Row

1. **Multi-Region Architecture** — 4-region hub topology with central coordination
2. **Region Registry & Proxy Logic** — Registry lookup and proxy routing system

#### PIPELINE Row

3. **Harvester Pipeline** — 5-stage data ingestion (fetch → parse → validate → enrich → store)
4. **Orchestrator Flow** — Task queue, worker pool, status tracking
5. **Queue & DLQ Management** — Primary queue, retry queue, dead-letter queue paths

#### SYSTEM-WIDE Row

6. **Reverse Image Search Workflow** — Feature extraction → similarity search → ranking
7. **Control Plane Internal Routing** — Policy distribution to data plane nodes
8. **Telemetry & Observability** — Collector → aggregation → metrics/logs/traces

## Design System

### Palette

- **Background:** #1A1410 (forge black)
- **Grid:** #2C2420 (dark brass)
- **Strokes:** #B8922A (brass)
- **Ember:** #C4501A (ember orange)
- **Text Primary:** #E8E0D4 (warm light)
- **Text Secondary:** #9A9088 (muted steel)

### Typography

- **Titles:** Playfair Display (28px, bold)
- **Labels:** Barlow Condensed (14px, semi-bold)
- **Subtext:** Libre Baskerville (body text)

### Aesthetic Rules

- Brass grid lines (40px spacing)
- Brass stroke outlines (2px width)
- Ember nodes at connection points
- No drop shadows, gradients, or rounded corners
- Strict geometric alignment
- CIC crest watermark (opacity 0.22, bottom-right)

## Output Formats

### Variant A: Raster-Embedded (Docs-Ready)

```xml
<image href="diagrams/multi_region.png" x="..." y="..." width="1200" height="800"/>
```

- Uses PNG diagram references
- Lightweight, embed-friendly
- Best for documentation sites

### Variant B: Full-SVG (Infinite Resolution)

```xml
<g id="diagram_multi_region">
  <!-- Full SVG content inlined -->
</g>
```

- Inlines complete SVG diagrams
- Infinite resolution scaling
- Archival-grade, self-contained

## BOB Execution Mode

When BOB specs are provided with RUN commands:

```
RUN BOB_CIC_MASTER_SHEET_V1 A
RUN BOB_CIC_MASTER_SHEET_V1 B
```

- Executes exactly as specified
- No inference or validation
- Returns "Specify A or B" if variant not provided

## Canvas Specifications

- **Diagram Size:** 1200×800px
- **Master Sheet Size:** 3840×2160px
- **Row Layout:** 3 rows (GLOBAL, PIPELINE, SYSTEM-WIDE)
- **Spacing:** 200px top margin, 160px between rows
- **Diagram Spacing:** 60px horizontal padding

## Development

### Adding New Diagrams

1. Create SVG template in `diagrams/` following design system
2. Update `generate_master_sheet.py` DIAGRAMS structure
3. Update this README

### Updating Design System

Edit `cic_design_system.md` and propagate changes to:
- SVG style blocks
- CSS in Streamlit app
- Design documentation

## Status

✅ Design system defined  
✅ BOB specification finalized  
✅ Master sheet generator implemented  
✅ 8 diagram templates created  
✅ Ready for output generation

## Next Steps

- Generate master sheet variants (A & B)
- Integrate into documentation site
- Add diagram customization workflows
