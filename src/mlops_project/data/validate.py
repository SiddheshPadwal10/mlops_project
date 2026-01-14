"""Basic data validation utilities."""

from typing import Tuple, List
import pandas as pd


def validate_data(df: pd.DataFrame) -> Tuple[bool, List[str]]:
    """Perform simple validation checks on a DataFrame.

    Returns a tuple `(is_valid, issues)` where `issues` is a list of human-
    readable problem descriptions.
    """
    issues: List[str] = []

    if df is None:
        issues.append("dataframe is None")
        return False, issues

    if df.empty:
        issues.append("dataframe is empty")

    if df.isnull().values.any():
        issues.append("contains missing values")

    return len(issues) == 0, issues
