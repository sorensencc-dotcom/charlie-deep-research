# CIC Master Sheet Diagrams

Placeholder directory for diagram assets referenced by the master sheet generator.

## Expected Diagrams

### Row 1: GLOBAL
- `multi_region.png` — Multi-Region Architecture
- `region_registry.png` — Region Registry & Proxy Logic

### Row 2: PIPELINE
- `harvester.png` — Harvester Pipeline
- `orchestrator.png` — Orchestrator Flow
- `queue_dlq.png` — Queue & DLQ Management

### Row 3: SYSTEM-WIDE
- `image_search.png` — Reverse Image Search Workflow
- `control_plane.png` — Control Plane Internal Routing
- `telemetry.png` — Telemetry & Observability

## Format Requirements

- **Size:** 1200×800 px
- **Format:** PNG (raster variant) or SVG (full-SVG variant)
- **Style:** Industrial CIC aesthetic (see cic_design_system.md)
- **Color Palette:** Use design system colors only
- **Grid/Strokes:** Brass (#B8922A) grid and outlines
- **Nodes:** Ember (#C4501A) connection points

## Generator Usage

The master sheet generator will:
- **Variant A:** Embed these PNG files as rasterized diagrams
- **Variant B:** Inline SVG content from these files into the master sheet

Ensure diagram files exist before generating master sheets.
