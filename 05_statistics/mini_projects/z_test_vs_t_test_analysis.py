import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


np.random.seed(42)


# Create a population

population = np.random.normal(
    loc=75,
    scale=10,
    size=10000
)


# Take a sample

sample = np.random.choice(
    population,
    size=30,
    replace=False
)


sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
sample_size = len(sample)

hypothesized_mean = 70

standard_error = sample_std / np.sqrt(sample_size)

t_statistic = (
    sample_mean - hypothesized_mean
) / standard_error

degrees_of_freedom = sample_size - 1

p_value = 2 * stats.t.sf(
    abs(t_statistic),
    df=degrees_of_freedom
)


summary = pd.DataFrame({
    "Metric": [
        "Sample Size",
        "Sample Mean",
        "Sample Standard Deviation",
        "Standard Error",
        "Hypothesized Mean",
        "T-statistic",
        "Degrees of Freedom",
        "P-value"
    ],
    "Value": [
        sample_size,
        sample_mean,
        sample_std,
        standard_error,
        hypothesized_mean,
        t_statistic,
        degrees_of_freedom,
        p_value
    ]
})

print(summary)


# One-sample t-test using SciPy

t_statistic, p_value = stats.ttest_1samp(
    sample,
    hypothesized_mean
)

print("\nOne-sample t-test")
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# Before and after training data

before = np.array([
    60, 64, 68, 70, 65,
    72, 69, 63, 67, 71
])

after = np.array([
    67, 70, 74, 76, 72,
    78, 75, 69, 73, 77
])


paired_t, paired_p = stats.ttest_rel(
    before,
    after
)

print("\nPaired t-test")
print("T-statistic:", paired_t)
print("P-value:", paired_p)


# Visualization

plt.hist(
    sample,
    bins=8,
    edgecolor="black"
)

plt.axvline(
    sample_mean,
    linestyle="--",
    label="Sample Mean"
)

plt.axvline(
    hypothesized_mean,
    linestyle="--",
    label="Hypothesized Mean"
)

plt.title("Sample Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.show()