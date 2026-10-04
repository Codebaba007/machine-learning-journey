import numpy as np
from scipy import stats


# Three groups

group_a = np.array([
    69, 70, 71, 70, 69
])

group_b = np.array([
    79, 80, 81, 80, 79
])

group_c = np.array([
    89, 90, 91, 90, 89
])


# Group means

print("Group A mean:", np.mean(group_a))
print("Group B mean:", np.mean(group_b))
print("Group C mean:", np.mean(group_c))


# One-way ANOVA

f_statistic, p_value = stats.f_oneway(
    group_a,
    group_b,
    group_c
)

print("\nOne-way ANOVA")
print("F-statistic:", f_statistic)
print("P-value:", p_value)


# Decision

alpha = 0.05

if p_value <= alpha:
    print("Reject H0")
    print("At least one group mean is different.")
else:
    print("Fail to reject H0")
    print("There is not enough evidence that the group means differ.")


# Another example with overlapping groups

group_a = np.array([
    65, 80, 72, 76, 67
])

group_b = np.array([
    70, 75, 68, 80, 73
])

group_c = np.array([
    71, 69, 77, 74, 73
])

f_statistic, p_value = stats.f_oneway(
    group_a,
    group_b,
    group_c
)

print("\nSecond ANOVA")
print("F-statistic:", f_statistic)
print("P-value:", p_value)