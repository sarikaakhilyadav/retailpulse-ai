
import pandas as pd


def calculate_product_performance(df, top_n=10):
    """Return the top products ranked by revenue."""

    required_columns = [
        "Invoice",
        "StockCode",
        "Description",
        "Quantity",
        "Price",
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    sales = df.copy()

    sales["Quantity"] = pd.to_numeric(
        sales["Quantity"], errors="coerce"
    )
    sales["Price"] = pd.to_numeric(
        sales["Price"], errors="coerce"
    )

    valid_sales = (
        (sales["Quantity"] > 0)
        & (sales["Price"] > 0)
        & ~sales["Invoice"].astype(
            "string"
        ).str.startswith("C", na=False)
    )

    sales = sales.loc[valid_sales].copy()

    sales["Revenue"] = (
        sales["Quantity"] * sales["Price"]
    )

    product_summary = (
        sales.groupby(
            ["StockCode", "Description"],
            dropna=False,
        )
        .agg(
            UnitsSold=("Quantity", "sum"),
            TotalRevenue=("Revenue", "sum"),
        )
        .reset_index()
    )

    product_summary = product_summary.sort_values(
        "TotalRevenue", ascending=False
    )

    return product_summary.head(top_n).reset_index(
        drop=True
    )
