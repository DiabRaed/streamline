import streamlit as st
import pandas as pd

# from analysis import generate_summary
from export_report import export_report


COLUMN_MAP = {
    "date": ["order_date", "date", "transaction_date"],
    "country": ["country", "region", "market"],
    "sales": ["sales", "revenue", "amount"],
    "product": ["product", "item", "category"]
}

def find_column(df, possible_names):
    for col in df.columns:
        if col.lower() in possible_names:
            return col
    return None


st.title("Excel Report Automation Tool")
st.markdown("📧 [contact@raeddiab.com](mailto:contact@raeddiab.com)")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    df.columns = [c.strip().lower() for c in df.columns]
    date_col = find_column(df, COLUMN_MAP["date"])
    country_col = find_column(df, COLUMN_MAP["country"])
    sales_col = find_column(df, COLUMN_MAP["sales"])
    product_col = find_column(df, COLUMN_MAP["product"])

    missing = []
    for name, col in {
        "date": date_col,
        "country": country_col,
        "sales": sales_col
    }.items():
        if col is None:
            missing.append(name)

    if missing:
        st.error(f"Missing required columns: {missing}")
        st.stop()
        

    st.write("Detected columns:", {
        "date": date_col,
        "country": country_col,
        "sales": sales_col,
        "product": product_col
    })
    df["date"] = pd.to_datetime(df[date_col])

    summary = {
        "total_sales": df[sales_col].sum(),
        "avg_sales": df[sales_col].mean(),
    }

    by_region = df.groupby(country_col)[sales_col].sum().reset_index()

    by_region_product = df.pivot_table(
        index=country_col,
        columns=product_col,
        values=sales_col,
        aggfunc="sum",
        fill_value=0
    ).reset_index()

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