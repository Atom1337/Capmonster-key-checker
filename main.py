import requests

def kalamkaar(api_key):
    url = "https://api.capmonster.cloud/getBalance"
    payload = {
        "clientKey": api_key
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        balance = response.json().get("balance", 0)
        print("CapMonster balance:", balance)
    else:
        print("Failed to retrieve balance. Status code:", response.status_code)


# Replace 'YOUR_CAPMONSTER_API_KEY' with your actual CapMonster API key
api_key = 'YOUR_CAPMONSTER_API_KEY'

kalamkaar(api_key)
