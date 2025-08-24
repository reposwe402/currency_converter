import requests
import json

API_URL = "http://data.fixer.io/api/latest?access_key=33ec7c73f8a4eb6b9b5b5f95118b2275"


def fetch_exchange_rates():
    """Fetches the latest exchange rates from the Fixer.io API."""
    response = requests.get(API_URL)
    data = response.text
    data_json = json.loads(data)
    return data_json.get("rates", {})
