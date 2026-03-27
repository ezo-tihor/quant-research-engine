import numpy as np
import pandas as pd

class Backtester:

    def __init__(self, data, strategy, cost = 0.001):
        
        self.data = data
        self.strategy = strategy
        self.cost = cost
        self.results = None

    def run(self):
        
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


    # def performance(self):

    #     if self.results is None:
    #         raise ValueError("Run the backtest first")
        
    #     data = self.results
        
    #     total_return = data['cum_strategy'].iloc[-1] - 1

    #     sharpe = (np.sqrt(252) * data['strategy'].mean()) / data['strategy'].std()

    #     maxDrawdown = data['drawdown'].min()

    #     return {"Total Return" : round(total_return, 4), "Sharpe" : round(sharpe, 4), "Max Drawdown" : round(maxDrawdown, 4)}


