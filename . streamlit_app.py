import streamlit as st
import pandas as pd
import requests
import io
import re
import zipfile
import plotly.express as px
from datetime import datetime

# --- Cast Iron Charlie Branding ---
st.set_page_config(page_title="Deep Research Lab", page_icon="⚒️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #f4f4f4; }
    .stButton>button { background-color: #e67e22; color: white; border-radius: 4px; font-weight: bold; border: none; width: 100%; }
    .stButton>button:hover { background-color: #d35400; }
    h1 { color: #e67e22; text-transform: uppercase; letter-spacing: 2px; }
    div[data-testid="stExpander"] { background: #2d2d2d; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

# --- App Header ---
st.title("⚒️ Deep Research Lab")
st.caption("Strategic Intelligence Engine for Cast Iron Charlie")

# --- Sidebar & Credit Tracker ---
with st.sidebar:
    st.header("Forge Settings")
    # API Key Handling (Checks Secrets first, then User Input)
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    
    intensity = st.radio(
        "Search Intensity",
        ["Surface Scan", "Deep Dive"],
        help="Surface: Snippets only. Deep Dive: Full page analysis (Token heavy)."
    )
    
    st.divider()

    # --- Credit Tracker ---
    if api_key:
        try:
            account_resp = requests.get(f"https://serpapi.com/account?api_key={api_key}").json()
            total_limit = account_resp.get("searches_per_month", 250)
            searches_left = account_resp.get("plan_searches_left", 0)
            st.subheader("⚒️ Forge Capacity")
            st.metric("Searches Left", f"{searches_left} / {total_limit}")
            st.progress((total_limit - searches_left) / total_limit)
        except:
            st.caption("Unable to fetch credit balance.")
    
    st.divider()
    st.info("💡 2026 Quota Protection: Deep scans are automatically trimmed to ~500 tokens.")

# --- Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Antique foundry patterns 1850-1920")

if st.button("Engage Engines"):
    if not api_key:
        st.error("Please add your SerpApi Key to continue.")
    else:
        with st.spinner("⚒️ Forging results..."):
            try:
                # 1. Search Results
                params = {"q": query, "api_key": api_key}
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                final_results = []
                timeline_data = []

                for res in results[:5]:
                    item = {"Title": res['title'], "Link": res['link'], "
