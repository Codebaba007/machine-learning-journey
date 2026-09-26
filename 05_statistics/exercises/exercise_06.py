import numpy as np

total_students = 200
python_students = 120
javascript_students = 80
both_students = 50

probability_python = python_students / total_students

probability_javascript_given_python = (
    both_students / python_students
)

probability_python_given_javascript = (
    both_students / javascript_students
)

probability_javascript = javascript_students / total_students

independent = np.isclose(
    probability_javascript_given_python,
    probability_javascript
)

print("P(Python):", probability_python)
print("P(JavaScript | Python):", probability_javascript_given_python)
print("P(Python | JavaScript):", probability_python_given_javascript)
print("Independent:", independent)