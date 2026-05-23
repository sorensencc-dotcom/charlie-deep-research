import streamlit as st
import pandas as pd
import requests
import re
import os
from datetime import datetime

# --- Cast Iron Charlie Branding ---
st.set_page_config(page_title="Deep Research Lab", page_icon="⚒️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Barlow+Condensed:wght@300;400;600;700;800&display=swap');

    /* Design System Vars */
    :root {
      --black: #0a0806;
      --forge: #1a1410;
      --iron: #2c2420;
      --rust: #8B3A1A;
      --ember: #C4501A;
      --brass: #B8922A;
      --ash: #9a9088;
      --bone: #e8e0d4;
    }

    .main {
        background-color: var(--black);
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: var(--bone) !important;
    }
    
    .stMarkdown, p, span, div {
        font-family: 'Libre Baskerville', serif !important;
    }
    
    .stButton>button {
        font-family: 'Barlow Condensed', sans-serif !important;
        background-color: var(--ember) !important;
        color: var(--black) !important;
        border-radius: 0px !important;
        border: none !important;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        font-weight: 700;
    }
    
    .stButton>button:hover {
        background-color: var(--rust) !important;
    }
    
    .stTextInput>div>div>input {
        background-color: var(--forge) !important;
        color: var(--bone) !important;
        border-radius: 0px !important;
        border: 1px solid var(--iron) !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: var(--forge) !important;
        border-right: 1px solid var(--iron);
    }
    
    [data-testid="stMetricValue"] {
        color: var(--brass) !important;
    }
</style>
""", unsafe_allow_html=True)

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
