# tests/data/test_transform.py
import pandas as pd
from mlops_project.data.transform import transform_features

def test_transform_features_output_columns():
    df = pd.DataFrame({
        "age": [25, 40],
        "income": [50000, 100000],
        "target": [1, 0],
    })

    transformed = transform_features(df)

    assert "age_scaled" in transformed.columns
    assert "income_log" in transformed.columns
    assert "target" in transformed.columns
