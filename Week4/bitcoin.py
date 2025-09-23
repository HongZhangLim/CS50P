import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f82b56cee4526e0f8a4399a2b8a844b7589a15759c0ab69487f830fb4bc83e77")
price = float(response.json()["data"]["priceUsd"])
amount = price * n
print(f"${amount:,.4f}")

