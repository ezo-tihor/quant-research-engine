class Strategy:
    def generate_signals(self, data):
        '''
        prices: pd.DataFrame (time x Series)
        returns: pd.DataFrame (same shape)
        '''
        raise NotImplementedError("Strategy must implement generate signals")
    