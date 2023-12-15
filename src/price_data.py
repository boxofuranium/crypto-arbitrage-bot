import requests

class PriceData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.coinlayer.com/live"

    def get_live_ticker(self, symbols, target_currency='USD'):
        params = {
            'access_key': self.api_key,
            'symbols': ','.join(symbols),
            'target': target_currency
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()
