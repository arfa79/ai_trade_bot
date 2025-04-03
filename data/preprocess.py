import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def clean_data(df):
    """Handle missing values and outliers."""
    # Forward-fill missing values
    df.ffill(inplace=True)
    
    # Remove outliers using IQR
    Q1 = df['close'].quantile(0.25)
    Q3 = df['close'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df['close'] < (Q1 - 1.5 * IQR)) | (df['close'] > (Q3 + 1.5 * IQR)))]
    return df

def scale_features(df, features=['close', 'volume', 'rsi']):
    """Normalize features to [0,1] range."""
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])
    return df, scaler