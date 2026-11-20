
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "online_retail_II.xlsx"


def generate_missing_data_report(dataset_path=DATASET_PATH):
    if not Path(dataset_path).exists():
        print("Dataset not found.")
        return

    workbook = pd.ExcelFile(dataset_path)

    for sheet_name in workbook.sheet_names:
        df = pd.read_excel(workbook, sheet_name=sheet_name)

        print(f"\nMissing Data Report: {sheet_name}")
        print("-" * 40)

        report = pd.DataFrame({
            "Missing Count": df.isnull().sum(),
            "Missing Percentage": (
                df.isnull().mean() * 100
            ).round(2),
        })

        print(report)


if __name__ == "__main__":
    generate_missing_data_report()
  
