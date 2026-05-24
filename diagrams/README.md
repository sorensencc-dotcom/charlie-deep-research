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

Each diagram follows the CIC Industrial Design System:

- Forge black background
- Brass grid and strokes
- Ember nodes
- Playfair / Barlow / Baskerville typography

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
