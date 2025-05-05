import streamlit as st
from core.rugcheck_api import get_wallet_summary, get_wallet_risk

def render():
    st.header("🔍 Wallet Risk Profiler")
    st.markdown("Analyze any wallet's risk score, transaction history, and behavioral profile.")

    wallet = st.text_input("Enter Wallet Address", key="wallet_profiler_input")

    if wallet:
        risk_score = get_wallet_risk(wallet)
        summary = get_wallet_summary(wallet)

        # st.subheader("Debug API Response")
        # st.json(risk_score)

        if not risk_score or "score" not in risk_score:
            st.warning("⚠️ This wallet has no available risk score. It may be inactive or not indexed by RugCheck.")
            st.json(risk_score)
            return

        if summary:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("🧠 Risk Score", f"{risk_score.get('score', 'N/A')}/100")
                st.markdown(f"**Category:** {risk_score.get('category', 'Unknown')}")

            with col2:
                st.markdown("**Transaction Overview:**")
                st.write(summary)

            st.success("✅ Wallet analysis completed.")
        else:
            st.error("❌ Failed to fetch summary data. Please check the wallet address or try another.")
