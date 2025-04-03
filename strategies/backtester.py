import pandas as pd
import vectorbt as vbt

def backtest_ma_crossover(df):
    """Backtest Moving Average Crossover strategy."""
    fast_ma = vbt.MA.run(df['close'], window=10)
    slow_ma = vbt.MA.run(df['close'], window=50)
    entries = fast_ma.ma_crossed_above(slow_ma)
    exits = fast_ma.ma_crossed_below(slow_ma)
    
    portfolio = vbt.Portfolio.from_signals(
        df['close'], 
        entries, 
        exits,
        fees=0.001  # Binance trading fee
    )
    
    # Generate report
    report = {
        "total_return": portfolio.total_return(),
        "sharpe_ratio": portfolio.sharpe_ratio(),
        "max_drawdown": portfolio.max_drawdown()
    }
    return portfolio, report