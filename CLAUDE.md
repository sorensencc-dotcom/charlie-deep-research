# Claude Execution Protocol (BOB Mode)

Claude operates in BOB‑execution mode for CIC diagram and master sheet generation.

## Load Everything (Single‑Paste)

Paste the combined loader block (Design System Primer + BOB + Execution Rules).
Claude will respond:

```text
Ready for BOB execution.
```

## Running the Master Sheet Generator

After loading the BOB:

### Raster Variant (A)

```text
RUN BOB_CIC_MASTER_SHEET_V1 A
```

### Full‑SVG Variant (B)

```text
RUN BOB_CIC_MASTER_SHEET_V1 B
```

Claude will output the corresponding 3840×2160 Industrial master sheet.

## Rules

- Claude does not infer tasks.
- Claude does not modify specs.
- Claude executes only when given a RUN command.
- Claude outputs only the artifact defined by the BOB.
