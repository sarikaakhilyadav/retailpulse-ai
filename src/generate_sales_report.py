
import argparse
from pathlib import Path

import pandas as pd

from sales_kpis import calculate_sales_kpis
from sales_trends import calculate_monthly_sales


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_DATASET = (
    PROJECT_ROOT / "data" / "online_retail_II.xlsx"
)

DATASET_PATH = DEFAULT_DATASET

OUTPUT_PATH = (
    PROJECT_ROOT / "reports" / "sales_kpi_summary.csv"
)

MONTHLY_OUTPUT_PATH = (
    PROJECT_ROOT / "reports" / "monthly_sales.csv"
)


def generate_sales_report(dataset_path=None):
    source = (
        Path(dataset_path)
        if dataset_path is not None
        else DATASET_PATH
    )

    if not source.exists():
        print(f"Dataset not found: {source}")
        return

    report_rows = []
    monthly_rows = []

    with pd.ExcelFile(source) as workbook:
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

            if "InvoiceDate" in df.columns:
                monthly = calculate_monthly_sales(df)
                monthly["sheet_name"] = sheet_name
                monthly_rows.append(monthly)
            else:
                print(
                    f"Monthly analysis skipped for "
                    f"{sheet_name}: InvoiceDate missing."
                )

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

        print(f"\nKPI report saved to: {OUTPUT_PATH}")

    if monthly_rows:
        MONTHLY_OUTPUT_PATH.parent.mkdir(
            parents=True, exist_ok=True
        )

        pd.concat(
            monthly_rows, ignore_index=True
        ).to_csv(
            MONTHLY_OUTPUT_PATH, index=False
        )

        print(
            f"Monthly report saved to: "
            f"{MONTHLY_OUTPUT_PATH}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate RetailPulse AI sales reports."
    )

    parser.add_argument(
        "--dataset",
        type=Path,
        default=None,
        help="Path to an Excel retail dataset.",
    )

    args = parser.parse_args()
    generate_sales_report(args.dataset)
