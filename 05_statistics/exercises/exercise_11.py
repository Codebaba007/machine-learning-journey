
import numpy as np
from scipy import stats

scores = np.array([
    60, 65, 70, 72, 68,
    75, 80, 77, 73, 69,
    74, 78, 82, 71, 76,
    79, 85, 67, 72, 74
])

sample_mean = np.mean(scores)
sample_sd = np.std(scores, ddof=1)
sample_size = len(scores)

standard_error = sample_sd / np.sqrt(sample_size)
degrees_of_freedom = sample_size - 1

print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_sd)
print("Standard Error:", standard_error)

for confidence in [0.90, 0.95, 0.99]:
    critical_value = stats.t.ppf(
        (1 + confidence) / 2,
        df=degrees_of_freedom
    )

    margin_of_error = critical_value * standard_error

    lower = sample_mean - margin_of_error
    upper = sample_mean + margin_of_error

    print(f"\n{confidence * 100:.0f}% Confidence Interval:")
    print(lower, upper)
    print("Margin of Error:", margin_of_error)
