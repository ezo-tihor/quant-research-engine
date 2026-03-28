import numpy as np
import pandas as pd

class Backtester:

    def __init__(self, data, strategy, cost = 0.001):
        
        self.data = data
        self.strategy = strategy
        self.cost = cost
        self.results = None

    def run1(self):
        
        data = self.data.copy()

        # Compute return (log)
        data['returns'] = np.log(data['price'] / data['price'].shift(1))

        # Generate signals
        data['position'] = self.strategy.generate_signals(data)

        # Strategy returns
        data['strategy'] = data['position'].shift(1) * data['return']

        # Transaction costs
        data['trades'] = data['position'].diff().abs()
        data['strategy'] = data['strategy'] - data['trades'] * self.cost

        # Drop NaNs
        data.dropna(inplace=True)

        # Equity curves
        data['cum_return'] = np.exp(data['returns'].cumsum())
        data['cum_strategy'] = np.exp(data['strategy'].cumsum())

        # Drawdown
        data['cum_max'] = data['cum_strategy'].cummax()
        data['drawdown'] = data['cum_strategy']/(data['cum_strategy'].cummax()) - 1

        self.results = data

        return data


    def run(self):
        print('oze')
        prices = self.data.copy()
        # Simple returns for all the assets
        returns = prices.pct_change().fillna(0)
        # print(type(returns))
        # print(returns.head())

        # Signals (DataFrame now)
        signals = self.strategy.generate_signals(prices)

        # print('Signals')
        # print(signals.head())   

        # Positions (to be taken based on our signals. Shift(1) because they'll be applied in the future)
        positions = signals.shift(1).fillna(0)

        # print('Positions')
        # print(positions.head())

        # Strategy returns (per asset)
        strategy_returns = positions * returns
        # print('Strategy returns')
        # print(strategy_returns.head())

        # Transaction costs
        # print("positions diff")
        # print(positions.diff().head())
        trades = positions.diff().abs()
        costs = trades * self.cost
        # print('Trades')
        # print(trades.head())
        # print(costs.head())

        strategy_returns = strategy_returns - costs

        # Portfolio Aggregation. axis=1 as the index will be fixed and we take sum of returns across all assets
        portfolio_returns = strategy_returns.sum(axis=1)

        # print('Portfolio returns')
        # print(portfolio_returns.head())

        # Equity Curve
        cum_strategy = (1 + portfolio_returns).cumprod()
        # print('Cum Strategy')
        # print(cum_strategy.head())

        # Drawdown
        cum_max = cum_strategy.cummax()
        # print('cum_max')
        # print(cum_max)
        drawdown = cum_strategy/cum_max - 1
        # print('drawdown')
        # print(drawdown)

        self.results = {
            'returns' : returns,
            'signals' : signals,
            'positions' : positions,
            'strategy_returns' : strategy_returns,
            'portfolio_returns' : portfolio_returns,
            'cum_strategy' : cum_strategy,
            'drawdown' : drawdown
        }

        self.results = self.results
        
        return self.results