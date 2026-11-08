
from collections import Counter

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    balanced_accuracy_score,
    confusion_matrix,
    classification_report
)

from imblearn.pipeline import Pipeline
from imblearn.over_sampling import RandomOverSampler, SMOTE

# -----------------------------------
# 1. Create synthetic fraud dataset
# -----------------------------------

X, y = make_classification(
    n_samples=2000,
    n_features=8,
    n_informative=5,
    n_redundant=1,
    n_clusters_per_class=2,
    weights=[0.95, 0.05],
    class_sep=1.0,
    random_state=42
)

print("Original class distribution:")
print(Counter(y))

# -----------------------------------
# 2. Split the dataset
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining distribution:")
print(Counter(y_train))

print("\nTesting distribution:")
print(Counter(y_test))

# -----------------------------------
# 3. Create three models
# -----------------------------------

models = {
    "Baseline": Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000))
    ]),

    "Random Oversampling": Pipeline([
        ("scaler", StandardScaler()),
        ("sampler", RandomOverSampler(random_state=42)),
        ("classifier", LogisticRegression(max_iter=1000))
    ]),

    "SMOTE": Pipeline([
        ("scaler", StandardScaler()),
        ("sampler", SMOTE(random_state=42)),
        ("classifier", LogisticRegression(max_iter=1000))
    ])
}

# -----------------------------------
# 4. Train and evaluate each model
# -----------------------------------

results = {}

for name, model in models.items():

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    # Train the model
    model.fit(X_train, y_train)

    # Predict on untouched test data
    predictions = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    balanced_accuracy = balanced_accuracy_score(
        y_test,
        predictions
    )

    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1,
        "Balanced Accuracy": balanced_accuracy
    }

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")
    print(f"Balanced accuracy: {balanced_accuracy:.4f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions,
        zero_division=0
    ))

# -----------------------------------
# 5. Compare all models
# -----------------------------------

print("\n" + "=" * 65)
print("FINAL MODEL COMPARISON")
print("=" * 65)

print(
    f"{'Model':<23}"
    f"{'Precision':<12}"
    f"{'Recall':<12}"
    f"{'F1':<12}"
    f"{'Balanced Acc':<12}"
)

for name, metrics in results.items():
    print(
        f"{name:<23}"
        f"{metrics['Precision']:<12.3f}"
        f"{metrics['Recall']:<12.3f}"
        f"{metrics['F1']:<12.3f}"
        f"{metrics['Balanced Accuracy']:<12.3f}"
    )

# -----------------------------------
# 6. Identify the best F1 score
# -----------------------------------

best_model = max(
    results,
    key=lambda name: results[name]["F1"]
)

print("\nBest model by F1-score:", best_model)
