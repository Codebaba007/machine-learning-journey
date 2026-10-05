import numpy as np
from scipy import stats


# Exercise 1
# Determine whether four payment methods
# are equally preferred.

observed = np.array([80, 50, 40, 30])
expected = np.array([50, 50, 50, 50])

result = stats.chisquare(
    f_obs=observed,
    f_exp=expected
)

print("Exercise 1")
print("Chi-Square:", result.statistic)
print("P-value:", result.pvalue)


# Exercise 2
# Determine whether study method
# is associated with exam results.

study_table = np.array([
    [45, 15],
    [30, 30]
])

chi2, p_value, dof, expected = (
    stats.chi2_contingency(
        study_table,
        correction=False
    )
)

print("\nExercise 2")
print("Chi-Square:", chi2)
print("P-value:", p_value)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:")
print(expected)


# Exercise 3
# Test whether device type is associated
# with subscription status.

device_table = np.array([
    [50, 30],
    [40, 40],
    [20, 60]
])

chi2, p_value, dof, expected = (
    stats.chi2_contingency(device_table)
)

print("\nExercise 3")
print("Chi-Square:", chi2)
print("P-value:", p_value)
print("Degrees of Freedom:", dof)


# Exercise 4
# Calculate the expected frequencies manually.

row_totals = device_table.sum(axis=1)
column_totals = device_table.sum(axis=0)
total = device_table.sum()

manual_expected = np.outer(
    row_totals,
    column_totals
) / total

print("\nExercise 4")
print(manual_expected)


# Exercise 5
# Interpret the independence test.

alpha = 0.05

if p_value <= alpha:
    print("\nReject H0")
    print("Evidence of an association.")
else:
    print("\nFail to reject H0")
    print("Insufficient evidence of an association.")


# Exercise 6
# Calculate Cramer's V.

n = device_table.sum()
rows, columns = device_table.shape

cramers_v = np.sqrt(
    chi2 / (n * min(rows - 1, columns - 1))
)

print("\nExercise 6")
print("Cramer's V:", cramers_v)