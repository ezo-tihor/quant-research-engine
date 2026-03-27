#Code starts here
from data.data_loader_yves import load_data_yves
from strategy.sma_strategy import SMAStrategy
from backtester.backtester import Backtester
from performance.analyzer import PerformanceAnalyzer

data = load_data_yves('EUR=', '2010-1-1', '2020-12-31')
strategy = SMAStrategy(42, 252)
bt = Backtester(data, strategy)

data = bt.run()

print(data.head())

perf = PerformanceAnalyzer(data)

summary = perf.summary()

for key, value in summary.items():
    print(key, value, sep=': ')
