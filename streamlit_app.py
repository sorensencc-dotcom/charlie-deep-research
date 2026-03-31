import streamlit as st
import pandas as pd
import requests
import re
import os
from datetime import datetime

# --- Cast Iron Charlie Branding ---
st.set_page_config(page_title="Deep Research Lab", page_icon="⚒️", layout="wide")

# --- Persistence Layer (The "Black Box") ---
DB_FILE = "research_inventory.csv"

# Initialize local session log
if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

# Load existing master database from the physical file if it exists
if os.path.exists(DB_FILE):
    try:
        st.session_state['master_db'] = pd.read_csv(DB_FILE).to_dict('records')
    except:
        st.session_state['master_db'] = []
else:
    st.session_state['master_db'] = []

def save_to_permanent_db(query, results, persona):
    """Automatically writes every finding to a persistent CSV file."""
    for res in results:
        entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Persona": persona,
            "Query": query,
            "Source": res.get('title'),
            "URL": res.get('link'),
            "Snippet": res.get('snippet', '')
        }
        st.session_state['master_db'].append(entry)
    
    # Physically write to the drive
    pd.DataFrame(st.session_state['master_db']).to_csv(DB_FILE, index=False)

# --- Logic & UI ---
st.title("⚒️ Cast Iron Deep Research Labs")
st.caption("Persistent Intelligence Engine for the Sorensen 'Straight Line' Project")

with st.sidebar:
    st.header("Forge Settings")
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    persona = st.selectbox("Active Persona", ["The Industrial Architect", "The Metallurgist", "The Genealogist"])
    
    st.divider()
    st.subheader("📦 Inventory Status")
    # Shows how many items are safely written to the "Hard Drive"
    st.metric("Permanent Records", len(st.session_state['master_db']))
    
    if st.button("🗑️ Reset Local Session"):
        st.session_state['daily_log'] = []
        st.rerun()

# --- Main Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Sorensen 1913 conveyor belt experiments")

if st.button("Engage Engines"):
    if not api_key:
        st.error("Please add your SerpApi Key.")
    else:
        with st.spinner("📥 Writing to permanent archive..."):
            # Clean filters to keep out math/PDF noise
            clean_query = f"{query} -PDF -math -midpoint -question"
            params = {"q": clean_query, "api_key": api_key}
            
            try:
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                # IMMEDIATE PERSISTENCE: Save before displaying
                save_to_permanent_db(clean_query, results[:5], persona)
                
                st.success(f"Successfully archived {len(results[:5])} new records.")
                st.rerun() # Refresh to show new data in the table
            except Exception as e:
                st.error(f"Forge Error: {e}")

# --- Display Master Inventory ---
if st.session_state['master_db']:
    st.subheader("🗃️ Master Research Inventory (Persistent Archive)")
    df = pd.DataFrame(st.session_state['master_db'])
    
    # Sort by newest first
    display_df = df.sort_values(by="Timestamp", ascending=False)
    
    st.data_editor(
        display_df,
        column_config={
            "URL": st.column_config.LinkColumn("Source Link", display_text="Open Record")
        },
        hide_index=True,
        use_container_width=True
    )
    
    # One-click export for Claude
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Dataset for Claude",
        data=csv,
        file_name=f"sorensen_master_intel_{datetime.now().strftime('%Y%m%d')}.csv",
        mime='text/csv'
    )
