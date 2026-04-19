def generate_summary(df):
    summary = {
        "total_sales": df["sales"].sum(),
        "avg_sales": df["sales"].mean(),
        "top_product": df.groupby("product")["sales"].sum().idxmax(),
    }
    
    by_region = df.groupby("country")["sales"].sum().reset_index()

    by_region_product = df.pivot_table(
        index="country",
        columns="product",
        values="sales",
        aggfunc="sum",
        fill_value=0
    ).reset_index()
    return summary, by_region_product, by_region