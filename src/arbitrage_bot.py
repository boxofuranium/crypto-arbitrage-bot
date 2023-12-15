import json
import requests
from arbitrage_strategy import ArbitrageAlgorithm
from utils import print_profit_report

# Replace with your actual API key for Coinlayer
coinlayer_api_key = '290ab78059844ff0a44ab1bd0a990d73'

# Specify the base URL for Coinlayer API
coinlayer_base_url = f'http://api.coinlayer.com/live?access_key={coinlayer_api_key}'

# Specify your preferred target currency (optional)
target_currency = 'USD'

# Specify the cryptocurrency symbols you want to include (optional)
symbols = ['BTC', 'ETH', 'LTC']

# Specify other optional parameters, such as expand or callback
params = {
    'target': target_currency,
    'symbols': ','.join(symbols),
    'expand': 1,
    'callback': 'your_callback_function'  # Replace with your desired callback function name
}

# Make a request to get the live ticker data
response = requests.get(coinlayer_base_url, params=params)

try:
    # Extract JSON content from the response (handling JSONP callback)
    json_start = response.text.find('(') + 1
    json_end = response.text.rfind(')')
    json_content = response.text[json_start:json_end]
    
    # Parse the extracted JSON content
    ticker_data = json.loads(json_content)

    # Initialize the arbitrage algorithm
    arbitrage_algorithm = ArbitrageAlgorithm()

    # Identify arbitrage opportunities without considering transaction fees
    arbitrage_opportunity = arbitrage_algorithm.identify_arbitrage_opportunity(ticker_data)

    # Print the identified arbitrage opportunity
    if arbitrage_opportunity:
        print_profit_report(arbitrage_opportunity)
    else:
        print("No arbitrage opportunity identified.")
except Exception as e:
    print(f"Error processing response: {e}")
