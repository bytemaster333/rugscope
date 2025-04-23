import streamlit as st
from utils.telegram_bot import send_telegram_message
import json
import os

WATCHLIST_FILE = "data/watchlist.json"

def render():
    st.header("🚨 Alert System")
    st.markdown("Set up Telegram alerts for wallets or tokens you want to monitor.")

    # Telegram config
    telegram_token = st.text_input("Enter your Telegram Bot Token", type="password")
    chat_id = st.text_input("Enter your Telegram Chat ID")

    st.divider()

    # Watchlist management
    st.markdown("### 📋 Your Watchlist")
    if os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE, "r") as file:
            watchlist = json.load(file)
    else:
        watchlist = {"wallets": [], "tokens": []}

    wallet_input = st.text_input("Add Wallet to Watchlist", key="alerts_wallet_input")
    token_input = st.text_input("Add Token to Watchlist", key="alerts_token_input")

    if st.button("➕ Add to Watchlist"):
        if wallet_input:
            watchlist["wallets"].append(wallet_input)
        if token_input:
            watchlist["tokens"].append(token_input)
        with open(WATCHLIST_FILE, "w") as file:
            json.dump(watchlist, file, indent=2)
        st.success("Watchlist updated!")

    st.write("**Wallets being watched:**", watchlist["wallets"])
    st.write("**Tokens being watched:**", watchlist["tokens"])

    st.divider()
    st.markdown("### 🔔 Test Alert")
    if st.button("Send Test Alert"):
        if telegram_token and chat_id:
            message = "🔔 *RugScope Alert:* This is a test message!"
            sent = send_telegram_message(token=telegram_token, chat_id=chat_id, message=message)
            if sent:
                st.success("✅ Test alert sent!")
            else:
                st.error("Failed to send alert. Check your token and chat ID.")
        else:
            st.warning("Please enter both your Telegram Bot Token and Chat ID.")