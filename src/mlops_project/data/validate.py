# src/mlops_project/data/validate.py
import pandas as pd
from pandera.errors import SchemaError
from mlops_project.data.schema import get_training_schema
from mlops_project.core.logger import get_logger

logger = get_logger(__name__)

def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    schema = get_training_schema()

    try:
        validated_df = schema.validate(df)
        logger.info("Data validation successful")
        return validated_df
    except SchemaError:
        logger.error("Data validation failed")
        raise
