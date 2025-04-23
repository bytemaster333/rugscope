import streamlit as st
import pandas as pd
from core.rugcheck_api import get_token_flow_data
from utils.helpers import display_sankey_diagram

def render():
    st.header("🌐 Token Flow Tracker")
    st.markdown("Visualize how funds flow between wallets for a specific token.")

    token = st.text_input("Enter Token Address", key="token_flow_input")

    if token:
        with st.spinner("Fetching token flow data..."):
            flow_data = get_token_flow_data(token)

        if flow_data and "edges" in flow_data:
            st.success("✅ Token flow data loaded.")
            display_sankey_diagram(flow_data["edges"])
        else:
            st.error("❌ Failed to fetch flow data. Try another token.")
