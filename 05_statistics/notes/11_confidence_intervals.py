
import numpy as np
from scipy import stats

# 1. Sample data
scores = np.array([
    65, 70, 72, 68, 75,
    80, 77, 73, 69, 74,
    78, 82, 71, 76, 79
])

sample_mean = np.mean(scores)
sample_sd = np.std(scores, ddof=1)
sample_size = len(scores)

print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_sd)
print("Sample Size:", sample_size)


# 2. Standard error
standard_error = sample_sd / np.sqrt(sample_size)

print("\nStandard Error:", standard_error)


# 3. Z-confidence interval (known population SD)
population_sd = 10
confidence_level = 0.95

z_critical = stats.norm.ppf(
    (1 + confidence_level) / 2
)

z_margin_error = z_critical * (
    population_sd / np.sqrt(sample_size)
)

z_lower = sample_mean - z_margin_error
z_upper = sample_mean + z_margin_error

print("\n95% Z-Confidence Interval:")
print(z_lower, z_upper)


# 4. T-confidence interval (unknown population SD)
degrees_of_freedom = sample_size - 1

t_critical = stats.t.ppf(
    (1 + confidence_level) / 2,
    df=degrees_of_freedom
)

t_margin_error = t_critical * standard_error

t_lower = sample_mean - t_margin_error
t_upper = sample_mean + t_margin_error

print("\n95% T-Confidence Interval:")
print(t_lower, t_upper)


# 5. Compare confidence levels
for confidence in [0.90, 0.95, 0.99]:
    critical = stats.t.ppf(
        (1 + confidence) / 2,
        df=degrees_of_freedom
    )

    margin = critical * standard_error

    lower = sample_mean - margin
    upper = sample_mean + margin

    print(f"\n{confidence * 100:.0f}% Confidence Interval:")
    print(lower, upper)
