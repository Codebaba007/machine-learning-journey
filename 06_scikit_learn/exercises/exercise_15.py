
from collections import Counter

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

from imblearn.over_sampling import SMOTE

# -----------------------------------
# 1. Create an imbalanced dataset
# -----------------------------------

X, y = make_classification(
    n_samples=800,
    n_features=6,
    n_informative=4,
    n_redundant=1,
    weights=[0.90, 0.10],
    random_state=42
)

print("Original distribution:")
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
# 3. Scale the features
# -----------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------------
# 4. Apply SMOTE to training data
# -----------------------------------

smote = SMOTE(random_state=42)

X_resampled, y_resampled = smote.fit_resample(
    X_train_scaled,
    y_train
)

print("\nDistribution after SMOTE:")
print(Counter(y_resampled))

# -----------------------------------
# 5. Train Logistic Regression
# -----------------------------------

model = LogisticRegression(max_iter=1000)

model.fit(X_resampled, y_resampled)

# -----------------------------------
# 6. Predict test data
# -----------------------------------

predictions = model.predict(X_test_scaled)

# -----------------------------------
# 7. Evaluate the model
# -----------------------------------

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))
