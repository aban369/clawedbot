# 🚀 ClawedBot Deployment Guide

Complete guide to deploy ClawedBot on various platforms.

## 📋 Prerequisites

- Python 3.9 or higher
- Git installed
- API keys for exchanges (Binance, Bybit, etc.)
- Telegram bot token (optional)
- Google Gemini API key (optional)

---

## 🖥️ Local Deployment

### 1. Clone Repository
```bash
git clone https://github.com/aban369/clawedbot.git
cd clawedbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env with your API keys
nano .env  # or use any text editor
```

### 5. Run the Bot
```bash
# Paper trading mode (default)
python main.py

# Live trading mode (⚠️ USE WITH CAUTION)
# Edit config.py and set TRADING_MODE = 'live'
python main.py
```

---

## ☁️ Replit Deployment

### Method 1: Import from GitHub

1. Go to [Replit](https://replit.com)
2. Click "Create Repl"
3. Select "Import from GitHub"
4. Enter: `https://github.com/aban369/clawedbot`
5. Click "Import from GitHub"

### Method 2: Manual Setup

1. Create a new Python Repl
2. In the Shell tab:
```bash
git clone https://github.com/aban369/clawedbot.git
cd clawedbot
pip install -r requirements.txt
```

### Configure Secrets

1. Click the "Secrets" tab (🔒 icon)
2. Add your environment variables:
   - `BINANCE_API_KEY`
   - `BINANCE_API_SECRET`
   - `TELEGRAM_BOT_TOKEN`
   - etc.

### Run on Replit

1. Set the run command in `.replit` file:
```toml
run = "python main.py"
```

2. Click the "Run" button

### Keep Alive on Replit

Add this to keep your bot running 24/7:

```python
# Add to main.py
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "ClawedBot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Call before bot starts
keep_alive()
```

Then use [UptimeRobot](https://uptimerobot.com) to ping your Repl URL every 5 minutes.

---

## 🐳 Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Build and Run
```bash
# Build image
docker build -t clawedbot .

# Run container
docker run -d \
  --name clawedbot \
  --env-file .env \
  clawedbot
```

### Docker Compose
```yaml
version: '3.8'

services:
  clawedbot:
    build: .
    container_name: clawedbot
    env_file: .env
    restart: unless-stopped
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data
```

Run with:
```bash
docker-compose up -d
```

---

## ☁️ VPS Deployment (Ubuntu/Debian)

### 1. Connect to VPS
```bash
ssh user@your-vps-ip
```

### 2. Install Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip git -y
```

### 3. Clone and Setup
```bash
git clone https://github.com/aban369/clawedbot.git
cd clawedbot
pip3 install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
nano .env  # Add your API keys
```

### 5. Run with Screen (keeps running after disconnect)
```bash
# Install screen
sudo apt install screen -y

# Start screen session
screen -S clawedbot

# Run bot
python3 main.py

# Detach: Press Ctrl+A then D
# Reattach: screen -r clawedbot
```

### 6. Run as Systemd Service (recommended)

Create service file:
```bash
sudo nano /etc/systemd/system/clawedbot.service
```

Add:
```ini
[Unit]
Description=ClawedBot Trading System
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/home/your-username/clawedbot
ExecStart=/usr/bin/python3 /home/your-username/clawedbot/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable clawedbot
sudo systemctl start clawedbot

# Check status
sudo systemctl status clawedbot

# View logs
sudo journalctl -u clawedbot -f
```

---

## 🌐 Heroku Deployment

### 1. Create Procfile
```
worker: python main.py
```

### 2. Deploy
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-clawedbot

# Set environment variables
heroku config:set BINANCE_API_KEY=your_key
heroku config:set BINANCE_API_SECRET=your_secret

# Deploy
git push heroku main

# Scale worker
heroku ps:scale worker=1

# View logs
heroku logs --tail
```

---

## 📱 Railway Deployment

1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose `aban369/clawedbot`
5. Add environment variables in Settings
6. Deploy!

---

## ⚙️ Configuration Tips

### Paper Trading (Safe Testing)
```python
# In config.py
TRADING_MODE = 'paper'
```

### Live Trading (⚠️ Real Money)
```python
# In config.py
TRADING_MODE = 'live'

# Start with small amounts!
MAX_POSITION_SIZE = 100  # $100 max per trade
RISK_PER_TRADE = 0.01    # 1% risk
```

### Enable Features
```python
# In .env
ENABLE_ML_PREDICTIONS=true
ENABLE_HAWKES_DETECTION=true
ENABLE_ECONOPHYSICS=true
ENABLE_SENTIMENT_ANALYSIS=false
```

---

## 🔍 Monitoring

### View Logs
```bash
# Local
tail -f logs/clawedbot.log

# Docker
docker logs -f clawedbot

# Systemd
sudo journalctl -u clawedbot -f
```

### Dashboard
Access web dashboard at:
```
http://localhost:8050
```

---

## 🛡️ Security Best Practices

1. **Never commit .env file**
   - Already in .gitignore
   - Use environment variables

2. **Use API restrictions**
   - Enable IP whitelist on exchange
   - Disable withdrawals for API keys
   - Use read-only keys for testing

3. **Start with paper trading**
   - Test thoroughly before live trading
   - Verify all strategies work correctly

4. **Monitor regularly**
   - Check logs daily
   - Set up Telegram alerts
   - Review performance metrics

5. **Backup data**
   - Backup logs and trade history
   - Keep configuration files safe

---

## 🆘 Troubleshooting

### Bot won't start
```bash
# Check Python version
python --version  # Should be 3.9+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check logs
cat logs/clawedbot.log
```

### API connection errors
- Verify API keys are correct
- Check exchange API status
- Ensure IP is whitelisted (if required)
- Check rate limits

### Import errors
```bash
# Install missing packages
pip install package-name

# Or reinstall all
pip install -r requirements.txt
```

---

## 📞 Support

- **GitHub Issues**: [Report bugs](https://github.com/aban369/clawedbot/issues)
- **Email**: raiz.s.group1@gmail.com
- **Documentation**: [docs.bhindi.io](https://docs.bhindi.io)

---

## ⚠️ Important Warnings

1. **Trading involves risk** - Never invest more than you can afford to lose
2. **Test thoroughly** - Always use paper trading first
3. **Monitor actively** - Don't leave bot unattended for long periods
4. **Start small** - Begin with minimal position sizes
5. **Understand the code** - Know what the bot is doing

---

**Happy Trading! 🚀**

*Remember: Past performance does not guarantee future results.*
