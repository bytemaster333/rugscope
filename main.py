import streamlit as st
from app import overview, wallet_profiler, token_flow, insider_watch, alert_system

st.set_page_config(
    page_title="RugScope – Token Risk Intelligence",
    layout="wide"
)

# Ana başlık
st.markdown("<h1 style='text-align: center;'>🛡️ RugScope</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Detect rug risks, monitor wallet behaviors and stay ahead of scams.</p>",
            unsafe_allow_html=True)

# Sekmeli görünüm
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "🔍 Wallet Profiler",
    "🌐 Token Flow",
    "🕵️ Insider Watch",
    "🚨 Alerts"
])

with tab1:
    overview.render()

with tab2:
    wallet_profiler.render()

with tab3:
    token_flow.render()

with tab4:
    insider_watch.render()

with tab5:
    alert_system.render()