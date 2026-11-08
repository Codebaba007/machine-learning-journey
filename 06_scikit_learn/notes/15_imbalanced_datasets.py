
from collections import Counter

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    balanced_accuracy_score,
    confusion_matrix
)

from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler

# -----------------------------------
# 1. Create an imbalanced dataset
# -----------------------------------

X, y = make_classification(
    n_samples=1000,
    n_features=6,
    n_informative=4,
    n_redundant=1,
    weights=[0.95, 0.05],
    random_state=42
)

print("Original class distribution:")
print(Counter(y))

# -----------------------------------
# 2. Split before resampling
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
# 3. Scale the features
# -----------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------------
# 4. Random oversampling
# -----------------------------------

oversampler = RandomOverSampler(random_state=42)

X_over, y_over = oversampler.fit_resample(
    X_train_scaled,
    y_train
)

print("\nAfter random oversampling:")
print(Counter(y_over))

# -----------------------------------
# 5. Random undersampling
# -----------------------------------

undersampler = RandomUnderSampler(random_state=42)

X_under, y_under = undersampler.fit_resample(
    X_train_scaled,
    y_train
)

print("\nAfter random undersampling:")
print(Counter(y_under))

# -----------------------------------
# 6. SMOTE
# -----------------------------------

smote = SMOTE(random_state=42)

X_smote, y_smote = smote.fit_resample(
    X_train_scaled,
    y_train
)

print("\nAfter SMOTE:")
print(Counter(y_smote))

# -----------------------------------
# 7. Evaluate an example prediction
# -----------------------------------

y_true = [0, 0, 0, 0, 1, 1]
y_pred = [0, 0, 0, 1, 0, 1]

print("\nConfusion matrix:")
print(confusion_matrix(y_true, y_pred))

print("\nAccuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1-score:", f1_score(y_true, y_pred))
print("Balanced accuracy:", balanced_accuracy_score(y_true, y_pred))
