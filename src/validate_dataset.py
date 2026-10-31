from pathlib import Path
import pandas as pd

from data_quality import (
    count_missing_values,
    count_duplicate_rows,
    count_non_positive_values,
    count_cancellations,
)

DATASET_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "online_retail_II.xlsx"
)


def validate_dataset():
    if not DATASET_PATH.exists():
        print(f"Dataset not found: {DATASET_PATH}")
        return

    workbook = pd.ExcelFile(DATASET_PATH)

    for sheet_name in workbook.sheet_names:
        df = pd.read_excel(
            workbook, sheet_name=sheet_name
        )

        print(f"\n--- Validating: {sheet_name} ---")
        print(f"Total records: {len(df)}")

        print("\nMissing values:")
        print(count_missing_values(df))

        print(
            "Duplicate rows:",
            count_duplicate_rows(df)
        )

        if "Quantity" in df.columns:
            print(
                "Non-positive quantities:",
                count_non_positive_values(
                    df, "Quantity"
                )
            )

        price_column = next(
            (col for col in ["Price", "UnitPrice"]
             if col in df.columns),
            None
        )

        if price_column:
            print(
                "Non-positive prices:",
                count_non_positive_values(
                    df, price_column
                )
            )

        invoice_column = next(
            (col for col in ["Invoice", "InvoiceNo"]
             if col in df.columns),
            None
        )

        if invoice_column:
            print(
                "Cancellation records:",
                count_cancellations(
                    df, invoice_column
                )
            )


if __name__ == "__main__":
    validate_dataset()
