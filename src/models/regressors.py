from dataclasses import dataclass
from typing import Any, Dict, List
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import cross_val_score

@dataclass
class RegressorResult:
    name: str
    model: Any
    cv_mean_score: float
    cv_std_score: float

def get_regressor(name: str) -> Any:
    """Factory function returning sklearn regressors."""
    regressors = {
        'random_forest': RandomForestRegressor(),
        'gradient_boosting': GradientBoostingRegressor(),
        'linear_regression': LinearRegression(),
        'ridge': Ridge(),
        'lasso': Lasso()
    }
    if name not in regressors:
        raise ValueError(f"Regressor {name} not supported.")
    return regressors[name]

def compare_regressors(X: Any, y: Any, regressors: List[str], cv: int = 5) -> List[RegressorResult]:
    """Compare multiple regressors using cross-validation (neg_mean_squared_error)."""
    results = []
    for name in regressors:
        reg = get_regressor(name)
        scores = cross_val_score(reg, X, y, cv=cv, scoring='neg_mean_squared_error')
        results.append(RegressorResult(
            name=name,
            model=reg,
            cv_mean_score=-scores.mean(),  # make it positive MSE
            cv_std_score=scores.std()
        ))
    return sorted(results, key=lambda x: x.cv_mean_score) # Lower MSE is better
