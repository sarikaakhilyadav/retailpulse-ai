from pathlib import Path
import pandas as pd

from sales_kpis import calculate_sales_kpis


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "online_retail_II.xlsx"
OUTPUT_PATH = PROJECT_ROOT / "reports" / "sales_kpi_summary.csv"


def generate_sales_report():
    if not DATASET_PATH.exists():
        print(f"Dataset not found: {DATASET_PATH}")
        return

    workbook = pd.ExcelFile(DATASET_PATH)
    report_rows = []

    for sheet_name in workbook.sheet_names:
        df = pd.read_excel(
            workbook, sheet_name=sheet_name
        )

        df = df.rename(columns={
            "InvoiceNo": "Invoice",
            "UnitPrice": "Price",
        })

        results = calculate_sales_kpis(df)
        results["sheet_name"] = sheet_name
        report_rows.append(results)

        print(
            f"\n--- Sales KPI Report: {sheet_name} ---"
        )

        for metric, value in results.items():
            print(f"{metric}: {value}")

    if report_rows:
        OUTPUT_PATH.parent.mkdir(
            parents=True, exist_ok=True
        )

        report_df = pd.DataFrame(report_rows)
        report_df.to_csv(
            OUTPUT_PATH, index=False
        )

        print(
            f"\nReport saved to: {OUTPUT_PATH}"
        )


if __name__ == "__main__":
    generate_sales_report()
