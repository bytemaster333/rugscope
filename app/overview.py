import streamlit as st
from core.rugcheck_api import get_token_report

def display_token_summary(report: dict):
    with st.expander("📊 Token Report (Readable Format)"):
        for key, value in report.items():
            label = key.replace("_", " ").title()
            if isinstance(value, bool):
                icon = "✅ Yes" if value else "❌ No"
                st.markdown(f"**{label}:** {icon}")
            elif isinstance(value, list):
                continue 
            elif value is None or value == "":
                st.markdown(f"**{label}:** `N/A`")
            else:
                st.markdown(f"**{label}:** `{value}`")

def display_risks(report: dict):
    risks = report.get("risks", [])
    if risks:
        st.markdown("### ⚠️ Risk Factors Detected")
        for risk in risks:
            name = risk.get("name", "Unnamed Risk")
            description = risk.get("description", "")
            score = risk.get("score", "N/A")
            level = risk.get("level", "N/A")

            st.markdown(f"""
**🟠 {name}**
- 📌 **Level:** `{level}`
- 🧾 **Description:** {description}
- 🔢 **Score:** `{score}`
""")
    else:
        st.info("✅ No specific risk factors found.")

def render():
    st.subheader("📊 Overview")
    st.markdown("""
Welcome to **RugScope** – your all-in-one dashboard for on-chain token security.

With RugScope, you can:
- 🧠 **Check token safety** with real-time risk analysis powered by **RugCheck API**
- 🕵️‍♂️ **Identify potential insider wallets** before they act
- 🌐 **Visualize token movement** between wallets to detect manipulation
- 🚨 **Get alerted** about suspicious activity (in future versions)

---
""")

    mint = st.text_input("🔍 Enter Token Mint Address", key="overview_token_input",
                         help="Paste a Solana token mint address from explorers like Solscan.")
    st.caption("Example: `DezXyE4QxFh94X8LzAzc1AFgyxSpdGTbA1YAnGWA1uQF`")

    if mint:
        with st.spinner("Fetching token report..."):
            report = get_token_report(mint)

        if report:
            st.success("✅ Token report loaded.")
            
            display_token_summary(report)
            
            display_risks(report)

            with st.expander("📦 Raw Token Report JSON"):
                st.json(report)

        else:
            st.error("❌ Failed to fetch token report. Check mint address.")
