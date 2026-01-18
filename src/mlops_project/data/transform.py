# src/mlops_project/data/transform.py
import numpy as np
import pandas as pd
from mlops_project.core.logger import get_logger

logger = get_logger(__name__)

def transform_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply feature transformations to validated data.
    This function must be pure (no I/O).
    """
    logger.info("Starting feature transformations")

    df = df.copy()

    # Example transformations
    df["age_scaled"] = df["age"] / 100.0
    df["income_log"] = (df["income"] + 1).apply(lambda x: float(np.log(x)))

    features = df[["age_scaled", "income_log", "target"]]

    logger.info("Feature transformation completed")
    return features
