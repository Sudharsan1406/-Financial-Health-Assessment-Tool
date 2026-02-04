def generate_insights(metrics, score, risks):
    insights = []

    if score < 40:
        insights.append(
            "The business is financially weak. Immediate cost control and cash flow stabilization are required."
        )
    elif score < 70:
        insights.append(
            "The business shows moderate financial health but has scope for optimization."
        )
    else:
        insights.append(
            "The business is financially strong with stable growth indicators."
        )

    if "High operating expenses" in risks:
        insights.append("Reduce discretionary spending and renegotiate vendor contracts.")

    if "Negative cash flow risk" in risks:
        insights.append("Improve receivables collection and consider short-term working capital.")

    insights.append("Maintain a minimum 3-month cash buffer for financial resilience.")

    return "\n".join(insights)
