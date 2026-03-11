import os
from openai import OpenAI
from dotenv import load_dotenv

from src.analytics_engine import (
    drug_performance,
    specialty_performance,
    call_gap_analysis,
    underperforming_regions,
    top_hcps
)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer_question(question):

    q = question.lower()

    if "drug" in q:
        result = drug_performance()

    elif "specialty" in q:
        result = specialty_performance()

    elif "call" in q or "rep" in q:
        result = call_gap_analysis()

    elif "region" in q:
        result = underperforming_regions()

    elif "hcp" in q or "doctor" in q:
        result = top_hcps()

    else:
        return "I couldn't determine the correct pharma analytics query."

    explanation = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a pharma commercial analytics assistant explaining insights to business users."
            },
            {
                "role": "user",
                "content": f"Explain this pharma analytics output in simple business terms:\n{result}"
            }
        ]
    )

    return explanation.choices[0].message.content