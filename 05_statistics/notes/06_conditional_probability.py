import numpy as np
import pandas as pd

# 1. Basic conditional probability
probability_both = 30 / 100
probability_python = 60 / 100

conditional_probability = probability_both / probability_python

print("P(JavaScript | Python):", conditional_probability)


# 2. Conditional probability formula
probability_a_and_b = 0.3
probability_b = 0.6

probability_a_given_b = probability_a_and_b / probability_b

print("P(A | B):", probability_a_given_b)


# 3. Conditional probability using a table
data = pd.DataFrame({
    "Python": [True, True, False, False],
    "JavaScript": [True, False, True, False],
    "Count": [30, 30, 10, 30]
})

total_students = data["Count"].sum()

python_students = data.loc[data["Python"], "Count"].sum()

both_students = data.loc[
    data["Python"] & data["JavaScript"], "Count"
].sum()

probability_javascript_given_python = both_students / python_students

print("Total Students:", total_students)
print("Python Students:", python_students)
print("Both Courses:", both_students)
print("P(JavaScript | Python):", probability_javascript_given_python)


# 4. Reverse conditional probability
javascript_students = data.loc[
    data["JavaScript"], "Count"
].sum()

probability_python_given_javascript = both_students / javascript_students

print("P(Python | JavaScript):", probability_python_given_javascript)


# 5. Independent events
probability_python = python_students / total_students
probability_javascript = javascript_students / total_students
probability_both = both_students / total_students

independent = np.isclose(
    probability_javascript_given_python,
    probability_javascript
)

print("P(Python):", probability_python)
print("P(JavaScript):", probability_javascript)
print("P(Both):", probability_both)
print("Independent:", independent)