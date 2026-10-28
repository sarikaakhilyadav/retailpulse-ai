from pathlib import Path
import pandas as pd

DATASET_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "online_retail_II.xlsx"
)


def validate_dataset():
    if not DATASET_PATH.exists():
        print("Dataset not found.")
        print(f"Expected location: {DATASET_PATH}")
        return

    workbook = pd.ExcelFile(DATASET_PATH)

    for sheet_name in workbook.sheet_names:
        df = pd.read_excel(workbook, sheet_name=sheet_name)

        print(f"\n--- Validating: {sheet_name} ---")
        print(f"Total records: {len(df)}")

        print("\nMissing values:")
        print(df.isnull().sum())

        print(f"\nDuplicate rows: {df.duplicated().sum()}")

        if "Quantity" in df.columns:
            print(
                "Non-positive quantities:",
                (df["Quantity"] <= 0).sum()
            )

        price_column = next(
            (col for col in ["Price", "UnitPrice"]
             if col in df.columns),
            None
        )

        if price_column:
            print(
                "Non-positive prices:",
                (df[price_column] <= 0).sum()
            )

        invoice_column = next(
            (col for col in ["Invoice", "InvoiceNo"]
             if col in df.columns),
            None
        )

        if invoice_column:
            cancellations = (
                df[invoice_column]
                .astype(str)
                .str.startswith("C")
                .sum()
            )
            print(
                "Cancellation records:",
                cancellations
            )


if __name__ == "__main__":
    validate_dataset()
