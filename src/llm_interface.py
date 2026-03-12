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

tool_map = {
    "drug_performance": drug_performance,
    "specialty_performance": specialty_performance,
    "call_gap_analysis": call_gap_analysis,
    "underperforming_regions": underperforming_regions,
    "top_hcps": top_hcps
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "drug_performance",
            "description": "Analyze prescription performance of drugs",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "specialty_performance",
            "description": "Analyze which medical specialties generate the most prescriptions",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "call_gap_analysis",
            "description": "Analyze whether HCP calls are aligned with prescription potential",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "underperforming_regions",
            "description": "Identify regions with low prescription performance",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "top_hcps",
            "description": "Identify HCPs with the highest prescription volume",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]

def answer_question(question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a pharma commercial analytics assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:

        tool_name = message.tool_calls[0].function.name
        tool_function = tool_map[tool_name]

        result = tool_function()

        explanation = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Explain the pharma analytics insight to a business user."
                },
                {
                    "role": "user",
                    "content": f"User question: {question}\n\nAnalytics output:\n{result}"
                }
            ]
        )

        return explanation.choices[0].message.content

    return "I couldn't determine the correct analysis."