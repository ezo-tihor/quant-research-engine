import numpy as np
import pandas as pd
from scipy.optimize import brute

class SMAVectorBacktester(object):

    def __init__(self, symbol, SMA1, SMA2, start, end):
        self.symbol = symbol
        self.SMA1 = SMA1
        self.SMA2 = SMA2
        self.start = start
        self.end = end
        self.results = None
        self.get_data()

    def get_data(self):

        raw = pd.read_csv('data/pyalgo_eikon_eod_data.csv', index_col=0, parse_dates=True).dropna()
        raw = pd.DataFrame(raw[self.symbol])
        raw = raw.loc[self.start : self.end]
        raw.rename(columns={self.symbol : 'price'}, inplace=True)
        raw['return'] = np.log(raw / raw.shift(1))

        # Strategy code mixed with data loading
        raw['SMA1'] = raw['price'].rolling(self.SMA1).mean()
        raw['SMA2'] = raw['price'].rolling(self.SMA2).mean()
        #--------#
        
        self.data = raw

    def set_paramters(self, SMA1 = None, SMA2 = None):
        
        if SMA1 is not None:
            self.SMA1 = SMA1
            self.data['SMA1'] = self.data['price'].rolling(self.SMA1).mean()
        if SMA2 is not None:
            self.SMA2 = SMA2
            self.data['SMA2'] = self.data['price'].rolling(self.SMA2).mean()

    def run_strategy(self):

        data = self.data.copy().dropna()
        data['position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
        #Backtesting happens here
        data['strategy'] = data['position'].shift(1) * data['return']
        data.dropna(inplace=True)
        data['cum_return'] = np.exp(data['return'].cumsum())
        data['cum_strategy'] = np.exp(data['strategy'].cumsum())
        self.results = data

        gross_perf = data['cum_strategy'].iloc[-1]
        # Calculate difference in performance between actual return vs Strategy return
        perf = gross_perf - data['cum_return'].iloc[-1]

        return round(gross_perf,2), round(perf, 2)

    def plot_results(self):

        if self.results is None:
            print('No results to plot yet. Run a strategy')

        title = '%s | SMA1=%d SMA2=%d' % (self.symbol, self.SMA1, self.SMA2)

        self.results[['cum_return', 'cum_strategy']].plot(title=title, figsize=(16,8))

    def update_and_run(self, SMA): #Check for its return value. Why -gross_perf?

        self.set_paramters(int(SMA[0]), int(SMA[1]))
        return -self.run_strategy()[0]
    
    def optimize_parameters(self, SMA1_range, SMA2_range): #Brute force way of optimizing results

        opt = brute(self.update_and_run, (SMA1_range, SMA2_range), finish=None)
        return opt, -self.update_and_run(opt)
    
if __name__ == '__main__':
    
    smabt = SMAVectorBacktester('EUR=', 42, 252, '2010-1-1', '2020-12-31')
    
    print(smabt.run_strategy())
    smabt.set_paramters(SMA1=20, SMA2=100)
    print(smabt.run_strategy())
    print(smabt.optimize_parameters((30,56,4), (200,300,4)))