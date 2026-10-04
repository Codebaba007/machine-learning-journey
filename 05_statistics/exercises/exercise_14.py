import numpy as np
from scipy import stats


# Exercise 1
# Compare three teaching methods.

method_a = np.array([
    72, 75, 70, 74, 73,
    71, 76, 72, 74, 70
])

method_b = np.array([
    78, 80, 82, 79, 81,
    77, 83, 80, 79, 82
])

method_c = np.array([
    74, 76, 73, 75, 77,
    72, 78, 74, 76, 75
])

f_statistic, p_value = stats.f_oneway(
    method_a,
    method_b,
    method_c
)

print("Exercise 1")
print("F-statistic:", f_statistic)
print("P-value:", p_value)


# Exercise 2
# Compare three training programs.

program_a = np.array([
    60, 62, 61, 63, 59,
    64, 60, 62
])

program_b = np.array([
    70, 72, 71, 69, 73,
    74, 70, 72
])

program_c = np.array([
    61, 64, 60, 62, 63,
    65, 61, 62
])

f_statistic, p_value = stats.f_oneway(
    program_a,
    program_b,
    program_c
)

print("\nExercise 2")
print("F-statistic:", f_statistic)
print("P-value:", p_value)


# Exercise 3
# Determine whether four groups have different means.

group_1 = np.array([50, 52, 49, 51, 53])
group_2 = np.array([51, 50, 52, 49, 53])
group_3 = np.array([70, 72, 69, 71, 73])
group_4 = np.array([50, 54, 51, 52, 49])

f_statistic, p_value = stats.f_oneway(
    group_1,
    group_2,
    group_3,
    group_4
)

print("\nExercise 3")
print("F-statistic:", f_statistic)
print("P-value:", p_value)