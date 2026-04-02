from .metrics import(equity_curve, total_return,
    sharpe_ratio,
    volatility, 
    max_drawdown,
    win_rate,
    pnl_stats,
    turnover,
    gross_exposure)

class PerformanceAnalyzer:
    def __init__(self, result: dict):
        """
        
        """

        self.returns = result.get('portfolio_returns')
        self.position = result.get('positions', None)

        if self.returns is None:
            raise ValueError("Result must contain ' portfolio_returns'")
        
    def summary(self) -> dict:
        summary = {
            'Total Return': round(total_return(self.returns), 4),
            'Share Ratio': round(sharpe_ratio(self.returns), 4),
            'Volatility': round(volatility(self.returns), 4),
            'Max Drawdown': round(max_drawdown(self.returns), 4),
            "Win Rate": round(win_rate(self.returns), 4),
            'Final Equity': round(equity_curve(self.returns).iloc[-1], 4)

        }

        summary.update(pnl_stats(self.returns))

        if self.position is not None:
            summary['Turnover'] = round(turnover(self.position), 4)
            summary['Avg Gross Exposure'] = round(gross_exposure(self.position).mean(), 4)

        return summary



