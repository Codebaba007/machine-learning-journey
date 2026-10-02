
import numpy as np
from scipy import stats

# 1. Hypothesis Testing
# Hypothesis testing uses sample data to evaluate a claim
# about a population.

# Example:
# A university claims that the average student score is 75.
# We collect a sample to investigate this claim.


# 2. Null and Alternative Hypotheses
#
# Null hypothesis (H0):
# The default claim being tested.
#
# Alternative hypothesis (H1):
# The claim we investigate evidence for.
#
# H0: mu = 75
# H1: mu != 75


# 3. Types of Hypothesis Tests
#
# Two-tailed:
# H1: mu != 75
#
# Right-tailed:
# H1: mu > 75
#
# Left-tailed:
# H1: mu < 75


# 4. Significance Level
#
# Alpha is the threshold used to make a decision.
# Common values: 0.10, 0.05, 0.01

alpha = 0.05


# 5. Sample Data

scores = np.array([
    65, 70, 68, 75, 80,
    77, 73, 69, 74, 78,
    82, 71, 76, 79
])

# Hypothesized population mean
population_mean = 75

# Known population standard deviation
population_sd = 10

sample_mean = np.mean(scores)
sample_size = len(scores)

print("Sample Mean:", sample_mean)
print("Sample Size:", sample_size)


# 6. Standard Error
#
# SE = sigma / sqrt(n)

standard_error = population_sd / np.sqrt(sample_size)

print("Standard Error:", standard_error)


# 7. Z-Test Statistic
#
# Z = (sample mean - hypothesized mean) / standard error

z_statistic = (
    sample_mean - population_mean
) / standard_error

print("Z Statistic:", z_statistic)


# 8. P-value
#
# For a two-tailed Z-test:
# p = 2 * P(Z <= -abs(z))

p_value = 2 * stats.norm.cdf(-abs(z_statistic))

print("P-value:", p_value)


# 9. Decision
#
# If p <= alpha, reject H0.
# Otherwise, fail to reject H0.

if p_value <= alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")


# 10. Critical Value
#
# For a two-tailed test, divide alpha between
# the two tails.

z_critical = stats.norm.ppf(1 - alpha / 2)

print("Critical Z-value:", z_critical)

if abs(z_statistic) > z_critical:
    print("Reject H0 using the critical value")
else:
    print("Fail to reject H0 using the critical value")


# 11. Type I and Type II Errors
#
# Type I: Rejecting a true null hypothesis.
# Type II: Failing to reject a false null hypothesis.
#
# Alpha is the probability of a Type I error
# under the assumptions of the test.
#
# Beta is the probability of a Type II error.
# Power = 1 - beta.


# 12. Machine Learning Applications
#
# Hypothesis testing can help investigate whether
# observed differences in model performance are
# statistically significant.
#
# The appropriate test depends on the experiment
# and how the data was collected.
