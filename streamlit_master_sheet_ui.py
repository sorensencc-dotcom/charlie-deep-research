#!/usr/bin/env python3
"""
CIC Master Sheet Live Preview UI
Displays both master sheet variants side-by-side with diagram selection.
"""

import streamlit as st
from pathlib import Path
import base64

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="CIC Master Sheet Preview",
    page_icon="⚒️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# STYLING
# ============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Barlow+Condensed:wght@300;400;600;700;800&display=swap');

    :root {
      --forge: #1a1410;
      --iron: #2c2420;
      --brass: #B8922A;
      --ember: #C4501A;
      --ash: #9a9088;
      --bone: #e8e0d4;
    }

    body {
        background-color: var(--forge);
        color: var(--bone);
    }

    .stApp {
        background-color: var(--forge);
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: var(--bone) !important;
    }

    .stTabs [data-baseweb="tab-list"] button {
        font-family: 'Barlow Condensed', sans-serif !important;
        color: var(--ash) !important;
        letter-spacing: 0.1em;
    }

    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: var(--bone) !important;
        border-bottom-color: var(--brass) !important;
    }

    .stButton > button {
        font-family: 'Barlow Condensed', sans-serif !important;
        background-color: var(--ember) !important;
        color: var(--forge) !important;
        border: none !important;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        font-weight: 700;
    }

    .stButton > button:hover {
        background-color: #d45a23 !important;
    }

    .diagram-tile {
        background: var(--iron);
        border: 1px solid var(--brass);
        padding: 12px;
        border-radius: 0;
        cursor: pointer;
        transition: all 0.2s;
    }

    .diagram-tile:hover {
        border-color: var(--ember);
        box-shadow: 0 0 8px rgba(196, 80, 26, 0.3);
    }

    .diagram-tile.active {
        border-color: var(--ember);
        background: rgba(196, 80, 26, 0.1);
    }

    .info-box {
        background: var(--iron);
        border-left: 3px solid var(--brass);
        padding: 16px;
        margin: 16px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# STATE
# ============================================================================

if "variant" not in st.session_state:
    st.session_state.variant = "A"

if "selected_diagrams" not in st.session_state:
    st.session_state.selected_diagrams = set()

# ============================================================================
# DIAGRAMS
# ============================================================================

DIAGRAMS = {
    "multi_region": "Multi-Region Architecture",
    "region_registry": "Region Registry & Proxy Logic",
    "harvester": "Harvester Pipeline",
    "orchestrator": "Orchestrator Flow",
    "queue_dlq": "Queue & DLQ Management",
    "image_search": "Reverse Image Search Workflow",
    "control_plane": "Control Plane Internal Routing",
    "telemetry": "Telemetry & Observability",
}

# ============================================================================
# HELPERS
# ============================================================================

def load_svg_file(filepath):
    """Load SVG file and return as base64-encoded string."""
    try:
        with open(filepath, 'r') as f:
            svg_content = f.read()
        return svg_content
    except FileNotFoundError:
        return None

def get_master_sheet_file(variant):
    """Find the most recent master sheet file for variant."""
    pattern = f"master_sheet_{variant}_*.svg"
    matches = list(Path(".").glob(pattern))
    if matches:
        return sorted(matches)[-1]
    return None

# ============================================================================
# HEADER
# ============================================================================

col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.markdown("# CIC Master Sheet Preview")
    st.markdown("Industrial‑style system architecture visualization")

with col2:
    st.write("")
    st.write("")
    variant = st.radio(
        "Variant",
        options=["A", "B"],
        horizontal=True,
        format_func=lambda x: f"{x} — {'Raster' if x == 'A' else 'Full-SVG'}",
        key="variant_selector"
    )
    st.session_state.variant = variant

# ============================================================================
# INFO
# ============================================================================

st.markdown("---")

if st.session_state.variant == "A":
    st.markdown("""
    <div class="info-box">
    <strong>Variant A: Raster-Embedded</strong><br>
    Lightweight, docs-ready format with embedded diagram images. Ideal for README and web embedding.
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="info-box">
    <strong>Variant B: Full-SVG</strong><br>
    Infinite-resolution archival format with fully inlined vector diagrams. Self-contained, scalable.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MASTER SHEET DISPLAY
# ============================================================================

st.markdown("## Master Sheet")

master_sheet_file = get_master_sheet_file(st.session_state.variant)

if master_sheet_file:
    svg_content = load_svg_file(master_sheet_file)
    if svg_content:
        st.markdown(f"**Generated:** {master_sheet_file.name}")
        st.divider()

        # Display SVG
        col_left, col_right = st.columns([2, 1])

        with col_left:
            st.markdown(f"""
            <iframe
                srcDoc="{svg_content.replace('"', '&quot;')}"
                style="width:100%; height:600px; border: 1px solid #2c2420;"
                frameborder="0"
            ></iframe>
            """, unsafe_allow_html=True)

        with col_right:
            st.markdown("### Diagrams")
            st.markdown("8 architecture diagrams across 3 rows")

            st.markdown("**GLOBAL**")
            for diagram_id in ["multi_region", "region_registry"]:
                st.caption(DIAGRAMS[diagram_id])

            st.markdown("**PIPELINE**")
            for diagram_id in ["harvester", "orchestrator", "queue_dlq"]:
                st.caption(DIAGRAMS[diagram_id])

            st.markdown("**SYSTEM-WIDE**")
            for diagram_id in ["image_search", "control_plane", "telemetry"]:
                st.caption(DIAGRAMS[diagram_id])
    else:
        st.error("Failed to load master sheet SVG content")
else:
    st.warning(f"No master sheet found for Variant {st.session_state.variant}")
    st.info("Generate with: `python generate_master_sheet.py {variant}`")

# ============================================================================
# DIAGRAM EXPLORER
# ============================================================================

st.markdown("---")
st.markdown("## Individual Diagrams")

col1, col2 = st.columns([3, 1])

with col2:
    if st.button("Refresh", use_container_width=True):
        st.rerun()

tabs = st.tabs(["GLOBAL", "PIPELINE", "SYSTEM-WIDE"])

diagram_groups = {
    "GLOBAL": ["multi_region", "region_registry"],
    "PIPELINE": ["harvester", "orchestrator", "queue_dlq"],
    "SYSTEM-WIDE": ["image_search", "control_plane", "telemetry"],
}

for tab_idx, (tab_name, diagram_ids) in enumerate(diagram_groups.items()):
    with tabs[tab_idx]:
        cols = st.columns(2)

        for col_idx, diagram_id in enumerate(diagram_ids):
            with cols[col_idx]:
                svg_file = Path(f"diagrams/{diagram_id}.svg")

                if svg_file.exists():
                    svg_content = load_svg_file(svg_file)

                    st.markdown(f"**{DIAGRAMS[diagram_id]}**")
                    st.markdown(f"""
                    <iframe
                        srcDoc="{svg_content.replace('"', '&quot;')}"
                        style="width:100%; height:350px; border: 1px solid #2c2420;"
                        frameborder="0"
                    ></iframe>
                    """, unsafe_allow_html=True)
                else:
                    st.warning(f"Diagram not found: {diagram_id}.svg")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9a9088; font-size: 0.85rem;">
Cast Iron Charlie • CIC Deep Research Toolkit • Master Sheet v1.0
</div>
""", unsafe_allow_html=True)
