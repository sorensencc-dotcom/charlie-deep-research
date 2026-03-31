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

# Initialize Session State for Daily Batching
if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

st.title("⚒️ Deep Research Lab")
st.caption("Strategic Intelligence Engine for Cast Iron Charlie")

# --- Sidebar & Credit Tracker ---
with st.sidebar:
    st.header("Forge Settings")
    # Pulls from Streamlit Secrets or manual input
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    intensity = st.radio("Search Intensity", ["Surface Scan", "Deep Dive"])
    
    st.divider()

    # --- Daily Batcher (The Forge Log) ---
    st.subheader("📋 Today's Forge Log")
    log_count = len(st.session_state['daily_log'])
    st.write(f"Items collected: **{log_count}**")
    
    if log_count > 0:
        # Create the text file for Claude
        log_text = f"DAILY RESEARCH LOG: {datetime.now().strftime('%Y-%m-%d')}\n"
        log_text += "INSTRUCTIONS: Analyze the following cast iron research data for patterns.\n"
        log_text += "="*30 + "\n\n"
        for entry in st.session_state['daily_log']:
            log_text += f"SOURCE: {entry['Title']}\nURL: {entry['Link']}\nDATA: {entry['Content']}\n"
            log_text += "-"*20 + "\n"
        
        st.download_button("📥 Export Daily Log for Claude", data=log_text, file_name=f"charlie_log_{datetime.now().strftime('%Y%m%d')}.txt")
        if st.button("Clear Log"):
            st.session_state['daily_log'] = []
            st.rerun()

    st.divider()
    if api_key:
        try:
            # Check SerpApi balance
            account_resp = requests.get(f"https://serpapi.com/account?api_key={api_key}").json()
            searches_left = account_resp.get('plan_searches_left', 0)
            st.metric("Searches Left", f"{searches_left} / 250")
        except:
            st.caption("Unable to fetch credit balance.")

# --- Research Logic ---
query = st.text_input("Research
