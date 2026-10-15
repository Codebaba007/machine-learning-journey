import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "study_hours": [
        1, 2, 2, 3, 3, 4, 4, 5,
        5, 6, 6, 7, 7, 8, 8, 9
    ],
    "attendance": [
        40, 50, 45, 55, 60, 55, 65, 60,
        70, 65, 75, 70, 80, 75, 90, 95
    ],
    "passed": [
        0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1
    ]
})

x = data[["study_hours", "attendance"]]
y = data["passed"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = LogisticRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
probabilities = model.predict_proba(x_test)

results = x_test.copy()
results["Actual Passed"] = y_test
results["Predicted Passed"] = predictions
results["Pass Probability"] = probabilities[:, 1]

print(results.round(3))
print(results.to_string(index=False))