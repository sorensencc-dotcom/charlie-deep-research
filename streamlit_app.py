# --- New Learning Logic Function ---
def refine_query_with_memory(user_query, logs):
    if not logs:
        return user_query # Keep it simple if the forge is empty
    
    # Extract existing context (last 5 discoveries)
    context = [f"{item['Title']} ({item.get('Year', 'No Date')})" for item in logs[-5:]]
    
    # This acts as the 'Strategy Planner'
    # It tells the search engine: "I already know X, show me Y"
    refined = f"{user_query} -intitle:\"{'\" -intitle:\"'.join([c[:20] for c in context])}\""
    return refined

# --- Updated Button Logic ---
if st.button("Engage Engines (Agentic Mode)"):
    if not api_key:
        st.error("Please add your API Key.")
    else:
        with st.spinner("🧠 Thinking & Forging..."):
            # STEP 1: LEARN (The app reads its own memory)
            smart_query = refine_query_with_memory(query, st.session_state['daily_log'])
            
            # STEP 2: SEARCH
            params = {"q": smart_query, "api_key": api_key}
            search_data = requests.get("https://serpapi.com/search.json", params=params).json()
            results = search_data.get("organic_results", [])
            
            # (Rest of your processing logic follows here...)
            st.toast(f"Strategic Query Used: {smart_query}")
