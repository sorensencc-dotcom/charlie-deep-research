#!/usr/bin/env python3
"""
CIC Diagram Template Generator
Produces 8 individual diagram templates following the industrial design system.
"""

from xml.etree.ElementTree import Element, SubElement, tostring
from pathlib import Path

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

WIDTH = 1200
HEIGHT = 800


def create_base_svg(title: str) -> Element:
    """Create SVG base with grid and styling"""
    svg = Element("svg")
    svg.set("width", str(WIDTH))
    svg.set("height", str(HEIGHT))
    svg.set("viewBox", f"0 0 {WIDTH} {HEIGHT}")
    svg.set("xmlns", "http://www.w3.org/2000/svg")

    # Styles
    defs = SubElement(svg, "defs")
    style = SubElement(defs, "style")
    style.text = f"""
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Barlow+Condensed:wght@400;600;700&family=Libre+Baskerville:wght@400;700&display=swap');

    .title {{
        font-family: '{FONTS["title"]}', serif;
        font-size: 28px;
        font-weight: 700;
        fill: {PALETTE["text_primary"]};
    }}

    .label {{
        font-family: '{FONTS["label"]}', sans-serif;
        font-size: 14px;
        font-weight: 600;
        fill: {PALETTE["text_secondary"]};
        letter-spacing: 0.05em;
    }}

    .box {{
        stroke: {PALETTE["strokes"]};
        stroke-width: 2;
        fill: none;
    }}

    .node {{
        fill: {PALETTE["ember"]};
    }}

    .connector {{
        stroke: {PALETTE["strokes"]};
        stroke-width: 1.5;
        fill: none;
    }}

    .grid-line {{
        stroke: {PALETTE["grid"]};
        stroke-width: 0.5;
    }}
    """

    # Background
    bg = SubElement(svg, "rect")
    bg.set("width", str(WIDTH))
    bg.set("height", str(HEIGHT))
    bg.set("fill", PALETTE["background"])

    # Grid
    for x in range(0, WIDTH, 50):
        line = SubElement(svg, "line")
        line.set("class", "grid-line")
        line.set("x1", str(x))
        line.set("y1", "0")
        line.set("x2", str(x))
        line.set("y2", str(HEIGHT))

    for y in range(0, HEIGHT, 50):
        line = SubElement(svg, "line")
        line.set("class", "grid-line")
        line.set("x1", "0")
        line.set("y1", str(y))
        line.set("x2", str(WIDTH))
        line.set("y2", str(y))

    # Title
    title_elem = SubElement(svg, "text")
    title_elem.set("class", "title")
    title_elem.set("x", "40")
    title_elem.set("y", "50")
    title_elem.text = title

    return svg


def add_box(svg: Element, x: int, y: int, w: int, h: int, label: str = ""):
    """Add a labeled box"""
    rect = SubElement(svg, "rect")
    rect.set("class", "box")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", str(w))
    rect.set("height", str(h))

    if label:
        text = SubElement(svg, "text")
        text.set("class", "label")
        text.set("x", str(x + w // 2))
        text.set("y", str(y + h // 2 + 5))
        text.set("text-anchor", "middle")
        text.text = label


def add_circle(svg: Element, cx: int, cy: int, r: int, label: str = ""):
    """Add a labeled circle node"""
    circle = SubElement(svg, "circle")
    circle.set("class", "node")
    circle.set("cx", str(cx))
    circle.set("cy", str(cy))
    circle.set("r", str(r))

    if label:
        text = SubElement(svg, "text")
        text.set("class", "label")
        text.set("x", str(cx))
        text.set("y", str(cy + 5))
        text.set("text-anchor", "middle")
        text.text = label


def add_connector(svg: Element, x1: int, y1: int, x2: int, y2: int):
    """Add a connection line with arrow"""
    line = SubElement(svg, "line")
    line.set("class", "connector")
    line.set("x1", str(x1))
    line.set("y1", str(y1))
    line.set("x2", str(x2))
    line.set("y2", str(y2))
    line.set("marker-end", "url(#arrowhead)")


def add_arrow_marker(svg: Element):
    """Add arrow marker definition"""
    defs = svg.find("defs")
    marker = SubElement(defs, "marker")
    marker.set("id", "arrowhead")
    marker.set("markerWidth", "10")
    marker.set("markerHeight", "10")
    marker.set("refX", "9")
    marker.set("refY", "3")
    marker.set("orient", "auto")
    polygon = SubElement(marker, "polygon")
    polygon.set("points", f"0 0, 10 3, 0 6")
    polygon.set("fill", PALETTE["strokes"])


def save_svg(svg: Element, filename: str):
    """Save SVG to file"""
    svg_string = tostring(svg, encoding="unicode")
    output = f'<?xml version="1.0" encoding="UTF-8"?>\n{svg_string}'
    Path(f"diagrams/{filename}").write_text(output)


# ============================================================================
# DIAGRAM GENERATORS
# ============================================================================


def diagram_multi_region():
    """Multi-Region Architecture: Global distribution with region nodes"""
    svg = create_base_svg("Multi-Region Architecture")
    add_arrow_marker(svg)

    # Central hub
    add_circle(svg, 600, 300, 30, "HUB")

    # Regional nodes
    regions = [
        (200, 150, "US-E"),
        (1000, 150, "US-W"),
        (200, 450, "EU"),
        (1000, 450, "APAC"),
    ]

    for x, y, label in regions:
        add_circle(svg, x, y, 25, label)
        add_connector(svg, x, y, 570, 300)

    # Region boxes
    add_box(svg, 120, 90, 160, 140, "Region 1")
    add_box(svg, 920, 90, 160, 140, "Region 2")
    add_box(svg, 120, 390, 160, 140, "Region 3")
    add_box(svg, 920, 390, 160, 140, "Region 4")

    save_svg(svg, "multi_region.svg")


def diagram_region_registry():
    """Region Registry & Proxy Logic: Registry lookup and routing"""
    svg = create_base_svg("Region Registry & Proxy Logic")
    add_arrow_marker(svg)

    # Input
    add_box(svg, 100, 300, 120, 80, "Request")

    # Registry
    add_box(svg, 300, 250, 160, 180, "Region Registry")

    # Proxy nodes
    for i, label in enumerate(["P1", "P2", "P3"]):
        y = 100 + i * 200
        add_circle(svg, 600, y + 40, 20, label)
        add_connector(svg, 460, 340, 580, y + 40)

    # Output routing
    add_box(svg, 750, 250, 140, 180, "Route\nLogic")
    add_connector(svg, 460, 340, 750, 340)

    save_svg(svg, "region_registry.svg")


def diagram_harvester_pipeline():
    """Harvester Pipeline: Data ingestion workflow"""
    svg = create_base_svg("Harvester Pipeline")
    add_arrow_marker(svg)

    stages = [
        (150, "Fetch"),
        (350, "Parse"),
        (550, "Validate"),
        (750, "Enrich"),
        (950, "Store"),
    ]

    for x, label in stages:
        add_box(svg, x - 50, 250, 100, 100, label)

    # Connect stages
    for i in range(len(stages) - 1):
        x1 = stages[i][0] + 50
        x2 = stages[i + 1][0] - 50
        add_connector(svg, x1, 300, x2, 300)

    # Error paths
    add_circle(svg, 600, 500, 20, "DLQ")
    add_connector(svg, 600, 350, 600, 480)

    save_svg(svg, "harvester.svg")


def diagram_orchestrator_flow():
    """Orchestrator Flow: Task orchestration and scheduling"""
    svg = create_base_svg("Orchestrator Flow")
    add_arrow_marker(svg)

    # Central orchestrator
    add_box(svg, 500, 250, 120, 100, "Orchestrator")

    # Task queue
    add_box(svg, 150, 150, 120, 80, "Task Queue")
    add_connector(svg, 270, 190, 500, 280)

    # Worker pool
    workers = [(700, 150), (700, 300), (700, 450)]
    for x, y in workers:
        add_circle(svg, x, y, 25, "W")
        add_connector(svg, 620, 250 + (y - 300) // 3, 675, y)

    # Status tracking
    add_box(svg, 150, 400, 120, 80, "Status DB")
    add_connector(svg, 560, 350, 210, 400)

    save_svg(svg, "orchestrator.svg")


def diagram_queue_dlq():
    """Queue & DLQ Management: Message handling and failure routing"""
    svg = create_base_svg("Queue & DLQ Management")
    add_arrow_marker(svg)

    # Main queue
    add_box(svg, 200, 250, 140, 100, "Primary\nQueue")

    # Processing
    add_circle(svg, 500, 300, 25, "PROC")
    add_connector(svg, 340, 300, 475, 300)

    # Success path
    add_box(svg, 700, 200, 120, 80, "Success")
    add_connector(svg, 525, 280, 700, 240)

    # DLQ path
    add_box(svg, 700, 400, 120, 80, "DLQ")
    add_connector(svg, 525, 320, 700, 440)

    # Retry mechanism
    add_box(svg, 200, 500, 140, 80, "Retry\nQueue")
    add_connector(svg, 270, 500, 270, 350)

    save_svg(svg, "queue_dlq.svg")


def diagram_reverse_image_search():
    """Reverse Image Search Workflow: Image matching pipeline"""
    svg = create_base_svg("Reverse Image Search Workflow")
    add_arrow_marker(svg)

    # Input image
    add_box(svg, 100, 300, 100, 100, "Input\nImage")

    # Feature extraction
    add_box(svg, 280, 280, 110, 140, "Feature\nExtraction")
    add_connector(svg, 200, 350, 280, 350)

    # Similarity search
    add_box(svg, 480, 280, 110, 140, "Similarity\nSearch")
    add_connector(svg, 390, 350, 480, 350)

    # Index
    add_circle(svg, 590, 550, 30, "Index")
    add_connector(svg, 535, 420, 590, 520)

    # Results
    add_box(svg, 700, 280, 110, 140, "Results\nRanking")
    add_connector(svg, 590, 350, 700, 350)

    save_svg(svg, "image_search.svg")


def diagram_control_plane():
    """Control Plane Internal Routing: Configuration and policy distribution"""
    svg = create_base_svg("Control Plane Internal Routing")
    add_arrow_marker(svg)

    # Control plane
    add_box(svg, 450, 150, 140, 100, "Control\nPlane")

    # Config sources
    sources = [(150, 200, "Policies"), (150, 350, "Rules")]
    for x, y, label in sources:
        add_box(svg, x, y, 100, 80, label)
        add_connector(svg, 250, y + 40, 450, y + 40)

    # Data plane nodes
    nodes = [(900, 200, "DP1"), (900, 350, "DP2")]
    for x, y, label in nodes:
        add_circle(svg, x, y, 25, label)
        add_connector(svg, 590, 200 if y == 200 else 350, x - 25, y)

    # Sync indicator
    add_box(svg, 300, 500, 100, 80, "Sync Status")

    save_svg(svg, "control_plane.svg")


def diagram_telemetry():
    """Telemetry & Observability: Metrics and monitoring"""
    svg = create_base_svg("Telemetry & Observability")
    add_arrow_marker(svg)

    # Data sources
    sources = [(150, 150), (150, 350), (150, 550)]
    for i, (x, y) in enumerate(sources):
        add_circle(svg, x, y, 20, f"S{i + 1}")

    # Collector
    add_box(svg, 350, 300, 120, 120, "Collector")

    # Connect sources to collector
    for x, y in sources:
        add_connector(svg, x + 20, y, 350, 360)

    # Processing
    add_box(svg, 600, 250, 120, 100, "Aggregation")
    add_connector(svg, 470, 360, 600, 300)

    # Outputs
    outputs = [(900, 200, "Metrics"), (900, 350, "Logs"), (900, 500, "Traces")]
    for x, y, label in outputs:
        add_box(svg, x - 60, y - 40, 120, 80, label)
        add_connector(svg, 720, 300, x - 60, y)

    save_svg(svg, "telemetry.svg")


def generate_all():
    """Generate all 8 diagram templates"""
    diagrams = [
        ("Multi-Region Architecture", diagram_multi_region),
        ("Region Registry & Proxy Logic", diagram_region_registry),
        ("Harvester Pipeline", diagram_harvester_pipeline),
        ("Orchestrator Flow", diagram_orchestrator_flow),
        ("Queue & DLQ Management", diagram_queue_dlq),
        ("Reverse Image Search Workflow", diagram_reverse_image_search),
        ("Control Plane Internal Routing", diagram_control_plane),
        ("Telemetry & Observability", diagram_telemetry),
    ]

    for name, generator in diagrams:
        print(f"Generating {name}...")
        generator()

    print(f"\n✓ Generated {len(diagrams)} diagram templates in diagrams/")


if __name__ == "__main__":
    generate_all()
