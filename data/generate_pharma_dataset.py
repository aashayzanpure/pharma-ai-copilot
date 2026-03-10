import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

hcp_ids = np.arange(100000, 100000+n)

specialties = [
    "Cardiology",
    "Oncology",
    "Endocrinology",
    "General Physician",
    "Pulmonology"
]

regions = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

drugs = [
    "DrugA",
    "DrugB",
    "DrugC"
]

payer_type = [
    "Commercial",
    "Medicare",
    "Medicaid"
]

access = [
    "High",
    "Medium",
    "Low"
]

months = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

data = {
    
    "hcp_id": np.random.choice(hcp_ids, n),
    
    "specialty": np.random.choice(specialties, n),
    
    "region": np.random.choice(regions, n),
    
    "drug": np.random.choice(drugs, n),
    
    "month": np.random.choice(months, n),
    
    "trx": np.random.randint(5, 200, n),  # prescriptions
    
    "nrx": np.random.randint(1, 80, n),   # new prescriptions
    
    "rep_calls": np.random.randint(0, 12, n),
    
    "emails_sent": np.random.randint(0, 8, n),
    
    "payer_type": np.random.choice(payer_type, n),
    
    "access_level": np.random.choice(access, n),
    
    "sales_rep_id": np.random.randint(1000, 1100, n)
}

df = pd.DataFrame(data)

df.to_csv("pharma_sales.csv", index=False)

print("Dataset generated successfully!")
print(df.head())