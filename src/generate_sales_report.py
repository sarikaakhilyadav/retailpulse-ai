from pathlib import Path
import pandas as pd

from sales_kpis import calculate_sales_kpis


DATASET_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "online_retail_II.xlsx"
)


def generate_sales_report():
    if not DATASET_PATH.exists():
        print(f"Dataset not found: {DATASET_PATH}")
        print(
            "Download the dataset and place it "
            "in the data folder."
        )
        return

    workbook = pd.ExcelFile(DATASET_PATH)

    for sheet_name in workbook.sheet_names:
        df = pd.read_excel(
            workbook, sheet_name=sheet_name
        )

        # Standardise column names across workbook versions
        df = df.rename(columns={
            "InvoiceNo": "Invoice",
            "UnitPrice": "Price",
        })

        results = calculate_sales_kpis(df)

        print(
            f"\n--- Sales KPI Report: {sheet_name} ---"
        )
        print(
            f"Total Revenue: "
            f"£{results['total_revenue']:,.2f}"
        )
        print(
            f"Units Sold: "
            f"{results['total_units_sold']:,}"
        )
        print(
            f"Transactions: "
            f"{results['total_transactions']:,}"
        )
        print(
            f"Average Order Value: "
            f"£{results['average_order_value']:,.2f}"
        )


if __name__ == "__main__":
    generate_sales_report()
