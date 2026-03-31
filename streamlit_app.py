import streamlit as st
import pandas as pd
import requests
import io
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
    div[data-testid="stExpander"] { background: #2d2d2d; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

st.title("⚒️ Deep Research Lab")
st.caption("Strategic Intelligence Engine for Cast Iron Charlie")

# --- Sidebar ---
with st.sidebar:
    st.header("Forge Settings")
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    intensity = st.radio("Search Intensity", ["Surface Scan", "Deep Dive"])
    
    st.divider()
    st.subheader("📋 Today's Forge Log")
    log_count = len(st.session_state['daily_log'])
    st.write(f"Items collected: **{log_count}**")
    
    if log_count > 0:
        log_text = f"DAILY RESEARCH LOG: {datetime.now().strftime('%Y-%m-%d')}\n"
        log_text += "INSTRUCTIONS: Analyze these cast iron sources for patterns.\n" + "="*30 + "\n\n"
        for entry in st.session_state['daily_log']:
            log_text += f"SOURCE: {entry['Title']}\nURL: {entry['Link']}\nDATA: {entry['Content']}\n" + "-"*20 + "\n"
        
        st.download_button("📥 Export Log for Claude", data=log_text, file_name=f"charlie_log_{datetime.now().strftime('%Y%m%d')}.txt")
        if st.button("Clear Log"):
            st.session_state['daily_log'] = []
            st.rerun()

    if api_key:
        try:
            account_resp = requests.get(f"https://serpapi.com/account?api_key={api_key}").json()
            st.metric("Searches Left", f"{account_resp.get('plan_searches_left', 0)} / 250")
        except:
            st.caption("Searching enabled.")

# --- Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Griswold vs Wagner metallurgy")

if st.button("Engage Engines"):
    if not api_key:
        st.error("Please add your API Key.")
    else:
        with st.spinner("⚒️ Forging..."):
            try:
                params = {"q": query, "api_key": api_key}
                search_data = requests.get("https://serpapi.com/search.json", params=params).json()
                results = search_data.get("organic_results", [])
                
                final_results = []
                timeline_data = []

                for res in results[:5]:
                    snippet = res.get('snippet', '')
                    content = snippet
                    if intensity == "Deep Dive":
                        full_text = requests.get(f"https://r.jina.ai/{res['link']}").text
                        content = full_text[:1800]

                    st.session_state['daily_log'].append({"Title": res['title'], "Link": res['link'], "Content": content})
                    years = re.findall(r'\b(1[89]\d{2}|20\d{2})\b', content)
                    for year in set(years):
                        timeline_data.append({"Year": int(year), "Source": res['title'][:30]})
                    final_results.append({"Title": res['title'], "Link": res['link'], "Snippet": snippet})
                
                st.session_state['results'] = pd.DataFrame(final_results)
                st.session_state['timeline'] = pd.DataFrame(timeline_data)
            except Exception as e:
                st.error(f"Error: {e}")

# --- Display ---
if 'results' in st.session_state:
    st.subheader("📊 Findings")
    st.dataframe(st.session_state['results'], use_container_width=True)
    if not st.session_state['timeline'].empty:
        st.subheader("📅 Historical Timeline")
        fig = px.scatter(st.session_state['timeline'], x="Year", y="Source", color="Year", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
