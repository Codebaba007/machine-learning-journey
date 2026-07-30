import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from typing import List, Union, Any

def handle_missing_values(df: pd.DataFrame, strategy: str = 'mean') -> pd.DataFrame:
    """Handle missing values in a dataframe."""
    imputer = SimpleImputer(strategy=strategy)
    return pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

def encode_categorical(df: pd.DataFrame, columns: List[str], method: str = 'onehot') -> pd.DataFrame:
    """Encode categorical columns."""
    df_encoded = df.copy()
    if method == 'onehot':
        df_encoded = pd.get_dummies(df_encoded, columns=columns)
    elif method == 'label':
        le = LabelEncoder()
        for col in columns:
            df_encoded[col] = le.fit_transform(df_encoded[col])
    return df_encoded

def scale_features(X: Union[pd.DataFrame, np.ndarray], method: str = 'standard') -> Any:
    """Scale features."""
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'robust':
        scaler = RobustScaler()
    else:
        raise ValueError(f"Unknown scaling method: {method}")
    
    return scaler.fit_transform(X)

def remove_outliers(df: pd.DataFrame, columns: List[str], method: str = 'iqr') -> pd.DataFrame:
    """Remove outliers from specified columns."""
    df_clean = df.copy()
    for col in columns:
        if method == 'iqr':
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
        elif method == 'zscore':
            z_scores = np.abs((df_clean[col] - df_clean[col].mean()) / df_clean[col].std())
            df_clean = df_clean[z_scores < 3]
    return df_clean

def create_preprocessing_pipeline() -> Pipeline:
    """Create a standard preprocessing pipeline."""
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    return pipeline
