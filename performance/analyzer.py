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

        self.returns = result.get('returns')
        self.position = result.get('position', None)

        if self.returns is None:
            raise ValueError("Result must contain 'returns'")
        
    def summary(self) -> dict:
        summary = {
            'Total Return': round(total_return(self.returns), 4),
            'Share Ratilio': round(sharpe_ratio(self.returns), 4),
            'Volatility': round(volatility(self.returns), 4),
            'Equity Curve': round(equity_curve(self.returns), 4),
            'Max Drawdown': round(max_drawdown(self.returns), 4),
            "Win Rate": round(win_rate(self.returns), 4)
        }

        summary.update(pnl_stats(self.returns))

        if self.position is not None:
            summary['Turnover'] = round(turnover(self.returns), 4)
            summary['Avg Gross Exposure'] = round(gross_exposure(self.position).mean(), 4)

        return summary



