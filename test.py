import requests

# RugCheck'ten aldığın JWT token
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDU1NzQwMTgsImlkIjoiOFRUc3kyV2hHbkRxRlpxTFFWZ2J2cU12TVV6UEZubkZrRFUzSnZwYkE2U0cifQ.n42FvZf7_1evFBskH8xx0gnRxyfaObZbvM5MHyLlUs8"

# Örnek geçerli bir mint address — test için bu örneği kullanabilirsin
mint_address = "6vtV6KNYZxNj2Qoo9cdvhyQ8YNFVf695A7mCBQeb4AHK"  # USDC değilse dummy bir token olabilir

url = f"https://api.rugcheck.xyz/v1/tokens/{mint_address}/report"
headers = {
    "Authorization": f"Bearer {JWT_TOKEN}",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Non-JSON response:", response.text)
