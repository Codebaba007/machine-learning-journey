
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.normal(
    loc=70,
    scale=12,
    size=10000
)

population_mean = np.mean(population)
population_sd = np.std(population)

sample_sizes = [10, 30, 100, 500]
results = []

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

for ax, sample_size in zip(axes.flat, sample_sizes):
    sample_means = []

    for _ in range(1000):
        sample = np.random.choice(
            population,
            size=sample_size,
            replace=False
        )

        sample_means.append(np.mean(sample))

    sample_means = np.array(sample_means)

    results.append({
        "Sample Size": sample_size,
        "Mean of Sample Means": np.mean(sample_means),
        "Standard Error": np.std(sample_means),
        "Theoretical SE": population_sd / np.sqrt(sample_size)
    })

    ax.hist(sample_means, bins=30, edgecolor="black")
    ax.axvline(
        population_mean,
        linestyle="--",
        label="Population Mean"
    )
    ax.set_title(f"Sample Size: {sample_size}")
    ax.set_xlabel("Sample Mean")
    ax.set_ylabel("Frequency")
    ax.legend()

plt.tight_layout()
plt.show()

results_df = pd.DataFrame(results)

print("Population Mean:", population_mean)
print("\nSampling Analysis")
print(results_df.round(3))

plt.figure(figsize=(8, 5))
plt.plot(
    results_df["Sample Size"],
    results_df["Standard Error"],
    marker="o",
    label="Observed SE"
)
plt.plot(
    results_df["Sample Size"],
    results_df["Theoretical SE"],
    marker="s",
    label="Theoretical SE"
)
plt.xlabel("Sample Size")
plt.ylabel("Standard Error")
plt.title("Sample Size vs Standard Error")
plt.legend()
plt.grid()
plt.show()
