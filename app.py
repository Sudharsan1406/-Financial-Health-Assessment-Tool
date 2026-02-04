import streamlit as st
import pandas as pd
import io

from analysis.metrics import calculate_metrics
from analysis.scoring import financial_health_score
from analysis.risks import assess_risks
from ai.insights import generate_insights

st.set_page_config(page_title="Financial Health Tool", layout="wide")

st.title("📊 SME Financial Health Assessment Tool")

file = st.file_uploader(
    "Upload Financial Data (Excel)",
    type=["xlsx"]
)

if file:
    if file.size == 0:
        st.error("Uploaded file is empty")
        st.stop()

    try:
        df = pd.read_excel(file)
    except Exception as e:
        st.error(f"Excel parsing failed: {e}")
        st.stop()
            
    required_cols = {
    "date", "revenue", "expenses", "cash_in", "cash_out", "loan_emi"}

    if not required_cols.issubset(df.columns):
        st.error(f"CSV must contain columns: {required_cols}")
        st.stop()



    metrics = calculate_metrics(df)
    score = financial_health_score(metrics)
    risks = assess_risks(metrics)

    st.metric("Financial Health Score", score)

    col1, col2 = st.columns(2)
    col1.line_chart(df[['revenue', 'expenses']])
    col2.line_chart(df[['cash_in', 'cash_out']])

    st.subheader("⚠️ Risk Assessment")
    for r in risks:
        st.write("- ", r)

    if st.button("Generate AI Insights"):
        insights = generate_insights(metrics, score, risks)
        st.subheader("🤖 AI Financial Insights")
        st.write(insights)
