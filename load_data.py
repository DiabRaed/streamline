import pandas as pd

def load_data(path):
    df = pd.read_excel(path)  # or read_csv
    return df