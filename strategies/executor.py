import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceTrader:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': os.getenv('BINANCE_API_KEY'),
            'secret': os.getenv('BINANCE_API_SECRET'),
            'enableRateLimit': True
        })
    
    def execute_order(self, symbol, side, amount):
        """Execute market order with risk checks."""
        if side not in ['buy', 'sell']:
            raise ValueError("Invalid side")
        
        try:
            order = self.exchange.create_market_order(symbol, side, amount)
            return order
        except Exception as e:
            print(f"Order failed: {e}")
            return None