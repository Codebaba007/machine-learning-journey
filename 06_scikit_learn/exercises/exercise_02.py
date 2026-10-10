import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


data = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 6, 7],
    "previous_score": [35, 40, 48, 52, 60, 65, 75, 82, 45, 58, 70, 78],
    "final_score": [38, 43, 50, 55, 63, 69, 79, 86, 47, 61, 74, 82]
})

X = data[["hours_studied", "previous_score"]]
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X.columns,
    index=X_train.index
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=X.columns,
    index=X_test.index
)

print("Original Training Features")
print(X_train)

print("\nScaled Training Features")
print(X_train_scaled.round(3))

print("\nScaled Test Features")
print(X_test_scaled.round(3))

print("\nTraining Shape:", X_train_scaled.shape)
print("Testing Shape:", X_test_scaled.shape)

print("\nTarget Values Remain Unchanged")
print(y_train.head())

print("\nTraining Means After Scaling")
print(X_train_scaled.mean().round(6))

print("\nTraining Standard Deviations After Scaling")
print(X_train_scaled.std(ddof=0).round(6))