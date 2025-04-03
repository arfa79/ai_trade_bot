# AI Trading Bot 🤖📈 [![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A professional-grade cryptocurrency trading system with AI/ML capabilities.

## Features ✨
- **Multi-model AI** (LSTM + Transformer + RL)
- **Secure credential management** (Vault-compatible)
- **Real-time dashboard** (Grafana + TimescaleDB)
- **News sentiment analysis** (FinBERT)
- **Exchange-agnostic** (Binance/Coinbase ready)

## Quick Start 🚀

### Prerequisites
- Python 3.9+
- Docker 20.10+
- PostgreSQL 14+ (for TimescaleDB)

### Clone and setup

```bash
git clone https://github.com/arfa79/ai-trading-bot.git
cd ai-trading-bot
```

### Initialize environment

```bash
cp .env.example .env  # Update with your credentials
chmod 600 .env  # Restrict file permissions
```

### Start infrastructure

```bash
docker-compose -f monitoring/dashboard/docker-compose.yml up -d
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run main pipeline

```bash
python run.py
```

## Project Structure 🗂️

```bash
ai_trading_bot/
├── data/                # Data pipeline
│   ├── fetcher.py       # Live data collection
│   ├── storage.py       # TimescaleDB operations
│   └── preprocess.py    # Data cleaning
├── models/
│   ├── lstm_model.py    # Price prediction
│   └── rl_agent.py      # Reinforcement Learning
├── monitoring/
│   ├── alerts.py        # Telegram notifications
│   └── dashboard/       # Grafana configs
└── Dockerfile           # Containerization
```

## Configuration ⚙️

Rename .env.example to .env and fill in:

```bash 
# Binance API
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

# TimescaleDB
DB_PASSWORD=your_db_password

# Telegram
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
```
## Dashboard Setup 📊

1.Access Grafana at http://localhost:3000

2.Login with admin + password from .env

3.Import dashboard ID 18604 (Trading Analytics)

## Contributing 🤝

Pull requests welcome! For major changes, open an issue first.