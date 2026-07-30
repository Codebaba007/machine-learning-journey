import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from typing import List, Any

def create_polynomial_features(df: pd.DataFrame, columns: List[str], degree: int = 2) -> pd.DataFrame:
    """Create polynomial features for specified columns."""
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly_features = poly.fit_transform(df[columns])
    feature_names = poly.get_feature_names_out(columns)
    poly_df = pd.DataFrame(poly_features, columns=feature_names, index=df.index)
    return pd.concat([df.drop(columns=columns), poly_df], axis=1)

def create_interaction_features(df: pd.DataFrame, col1: str, col2: str) -> pd.DataFrame:
    """Create interaction feature between two columns."""
    df_new = df.copy()
    df_new[f"{col1}_{col2}_interaction"] = df_new[col1] * df_new[col2]
    return df_new

def bin_continuous(df: pd.DataFrame, column: str, bins: int, labels: List[str] = None) -> pd.DataFrame:
    """Bin continuous variable into discrete intervals."""
    df_new = df.copy()
    df_new[f"{column}_binned"] = pd.cut(df_new[column], bins=bins, labels=labels)
    return df_new

def extract_datetime_features(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Extract datetime features from a datetime column."""
    df_new = df.copy()
    df_new[column] = pd.to_datetime(df_new[column])
    df_new[f"{column}_year"] = df_new[column].dt.year
    df_new[f"{column}_month"] = df_new[column].dt.month
    df_new[f"{column}_day"] = df_new[column].dt.day
    df_new[f"{column}_dayofweek"] = df_new[column].dt.dayofweek
    return df_new

def calculate_feature_importance(model: Any, feature_names: List[str]) -> pd.DataFrame:
    """Calculate and return feature importances if model supports it."""
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        return pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False)
    else:
        raise ValueError("Model does not have feature_importances_ attribute.")
