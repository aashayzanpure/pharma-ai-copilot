import pandas as pd
from src.analytics_engine import (
    top_hcps,
    underperforming_regions,
    call_gap_analysis,
    specialty_performance,
    drug_performance
)

df = pd.read_csv("data/pharma_sales.csv")


def answer_question(question):

    question = question.lower()

    if "top hcp" in question or "top doctors" in question:
        result = top_hcps(df)

    elif "underperforming region" in question:
        result = underperforming_regions(df)

    elif "call gap" in question or "rep activity" in question:
        result = call_gap_analysis(df)

    elif "specialty" in question:
        result = specialty_performance(df)

    elif "drug performance" in question:
        result = drug_performance(df)

    else:
        return "Sorry, I cannot answer that question yet."

    return result