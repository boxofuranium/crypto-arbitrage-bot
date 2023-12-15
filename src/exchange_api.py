import requests
import json  # Add this line to import the json module

class ExchangeAPI:
    def __init__(self, api_key, api_secret, api_passphrase, exchange_name):
        self.api_key = '290ab78059844ff0a44ab1bd0a990d73'
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.exchange_name = exchange_name
        self.base_url = "http://api.coinlayer.com/live"

        # Initialize API client
        self.client = self._init_client()

    def _init_client(self):
        client = requests.Session()
        client.headers.update({'Content-Type': 'application/json'})
        return client

    def get_ticker_data(self, callback=None):
        url = f"{self.base_url}?access_key={self.api_key}"
        if callback:
            url += f"&callback={callback}"

        response = self.client.get(url)

        # Handle JSONP callback
        if callback:
            json_start = response.text.find('(') + 1
            json_end = response.text.rfind(')')
            json_content = response.text[json_start:json_end]

            try:
                # Parse the extracted JSON content
                return json.loads(json_content)
            except json.JSONDecodeError as json_err:
                print(f"Error decoding JSON content: {json_err}")
                return None  # Return None or handle the error as needed

        response.raise_for_status()
        return response.json()

# Example usage with JSONP callback
# exchange_client = ExchangeAPI(api_key='your_api_key', api_secret='your_api_secret', api_passphrase='your_passphrase', exchange_name='your_exchange')
# ticker_data = exchange_client.get_ticker_data(callback='your_callback_function')
