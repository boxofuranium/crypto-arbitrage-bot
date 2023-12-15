import json
import requests
from arbitrage_strategy import ArbitrageAlgorithm
from utils import print_profit_report

coinlayer_api_key = '290ab78059844ff0a44ab1bd0a990d73'

coinlayer_base_url = f'http://api.coinlayer.com/live?access_key={coinlayer_api_key}'

target_currency = 'USD'


symbols = ['BTC', 'ETH', 'LTC']


params = {
    'target': target_currency,
    'symbols': ','.join(symbols),
    'expand': 1,
    'callback': 'your_callback_function'  # Replace with desired callback function name
}


response = requests.get(coinlayer_base_url, params=params)

try:
    
    json_start = response.text.find('(') + 1
    json_end = response.text.rfind(')')
    json_content = response.text[json_start:json_end]
    
    
    ticker_data = json.loads(json_content)

    
    arbitrage_algorithm = ArbitrageAlgorithm()

    
    arbitrage_opportunity = arbitrage_algorithm.identify_arbitrage_opportunity(ticker_data)

    
    if arbitrage_opportunity:
        print_profit_report(arbitrage_opportunity)
    else:
        print("No arbitrage opportunity identified.")
except Exception as e:
    print(f"Error processing response: {e}")
