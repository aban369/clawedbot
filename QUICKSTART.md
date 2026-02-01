# ⚡ ClawedBot Quick Start Guide

Get ClawedBot running in 5 minutes!

## 🚀 Fastest Way to Start

### Option 1: Replit (Easiest - No Installation)

1. **Click this link**: [Import to Replit](https://replit.com/github/aban369/clawedbot)
2. **Add Secrets** (🔒 icon):
   ```
   BINANCE_API_KEY = your_key_here
   BINANCE_API_SECRET = your_secret_here
   TRADING_MODE = paper
   ```
3. **Click Run** ▶️
4. **Done!** Bot is running in paper trading mode

### Option 2: Local (5 Minutes)

```bash
# 1. Clone
git clone https://github.com/aban369/clawedbot.git
cd clawedbot

# 2. Install
pip install -r requirements.txt

# 3. Configure
cp .env.example .env
# Edit .env with your API keys

# 4. Run
python main.py
```

---

## 📝 Minimum Configuration

Edit `.env` file:

```bash
# Required for basic operation
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_secret

# Trading mode (ALWAYS start with paper!)
TRADING_MODE=paper

# Optional but recommended
TELEGRAM_BOT_TOKEN=your_telegram_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

## 🎯 First Steps

### 1. Verify Bot is Running

You should see:
```
╔═══════════════════════════════════════════╗
║         🤖  CLAWEDBOT v1.0.0  🤖         ║
╚═══════════════════════════════════════════╝

✅ Configuration validated successfully
🤖 Initializing ClawedBot...
Trading Mode: PAPER
✅ ClawedBot initialized successfully
🚀 ClawedBot is now running...
```

### 2. Check Logs

```bash
tail -f logs/clawedbot.log
```

### 3. Monitor Performance

Open dashboard (if enabled):
```
http://localhost:8050
```

---

## ⚙️ Basic Configuration

### Choose Your Strategy

Edit `config.py`:

```python
# Available strategies:
STRATEGY = 'quantum_flow'  # Advanced multi-indicator
# STRATEGY = 'swing_trade'  # Swing trading
# STRATEGY = 'mt5_forex'    # MT5 forex trading
```

### Set Trading Pairs

```python
TRADING_PAIRS = [
    'BTC/USDT',
    'ETH/USDT',
    'BNB/USDT'
]
```

### Adjust Risk

```python
RISK_PER_TRADE = 0.02      # 2% risk per trade
MAX_POSITION_SIZE = 1000   # Max $1000 per position
MAX_DAILY_LOSS = 0.05      # Stop if 5% daily loss
```

---

## 🔔 Setup Telegram Alerts (Optional)

### 1. Create Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Follow instructions
4. Copy the bot token

### 2. Get Your Chat ID

1. Search for `@userinfobot` on Telegram
2. Start the bot
3. Copy your chat ID

### 3. Add to .env

```bash
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

---

## 📊 Understanding the Output

### Normal Operation
```
Trading cycle completed at 2026-02-01 12:00:00
```

### Signal Detected
```
✅ BUY signal detected for BTC/USDT
Entry: $45,000 | Stop: $44,100 | Target: $46,800
Position size: 0.022 BTC
```

### Position Closed
```
✅ Position closed: BTC/USDT | PnL: $150.00
```

---

## ⚠️ Important Safety Tips

### ✅ DO:
- Start with **paper trading**
- Test for at least **1 week** before live trading
- Start with **small amounts** ($100-500)
- Monitor **daily**
- Set **stop losses**
- Keep API keys **secure**

### ❌ DON'T:
- Jump straight to live trading
- Use your entire capital
- Leave bot unattended for days
- Share your API keys
- Disable risk management
- Trade without understanding the strategy

---

## 🆘 Common Issues

### "Configuration validation failed"
- Check your `.env` file exists
- Verify API keys are correct
- Ensure no extra spaces in keys

### "Failed to connect to exchange"
- Check internet connection
- Verify API keys are active
- Check exchange API status
- Ensure IP is whitelisted (if required)

### "Module not found"
- Run: `pip install -r requirements.txt`
- Check Python version: `python --version` (need 3.9+)

### Bot stops unexpectedly
- Check logs: `cat logs/clawedbot.log`
- Verify API rate limits not exceeded
- Check daily loss limit not reached

---

## 📈 Next Steps

1. **Read Full Documentation**: Check `README.md`
2. **Understand Strategies**: Review your notes on trading strategies
3. **Backtest**: Test strategies on historical data
4. **Paper Trade**: Run for 1-2 weeks minimum
5. **Start Small**: Begin with minimal capital
6. **Scale Gradually**: Increase as you gain confidence

---

## 📚 Resources

- **Full README**: [README.md](README.md)
- **Deployment Guide**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **GitHub Issues**: [Report Problems](https://github.com/aban369/clawedbot/issues)
- **Your Trading Notes**: Check your Bhindi notes for strategies

---

## 🎓 Learning Path

### Week 1: Setup & Testing
- Install and configure
- Run in paper mode
- Monitor logs
- Understand output

### Week 2: Strategy Understanding
- Review indicator logic
- Study signal generation
- Analyze paper trades
- Adjust parameters

### Week 3: Risk Management
- Test stop losses
- Verify position sizing
- Check daily limits
- Monitor performance

### Week 4: Live Trading (Optional)
- Start with $100-500
- Monitor closely
- Keep detailed records
- Adjust as needed

---

## 💡 Pro Tips

1. **Keep a Trading Journal**: Document all trades and decisions
2. **Review Daily**: Check performance and logs every day
3. **Stay Updated**: Pull latest code regularly: `git pull`
4. **Join Community**: Share experiences, learn from others
5. **Never Stop Learning**: Markets evolve, so should your strategies

---

## 🤝 Need Help?

- **Email**: raiz.s.group1@gmail.com
- **GitHub Issues**: [Create an issue](https://github.com/aban369/clawedbot/issues/new)
- **Documentation**: [Full docs](README.md)

---

**Ready to start? Run `python main.py` and let's go! 🚀**

*Remember: Start with paper trading. Real money comes later.*
