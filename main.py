#Code starts here
from data.data_loader_yves import load_data_yves
from data.data_loader import load_price_data
from strategy.sma_strategy import SMAStrategy
from backtester.backtester import Backtester
from performance.analyzer import PerformanceAnalyzer
from strategy.equal_weight import EqualWeightStrategy

# The below code is for basic version where only single asset class is dealt with.

'''

data = load_data_yves('EUR=', '2010-1-1', '2020-12-31')
strategy = SMAStrategy(42, 252)
bt = Backtester(data, strategy)

data = bt.run()

print(data.head())

perf = PerformanceAnalyzer(data)

summary = perf.summary()

for key, value in summary.items():
    print(key, value, sep=': ')

'''

# Code for multi asset

tickers = ['AAPL', 'MSFT', 'GOOG']

prices = load_price_data(tickers)

print(prices.head())
print(prices.shape)



