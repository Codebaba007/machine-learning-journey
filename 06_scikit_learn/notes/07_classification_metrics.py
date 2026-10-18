
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

actual = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
predicted = [1, 0, 1, 1, 1, 0, 0, 0, 1, 0]

accuracy = accuracy_score(actual, predicted)
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f1 = f1_score(actual, predicted)
matrix = confusion_matrix(actual, predicted, labels=[0, 1])

print("Confusion Matrix:")
print(matrix)

print("\nClassification Metrics:")
print(f"Accuracy:  {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-score:  {f1:.2%}")

print("\nClassification Report:")
print(
    classification_report(
        actual,
        predicted,
        labels=[0, 1],
        target_names=["No Churn", "Churn"],
        zero_division=0
    )
)
