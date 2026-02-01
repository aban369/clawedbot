"""
ClawedBot Configuration
Central configuration for all bot settings
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Main configuration class"""
    
    # ===== EXCHANGE SETTINGS =====
    EXCHANGES = {
        'binance': {
            'api_key': os.getenv('BINANCE_API_KEY'),
            'api_secret': os.getenv('BINANCE_API_SECRET'),
            'enabled': True
        },
        'bybit': {
            'api_key': os.getenv('BYBIT_API_KEY'),
            'api_secret': os.getenv('BYBIT_API_SECRET'),
            'enabled': True
        },
        'okx': {
            'api_key': os.getenv('OKX_API_KEY'),
            'api_secret': os.getenv('OKX_API_SECRET'),
            'passphrase': os.getenv('OKX_PASSPHRASE'),
            'enabled': False
        }
    }
    
    # ===== MT5 SETTINGS =====
    MT5_CONFIG = {
        'login': int(os.getenv('MT5_LOGIN', 0)),
        'password': os.getenv('MT5_PASSWORD'),
        'server': os.getenv('MT5_SERVER'),
        'enabled': False
    }
    
    # ===== TRADING SETTINGS =====
    TRADING_MODE = os.getenv('TRADING_MODE', 'paper')  # paper or live
    DEFAULT_PAIR = os.getenv('DEFAULT_PAIR', 'BTC/USDT')
    
    # Trading pairs to monitor
    TRADING_PAIRS = [
        'BTC/USDT', 'ETH/USDT', 'BNB/USDT',
        'XRP/USDT', 'SOL/USDT', 'ADA/USDT',
        'DOGE/USDT', 'MATIC/USDT', 'DOT/USDT',
        'AVAX/USDT', 'LINK/USDT', 'UNI/USDT'
    ]
    
    # Timeframes
    TIMEFRAMES = ['1m', '5m', '15m', '1h', '4h', '1d']
    PRIMARY_TIMEFRAME = '15m'
    
    # ===== RISK MANAGEMENT =====
    MAX_POSITION_SIZE = float(os.getenv('MAX_POSITION_SIZE', 1000))
    RISK_PER_TRADE = float(os.getenv('RISK_PER_TRADE', 0.02))  # 2%
    MAX_DAILY_LOSS = float(os.getenv('MAX_DAILY_LOSS', 0.05))  # 5%
    MAX_OPEN_POSITIONS = 5
    
    # Stop loss and take profit
    DEFAULT_STOP_LOSS = 0.02  # 2%
    DEFAULT_TAKE_PROFIT = 0.04  # 4%
    TRAILING_STOP = True
    TRAILING_STOP_DISTANCE = 0.015  # 1.5%
    
    # ===== STRATEGY SETTINGS =====
    STRATEGY = 'quantum_flow'  # quantum_flow, swing_trade, mt5_forex
    
    # Signal confirmation requirements
    MIN_CONFIRMATIONS = 3
    REQUIRE_VOLUME_CONFIRMATION = True
    REQUIRE_TREND_CONFIRMATION = True
    
    # ===== FEATURE FLAGS =====
    ENABLE_ML_PREDICTIONS = os.getenv('ENABLE_ML_PREDICTIONS', 'true').lower() == 'true'
    ENABLE_HAWKES_DETECTION = os.getenv('ENABLE_HAWKES_DETECTION', 'true').lower() == 'true'
    ENABLE_ECONOPHYSICS = os.getenv('ENABLE_ECONOPHYSICS', 'true').lower() == 'true'
    ENABLE_SENTIMENT_ANALYSIS = os.getenv('ENABLE_SENTIMENT_ANALYSIS', 'false').lower() == 'true'
    
    # ===== TELEGRAM SETTINGS =====
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    TELEGRAM_ENABLED = bool(TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID)
    
    # ===== GEMINI AI SETTINGS =====
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_ENABLED = bool(GEMINI_API_KEY)
    
    # ===== WEBHOOK SETTINGS =====
    WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET', 'your_secret_key')
    WEBHOOK_PORT = int(os.getenv('WEBHOOK_PORT', 5000))
    
    # ===== DATABASE SETTINGS =====
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'clawedbot')
    
    # ===== LOGGING SETTINGS =====
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/clawedbot.log')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # ===== DASHBOARD SETTINGS =====
    DASHBOARD_PORT = int(os.getenv('DASHBOARD_PORT', 8050))
    DASHBOARD_HOST = os.getenv('DASHBOARD_HOST', '0.0.0.0')
    
    # ===== UPDATE INTERVALS =====
    DATA_UPDATE_INTERVAL = int(os.getenv('DATA_UPDATE_INTERVAL', 60))  # seconds
    SIGNAL_CHECK_INTERVAL = int(os.getenv('SIGNAL_CHECK_INTERVAL', 30))
    RISK_CHECK_INTERVAL = int(os.getenv('RISK_CHECK_INTERVAL', 10))
    
    # ===== MODEL SETTINGS =====
    # DeepLOB
    DEEPLOB_LOOKBACK = 100
    DEEPLOB_HORIZON = 10
    
    # Hawkes Process
    HAWKES_WINDOW = 1000
    HAWKES_THRESHOLD = 0.8
    
    # Econophysics
    THERMODYNAMIC_WINDOW = 500
    ENTROPY_THRESHOLD = 0.7
    
    # ===== BACKTEST SETTINGS =====
    BACKTEST_START_DATE = os.getenv('BACKTEST_START_DATE', '2024-01-01')
    BACKTEST_END_DATE = os.getenv('BACKTEST_END_DATE', '2025-01-01')
    BACKTEST_INITIAL_CAPITAL = float(os.getenv('BACKTEST_INITIAL_CAPITAL', 10000))
    
    # ===== INDICATOR SETTINGS =====
    # Moving Averages
    MA_FAST = 9
    MA_MEDIUM = 21
    MA_SLOW = 50
    MA_TREND = 200
    
    # RSI
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30
    
    # MACD
    MACD_FAST = 12
    MACD_SLOW = 26
    MACD_SIGNAL = 9
    
    # Bollinger Bands
    BB_PERIOD = 20
    BB_STD = 2
    
    # Volume
    VOLUME_MA_PERIOD = 20
    VOLUME_SPIKE_THRESHOLD = 2.0
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        errors = []
        
        # Check required API keys for enabled exchanges
        for exchange, config in cls.EXCHANGES.items():
            if config['enabled']:
                if not config.get('api_key') or not config.get('api_secret'):
                    errors.append(f"Missing API credentials for {exchange}")
        
        # Check trading mode
        if cls.TRADING_MODE not in ['paper', 'live']:
            errors.append("TRADING_MODE must be 'paper' or 'live'")
        
        # Check risk parameters
        if cls.RISK_PER_TRADE <= 0 or cls.RISK_PER_TRADE > 0.1:
            errors.append("RISK_PER_TRADE should be between 0 and 0.1 (10%)")
        
        if errors:
            raise ValueError(f"Configuration errors:\n" + "\n".join(errors))
        
        return True
    
    @classmethod
    def get_exchange_config(cls, exchange_name):
        """Get configuration for specific exchange"""
        return cls.EXCHANGES.get(exchange_name.lower())
    
    @classmethod
    def is_live_trading(cls):
        """Check if live trading is enabled"""
        return cls.TRADING_MODE == 'live'
    
    @classmethod
    def get_active_exchanges(cls):
        """Get list of enabled exchanges"""
        return [name for name, config in cls.EXCHANGES.items() if config['enabled']]


# Validate configuration on import
try:
    Config.validate()
    print("✅ Configuration validated successfully")
except ValueError as e:
    print(f"⚠️ Configuration validation failed: {e}")
    print("Please check your .env file and update the settings")
