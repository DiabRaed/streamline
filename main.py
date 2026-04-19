#%%
from load_data import load_data
from clean_data import clean_data
from analysis import generate_summary
from export_report import export_report

import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        # running as EXE
        return os.path.dirname(sys.executable)
    else:
        # running as normal python script
        return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_path()

INPUT_FILE = os.path.join(BASE_DIR, "data", "raw_data.xlsx")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "sales_report.xlsx")

def main():
    df = load_data(INPUT_FILE)
    df = clean_data(df)

    summary, by_region_product, by_region = generate_summary(df)

    export_report(summary, by_region_product, by_region, OUTPUT_FILE)
    print("Report generated successfully!")

if __name__ == "__main__":
    main()
# %%
