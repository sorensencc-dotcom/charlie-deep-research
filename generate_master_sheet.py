#!/usr/bin/env python3
"""
CIC Master Sheet Generator V1
Produces two variants: A (Raster-Embedded) and B (Full-SVG)
"""

from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from datetime import datetime

# Design System
PALETTE = {
    "background": "#1A1410",
    "grid": "#2C2420",
    "strokes": "#B8922A",
    "ember": "#C4501A",
    "text_primary": "#E8E0D4",
    "text_secondary": "#9A9088",
}

FONTS = {
    "title": "Playfair Display",
    "label": "Barlow Condensed",
    "subtext": "Libre Baskerville",
}

CANVAS_WIDTH = 3840
CANVAS_HEIGHT = 2160

ROW_LABELS = ["GLOBAL", "PIPELINE", "SYSTEM-WIDE"]

DIAGRAMS = [
    # ROW 1: GLOBAL
    [
        {"title": "Multi-Region Architecture", "id": "multi_region"},
        {"title": "Region Registry & Proxy Logic", "id": "region_registry"},
    ],
    # ROW 2: PIPELINE
    [
        {"title": "Harvester Pipeline", "id": "harvester"},
        {"title": "Orchestrator Flow", "id": "orchestrator"},
        {"title": "Queue & DLQ Management", "id": "queue_dlq"},
    ],
    # ROW 3: SYSTEM-WIDE
    [
        {"title": "Reverse Image Search Workflow", "id": "image_search"},
        {"title": "Control Plane Internal Routing", "id": "control_plane"},
        {"title": "Telemetry & Observability", "id": "telemetry"},
    ],
]

DIAGRAM_WIDTH = 1200
DIAGRAM_HEIGHT = 800

TOP_MARGIN = 200
ROW_SPACING = 160
DIAGRAM_SPACING = 60


class MasterSheetGenerator:
    def __init__(self, variant: str):
        """Initialize generator for variant A (raster) or B (full_svg)"""
        if variant not in ("A", "B"):
            raise ValueError("Specify A or B.")
        self.variant = variant
        self.svg = None

    def create_svg(self) -> Element:
        """Create the base SVG element with styling"""
        svg = Element("svg")
        svg.set("width", str(CANVAS_WIDTH))
        svg.set("height", str(CANVAS_HEIGHT))
        svg.set("viewBox", f"0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}")
        svg.set("xmlns", "http://www.w3.org/2000/svg")
        svg.set("xmlns:xlink", "http://www.w3.org/1999/xlink")

        # Add styles
        defs = SubElement(svg, "defs")
        style = SubElement(defs, "style")
        style.text = self._get_styles()

        # Background
        bg = SubElement(svg, "rect")
        bg.set("width", str(CANVAS_WIDTH))
        bg.set("height", str(CANVAS_HEIGHT))
        bg.set("fill", PALETTE["background"])

        # Grid pattern
        pattern = SubElement(defs, "pattern")
        pattern.set("id", "brass_grid")
        pattern.set("width", "40")
        pattern.set("height", "40")
        pattern.set("patternUnits", "userSpaceOnUse")

        grid_h = SubElement(pattern, "line")
        grid_h.set("x1", "0")
        grid_h.set("y1", "0")
        grid_h.set("x2", "40")
        grid_h.set("y2", "0")
        grid_h.set("stroke", PALETTE["grid"])
        grid_h.set("stroke-width", "0.5")

        grid_v = SubElement(pattern, "line")
        grid_v.set("x1", "0")
        grid_v.set("y1", "0")
        grid_v.set("x2", "0")
        grid_v.set("y2", "40")
        grid_v.set("stroke", PALETTE["grid"])
        grid_v.set("stroke-width", "0.5")

        grid_rect = SubElement(svg, "rect")
        grid_rect.set("width", str(CANVAS_WIDTH))
        grid_rect.set("height", str(CANVAS_HEIGHT))
        grid_rect.set("fill", "url(#brass_grid)")

        self.svg = svg
        return svg

    def _get_styles(self) -> str:
        """Return embedded CSS styles"""
        return f"""
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Barlow+Condensed:wght@400;600;700&family=Libre+Baskerville:wght@400;700&display=swap');

        .row-label {{
            font-family: '{FONTS["label"]}', sans-serif;
            font-size: 48px;
            font-weight: 700;
            fill: {PALETTE["text_primary"]};
            letter-spacing: 0.15em;
            text-transform: uppercase;
        }}

        .diagram-title {{
            font-family: '{FONTS["title"]}', serif;
            font-size: 32px;
            font-weight: 700;
            fill: {PALETTE["text_primary"]};
        }}

        .diagram-box {{
            stroke: {PALETTE["strokes"]};
            stroke-width: 2;
            fill: none;
        }}

        .ember-node {{
            fill: {PALETTE["ember"]};
            r: 6;
        }}
        """

    def add_row(self, row_index: int, row_label: str, diagrams: list):
        """Add a row of diagrams with label"""
        # Calculate row position
        y_offset = TOP_MARGIN + (row_index * (DIAGRAM_HEIGHT + ROW_SPACING))

        # Add row label
        label = SubElement(self.svg, "text")
        label.set("class", "row-label")
        label.set("x", str(CANVAS_WIDTH // 2))
        label.set("y", str(y_offset - 60))
        label.set("text-anchor", "middle")
        label.text = row_label

        # Calculate x positions for diagrams in this row
        num_diagrams = len(diagrams)
        total_width = (num_diagrams * DIAGRAM_WIDTH) + (
            (num_diagrams - 1) * DIAGRAM_SPACING
        )
        start_x = (CANVAS_WIDTH - total_width) // 2

        # Add diagrams
        for i, diagram in enumerate(diagrams):
            x = start_x + (i * (DIAGRAM_WIDTH + DIAGRAM_SPACING))
            self.add_diagram(x, y_offset, diagram)

    def add_diagram(self, x: int, y: int, diagram: dict):
        """Add a single diagram box"""
        # Diagram border
        box = SubElement(self.svg, "rect")
        box.set("class", "diagram-box")
        box.set("x", str(x))
        box.set("y", str(y))
        box.set("width", str(DIAGRAM_WIDTH))
        box.set("height", str(DIAGRAM_HEIGHT))

        # Placeholder for diagram content
        placeholder_id = f"diagram_{diagram['id']}"

        if self.variant == "A":
            # Raster variant: embed as image reference
            img = SubElement(self.svg, "image")
            img.set("xlink:href", f"diagrams/{diagram['id']}.png")
            img.set("x", str(x))
            img.set("y", str(y))
            img.set("width", str(DIAGRAM_WIDTH))
            img.set("height", str(DIAGRAM_HEIGHT))
            img.set("preserveAspectRatio", "xMidYMid meet")
        else:
            # Full SVG variant: placeholder for inlined content
            group = SubElement(self.svg, "g")
            group.set("id", placeholder_id)
            group.set("data-diagram", diagram["id"])

            # Placeholder rectangle indicating where SVG content will be inlined
            placeholder = SubElement(group, "rect")
            placeholder.set("x", str(x + 10))
            placeholder.set("y", str(y + 10))
            placeholder.set("width", str(DIAGRAM_WIDTH - 20))
            placeholder.set("height", str(DIAGRAM_HEIGHT - 20))
            placeholder.set("fill", PALETTE["background"])
            placeholder.set("stroke", PALETTE["ember"])
            placeholder.set("stroke-width", "1")
            placeholder.set("stroke-dasharray", "5,5")

        # Diagram title below
        title = SubElement(self.svg, "text")
        title.set("class", "diagram-title")
        title.set("x", str(x + DIAGRAM_WIDTH // 2))
        title.set("y", str(y + DIAGRAM_HEIGHT + 40))
        title.set("text-anchor", "middle")
        title.text = diagram["title"]

        # Ember corner nodes
        self._add_corner_nodes(x, y)

    def _add_corner_nodes(self, x: int, y: int):
        """Add ember-colored corner nodes to diagram"""
        corners = [
            (x, y),
            (x + DIAGRAM_WIDTH, y),
            (x, y + DIAGRAM_HEIGHT),
            (x + DIAGRAM_WIDTH, y + DIAGRAM_HEIGHT),
        ]
        for cx, cy in corners:
            circle = SubElement(self.svg, "circle")
            circle.set("class", "ember-node")
            circle.set("cx", str(cx))
            circle.set("cy", str(cy))

    def add_watermark(self):
        """Add CIC crest watermark at bottom-right"""
        text = SubElement(self.svg, "text")
        text.set("x", str(CANVAS_WIDTH - 80))
        text.set("y", str(CANVAS_HEIGHT - 40))
        text.set("font-family", FONTS["label"])
        text.set("font-size", "24")
        text.set("fill", PALETTE["text_secondary"])
        text.set("opacity", "0.22")
        text.set("text-anchor", "end")
        text.text = "CIC"

    def generate(self) -> str:
        """Generate the master sheet SVG"""
        self.create_svg()

        # Add each row
        for row_idx, (label, diagrams) in enumerate(zip(ROW_LABELS, DIAGRAMS)):
            self.add_row(row_idx, label, diagrams)

        # Add watermark
        self.add_watermark()

        # Convert to string
        svg_string = tostring(self.svg, encoding="unicode")

        # Pretty print with XML declaration
        return f'<?xml version="1.0" encoding="UTF-8"?>\n{svg_string}'

    def save(self, filepath: str):
        """Save the generated SVG to file"""
        svg_content = self.generate()
        Path(filepath).write_text(svg_content)


def run(variant: str):
    """Run the generator for the specified variant"""
    if variant not in ("A", "B"):
        return "Specify A or B."

    variant_name = "RASTER" if variant == "A" else "FULL_SVG"
    filename = f"master_sheet_{variant}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.svg"

    generator = MasterSheetGenerator(variant)
    generator.save(filename)

    return f"Generated MASTER_SHEET_{variant_name}: {filename}"


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        result = run(sys.argv[1])
        print(result)
    else:
        print("Usage: python generate_master_sheet.py [A|B]")
        print("  A: Raster-Embedded Master Sheet (Docs-Ready)")
        print("  B: Full-SVG Master Sheet (Infinite-Resolution)")
