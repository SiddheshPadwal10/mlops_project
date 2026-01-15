# src/mlops_project/data/schema.py
import pandera.pandas as pa
from pandera.pandas import Column, DataFrameSchema, Check

def get_training_schema() -> DataFrameSchema:
    return DataFrameSchema(
        {
            "age": Column(int, Check.between(18, 100), nullable=False),
            "income": Column(float, Check.ge(0), nullable=False),
            "target": Column(int, Check.isin([0, 1]), nullable=False),
        },
        strict=True,
        coerce=True,
    )
