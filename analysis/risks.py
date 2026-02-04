def assess_risks(m):
    risks = []

    if m['profit_margin'] < 0.1:
        risks.append("Low profitability")
    if m['cash_flow_ratio'] < 1:
        risks.append("Negative cash flow risk")
    if m['expense_ratio'] > 0.7:
        risks.append("High operating expenses")
    if m['debt_ratio'] > 0.4:
        risks.append("High debt burden")

    return risks if risks else ["No major financial risks detected"]
