
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

data = pd.DataFrame({
    "monthly_bill": [
        400, 500, 600, 700, 800, 900,
        1200, 1300, 1400, 1500, 1600, 1700,
        450, 650, 750, 850, 1250, 1450,
        550, 950, 1150, 1350, 1550, 1650
    ],
    "complaints": [
        0, 0, 1, 0, 1, 1,
        3, 3, 4, 4, 5, 5,
        0, 1, 1, 1, 3, 4,
        0, 2, 2, 3, 5, 5
    ],
    "churn": [
        0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 1, 1,
        0, 0, 1, 1, 1, 1
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

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

print("Predictions:")
print(predictions)

print("\nActual labels:")
print(y_test.to_numpy())

print("\nAccuracy:")
print(accuracy_score(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions, labels=[0, 1]))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        labels=[0, 1],
        target_names=["No Churn", "Churn"],
        zero_division=0
    )
)

new_customer = pd.DataFrame({
    "monthly_bill": [1250],
    "complaints": [3]
})

print("\nNew customer prediction:")
print(pipeline.predict(new_customer))

print(
    "Churn probability:",
    round(pipeline.predict_proba(new_customer)[0, 1], 3)
)

# Tune the model using cross-validation.
param_grid = {
    "model__C": [0.1, 1, 10]
}

search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=3,
    scoring="accuracy"
)

search.fit(X_train, y_train)

print("\nBest hyperparameters:")
print(search.best_params_)

print("Best CV accuracy:", round(search.best_score_, 3))

best_pipeline = search.best_estimator_
print("Tuned model test accuracy:",
      round(best_pipeline.score(X_test, y_test), 3))
