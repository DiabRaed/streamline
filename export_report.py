import pandas as pd
from openpyxl.chart import BarChart, Reference

def export_report(summary, by_region_product, by_region, output_path):

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:

        # --- Sheet 1: Summary ---
        pd.DataFrame([summary]).to_excel(writer, sheet_name="Summary", index=False)

        # --- Sheet 2: By Country ---
        by_region.to_excel(writer, sheet_name="By Country", index=False)

        # --- Sheet 3: Country x Product ---
        by_region_product.to_excel(writer, sheet_name="Country_Product", index=False)

        # Get workbook + sheet
        workbook = writer.book
        sheet = writer.sheets["By Country"]

        # --- Create chart ---
        chart = BarChart()
        chart.title = "Sales by Country"
        chart.y_axis.title = "Sales"
        chart.x_axis.title = "Country"

        data = Reference(sheet, min_col=2, min_row=1, max_row=len(by_region)+1)
        categories = Reference(sheet, min_col=1, min_row=2, max_row=len(by_region)+1)

        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)

        # Place chart in Excel
        sheet.add_chart(chart, "E2")