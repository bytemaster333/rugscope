import streamlit as st
import pandas as pd
from core.rugcheck_api import get_insider_candidates

def render():
    st.header("🕵️ Insider Movement Detector")
    st.markdown("Detect wallets that might have insider knowledge based on early transaction activity.")

    token_address = st.text_input("Enter Token Mint Address", key="insider_watch_input")

    if token_address:
        with st.spinner("Analyzing early transactions..."):
            insiders = get_insider_candidates(token_address)

        # Swagger'dan gelen veri listede (list[dict])
        if insiders and isinstance(insiders, list) and len(insiders) > 0:
            network = insiders[0]
            nodes = network.get("nodes", [])

            if nodes:
                st.success(f"✅ Found {len(nodes)} potentially suspicious wallets.")
                df = pd.DataFrame(nodes)
                st.dataframe(df)
            else:
                st.warning("⚠️ No insider wallets found.")
        else:
            st.error("❌ Failed to fetch insider data. Check token address.")
