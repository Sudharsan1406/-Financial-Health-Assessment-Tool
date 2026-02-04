def financial_health_score(m):
    score = 0

    score += min(max(m['profit_margin'] * 100, 0), 30)
    score += min(max((m['cash_flow_ratio'] - 1) * 25, 0), 25)
    score += min(max((1 - m['expense_ratio']) * 20, 0), 20)
    score += min(max(m['growth_rate'] * 15, 0), 15)
    score += min(max((1 - m['debt_ratio']) * 10, 0), 10)

    return round(min(score, 100), 2)
