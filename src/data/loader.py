import pandas as pd
from typing import Tuple, Any, Optional
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from sklearn import datasets

@dataclass
class DatasetInfo:
    name: str
    num_samples: int
    num_features: int
    target_names: Optional[list] = None

def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file with basic validation."""
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"The CSV file at {path} is empty.")
    return df

def load_dataset(name: str) -> Tuple[Any, Any, DatasetInfo]:
    """Load a common dataset (e.g., iris, boston)."""
    if name == 'iris':
        data = datasets.load_iris()
    elif name == 'wine':
        data = datasets.load_wine()
    elif name == 'breast_cancer':
        data = datasets.load_breast_cancer()
    else:
        raise ValueError(f"Dataset {name} not found.")
    
    info = DatasetInfo(
        name=name,
        num_samples=data.data.shape[0],
        num_features=data.data.shape[1],
        target_names=list(data.target_names) if hasattr(data, 'target_names') else None
    )
    return data.data, data.target, info

def split_data(X: Any, y: Any, test_size: float = 0.2, random_state: int = 42) -> Tuple[Any, Any, Any, Any]:
    """Wrapper around train_test_split."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
