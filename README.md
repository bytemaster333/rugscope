# 🛡️ RugScope – Token Risk Intelligence Dashboard

**RugScope** is a lightweight, real-time dashboard that helps users identify risky tokens, insider wallets, and suspicious fund flows on the Solana blockchain.  
Built with Streamlit and powered by [RugCheck API](https://rugcheck.xyz).

> **Mission:** Make DeFi safer through transparency, accessibility, and actionable insights.

---

## 🚀 Features (MVP)

- 📊 **Token Overview:** Check LP lock status, mint authority, metadata mutability, risk score
- 🌐 **Token Flow Tracker:** Visualize token movement using Sankey diagrams
- 🕵️ **Insider Watch:** Detect wallets acting before key events
- 🔍 **Wallet Profiler:** (Currently mock data) Risk score simulator for wallet behaviors

---

## ⚙️ Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/<yourusername>/rugscope.git
cd rugscope

2. Setup Virtual Environment

python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

3. Install Required Packages

pip install -r requirements.txt

4. Setup Environment Variables

Copy the example file and insert your RugCheck JWT token:
cp .env.example .env
Inside .env:
RUGCHECK_TOKEN=your_jwt_token_here

🔒 Note: Keep your JWT token private. Never share your .env file publicly.

🔐 How to Get Your RugCheck JWT Token
Go to RugCheck API Swagger UI

Click on Authorize (top-right corner)

Connect your Solana wallet (e.g., Phantom)

Obtain the JWT Token issued after signature

Place it into your .env file under RUGCHECK_TOKEN

## 🙌 Contributing
We welcome community feedback, ideas, and code contributions!
If you have a suggestion or want to collaborate, feel free to open an issue or pull request.

## 📬 Contact
Developed by Salih Toruner
Contact via GitHub Issues or direct messages.




