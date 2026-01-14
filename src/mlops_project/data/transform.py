"""Data transformation helpers."""

import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply minimal transformations and return a new DataFrame.

    Current transforms:
    - Strip whitespace from string column names.
    - Return a copy so callers don't mutate the original unintentionally.
    """
    if df is None:
        raise ValueError("df must be a pandas DataFrame")

    out = df.copy()
    out.columns = [c.strip() if isinstance(c, str) else c for c in out.columns]
    return out
