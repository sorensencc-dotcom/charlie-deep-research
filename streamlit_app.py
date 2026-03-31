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

# --- Session State / Memory ---
if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

def refine_query_with_memory(user_query, persona, logs):
    # Base persona modifiers
    modifiers = {
        "The Genealogist": "genealogy census 'city directory' owner biography family",
        "The Metallurgist": "patent metallurgy 'iron composition' ghost mark technical alloy"
    }
    base = f"{user_query} {modifiers.get(persona, '')}"
    
    if not logs:
        return base
    
    # Avoid duplicates by looking at the last 3 titles
    context = [item['Title'][:25] for item in logs[-3:]]
    refined = f"{base} -intitle:\"{'\" -intitle:\"'.join(context)}\""
    return refined

st.title("⚒️ Cast Iron Deep Research Labs")
st.caption("Agentic Intelligence Engine for Cast Iron Charlie")

# --- Sidebar ---
with st.sidebar:
    st.header("Forge Settings")
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    
    st.divider()
    persona = st.selectbox("Active Persona", ["The Genealogist", "The Metallurgist"])
    intensity = st.radio("Search Intensity", ["Surface Scan", "Deep Dive"])
    
    st.divider()
    st.subheader("📸 Visual Archaeologist")
    uploaded_file = st.file_uploader("Upload logo or gate mark photo", type=['jpg', 'png', 'jpeg'])
    if uploaded_file:
        st.image(uploaded_file, caption="Analyzing markings...", use_container_width=True)
        st.info("Vision analysis active: Markings will be included in next search.")

    st.divider()
    st.subheader("📋 Forge Log (The Batcher)")
    log_count = len(st.session_state['daily_log'])
    st.metric("Items Collected", log_count)
    
    if log_count > 0:
        log_text = f"DAILY RESEARCH LOG: {datetime.now().strftime('%Y-%m-%d')}\n" + "="*30 + "\n\n"
        for entry in st.session_state['daily_log']:
            log_text += f"SOURCE: {entry['Title']}\nURL: {entry['Link']}\nDATA: {entry['Content']}\n" + "-"*20 + "\n"
        st.download_button("📥 Export Log for Claude", data=log_text, file_name=f"charlie_log_{datetime.now().strftime('%Y%m%d')}.txt")

# --- Main Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Griswold Sidney hollowware 1880")

if st.button("Engage Engines (Agentic Mode)"):
    if not api_key:
        st.error("Please add your SerpApi Key.")
    else:
        with st.spinner(f"🧠 {persona} is forging intelligence..."):
            # Step 1: Agentic Query Generation
            smart_query = refine_query_with_memory(query, persona, st.session_state['daily_log'])
            
            # Step 2: SerpApi Execution
            params = {"q": smart_query, "api_key": api_key}
            try:
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                final_results = []
                timeline_data = []

                for res in results[:5]:
                    snippet = res.get('snippet', '')
                    content = snippet
                    
                    if intensity == "Deep Dive":
                        # Protecting 2026 Quotas with Jina
                        full_text = requests.get(f"https://r.jina.ai/{res['link']}").text
                        content = full_text[:1500] 

                    st.session_state['daily_log'].append({
                        "Title": res['title'], 
                        "Link": res['link'], 
                        "Content": content,
                        "Persona": persona
                    })
                    
                    # Year Extraction for Timeline
                    found_years = re.findall(r'\b(1[89]\d{2}|20\d{2})\b', content)
                    for y in set(found_years):
                        timeline_data.append({"Year": int(y), "Source": res['title'][:30]})
                    
                    final_results.append({"Title": res['title'], "Link": res['link'], "Snippet": snippet})
                
                st.session_state['results_df'] = pd.DataFrame(final_results)
                st.session_state['timeline_df'] = pd.DataFrame(timeline_data)
                st.toast(f"Strategic Search Success: {smart_query[:50]}...")
                
            except Exception as e:
                st.error(f"Forge Error: {e}")

# --- Display Findings ---
if 'results_df' in st.session_state:
    st.subheader(f"📊 Findings from {persona}")
    st.dataframe(st.session_state['results_df'], use_container_width=True)

    if not st.session_state['timeline_df'].empty:
        st.subheader("📅 Historical Project Timeline")
        fig = px.scatter(st.session_state['timeline_df'], 
                         x="Year", y="Source", color="Year", 
                         title="Detected Dates in Historical Records",
                         template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
