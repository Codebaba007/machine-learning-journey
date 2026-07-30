from dataclasses import dataclass
from typing import Dict, Any, Optional
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, classification_report
import numpy as np

@dataclass
class EvaluationResult:
    metrics: Dict[str, float]

def evaluate_classifier(y_true: Any, y_pred: Any, y_proba: Optional[Any] = None) -> EvaluationResult:
    """Evaluate a classifier."""
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
        'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
        'f1': f1_score(y_true, y_pred, average='weighted', zero_division=0)
    }
    if y_proba is not None:
        try:
            metrics['roc_auc'] = roc_auc_score(y_true, y_proba, multi_class='ovr')
        except ValueError:
            pass # Handle cases where roc_auc cannot be computed
    return EvaluationResult(metrics=metrics)

def evaluate_regressor(y_true: Any, y_pred: Any) -> EvaluationResult:
    """Evaluate a regressor."""
    mse = mean_squared_error(y_true, y_pred)
    metrics = {
        'mse': mse,
        'rmse': np.sqrt(mse),
        'mae': mean_absolute_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred)
    }
    return EvaluationResult(metrics=metrics)

def print_classification_report(y_true: Any, y_pred: Any) -> None:
    """Print the detailed classification report."""
    print(classification_report(y_true, y_pred))
