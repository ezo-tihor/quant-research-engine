#data/data_loader.py

import yfinance as yf
import pandas as pd

def load_price_data(tickers, start='2020-01-01', end='2023-01-01'):
    '''
    '''
    
    data = yf.download(tickers, start=start, end=end)['Close']
    if isinstance(data, pd.Series):
        data = data.to_frame()
    
    data = data.dropna()

    return data