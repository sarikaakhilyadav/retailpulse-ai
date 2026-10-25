from pathlib import Path
import pandas as pd

# Locate the dataset in the project's data folder.
DATASET_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "online_retail_II.xlsx"
)


def inspect_dataset():
    if not DATASET_PATH.exists():
        print("Dataset not found.")
        print(f"Expected location: {DATASET_PATH}")
        print("Download the dataset before running.")
        return

    workbook = pd.ExcelFile(DATASET_PATH)

    for sheet_name in workbook.sheet_names:
        print(f"\n--- Worksheet: {sheet_name} ---")

        # Read the first 100 rows as a sample.
        data = pd.read_excel(
            workbook,
            sheet_name=sheet_name,
            nrows=100
        )

        print("\nSample shape:")
        print(data.shape)

        print("\nFirst five records:")
        print(data.head())

        print("\nColumn data types:")
        print(data.dtypes)

        print("\nMissing values in sample:")
        print(data.isnull().sum())


if __name__ == "__main__":
    inspect_dataset()
