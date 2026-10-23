
from hashlib import new

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

X = data[["study_hours", "attendance"]]
y = data["passed"]

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

print("Actual labels:")
print(y_test.to_numpy())

print("Predictions:")
print(predictions)

print("Accuracy:")
print(accuracy_score(y_test, predictions))

new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [80]
})

print("New student prediction:")
print(pipeline.predict(new_student))

print("New student prediction probabilities:")
new_student_proba = pipeline.predict_proba(new_student)
new_student_proba_df = pd.DataFrame(
    new_student_proba,
    columns=["Probability of Not Passing", "Probability of Passing"],
    index=["New Student"]
)
print(new_student_proba_df)
new_student_proba_df = pd.concat([new_student, new_student_proba_df], axis=1)
print("New student prediction probabilities:")
print(new_student_proba)