import pandas as pd
import os

DATA_PATH = os.path.join("data", "pharma_sales.csv")
df = pd.read_csv(DATA_PATH)


def drug_performance():
    result = (
        df.groupby("drug")["trx"]
        .sum()
        .sort_values(ascending=False)
    )
    return result.to_string()


def specialty_performance():
    result = (
        df.groupby("specialty")["trx"]
        .sum()
        .sort_values(ascending=False)
    )
    return result.to_string()


def call_gap_analysis():
    result = (
        df.groupby("hcp_id")[["calls", "trx"]]
        .sum()
    )
    
    result["trx_per_call"] = result["trx"] / result["calls"]
    result = result.sort_values("trx_per_call", ascending=False).head(10)

    return result.to_string()


def underperforming_regions():
    result = (
        df.groupby("region")["trx"]
        .sum()
        .sort_values()
        .head(5)
    )
    return result.to_string()


def top_hcps():
    result = (
        df.groupby("hcp_id")["trx"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    return result.to_string()