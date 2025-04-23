import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.rugcheck.xyz/v1"
RUGCHECK_TOKEN = os.getenv("RUGCHECK_TOKEN")  # JWT token

HEADERS = {
    "Authorization": f"Bearer {RUGCHECK_TOKEN}",
    "Accept": "application/json"
}

# ─────────────────────────────────────
# ✅ Gerçek API'den gelen veriler
# ─────────────────────────────────────

def get_token_report(mint_address):
    """Gerçek RugCheck token raporu verisini alır."""
    try:
        response = requests.get(f"{BASE_URL}/tokens/{mint_address}/report/summary", headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            print("API Error (token_report):", response.status_code, response.text)
            return None
    except Exception as e:
        print("Exception in get_token_report:", e)
        return None

def get_insider_candidates(mint_address):
    """Token için insider cüzdan grafiğini alır (varsa)."""
    try:
        response = requests.get(f"{BASE_URL}/tokens/{mint_address}/insiders/graph", headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            print("API Error (insiders):", response.status_code, response.text)
            return None
    except Exception as e:
        print("Exception in get_insider_candidates:", e)
        return None

# ─────────────────────────────────────
# 🚧 Gerçek API mevcut değil – Mock veri
# ─────────────────────────────────────

def get_wallet_risk(address):
    """Mock wallet risk verisi (API'de mevcut değil)."""
    print("⚠️ Using mock data for wallet risk")
    return {
        "score": 68,
        "category": "Moderate Risk",
        "flags": {
            "many_tokens": True,
            "interacts_with_unverified": False
        }
    }

def get_wallet_summary(address):
    """Mock wallet summary verisi (API'de mevcut değil)."""
    print("⚠️ Using mock data for wallet summary")
    return {
        "total_tx": 123,
        "first_tx_date": "2023-08-01",
        "last_tx_date": "2024-04-22",
        "active_tokens": ["USDC", "JUP", "BONK"]
    }

def get_token_flow_data(token_address):
    print("⚠️ Using mock data for token flow")
    return {
        "nodes": ["wallet1", "wallet2", "wallet3"],
        "edges": [
            {"from": "wallet1", "to": "wallet2", "value": 1200},
            {"from": "wallet2", "to": "wallet3", "value": 800},
            {"from": "wallet3", "to": "wallet1", "value": 500}
        ]
    }
