# 🧠 GenAI Pharma Analytics Copilot (PoC)

A proof-of-concept GenAI-powered analytics assistant that allows users to ask natural language questions about pharma commercial data and receive data-driven, business-ready insights.

---

## 🚀 Overview

Pharma commercial teams frequently rely on dashboards and analysts to answer questions like:

- Which HCPs are driving the most prescriptions?
- Are field force calls aligned with opportunity?
- Which regions are underperforming for a given drug?

This project explores how LLMs can act as a copilot to:

→ Understand business questions  
→ Select the right analytics workflow  
→ Execute data analysis  
→ Translate outputs into decision-ready insights  

---

## 🏗️ System Architecture

```
User Question
     ↓
LLM (Intent + Tool Selection)
     ↓
Analytics Engine (Python functions)
     ↓
LLM (Insight Generation)
     ↓
Business-Friendly Answer
```

---

## ⚙️ Key Features

### 💬 Natural Language Interface
Ask business questions conversationally (no SQL or dashboards needed)

### 🧠 LLM Tool Calling
Dynamically selects the appropriate analytics function based on user intent

### 📊 Pharma Analytics Engine
Supports key commercial use cases:

- Drug performance analysis
- HCP segmentation (top prescribers)
- Call gap analysis
- Specialty performance
- Regional underperformance

### 🔍 Parameterized Queries
Extracts inputs like drug names from user queries  
(e.g., “Show underperforming regions for Drug_A”)

### 📈 Business Insight Generation
Converts raw outputs into clear, actionable explanations for stakeholders

### 🖥️ Interactive UI (Streamlit)
Simple interface for real-time interaction

---

## 🧪 Dataset

A synthetic pharma commercial dataset (~1000 rows) was generated to simulate:

- Regional prescription variation  
- HCP-level prescribing behavior  
- Drug-level performance differences  
- Field force call activity  

This enables realistic experimentation with analytics + GenAI workflows.

---

## 🛠️ Tech Stack

- Python  
- OpenAI API (LLMs)  
- Pandas (data analysis)  
- Streamlit (UI)  
- dotenv (environment management)  

---

## 📂 Project Structure

```
pharma-analytics-copilot/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── analytics_engine.py
│   └── llm_interface.py
│
├── data/
│   └── pharma_sales_data.csv
│
├── notebook/
│   └── data_exploration.ipynb
│
├── .env
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repo
```
git clone <your-repo-link>
cd pharma-analytics-copilot
```

### 2. Create & activate environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the app
```
streamlit run app/streamlit_app.py
```

---

## 💡 Example Queries

- “Which drugs are performing best?”
- “Who are the top prescribing HCPs?”
- “Show underperforming regions for Drug_A”
- “Are calls aligned with prescription potential?”

---

## 🔍 What This Project Demonstrates

- Applying LLMs to structured business analytics problems  
- Designing tool-calling architectures for real-world use cases  
- Bridging data science + domain-specific decision-making  
- Rapid prototyping of AI copilots for enterprise workflows  

---

## ⚠️ Limitations

- Uses synthetic data (not production-grade)  
- Limited set of predefined analytics functions  
- No persistent memory or multi-step reasoning (yet)  

---

## 🔮 Future Improvements

- Add dynamic dataframe querying (beyond fixed functions)  
- Generate visualizations (charts) alongside insights  
- Enable multi-step reasoning / chained tool calls  
- Integrate real-world pharma datasets  

---

## 🤝 Why This Matters

This project explores how GenAI can augment pharma analytics workflows.

The goal is to move from **static dashboards → conversational intelligence systems**.

---

## 📬 Contact

If you're working on similar problems or exploring GenAI in analytics, feel free to connect!
