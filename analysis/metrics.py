import pandas as pd

def calculate_metrics(df):
    revenue = df['revenue'].sum()
    expenses = df['expenses'].sum()
    cash_in = df['cash_in'].sum()
    cash_out = df['cash_out'].sum()
    loan_emi = df['loan_emi'].sum()

    profit_margin = (revenue - expenses) / revenue
    expense_ratio = expenses / revenue
    cash_flow_ratio = cash_in / cash_out
    debt_ratio = loan_emi / revenue

    growth_rate = (
        df['revenue'].iloc[-1] - df['revenue'].iloc[0]
    ) / df['revenue'].iloc[0]

    return {
        "profit_margin": profit_margin,
        "expense_ratio": expense_ratio,
        "cash_flow_ratio": cash_flow_ratio,
        "debt_ratio": debt_ratio,
        "growth_rate": growth_rate
    }
