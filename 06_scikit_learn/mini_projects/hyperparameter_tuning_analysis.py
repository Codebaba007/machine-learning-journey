
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Generate illustrative data

X = np.arange(1, 61).reshape(-1, 1)

rng = np.random.default_rng(42)
noise = rng.normal(0, 8, size=60)
y = 6 * X.ravel() + noise

# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Define candidate hyperparameters

param_grid = {
    "max_depth": [1, 2, 3, 4, 5, 8, 12, None]
}

# Search using cross-validation

search = GridSearchCV(
    estimator=DecisionTreeRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="neg_mean_absolute_error",
    return_train_score=True
)

search.fit(X_train, y_train)

# Summarize cross-validation results

cv_results = pd.DataFrame(search.cv_results_)

results = pd.DataFrame({
    "Max Depth": cv_results["param_max_depth"].astype(str),
    "Mean Training MAE": -cv_results["mean_train_score"],
    "Mean CV MAE": -cv_results["mean_test_score"]
})

results["Mean Training MAE"] = results["Mean Training MAE"].round(2)
results["Mean CV MAE"] = results["Mean CV MAE"].round(2)

print("Hyperparameter Comparison")
print(results.to_string(index=False))

# Evaluate the selected model on held-out test data

best_model = search.best_estimator_

test_predictions = best_model.predict(X_test)
test_mae = mean_absolute_error(y_test, test_predictions)

print("\nBest hyperparameters:")
print(search.best_params_)

print("Best mean CV MAE:", round(-search.best_score_, 2))
print("Final test MAE:", round(test_mae, 2))
