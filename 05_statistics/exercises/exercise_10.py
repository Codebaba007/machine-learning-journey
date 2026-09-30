
import numpy as np

population = np.random.normal(
    loc=70,
    scale=12,
    size=10000
)

sample_sizes = [10, 30, 100, 500]

print("Population Mean:", np.mean(population))

for sample_size in sample_sizes:
    sample = np.random.choice(
        population,
        size=sample_size,
        replace=False
    )

    sample_mean = np.mean(sample)
    sample_sd = np.std(sample, ddof=1)
    standard_error = sample_sd / np.sqrt(sample_size)

    print("\nSample Size:", sample_size)
    print("Sample Mean:", sample_mean)
    print("Standard Error:", standard_error)
