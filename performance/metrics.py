import numpy as np
import pandas as pd

def total_return(returns) -> float: #Normal returns are considered for multi assets over log returns
    return (1 + returns).prod() - 1

def sharpe_ratio(returns : pd.Series, freq : int = 252) -> float:
    std = returns.std()
    if(std == 0):
        return np.nan
    
    return (returns.mean()*np.sqrt(freq)) / std

def volatility(returns : pd.Series, freq : int = 252) -> float:
    return np.sqrt(freq) * returns.std()

def equity_curve(returns: pd.Series) -> pd.Series: #Normal returns are used instead of log returns
    return (1 + returns).cumprod()


def max_drawdown(returns : pd.Series) -> float:
    eq = equity_curve(returns)
    cum_max = eq.cummax()
    drawdown = eq/cum_max - 1
    return drawdown.min()


def drawdown_series(returns : pd.Series) -> pd.Series:

    eq = equity_curve(returns)
    cum_max = eq.cummax()
    return eq/cum_max - 1

def win_rate(returns : pd.Series) -> float:
    return (returns > 0).mean()

def pnl_stats(returns : pd.Series) -> dict:

    return {
        'mean' : returns.mean(),
        'std' : returns.std(),
        'skew' : returns.skew(),
        'kurtosis' : returns.kurtosis()
    }

def turnover(positions) -> float:

    if isinstance(positions, pd.Series):
        return positions.diff().abs().sum()
    return positions.diff().abs().sum().sum()

def gross_exposure(positions : pd.DataFrame) -> pd.Series:
    if isinstance(positions, pd.Series):
        return positions.abs()
    return positions.abs().sum(axis=1)