from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_ROOT / "data" / "sample_retail.xlsx"


def generate_sample_data():
    transactions = [
        {
            "Invoice": "1001",
            "StockCode": "P001",
            "Description": "Notebook",
            "Quantity": 3,
            "InvoiceDate": "2026-01-05",
            "Price": 5.00,
            "Customer ID": 101,
            "Country": "United Kingdom",
        },
        {
            "Invoice": "1002",
            "StockCode": "P002",
            "Description": "Pen Set",
            "Quantity": 2,
            "InvoiceDate": "2026-01-06",
            "Price": 8.50,
            "Customer ID": 102,
            "Country": "United Kingdom",
        },
        {
            "Invoice": "1003",
            "StockCode": "P003",
            "Description": "Desk Lamp",
            "Quantity": 1,
            "InvoiceDate": "2026-01-07",
            "Price": 25.00,
            "Customer ID": 103,
            "Country": "France",
        },
        {
            "Invoice": "C1004",
            "StockCode": "P001",
            "Description": "Notebook",
            "Quantity": -1,
            "InvoiceDate": "2026-01-08",
            "Price": 5.00,
            "Customer ID": 101,
            "Country": "United Kingdom",
        },
        {
            "Invoice": "1005",
            "StockCode": "P004",
            "Description": "Water Bottle",
            "Quantity": 4,
            "InvoiceDate": "2026-01-09",
            "Price": 12.00,
            "Customer ID": 104,
            "Country": "Germany",
        },
    ]

    df = pd.DataFrame(transactions)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    OUTPUT_PATH.parent.mkdir(
        parents=True, exist_ok=True
    )
    df.to_excel(OUTPUT_PATH, index=False)

    print(f"Sample dataset created: {OUTPUT_PATH}")
    print(f"Total records: {len(df)}")


if __name__ == "__main__":
    generate_sample_data()
