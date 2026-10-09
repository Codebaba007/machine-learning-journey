import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = pd.DataFrame({
    "hours_studied": [
        1, 2, 3, 4, 5, 6, 7, 8, 2, 3,
        4, 5, 6, 7, 8, 1, 2, 3, 4, 6
    ],
    "previous_score": [
        35, 40, 45, 50, 55, 60, 65, 70, 55, 60,
        65, 70, 75, 80, 85, 50, 60, 70, 75, 85
    ],
    "final_score": [
        38, 44, 50, 56, 62, 68, 74, 80, 50, 54,
        60, 66, 72, 78, 84, 44, 50, 57, 62, 77
    ]
})

X = data[["hours_studied", "previous_score"]]
y = data["final_score"]

print("Dataset shape:", data.shape)
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining feature shape:", X_train.shape)
print("Testing feature shape:", X_test.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)

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