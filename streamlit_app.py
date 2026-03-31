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
    </style>
    """, unsafe_allow_html=True)

# --- Memory Logic ---
if 'daily_log' not in st.session_state:
    st.session_state['daily_log'] = []

def refine_query_with_memory(user_query, logs):
    if not logs:
        return user_query
    # Memory: Look at last 3 discoveries to avoid duplicates
    context = [item['Title'][:20] for item in logs[-3:]]
    refined = f"{user_query} -intitle:\"{'\" -intitle:\"'.join(context)}\""
    return refined

st.title("⚒️ Cast Iron Deep Research Labs")
st.caption("Agentic Intelligence Engine for Cast Iron Charlie")

# --- Sidebar ---
with st.sidebar:
    st.header("Forge Settings")
    api_key = st.secrets.get("SERPAPI_KEY") or st.text_input("SerpApi Key", type="password")
    intensity = st.radio("Search Intensity", ["Surface Scan", "Deep Dive"])
    
    st.divider()
    st.subheader("📋 Forge Log (The Batcher)")
    log_count = len(st.session_state['daily_log'])
    st.write(f"Items collected: **{log_count}**")
    
    if log_count > 0:
        log_text = f"DAILY RESEARCH LOG: {datetime.now().strftime('%Y-%m-%d')}\n" + "="*30 + "\n\n"
        for entry in st.session_state['daily_log']:
            log_text += f"SOURCE: {entry['Title']}\nURL: {entry['Link']}\nDATA: {entry['Content']}\n" + "-"*20 + "\n"
        st.download_button("📥 Export Log for Claude", data=log_text, file_name=f"charlie_log_{datetime.now().strftime('%Y%m%d')}.txt")

    if api_key:
        st.success("API Key Active")

# --- Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Griswold metallurgy 1890")

if st.button("Engage Engines (Agentic Mode)"):
    if not api_key:
        st.error("Please add your SerpApi Key.")
    else:
        with st.spinner("🧠 Thinking & Forging..."):
            # Step 1: Use Memory
            smart_query = refine_query_with_memory(query, st.session_state['daily_log'])
            
            # Step 2: Search
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
                        # Protecting 2026 Claude Quotas with Jina Reader
                        full_text = requests.get(f"https://r.jina.ai/{res['link']}").text
                        content = full_text[:1500] 

                    st.session_state['daily_log'].append({"Title": res['title'], "Link": res['link'], "Content": content})
                    
                    # Extract Years for Timeline
                    years = re.findall(r'\b(1[89]\d{2}|20\d{2})\b', content)
                    for year in set(years):
                        timeline_data.append({"Year": int(year), "Source": res['title'][:30]})
                    
                    final_results.append({"Title": res['title'], "Link": res['link'], "Snippet": snippet})
                
                st.session_state['results_df'] = pd.DataFrame(final_results)
                st.session_state['timeline_df'] = pd.DataFrame(timeline_data)
                st.toast(f"Used Memory to Forge: {smart_query}")
            except Exception as e:
                st.error(f"Forge Error: {e}")

# --- Display ---
if 'results_df' in st.session_state:
    st.subheader("📊 Strategic Findings")
    st.dataframe(st.session_state['results_df'], use_container_width=True)

    if not st.session_state['timeline_df'].empty:
        st.subheader("📅 Historical Project Timeline")
        fig = px.scatter(st.session_state['timeline_df'], x="Year", y="Source", color="Year", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
