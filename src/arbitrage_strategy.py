class ArbitrageAlgorithm:
    @staticmethod
    def identify_arbitrage_opportunity(ticker_data, buy_currency, sell_currency):
        
        buy_price = ticker_data['rates'].get(buy_currency)
        sell_price = ticker_data['rates'].get(sell_currency)

        
        if buy_price is not None and sell_price is not None:
            
            profit = sell_price - buy_price

            
            if profit > 0:
                return {
                    'buy_exchange': 'Coinlayer',
                    'sell_exchange': 'Coinlayer',
                    'buy_currency': buy_currency,
                    'sell_currency': sell_currency,
                    'buy_price': buy_price,
                    'sell_price': sell_price,
                    'profit': profit
                }

        return None

