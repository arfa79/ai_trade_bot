import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def create_lstm_model(input_shape):
    """Build LSTM model for price prediction."""
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(32),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def preprocess_data(df, seq_length=60):
    """Prepare data for LSTM."""
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[['close', 'rsi', 'macd']])
    X, y = [], []
    for i in range(seq_length, len(scaled_data)):
        X.append(scaled_data[i-seq_length:i])
        y.append(scaled_data[i, 0])
    return np.array(X), np.array(y), scaler