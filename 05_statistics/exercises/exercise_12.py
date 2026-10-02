
import numpy as np
from scipy import stats

# Exercise 1
scores = np.array([
    68, 72, 75, 69, 71,
    74, 70, 73, 67, 76
])

sample_mean = np.mean(scores)
sample_size = len(scores)

print("Sample Mean:", sample_mean)
print("Sample Size:", sample_size)


# Exercise 2
population_mean = 70
population_sd = 5

standard_error = population_sd / np.sqrt(sample_size)

print("Standard Error:", standard_error)


# Exercise 3
z_statistic = (
    sample_mean - population_mean
) / standard_error

print("Z Statistic:", z_statistic)


# Exercise 4
alpha = 0.05

p_value = 2 * stats.norm.cdf(-abs(z_statistic))

print("P-value:", p_value)


# Exercise 5
if p_value <= alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")


# Exercise 6
z_critical = stats.norm.ppf(1 - alpha / 2)

print("Critical Z-value:", z_critical)

if abs(z_statistic) > z_critical:
    print("Reject H0 using the critical value")
else:
    print("Fail to reject H0 using the critical value")


# Exercise 7
# H0: mu = 70
# H1: mu > 70

right_tail_p_value = stats.norm.sf(z_statistic)

print("Right-tailed p-value:", right_tail_p_value)

if right_tail_p_value <= alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")
