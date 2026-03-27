import numpy as np
from .strategy import Strategy

class SMAStrategy(Strategy):

    def __init__(self, sma_short, sma_long):
        self.sma_short = sma_short
        self.sma_long = sma_long


    def generate_signals(self, data):

        data = data.copy()

        data['SMA_short'] = data['price'].rolling(self.sma_short).mean()
        data['SMA_long'] = data['price'].rolling(self.sma_long).mean()

        signal = np.where(data['SMA_short'] > data['SMA_long'], 1, -1)
        return signal


        