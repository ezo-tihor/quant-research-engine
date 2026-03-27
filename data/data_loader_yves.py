#data/data_loader_yves.py

import pandas as pd
import numpy as np

def load_data_yves(symbol, start_date, end_date):

    raw = pd.read_csv('data/pyalgo_eikon_eod_data.csv', index_col=0, parse_dates=True).dropna()
    raw = pd.DataFrame(raw[symbol])
    raw = raw.loc[start_date : end_date]
    raw = raw.rename(columns={symbol : 'price'})
    # print(raw.head())
    raw['return'] = np.log(raw['price'] / raw['price'].shift(1))
    return raw