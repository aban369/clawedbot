# 🤖 ClawedBot - Advanced AI Trading System

**ClawedBot** is a comprehensive, research-based trading bot that combines cutting-edge quantitative finance, machine learning, and real-time market analysis.

## 🌟 Features

### Core Trading Capabilities
- ✅ **Multi-Exchange Support** - Binance, Bybit, OKX, and more
- ✅ **MT5 Integration** - Forex and CFD trading
- ✅ **TradingView Webhooks** - Real-time signal execution
- ✅ **Order Book Analysis** - DeepLOB neural network predictions
- ✅ **Flash Crash Detection** - Hawkes Process monitoring
- ✅ **Econophysics Analysis** - Thermodynamic market modeling

### Advanced Features
- 🧠 **AI-Powered Predictions** - Neural networks and reinforcement learning
- 📊 **17+ Research Papers Integrated** - Academic-grade algorithms
- ⚡ **Real-Time Risk Management** - Dynamic position sizing
- 🎯 **Multi-Timeframe Analysis** - Comprehensive market view
- 📈 **Sentiment Analysis** - Social media and news integration
- 🔔 **Telegram Notifications** - Real-time alerts

### Research-Based Indicators
1. VPIN (Volume-Synchronized Probability of Informed Trading)
2. Hawkes Process Flash Crash Detection
3. DeepLOB Order Book Prediction
4. Econophysics Thermodynamic Analysis
5. Large Price Change Detection
6. Inter-Trade Duration Analysis
7. Regime Detection & Arbitrage
8. Tfin Optimization Framework
9. And 9 more advanced indicators...

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9+
pip install -r requirements.txt
```

### Installation
```bash
git clone https://github.com/aban369/clawedbot.git
cd clawedbot
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python main.py
```

### Configuration
Edit `config.py` to customize:
- Exchange API credentials
- Trading pairs and timeframes
- Risk management parameters
- Strategy settings

## 📁 Project Structure

```
clawedbot/
├── main.py                          # Main entry point
├── config.py                        # Configuration
├── requirements.txt                 # Dependencies
│
├── core/                            # Core systems
│   ├── exchange_collector.py       # Multi-exchange data collection
│   ├── mt5_manager.py              # MT5 connection & trading
│   ├── feature_engineer.py         # Feature extraction
│   └── risk_manager.py             # Risk management
│
├── models/                          # ML/AI models
│   ├── deeplob_predictor.py        # Order book prediction
│   ├── hawkes_detector.py          # Flash crash detection
│   ├── thermodynamic_analyzer.py   # Econophysics analysis
│   └── reinforcement_learner.py    # RL trading agent
│
├── strategies/                      # Trading strategies
│   ├── signal_generator.py         # Signal generation
│   ├── strategy_engine.py          # Strategy execution
│   └── indicators.py               # Technical indicators
│
├── integrations/                    # External integrations
│   ├── tradingview_webhook.py      # TradingView integration
│   ├── telegram_notifier.py        # Telegram alerts
│   └── gemini_ai.py                # AI analysis
│
└── utils/                           # Utilities
    ├── performance_tracker.py       # Performance metrics
    ├── dashboard.py                 # Web dashboard
    └── logger.py                    # Logging system
```

## 🎯 Trading Strategies

### 1. Quantum Flow Strategy
- Multi-timeframe confluence
- Order flow analysis
- Volume profile integration
- 17 research papers combined

### 2. Swing Trading Strategy
- Top 12 coin selection (research-based)
- CMC filters for pump detection
- Risk-adjusted position sizing
- 90-day alpha portfolio

### 3. MT5 Forex Strategy
- Advanced technical analysis
- Multi-indicator confirmation
- Dynamic stop-loss/take-profit
- Performance tracking

## 📊 Performance Metrics

- **Backtested Returns:** Available in `/backtests`
- **Win Rate:** Tracked in real-time
- **Sharpe Ratio:** Risk-adjusted performance
- **Max Drawdown:** Risk monitoring

## 🔐 Security

- API keys stored in `.env` (never committed)
- Encrypted credentials support
- Rate limiting and error handling
- Position size limits

## 📚 Research Papers Implemented

1. VPIN and Flash Crash Detection
2. DeepLOB: Deep Convolutional Neural Networks for Limit Order Books
3. Hawkes Processes for High-Frequency Trading
4. Econophysics and Thermodynamic Analysis
5. Large Price Change Detection
6. Inter-Trade Duration Modeling
7. Market Regime Detection
8. Tfin Optimization Framework
9. Order Flow Imbalance
10. Volume Profile Analysis
11. Sentiment Analysis Integration
12. Reinforcement Learning for Trading
13. Multi-Timeframe Analysis
14. Arbitrage Detection
15. Risk Management Frameworks
16. Machine Learning Predictors
17. Advanced Signal Generation

## 🛠️ Development

### Running Tests
```bash
pytest tests/
```

### Backtesting
```bash
python backtest.py --strategy quantum_flow --start 2024-01-01 --end 2025-01-01
```

### Live Trading
```bash
python main.py --mode live --strategy quantum_flow
```

## 📈 Dashboard

Access the web dashboard at `http://localhost:8050` after running:
```bash
python dashboard.py
```

## 🔔 Telegram Setup

1. Create a bot with @BotFather
2. Get your bot token
3. Add token to `.env`
4. Start receiving alerts!

## ⚠️ Disclaimer

**HIGH RISK WARNING:** Trading cryptocurrencies and forex involves substantial risk of loss. This bot is for educational and research purposes. Always test strategies thoroughly before live trading. Never invest more than you can afford to lose.

## 📝 License

MIT License - See LICENSE file

## 🤝 Contributing

Contributions welcome! Please read CONTRIBUTING.md first.

## 📧 Support

- GitHub Issues: [Report bugs](https://github.com/aban369/clawedbot/issues)
- Telegram: Coming soon
- Email: raiz.s.group1@gmail.com

## 🌟 Acknowledgments

Built with research from leading quantitative finance papers and powered by:
- Binance, Bybit, OKX APIs
- MetaTrader 5
- TradingView
- Google Gemini AI
- And many open-source libraries

---

**Made with 🔥 by Aban Ali**

*Last Updated: February 2026*
