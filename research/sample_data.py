import pandas as pd
import numpy as np

# print('Hello World')

def generate_sample_data(rows = 5, cols = 4):
    dates = pd.date_range('2021-01-01', periods=rows, freq='min')
    # print(dates)
    data = 100 + np.cumsum(np.random.randn(rows, cols), axis=0)
    return pd.DataFrame(data, index=dates, columns=[f"Col_{i}" for i in range(cols)])


# print(generate_sample_data())