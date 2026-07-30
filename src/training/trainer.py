import joblib
from dataclasses import dataclass
from typing import Any, Dict
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV
import logging

logger = logging.getLogger(__name__)

@dataclass
class TrainingResult:
    model: Any
    train_score: float
    val_score: float

def train_model(model: Any, X_train: Any, y_train: Any, X_val: Any, y_val: Any) -> TrainingResult:
    """Train a model and evaluate on validation set."""
    logger.info(f"Training {model.__class__.__name__}...")
    model.fit(X_train, y_train)
    train_score = model.score(X_train, y_train)
    val_score = model.score(X_val, y_val)
    logger.info(f"Train score: {train_score:.4f}, Val score: {val_score:.4f}")
    return TrainingResult(model=model, train_score=train_score, val_score=val_score)

def cross_validate_model(model: Any, X: Any, y: Any, cv: int = 5, scoring: str = 'accuracy') -> Any:
    """Perform cross-validation."""
    logger.info(f"Cross-validating {model.__class__.__name__}...")
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    return scores

def hyperparameter_search(model: Any, param_grid: Dict, X: Any, y: Any, method: str = 'grid') -> Any:
    """Perform hyperparameter search."""
    if method == 'grid':
        search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
    elif method == 'random':
        search = RandomizedSearchCV(model, param_grid, cv=5, n_jobs=-1, n_iter=10)
    else:
        raise ValueError(f"Unknown search method: {method}")
    
    logger.info(f"Starting {method} search for {model.__class__.__name__}...")
    search.fit(X, y)
    logger.info(f"Best params: {search.best_params_}")
    return search.best_estimator_

def save_model(model: Any, path: str) -> None:
    """Save model to disk."""
    joblib.dump(model, path)
    logger.info(f"Model saved to {path}")

def load_model(path: str) -> Any:
    """Load model from disk."""
    model = joblib.load(path)
    logger.info(f"Model loaded from {path}")
    return model
