import pandas as pd


def calculate_sales_kpis(df: pd.DataFrame) -> dict:
    """Calculate basic sales KPIs from retail transactions."""

    required_columns = [
        "Invoice",
        "Quantity",
        "Price"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )

    sales = df.copy()

    sales["Quantity"] = pd.to_numeric(
        sales["Quantity"], errors="coerce"
    )
    sales["Price"] = pd.to_numeric(
        sales["Price"], errors="coerce"
    )

    # Only include valid positive sales
    sales = sales[
        (sales["Quantity"] > 0)
        & (sales["Price"] > 0)
        & (~sales["Invoice"].astype("string").str.startswith("C", na=False))
    ].copy()

    sales["Revenue"] = (
        sales["Quantity"] * sales["Price"]
    )

    total_revenue = sales["Revenue"].sum()
    total_units = sales["Quantity"].sum()
    total_transactions = sales["Invoice"].nunique()

    average_order_value = (
        total_revenue / total_transactions
        if total_transactions > 0 else 0
    )

    return {
        "total_revenue": round(
            float(total_revenue), 2
        ),
        "total_units_sold": int(total_units),
        "total_transactions": int(total_transactions),
        "average_order_value": round(
            float(average_order_value), 2
        ),
  }
