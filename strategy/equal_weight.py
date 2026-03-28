import pandas as pd
import numpy as np
from .strategy import Strategy

class EqualWeightStrategy(Strategy):
    
    def generate_signals(self, prices):
        
        n_assets = prices.shape[1]
        '''
        What does our strategy do? It gives the signal which assigns equal weights to 
        the assets which we have chosen. We buy or sell the assets (with equal weight) 
        based on the previous return that we have gotten.
        '''
         
        signals = pd.DataFrame(1.0/n_assets, index=prices.index, columns=prices.columns)
        return signals