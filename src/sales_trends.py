import pandas as pd


def calculate_monthly_sales(
    df: pd.DataFrame
) -> pd.DataFrame:
    """Calculate monthly revenue from valid retail sales."""

    required = [
        "Invoice", "InvoiceDate", "Quantity", "Price"
    ]
    missing = [
        col for col in required if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    sales = df.copy()
    sales["InvoiceDate"] = pd.to_datetime(
        sales["InvoiceDate"], errors="coerce"
    )
    sales["Quantity"] = pd.to_numeric(
        sales["Quantity"], errors="coerce"
    )
    sales["Price"] = pd.to_numeric(
        sales["Price"], errors="coerce"
    )

    valid = (
        sales["InvoiceDate"].notna()
        & (sales["Quantity"] > 0)
        & (sales["Price"] > 0)
        & ~sales["Invoice"].astype("string")
        .str.startswith("C", na=False)
    )

    sales = sales.loc[valid].copy()
    sales["Revenue"] = (
        sales["Quantity"] * sales["Price"]
    )
    sales["Month"] = (
        sales["InvoiceDate"].dt.to_period("M")
    )

    monthly = (
        sales.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    monthly["Month"] = (
        monthly["Month"].astype(str)
    )
    monthly = monthly.rename(
        columns={"Revenue": "TotalRevenue"}
    )

    return monthly
