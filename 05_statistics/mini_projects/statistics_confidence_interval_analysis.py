
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

population = np.random.normal(
    loc=70,
    scale=12,
    size=10000
)

population_mean = np.mean(population)

sample_sizes = [20, 50, 100, 300]
confidence_levels = [0.90, 0.95, 0.99]

results = []

for sample_size in sample_sizes:
    sample = np.random.choice(
        population,
        size=sample_size,
        replace=False
    )

    sample_mean = np.mean(sample)
    sample_sd = np.std(sample, ddof=1)
    standard_error = sample_sd / np.sqrt(sample_size)

    for confidence in confidence_levels:
        critical_value = stats.t.ppf(
            (1 + confidence) / 2,
            df=sample_size - 1
        )

        margin_of_error = critical_value * standard_error

        lower = sample_mean - margin_of_error
        upper = sample_mean + margin_of_error

        results.append({
            "Sample Size": sample_size,
            "Confidence Level": confidence,
            "Sample Mean": sample_mean,
            "Lower Bound": lower,
            "Upper Bound": upper,
            "Margin of Error": margin_of_error,
            "Interval Width": upper - lower,
            "Contains Population Mean": lower <= population_mean <= upper
        })

results_df = pd.DataFrame(results)

print("Population Mean:", population_mean)
print("\nConfidence Interval Analysis")
print(results_df.round(3).to_string(index=False))


# Compare interval widths
for confidence in confidence_levels:
    subset = results_df[
        results_df["Confidence Level"] == confidence
    ]

    plt.plot(
        subset["Sample Size"],
        subset["Interval Width"],
        marker="o",
        label=f"{confidence * 100:.0f}% Confidence"
    )

plt.xlabel("Sample Size")
plt.ylabel("Confidence Interval Width")
plt.title("Sample Size vs Confidence Interval Width")
plt.legend()
plt.grid()
plt.show()


# Visualize intervals for different confidence levels
sample_size = 100
sample = np.random.choice(
    population,
    size=sample_size,
    replace=False
)

sample_mean = np.mean(sample)
sample_sd = np.std(sample, ddof=1)
standard_error = sample_sd / np.sqrt(sample_size)

intervals = []

for confidence in confidence_levels:
    critical_value = stats.t.ppf(
        (1 + confidence) / 2,
        df=sample_size - 1
    )

    margin = critical_value * standard_error

    intervals.append({
        "Confidence": f"{confidence * 100:.0f}%",
        "Lower": sample_mean - margin,
        "Upper": sample_mean + margin
    })

plt.figure(figsize=(8, 4))

for i, interval in enumerate(intervals):
    plt.plot(
        [interval["Lower"], interval["Upper"]],
        [i, i],
        marker="|",
        linewidth=3,
        label=interval["Confidence"]
    )

plt.axvline(
    population_mean,
    linestyle="--",
    label="Population Mean"
)

plt.yticks(range(len(intervals)), [
    interval["Confidence"] for interval in intervals
])

plt.xlabel("Estimated Population Mean")
plt.title("Confidence Intervals at Different Levels")
plt.legend()
plt.grid(axis="x")
plt.tight_layout()
plt.show()
