import streamlit as st
import pandas as pd
import requests
import re
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
    div[data-testid="stExpander"] { background: #2d2d2d; border: 1px solid #444; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- Logic Engines ---
if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

def refine_query_with_memory(user_query, persona, logs):
    # Industrial Exclusions to block math/vocab noise
    exclusions = "-PDF -math -midpoint -question -vocab -dictionary"
    
    modifiers = {
        "The Genealogist": f"genealogy census 'city directory' owner biography {exclusions}",
        "The Metallurgist": f"patent metallurgy 'iron composition' ghost mark technical alloy {exclusions}",
        "The Industrial Architect": f"assembly line 'moving chassis' 'Highland Park' 'Willow Run' foundry workflow {exclusions}"
    }
    
    base = f"{user_query} {modifiers.get(persona, '')}"
    if not logs:
        return base
    
    # Context-aware filtering of recent results
    context = [item['Title'][:25] for item in logs[-3:]]
    return f"{base} -intitle:\"{'\" -intitle:\"'.join(context)}\""

def extract_intel(text):
    # Enhanced entity extraction with noise filtering
    noise_words = ["Midpoint", "Equation", "Dictionary", "Midpoint", "Question"]
    
    names = re.findall(r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b', text)
    locs = re.findall(r'\b([A-Z][a-z]+, [A-Z]{2})\b', text)
    
    filtered_names = [n for n in names if not any(w in n for w in noise_words)]
    filtered_locs = [l for l in locs if not any(w in l for w in noise_words)]
    
    return list(set(filtered_names))[:5], list(set(filtered_locs))[:5]

st.title("⚒️ Cast Iron Deep Research Labs")
st.caption("Strategic Intelligence for the Sorensen 'Straight Line' Project")

# --- Sidebar ---
with st.sidebar:
    st.header("Forge Settings")
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    
    st.divider()
    persona = st.selectbox("Active Persona", ["The Industrial Architect", "The Metallurgist", "The Genealogist"])
    intensity = st.radio("Search Intensity", ["Surface Scan", "Deep Dive"])
    
    if persona == "The Industrial Architect":
        st.info("Industrial Guardrails: Active (-PDF, -math filters applied)")

    st.divider()
    st.subheader("📋 Forge Log")
    log_count = len(st.session_state['daily_log'])
    st.metric("Items Collected", log_count)
    
    if log_count > 0:
        log_text = f"DAILY RESEARCH LOG: {datetime.now().strftime('%Y-%m-%d')}\n" + "="*30 + "\n\n"
        for entry in st.session_state['daily_log']:
            log_text += f"SOURCE: {entry['Title']}\nDATA: {entry['Content']}\n" + "-"*20 + "\n"
        st.download_button("📥 Export Log for Claude", data=log_text, file_name=f"charlie_log_{datetime.now().strftime('%Y%m%d')}.txt")

# --- Main Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Ford foundry floor plan 1914")

if st.button("Engage Engines (Agentic Mode)"):
    if not api_key:
        st.error("Please add your SerpApi Key.")
    else:
        with st.spinner(f"🧠 {persona} is filtering for gold..."):
            smart_query = refine_query_with_memory(query, persona, st.session_state['daily_log'])
            params = {"q": smart_query, "api_key": api_key}
            try:
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                final_results = []
                timeline_data = []
                all_people, all_places = [], []

                for res in results
