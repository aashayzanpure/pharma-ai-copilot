import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.llm_interface import answer_question

st.title("Pharma Analytics AI Copilot")

st.write(
    "Ask questions about pharma commercial performance, HCP segmentation, and field force activity."
)

question = st.text_input("Enter your question")

if question:

    result = answer_question(question)

    st.write("### Result")
    st.write(result)