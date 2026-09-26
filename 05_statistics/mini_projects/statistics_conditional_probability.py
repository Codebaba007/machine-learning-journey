import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Student": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kevin", "Liam", "Mia", "Noah", "Olivia",
        "Paul", "Quinn", "Ryan", "Sophia", "Tom"
    ],
    "Python": [
        True, True, True, True, True,
        True, True, True, True, True,
        True, True, False, False, False,
        False, False, False, False, False
    ],
    "JavaScript": [
        True, True, True, True, True,
        False, False, False, False, False,
        False, False, True, True, True,
        True, True, True, False, False
    ]
})

total_students = len(data)

python_students = data["Python"].sum()
javascript_students = data["JavaScript"].sum()

both_students = (
    data["Python"] & data["JavaScript"]
).sum()

probability_python = python_students / total_students
probability_javascript = javascript_students / total_students
probability_both = both_students / total_students

probability_javascript_given_python = (
    both_students / python_students
)

probability_python_given_javascript = (
    both_students / javascript_students
)

independent = np.isclose(
    probability_javascript_given_python,
    probability_javascript
)

print("Student Course Probability Analysis")
print("Total Students:", total_students)
print("Python Students:", python_students)
print("JavaScript Students:", javascript_students)
print("Students Studying Both:", both_students)

print("\nProbabilities")
print("P(Python):", probability_python)
print("P(JavaScript):", probability_javascript)
print("P(Python and JavaScript):", probability_both)

print("\nConditional Probabilities")
print(
    "P(JavaScript | Python):",
    probability_javascript_given_python
)
print(
    "P(Python | JavaScript):",
    probability_python_given_javascript
)

print("\nAre the Events Independent?", independent)