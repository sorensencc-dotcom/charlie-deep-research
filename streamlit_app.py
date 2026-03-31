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
    modifiers = {
        "The Genealogist": "genealogy census 'city directory' owner biography family",
        "The Metallurgist": "patent metallurgy 'iron composition' ghost mark technical alloy",
        "The Industrial Architect": "assembly line 'moving chassis' 'Highland Park' 'Willow Run' foundry workflow mass production"
    }
    base = f"{user_query} {modifiers.get(persona, '')}"
    if not logs:
        return base
    context = [item['Title'][:25] for item in logs[-3:]]
    return f"{base} -intitle:\"{'\" -intitle:\"'.join(context)}\""

def extract_intel(text):
    names = re.findall(r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b', text)
    locs = re.findall(r'\b([A-Z][a-z]+, [A-Z]{2})\b', text)
    return list(set(names))[:5], list(set(locs))[:5]

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
        st.info("Focus: Sorensen’s assembly line techniques, factory flow, and mass production logistics.")

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
query = st.text_input("Research Topic", placeholder="e.g., Ford Piquette Avenue assembly line experiments 1910")

if st.button("Engage Engines (Agentic Mode)"):
    if not api_key:
        st.error("Please add your SerpApi Key.")
    else:
        with st.spinner(f"🧠 {persona} is reconstructing the line..."):
            smart_query = refine_query_with_memory(query, persona, st.session_state['daily_log'])
            params = {"q": smart_query, "api_key": api_key}
            try:
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                final_results = []
                timeline_data = []
                all_people, all_places = [], []

                for res in results[:5]:
                    content = res.get('snippet', '')
                    if intensity == "Deep Dive":
                        content = requests.get(f"https://r.jina.ai/{res['link']}").text[:1500] 

                    ppl, plc = extract_intel(content)
                    all_people.extend(ppl); all_places.extend(plc)
                    
                    st.session_state['daily_log'].append({"Title": res['title'], "Content": content})
                    
                    years = re.findall(r'\b(1[89]\d{2}|20\d{2})\b', content)
                    for y in set(years):
                        timeline_data.append({"Year": int(y), "Source": res['title'][:30]})
                    
                    final_results.append({"Source Title": res['title'], "Link": res['link']})
                
                st.session_state['results_df'] = pd.DataFrame(final_results)
                st.session_state['timeline_df'] = pd.DataFrame(timeline_data)
                st.session_state['intel'] = {"People": list(set(all_people)), "Places": list(set(all_places))}
                st.toast("Strategic Search Success!")
            except Exception as e:
                st.error(f"Forge Error: {e}")

# --- Display Findings ---
if 'results_df' in st.session_state:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"📊 Findings: {persona}")
        st.data_editor(
            st.session_state['results_df'],
            column_config={
                "Link": st.column_config.LinkColumn("Source Link", display_text="Open Record")
            },
            hide_index=True, use_container_width=True
        )
        
        if not st.session_state['timeline_df'].empty:
            st.subheader("📅 Industrial Evolution Timeline")
            fig = px.scatter(st.session_state['timeline_df'], x="Year", y="Source", color="Year", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        st.subheader("🕵️ Strategic Intel")
        if 'intel' in st.session_state:
            with st.expander("Key Figures (People)", expanded=True):
                for p in st.session_state['intel']['People']: st.write(f"👤 {p}")
            with st.expander("Strategic Hubs (Places)", expanded=True):
                for l in st.session_state['intel']['Places']: st.write(f"📍 {l}")
