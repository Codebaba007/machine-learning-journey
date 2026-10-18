
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

data = pd.DataFrame({
    "monthly_bill": [
        400, 500, 600, 700, 800, 900, 1000, 1100,
        1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
        450, 650, 750, 950, 1050, 1250, 1450, 1650
    ],
    "complaints": [
        0, 0, 1, 0, 1, 1, 0, 2,
        3, 3, 4, 4, 5, 5, 6, 6,
        0, 1, 1, 2, 2, 3, 4, 5
    ],
    "churn": [
        0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 1, 1, 1
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

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(
    y_test, predictions, zero_division=0
)
recall = recall_score(
    y_test, predictions, zero_division=0
)
f1 = f1_score(
    y_test, predictions, zero_division=0
)
matrix = confusion_matrix(
    y_test, predictions, labels=[0, 1]
)

results = X_test.copy()
results["Actual Churn"] = y_test
results["Predicted Churn"] = predictions
results["Correct"] = (
    results["Actual Churn"] == results["Predicted Churn"]
)

print("Test Predictions:")
print(results.to_string(index=False))

print("\nConfusion Matrix:")
print(matrix)

print("\nEvaluation Metrics:")
print(f"Accuracy:  {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-score:  {f1:.2%}")

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
