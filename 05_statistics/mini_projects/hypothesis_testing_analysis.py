
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# 1. Simulate student population

population_scores = np.random.normal(
    loc=75,
    scale=10,
    size=10000
)

population_scores = np.clip(
    population_scores,
    0,
    100
)

true_mean = np.mean(population_scores)

# 2. Draw a sample

sample_size = 100

sample_scores = np.random.choice(
    population_scores,
    size=sample_size,
    replace=False
)

sample_mean = np.mean(sample_scores)
sample_sd = np.std(sample_scores, ddof=1)

# 3. Set up hypotheses

hypothesized_mean = 75
population_sd = 10
alpha = 0.05

# H0: mu = 75
# H1: mu != 75

# 4. Calculate standard error

standard_error = population_sd / np.sqrt(sample_size)

# 5. Calculate Z-statistic

z_statistic = (
    sample_mean - hypothesized_mean
) / standard_error

# 6. Calculate two-tailed p-value

p_value = 2 * stats.norm.cdf(-abs(z_statistic))

# 7. Calculate critical value

z_critical = stats.norm.ppf(1 - alpha / 2)

# 8. Make decision

if p_value <= alpha:
    decision = "Reject H0"
else:
    decision = "Fail to reject H0"

# 9. Create a summary

results = pd.DataFrame({
    "Metric": [
        "Population Mean",
        "Hypothesized Mean",
        "Sample Mean",
        "Sample Standard Deviation",
        "Sample Size",
        "Standard Error",
        "Z Statistic",
        "Critical Z-value",
        "P-value",
        "Significance Level",
        "Decision"
    ],
    "Value": [
        true_mean,
        hypothesized_mean,
        sample_mean,
        sample_sd,
        sample_size,
        standard_error,
        z_statistic,
        z_critical,
        p_value,
        alpha,
        decision
    ]
})

print(results.to_string(index=False))

# 10. Visualize the sample distribution

plt.figure(figsize=(10, 6))

plt.hist(
    sample_scores,
    bins=15,
    edgecolor="black",
    alpha=0.75
)

plt.axvline(
    sample_mean,
    linestyle="--",
    linewidth=2,
    label=f"Sample Mean: {sample_mean:.2f}"
)

plt.axvline(
    hypothesized_mean,
    linestyle="-",
    linewidth=2,
    label=f"Hypothesized Mean: {hypothesized_mean}"
)

plt.title("Student Exam Score Distribution")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

# 11. Visualize the hypothesis test

z_values = np.linspace(-4, 4, 1000)
density = stats.norm.pdf(z_values)

plt.figure(figsize=(10, 6))

plt.plot(
    z_values,
    density,
    label="Standard Normal Distribution"
)

plt.fill_between(
    z_values,
    density,
    where=(z_values <= -z_critical),
    alpha=0.4,
    label="Left Rejection Region"
)

plt.fill_between(
    z_values,
    density,
    where=(z_values >= z_critical),
    alpha=0.4,
    label="Right Rejection Region"
)

plt.axvline(
    z_statistic,
    linestyle="--",
    linewidth=2,
    label=f"Observed Z: {z_statistic:.2f}"
)

plt.axvline(
    -z_critical,
    linestyle=":",
    linewidth=1.5,
    label=f"Critical Z: {-z_critical:.2f}"
)

plt.axvline(
    z_critical,
    linestyle=":",
    linewidth=1.5,
    label=f"Critical Z: {z_critical:.2f}"
)

plt.title("Two-Tailed Z-Test")
plt.xlabel("Z Statistic")
plt.ylabel("Probability Density")
plt.legend()
plt.tight_layout()
plt.show()
