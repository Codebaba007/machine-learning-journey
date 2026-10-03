import numpy as np
from scipy import stats


# One-sample t-test

sample = np.array([72, 75, 70, 68, 77, 74, 71, 76, 73, 79])

hypothesized_mean = 70

sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
sample_size = len(sample)

standard_error = sample_std / np.sqrt(sample_size)

t_statistic = (sample_mean - hypothesized_mean) / standard_error

degrees_of_freedom = sample_size - 1

p_value = 2 * stats.t.sf(abs(t_statistic), df=degrees_of_freedom)

print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_std)
print("Standard error:", standard_error)
print("T-statistic:", t_statistic)
print("Degrees of freedom:", degrees_of_freedom)
print("P-value:", p_value)


# Using SciPy directly

t_statistic, p_value = stats.ttest_1samp(
    sample,
    hypothesized_mean
)

print("\nSciPy result")
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# Independent two-sample t-test

group_a = np.array([72, 75, 70, 68, 77, 74, 71, 76])
group_b = np.array([80, 78, 82, 79, 81, 77, 83, 80])

t_statistic, p_value = stats.ttest_ind(
    group_a,
    group_b
)

print("\nIndependent two-sample t-test")
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# Paired t-test

before = np.array([60, 65, 70, 72, 68, 75, 71, 64])
after = np.array([68, 70, 74, 78, 73, 80, 76, 70])

t_statistic, p_value = stats.ttest_rel(
    before,
    after
)

print("\nPaired t-test")
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# Comparing t and normal distributions

x = np.linspace(-4, 4, 500)

normal_distribution = stats.norm.pdf(x)

t_distribution_df5 = stats.t.pdf(x, df=5)

t_distribution_df30 = stats.t.pdf(x, df=30)

print("\nDistribution comparison")
print("Normal distribution calculated")
print("T-distribution with df=5 calculated")
print("T-distribution with df=30 calculated")