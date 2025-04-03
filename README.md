# AI Trading Bot 🤖📈 [![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A professional-grade cryptocurrency trading system with AI/ML capabilities.

![System Architecture](https://i.imgur.com/JQ8y5Yl.png)

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

```bash
# Clone and setup
git clone https://github.com/arfa79/ai-trading-bot.git
cd ai-trading-bot

# Initialize environment
cp .env.example .env  # Update with your credentials
chmod 600 .env  # Restrict file permissions

# Start infrastructure
docker-compose -f monitoring/dashboard/docker-compose.yml up -d

# Install dependencies
pip install -r requirements.txt

# Run main pipeline
python run.py