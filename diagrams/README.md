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

Each diagram follows the **CIC Industrial Design System** (source of truth: [`../cic_design_system.md`](../cic_design_system.md); author checklist: [`../docs/CIC_DESIGN_SYSTEM_ENFORCEMENT.md`](../docs/CIC_DESIGN_SYSTEM_ENFORCEMENT.md)):

- Forge black background `#1A1410`
- Brass grid `#2C2420` and strokes `#B8922A`
- Ember nodes `#C4501A`
- Playfair / Barlow / Baskerville typography
- CIC crest watermark bottom-right at opacity 0.22
- No drop shadows, gradients, or rounded corners

## Master Sheets

Two master sheet variants are generated from these diagrams:

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
