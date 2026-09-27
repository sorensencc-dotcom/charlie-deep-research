# CIC Industrial Diagrams

This directory contains the eight canonical CIC Industrial‑style diagrams:

1. Multi‑Region Architecture
2. Region Registry & Proxy Logic
3. Harvester Pipeline
4. Orchestrator Flow
5. Queue & DLQ Management
6. Reverse Image Search Workflow
7. Control Plane Internal Routing
8. Telemetry & Observability

Wiki-facing SVGs / HTML embeds follow the **CIC Industrial Design System** in **readable parchment** mode (source of truth: [`../cic_design_system.md`](../cic_design_system.md); author checklist: [`../docs/CIC_DESIGN_SYSTEM_ENFORCEMENT.md`](../docs/CIC_DESIGN_SYSTEM_ENFORCEMENT.md)):

- Parchment board `#F5F0E6` (cream field — not forge black)
- Off-white node fills (light / cream); forge black `#1A1410` for **ink, borders, and labels only**
- Brass strokes `#B8922A` and ember accents `#C4501A` (highlights / feedback — not default fills)
- Playfair / Barlow / Baskerville typography
- CIC crest watermark bottom-right at opacity 0.22
- No drop shadows, gradients, or rounded corners

Industrial forge-black canvases (`#1A1410`) remain valid for **non-wiki** master sheets and dark preview UIs only — do not copy those fills onto curated wiki diagram skins.

## Master Sheets

Two master sheet variants are generated from these diagrams (intentionally forge-black canvases; not wiki embeds):

### A — Raster‑Embedded

```bash
python ../generate_master_sheet.py A
```

### B — Full‑SVG (Inline)

```bash
python ../generate_master_sheet.py B
```

Outputs are written to:

```bash
../master_sheets/
```
