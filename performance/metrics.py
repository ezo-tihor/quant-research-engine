import numpy as np
import pandas as pd

def total_return(log_returns) -> float:
    return np.exp(log_returns.sum()) - 1

def sharpe_ratio(log_returns : pd.Series, freq : int = 252) -> float:
    std = log_returns.std()
    if(std == 0):
        return np.nan
    
    return (log_returns.mean()*np.sqrt(freq)) / std

def volatility(log_returns : pd.Series, freq : int = 252) -> float:
    return np.sqrt(freq) * log_returns.std()

def equity_curve(log_returns: pd.Series) -> pd.Series:
    return np.exp(log_returns.cumsum())


def max_drawdown(log_returns : pd.Series) -> float:
    eq = equity_curve(log_returns)
    cum_max = eq.cummax()
    drawdown = eq/cum_max - 1
    return drawdown.min()


def drawdown_series(log_returns : pd.Series) -> pd.Series:

    eq = equity_curve(log_returns)
    cum_max = eq.cummax()
    return eq/cum_max - 1

def win_rate(log_returns : pd.Series) -> float:
    return (log_returns > 0).mean()

def pnl_stats(log_returns : pd.Series) -> dict:

    return {
        'mean' : log_returns.mean(),
        'std' : log_returns.std(),
        'skew' : log_returns.skew(),
        'kurtosis' : log_returns.kurtosis()
    }

def turnover(positions) -> float:

    if isinstance(positions, pd.Series):
        return positions.diff().abs().sum()
    return positions.diff().abs().sum().sum()

def gross_exposure(positions : pd.DataFrame) -> pd.Series:
    if isinstance(positions, pd.Series):
        return positions.abs()
    return positions.abs().sum(axis=1)