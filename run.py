from data.fetcher import fetch_ohlcv
from data.preprocess import clean_data, scale_features
from features.indicators import add_indicators
from features.sentiment import fetch_news, analyze_sentiment
from models.lstm_model import create_lstm_model, preprocess_data
from models.rl_agent import train_rl_agent
from strategies.backtester import backtest_ma_crossover
from monitoring.alerts import send_telegram_alert
import pandas as pd

# Pipeline
df = fetch_ohlcv()
df = clean_data(df)
df = add_indicators(df)
df, scaler = scale_features(df)

# AI Components
X, y, _ = preprocess_data(df)
lstm_model = create_lstm_model((X.shape[1], X.shape[2]))
lstm_model.fit(X, y, epochs=10)

rl_model = train_rl_agent(df[['close', 'rsi', 'macd']])

# Strategy
portfolio, report = backtest_ma_crossover(df)
send_telegram_alert(f"Backtest results: {report}")