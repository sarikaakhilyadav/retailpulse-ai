import argparse
from pathlib import Path

import pandas as pd

from sales_kpis import calculate_sales_kpis


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATASET = PROJECT_ROOT / "data" / "online_retail_II.xlsx"
OUTPUT_PATH = PROJECT_ROOT / "reports" / "sales_kpi_summary.csv"

# Keep the existing constant for compatibility with tests.
DATASET_PATH = DEFAULT_DATASET


def generate_sales_report(dataset_path=None):
    source = (
        Path(dataset_path)
        if dataset_path is not None
        else DATASET_PATH
    )

    if not source.exists():
        print(f"Dataset not found: {source}")
        return

    workbook = pd.ExcelFile(source)
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

        print(f"\n--- Sales KPI Report: {sheet_name} ---")
        for metric, value in results.items():
            print(f"{metric}: {value}")

    if report_rows:
        OUTPUT_PATH.parent.mkdir(
            parents=True, exist_ok=True
        )
        pd.DataFrame(report_rows).to_csv(
            OUTPUT_PATH, index=False
        )
        print(f"\nReport saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate RetailPulse AI sales KPI reports."
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=None,
        help="Path to an Excel retail dataset.",
    )
    args = parser.parse_args()
    generate_sales_report(args.dataset)
