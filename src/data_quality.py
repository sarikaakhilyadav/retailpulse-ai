import pandas as pd


def count_missing_values(df: pd.DataFrame) -> pd.Series:
    """Count missing values in each column."""
    return df.isna().sum()


def count_duplicate_rows(df: pd.DataFrame) -> int:
    """Count fully duplicated rows."""
    return int(df.duplicated().sum())


def count_non_positive_values(
    df: pd.DataFrame, column: str
) -> int:
    """Count values that are zero or negative."""
    if column not in df.columns:
        raise ValueError(f"Missing column: {column}")

    values = pd.to_numeric(
        df[column], errors="coerce"
    )
    return int((values <= 0).sum())


def count_cancellations(
    df: pd.DataFrame, column: str
) -> int:
    """Count invoice identifiers beginning with C."""
    if column not in df.columns:
        raise ValueError(f"Missing column: {column}")

    return int(
        df[column]
        .astype("string")
        .str.startswith("C", na=False)
        .sum()
    )
