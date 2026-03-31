import streamlit as st
import pandas as pd
import requests
import io
import zipfile
from datetime import datetime

# --- Cast Iron Charlie Styling ---
st.set_page_config(page_title="Deep Research Lab", page_icon="⚒️", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #f4f4f4; }
    .stButton>button { background-color: #e67e22; color: white; border-radius: 4px; font-weight: bold; border: none; width: 100%; }
    .stButton>button:hover { background-color: #d35400; }
    h1 { color: #e67e22; text-transform: uppercase; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚒️ Deep Research Lab")
st.caption("Strategic Intelligence Engine for Cast Iron Charlie")

# --- Configuration ---
with st.sidebar:
    st.header("Forge Settings")
    api_key = st.text_input("SerpApi Key", type="password")
    intensity = st.radio("Search Intensity", ["Surface Scan", "Deep Dive"])
    st.divider()

# --- Research Logic ---
query = st.text_input("Research Topic", placeholder="e.g., Antique foundry patterns")

if st.button("Engage Engines"):
    if not api_key:
        st.error("Please enter your SerpApi Key.")
    else:
        with st.spinner("⚒️ Forging results..."):
            params = {"q": query, "api_key": api_key}
            results = requests.get("https://serpapi.com/search.json", params=params).json().get("organic_results", [])
            final_data = []
            for res in results[:5]:
                item = {"Title": res['title'], "Link": res['link'], "Snippet": res.get('snippet', '')}
                if intensity == "Deep Dive":
                    content = requests.get(f"https://r.jina.ai/{res['link']}").text
                    item["Deep Intel"] = content[:1800] + "... [TRIMMED]"
                final_data.append(item)
            df = pd.DataFrame(final_data)
            st.session_state['results'] = df
            st.dataframe(df, use_container_width=True)

# --- CSV Export ---
if 'results' in st.session_state:
    csv = st.session_state['results'].to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV Report", data=csv, file_name="research_report.csv", mime="text/csv")

# --- Project ZIP Generator ---
def create_zip():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("streamlit_app.py", open(__file__).read())
        zf.writestr("requirements.txt", "streamlit\npandas\nrequests")
        zf.writestr("CLAUDE.md", "# CLAUDE.md\n## Project: Charlie Deep Research\n- **Style:** Rugged, Iron/Ember.\n- **Quota:** Max 2000 chars per page.")
    return buf.getvalue()

st.sidebar.download_button("📦 Download Project ZIP", data=create_zip(), file_name="charlie_research_repo.zip")
