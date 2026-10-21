
import numpy as np

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV
)
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

X = np.arange(1, 41).reshape(-1, 1)

rng = np.random.default_rng(42)
noise = rng.normal(0, 5, size=40)
y = 4 * X.ravel() + noise

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Part 1: Cross-validation for one model

model = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="neg_mean_absolute_error"
)

mae_scores = -scores

print("Cross-validation MAE scores:")
print(mae_scores)

print("Average CV MAE:", round(mae_scores.mean(), 2))

# Part 2: Search different hyperparameters

param_grid = {
    "max_depth": [1, 2, 3, 5, 10, None]
}

search = GridSearchCV(
    estimator=DecisionTreeRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="neg_mean_absolute_error"
)

search.fit(X_train, y_train)

print("\nBest hyperparameters:")
print(search.best_params_)

print("Best CV MAE:", round(-search.best_score_, 2))

# Part 3: Final evaluation on held-out test data

best_model = search.best_estimator_

test_predictions = best_model.predict(X_test)
test_mae = mean_absolute_error(y_test, test_predictions)

print("Final test MAE:", round(test_mae, 2))
