# CIC Master Sheet Diagrams

8 SVG architecture diagram templates for the CIC Master Sheet Generator.

## Diagram Templates

### Row 1: GLOBAL

- **multi_region.svg** — Multi-Region Architecture
  - 4-region hub topology with central coordination node
  - Shows US-E, US-W, EU, APAC regions

- **region_registry.svg** — Region Registry & Proxy Logic
  - Registry lookup system with proxy nodes (P1, P2, P3)
  - Routing logic distribution

### Row 2: PIPELINE

- **harvester.svg** — Harvester Pipeline
  - 5-stage data ingestion: Fetch → Parse → Validate → Enrich → Store
  - DLQ error routing

- **orchestrator.svg** — Orchestrator Flow
  - Task queue input, central orchestrator
  - Worker pool (W1, W2, W3), status database

- **queue_dlq.svg** — Queue & DLQ Management
  - Primary queue, processor node
  - Success path, DLQ path, retry queue

### Row 3: SYSTEM-WIDE

- **image_search.svg** — Reverse Image Search Workflow
  - Feature extraction → Similarity search → Results ranking
  - Index node integration

- **control_plane.svg** — Control Plane Internal Routing
  - Policies and rules input
  - Policy distribution to data plane nodes (DP1, DP2)
  - Sync status tracking

- **telemetry.svg** — Telemetry & Observability
  - 3 data sources → Collector → Aggregation
  - 3 outputs: Metrics, Logs, Traces

## Specifications

- **Size:** 1200×800px
- **Format:** SVG (vector, scalable)
- **Grid:** Brass (#2C2420) 50px spacing
- **Strokes:** Brass (#B8922A) 2px width
- **Nodes:** Ember (#C4501A) circles with 20-30px radius
- **Connectors:** Brass arrows, 1.5px width

## Styling

All diagrams use:

- **Background:** Forge black (#1A1410)
- **Fonts:**
  - Titles: Playfair Display (28px bold)
  - Labels: Barlow Condensed (14px semi-bold)
- **No shadows, no gradients, no rounded corners**
- **Strict geometric alignment**

## Usage

The master sheet generator automatically:
- **Variant A (Raster):** References these as `<image>` tags
- **Variant B (Full-SVG):** Inlines full SVG content as `<g>` groups

All diagrams are pre-built and ready for embedding.
