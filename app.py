import streamlit as st
import pandas as pd

from analysis import generate_summary
from export_report import export_report

st.title("Excel Report Automation Tool")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    df.columns = [c.strip().lower() for c in df.columns]

    summary, by_region_product, by_region = generate_summary(df)

    st.write("Preview:", df.head())

    if st.button("Generate Report"):
        output_path = "report.xlsx"
        export_report(summary, by_region_product, by_region, output_path)

        st.success("Report generated!")

        with open(output_path, "rb") as f:
            st.download_button(
                "Download Report",
                f,
                file_name="sales_report.xlsx"
            )