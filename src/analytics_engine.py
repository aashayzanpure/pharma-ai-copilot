import pandas as pd

def top_hcps(df, top_n=10):
    
    result = (
        df.groupby("hcp_id")["trx"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )
    
    return result

def underperforming_regions(df):
    
    region_trx = (
        df.groupby("region")["trx"]
        .mean()
        .sort_values()
        .reset_index()
    )
    
    return region_trx

def call_gap_analysis(df):
    
    calls = df.groupby("region")["rep_calls"].mean()
    trx = df.groupby("region")["trx"].mean()
    
    result = pd.DataFrame({
        "avg_calls": calls,
        "avg_trx": trx
    }).reset_index()
    
    result["trx_per_call"] = result["avg_trx"] / (result["avg_calls"] + 1)
    
    return result

def specialty_performance(df):
    
    result = (
        df.groupby("specialty")["trx"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )
    
    return result

def drug_performance(df):
    
    result = (
        df.groupby("drug")["trx"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    
    return result