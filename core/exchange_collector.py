"""
Exchange Data Collector
Handles multi-exchange data collection using CCXT
"""

import ccxt
import pandas as pd
import logging
from datetime import datetime
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class ExchangeCollector:
    """Collect and manage data from multiple exchanges"""
    
    def __init__(self, exchange_name: str, api_key: str = None, api_secret: str = None):
        """
        Initialize exchange collector
        
        Args:
            exchange_name: Name of the exchange (binance, bybit, etc.)
            api_key: API key for the exchange
            api_secret: API secret for the exchange
        """
        self.exchange_name = exchange_name.lower()
        self.exchange = None
        
        try:
            # Initialize exchange
            exchange_class = getattr(ccxt, self.exchange_name)
            
            config = {
                'enableRateLimit': True,
                'options': {'defaultType': 'future'}
            }
            
            if api_key and api_secret:
                config['apiKey'] = api_key
                config['secret'] = api_secret
            
            self.exchange = exchange_class(config)
            logger.info(f"✅ Connected to {exchange_name}")
            
        except Exception as e:
            logger.error(f"❌ Failed to connect to {exchange_name}: {e}")
            raise
    
    async def fetch_ohlcv(self, symbol: str, timeframe: str = '1h', limit: int = 100) -> pd.DataFrame:
        """
        Fetch OHLCV data
        
        Args:
            symbol: Trading pair (e.g., 'BTC/USDT')
            timeframe: Timeframe (1m, 5m, 15m, 1h, 4h, 1d)
            limit: Number of candles to fetch
            
        Returns:
            DataFrame with OHLCV data
        """
        try:
            ohlcv = await self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            
            df = pd.DataFrame(
                ohlcv,
                columns=['timestamp', 'open', 'high', 'low', 'close', 'volume']
            )
            
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            
            return df
            
        except Exception as e:
            logger.error(f"Error fetching OHLCV for {symbol}: {e}")
            return pd.DataFrame()
    
    async def fetch_order_book(self, symbol: str, limit: int = 20) -> Dict:
        """
        Fetch order book data
        
        Args:
            symbol: Trading pair
            limit: Depth of order book
            
        Returns:
            Order book dictionary
        """
        try:
            order_book = await self.exchange.fetch_order_book(symbol, limit)
            return order_book
            
        except Exception as e:
            logger.error(f"Error fetching order book for {symbol}: {e}")
            return {}
    
    async def fetch_ticker(self, symbol: str) -> Dict:
        """Fetch current ticker data"""
        try:
            ticker = await self.exchange.fetch_ticker(symbol)
            return ticker
        except Exception as e:
            logger.error(f"Error fetching ticker for {symbol}: {e}")
            return {}
    
    async def fetch_trades(self, symbol: str, limit: int = 100) -> List:
        """Fetch recent trades"""
        try:
            trades = await self.exchange.fetch_trades(symbol, limit=limit)
            return trades
        except Exception as e:
            logger.error(f"Error fetching trades for {symbol}: {e}")
            return []
    
    async def get_balance(self) -> Dict:
        """Get account balance"""
        try:
            balance = await self.exchange.fetch_balance()
            return balance
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            return {}
    
    async def create_order(self, symbol: str, order_type: str, side: str, 
                          amount: float, price: float = None) -> Dict:
        """
        Create an order
        
        Args:
            symbol: Trading pair
            order_type: 'market' or 'limit'
            side: 'buy' or 'sell'
            amount: Order amount
            price: Order price (for limit orders)
            
        Returns:
            Order details
        """
        try:
            if order_type == 'market':
                order = await self.exchange.create_market_order(symbol, side, amount)
            else:
                order = await self.exchange.create_limit_order(symbol, side, amount, price)
            
            logger.info(f"✅ Order created: {side} {amount} {symbol} @ {price}")
            return order
            
        except Exception as e:
            logger.error(f"❌ Order creation failed: {e}")
            return {}
    
    async def cancel_order(self, order_id: str, symbol: str) -> bool:
        """Cancel an order"""
        try:
            await self.exchange.cancel_order(order_id, symbol)
            logger.info(f"✅ Order {order_id} cancelled")
            return True
        except Exception as e:
            logger.error(f"❌ Order cancellation failed: {e}")
            return False
    
    async def get_open_orders(self, symbol: str = None) -> List:
        """Get open orders"""
        try:
            orders = await self.exchange.fetch_open_orders(symbol)
            return orders
        except Exception as e:
            logger.error(f"Error fetching open orders: {e}")
            return []
    
    async def close(self):
        """Close exchange connection"""
        if self.exchange:
            await self.exchange.close()
            logger.info(f"Closed connection to {self.exchange_name}")
