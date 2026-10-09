import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = pd.DataFrame({
    "hours_studied": [
        1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 5, 7
    ],
    "practice_tests": [
        1, 1, 2, 2, 3, 3, 4, 4, 2, 3, 4, 5
    ],
    "exam_score": [
        35, 40, 48, 53, 62, 68, 77, 85, 45, 59, 67, 82
    ]
})

X = data[["hours_studied", "practice_tests"]]
y = data["exam_score"]

print("Dataset shape:", data.shape)
print("X shape:", X.shape)
print("y shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=7
)

print("\nTraining observations:", len(X_train))
print("Testing observations:", len(X_test))

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results = pd.DataFrame({
    "Actual Score": y_test.to_numpy(),
    "Predicted Score": predictions
})

print("\nPredictions")
print(results.round(2))

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2))


