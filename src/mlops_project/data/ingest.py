# src/mlops_project/data/ingest.py
import pandas as pd
from mlops_project.core.logger import get_logger
from mlops_project.data.validate import validate_dataframe
from mlops_project.data.transform import transform_features

logger = get_logger(__name__)

def load_and_prepare_data(path: str) -> pd.DataFrame:
    logger.info(f"Loading data from {path}")
    df = pd.read_csv(path)

    logger.info("Validating data schema")
    df = validate_dataframe(df)

    logger.info("Transforming features")
    df = transform_features(df)

    logger.info(f"Final dataset shape: {df.shape}")
    return df
