import pandas as pd 

def clean_data(df):
    df.columns = [c.strip().lower() for c in df.columns]

    df = df.dropna(subset=["sales"])  # example column
    df["date"] = pd.to_datetime(df["order_date"])

    return df