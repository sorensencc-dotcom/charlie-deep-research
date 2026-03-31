import streamlit as st
import pandas as pd
import requests
import re
import os
from datetime import datetime

# --- Cast Iron Charlie Branding ---
st.set_page_config(page_title="Deep Research Lab", page_icon="⚒️", layout="wide")

# --- Persistence Layer ---
# This checks if a master database already exists on your GitHub/Streamlit drive
DB_FILE = "research_inventory.csv"

if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

# Load existing database if it exists
if os.path.exists(DB_FILE):
    st.session_state['master_db'] = pd.read_csv(DB_FILE).to_dict('records')
else:
    st.session_state['master_db'] = []

def save_to_permanent_db(query, results, persona):
    for res in results:
        entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Persona": persona,
            "Query": query,
            "Source": res.get('title'),
            "URL": res.get('link')
        }
        st.session_state['master_db'].append(entry)
    
    # Write to physical storage
    pd.DataFrame(st.session_state['master_db']).to_csv(DB_FILE, index=False)

# --- Logic & UI ---
st.title("⚒️ Cast Iron Deep Research Labs")
st.caption("Permanent Intelligence for the Sorensen 'Straight Line' Project")

with st.sidebar:
    st.header("Forge Settings")
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    persona = st.selectbox("Active Persona", ["The Industrial Architect", "The Metallurgist", "The Genealogist"])
    
    st.divider()
    st.subheader("📦 Inventory Status")
    st.metric("Total Records Saved", len(st.session_state['master_db']))
    
    if st.button("🗑️ Clear Local Session"):
        st.session_state['daily_log'] = []
        st.rerun()

# --- Main Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Sorensen conveyor belt patents 1913")

if st.button("Engage Engines"):
    if not api_key:
        st.error("Please add your SerpApi Key.")
    else:
        with st.spinner("📥 Forging permanent records..."):
            # Refine query with exclusions to avoid math/PDF noise
            clean_query = f"{query} -PDF -math -midpoint -question"
            params = {"q": clean_query, "api_key": api_key}
            
            try:
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                # Save to the Permanent Database immediately
                save_to_permanent_db(clean_query, results[:5], persona)
                
                st.success(f"Added {len(results[:5])} items to the permanent inventory.")
                st.rerun()
            except Exception as e:
                st.error(f"Forge Error: {e}")

# --- Display Master Inventory ---
if st.session_state['master_db']:
    st.subheader("🗃️ Master Research Inventory (Persistent)")
    df = pd.DataFrame(st.session_state['master_db'])
    
    st.data_editor(
        df.sort_values(by="Timestamp", ascending=False),
        column_config={
            "URL": st.column_config.LinkColumn("Source Link", display_text="Open Record")
        },
        hide_index=True,
        use_container_width=True
    )
    
    # Provide a single download for the entire historical database
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Master Database for Claude", data=csv, file_name="sorensen_master_intel.csv")
