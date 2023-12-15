# utils.py

def print_profit_report(profit_data):
    """
    Print a formatted report of the arbitrage profit.

    Args:
    - profit_data (dict): A dictionary containing information about the arbitrage opportunity.
      Example structure:
      {
          'buy_exchange': 'Exchange1',
          'sell_exchange': 'Exchange2',
          'buy_price': 100.0,
          'sell_price': 105.0,
          'profit': 5.0
      }
    """
    print("Arbitrage Opportunity Identified:")
    print(f"Buy on {profit_data['buy_exchange']} at {profit_data['buy_price']}")
    print(f"Sell on {profit_data['sell_exchange']} at {profit_data['sell_price']}")
    print(f"Potential Profit: {profit_data['profit']}")
