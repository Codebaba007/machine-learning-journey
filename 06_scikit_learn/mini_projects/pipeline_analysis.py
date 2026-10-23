
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

data = pd.DataFrame({
    "monthly_bill": [
        400, 500, 600, 700, 800, 900, 1000, 1100,
        1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
        450, 650, 750, 950, 1050, 1250, 1450, 1650,
        550, 850, 1150, 1350, 1550, 1750, 600, 1000
    ],
    "complaints": [
        0, 0, 1, 0, 1, 1, 0, 2,
        3, 3, 4, 4, 5, 5, 6, 6,
        0, 1, 1, 2, 2, 3, 4, 5,
        0, 1, 2, 3, 4, 5, 0, 2
    ],
    "churn": [
        0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 1, 1, 1,
        0, 0, 1, 1, 1, 1, 0, 0
    ]
})

X = data[["monthly_bill", "complaints"]]
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

param_grid = {
    "model__C": [0.01, 0.1, 1, 10, 100]
}

search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    return_train_score=True
)

search.fit(X_train, y_train)

cv_results = pd.DataFrame(search.cv_results_)

comparison = pd.DataFrame({
    "C": cv_results["param_model__C"].astype(str),
    "Mean Training Accuracy": cv_results["mean_train_score"],
    "Mean CV Accuracy": cv_results["mean_test_score"]
})

print("Hyperparameter Comparison:")
print(comparison.round(3).to_string(index=False))

best_pipeline = search.best_estimator_
predictions = best_pipeline.predict(X_test)

print("\nBest Hyperparameters:")
print(search.best_params_)

print("\nTest Evaluation:")
print(f"Accuracy:  {accuracy_score(y_test, predictions):.2%}")
print(
    f"Precision: {precision_score(y_test, predictions, zero_division=0):.2%}"
)
print(
    f"Recall:    {recall_score(y_test, predictions, zero_division=0):.2%}"
)
print(f"F1-score:  {f1_score(y_test, predictions, zero_division=0):.2%}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions, labels=[0, 1]))
