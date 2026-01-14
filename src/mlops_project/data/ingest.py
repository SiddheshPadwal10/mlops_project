# src/data/ingest.py
import pandas as pd
from mlops_project.core.logger import get_logger

logger = get_logger(__name__)

def load_csv(path: str) -> pd.DataFrame:
    logger.info(f"Loading data from {path}")
    df = pd.read_csv(path)
    logger.info(f"Loaded dataframe with shape {df.shape}")
    return df

