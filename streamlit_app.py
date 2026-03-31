import streamlit as st
import pandas as pd
import requests
import re
import os
from datetime import datetime

# --- Cast Iron Charlie Branding ---
st.set_page_config(page_title="Deep Research Lab", page_icon="⚒️", layout="wide")

# --- Persistence Layer ---
DB_FILE = "research_inventory.csv"

if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

if os.path.exists(DB_FILE):
    try:
        st.session_state['master_db'] = pd.read_csv(DB_FILE).to_dict('records')
    except:
        st.session_state['master_db'] = []
else:
    st.session_state['master_db'] = []

def save_and_log(query, results, persona):
    """Saves to the permanent CSV AND the live sidebar log."""
    for res in results:
        entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Persona": persona,
            "Query": query,
            "Source": res.get('title'),
            "URL": res.get('link'),
            "Snippet": res.get('snippet', '')
        }
        # Permanent Archive
        st.session_state['master_db'].append(entry)
        # Live Sidebar Log
        st.session_state['daily_log'].append({"Title": res.get('title'), "Content": res.get('snippet', '')})
    
    pd.DataFrame(st.session_state['master_db']).to_csv(DB_FILE, index=False)

# --- UI Layout ---
st.title("⚒️ Cast Iron Deep Research Labs")
st.caption("Permanent Intelligence for the Sorensen 'Straight Line' Project")

with st.sidebar:
    st.header("Forge Settings")
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    persona = st.selectbox("Active Persona", ["The Industrial Architect", "The Metallurgist", "The Genealogist"])
    
    st.divider()
    st.subheader("📋 Live Session Log")
    # This now correctly shows the sources found in the current session
    for item in st.session_state['daily_log']:
        st.write(f"✅ {item['Title']}")
    
    st.divider()
    st.metric("Total Permanent Records", len(st.session_state['master_db']))
    
    if st.button("🗑️ Clear Local Session"):
        st.session_state['daily_log'] = []
        st.rerun()

# --- Search Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Sorensen conveyor belt patents 1913")

if st.button("Engage Engines"):
    if not api_key:
        st.error("Please add your SerpApi Key.")
    else:
        with st.spinner("📥 Archiving sources..."):
            clean_query = f"{query} -PDF -math -midpoint -question"
            params = {"q": clean_query, "api_key": api_key}
            
            try:
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                # Use the new combined function to update both lists
                save_and_log(clean_query, results[:5], persona)
                
                st.success(f"Archived {len(results[:5])} new sources.")
                st.rerun()
            except Exception as e:
                st.error(f"Forge Error: {e}")

# --- Display Master Inventory ---
if st.session_state['master_db']:
    st.subheader("🗃️ Master Research Inventory")
    df = pd.DataFrame(st.session_state['master_db'])
    st.data_editor(
        df.sort_values(by="Timestamp", ascending=False),
        column_config={"URL": st.column_config.LinkColumn("Source Link", display_text="Open Record")},
        hide_index=True, use_container_width=True
    )
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Full Database for Claude", data=csv, file_name="sorensen_master_intel.csv")
