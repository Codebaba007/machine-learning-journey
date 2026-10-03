import numpy as np
from scipy import stats


# Exercise 1
# Test whether the average delivery time is different from 30 minutes.

delivery_times = np.array([
    28, 31, 35, 29, 32,
    27, 34, 30, 33, 31
])

hypothesized_mean = 30

t_statistic, p_value = stats.ttest_1samp(
    delivery_times,
    hypothesized_mean
)

print("Exercise 1")
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# Exercise 2
# Compare the average scores of two independent classes.

class_a = np.array([
    72, 75, 78, 70, 74,
    77, 73, 76, 71, 79
])

class_b = np.array([
    81, 84, 79, 85, 82,
    80, 83, 86, 78, 84
])

t_statistic, p_value = stats.ttest_ind(
    class_a,
    class_b
)

print("\nExercise 2")
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# Exercise 3
# Test whether scores changed after training.

before_training = np.array([
    55, 62, 68, 71, 64,
    70, 59, 66, 63, 60
])

after_training = np.array([
    61, 68, 72, 76, 70,
    75, 65, 71, 69, 67
])

t_statistic, p_value = stats.ttest_rel(
    before_training,
    after_training
)

print("\nExercise 3")
print("T-statistic:", t_statistic)
print("P-value:", p_value)