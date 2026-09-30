
import numpy as np

# 1. Population and simple random sampling
population = np.arange(1, 101)

sample = np.random.choice(
    population,
    size=10,
    replace=False
)

print("Population Mean:", np.mean(population))
print("Sample:", sample)
print("Sample Mean:", np.mean(sample))


# 2. Systematic sampling
population = np.arange(1, 101)

interval = 10
start = np.random.randint(0, interval)

systematic_sample = population[start::interval][:10]

print("\nSystematic Sample:", systematic_sample)


# 3. Stratified sampling
students = np.array([
    "Undergraduate", "Undergraduate", "Undergraduate",
    "Undergraduate", "Undergraduate", "Undergraduate",
    "Masters", "Masters", "Masters",
    "PhD"
])

undergraduates = np.random.choice(
    students[students == "Undergraduate"],
    size=3,
    replace=False
)

masters = np.random.choice(
    students[students == "Masters"],
    size=2,
    replace=False
)

phd = np.random.choice(
    students[students == "PhD"],
    size=1,
    replace=False
)

stratified_sample = np.concatenate([
    undergraduates,
    masters,
    phd
])

print("\nStratified Sample:", stratified_sample)


# 4. Sampling variability
population = np.arange(1, 101)
sample_means = []

for _ in range(1000):
    sample = np.random.choice(
        population,
        size=10,
        replace=False
    )
    sample_means.append(np.mean(sample))

print("\nPopulation Mean:", np.mean(population))
print("Average Sample Mean:", np.mean(sample_means))
print("Sampling Variability:", np.std(sample_means))


# 5. Standard error
sample = np.random.choice(
    population,
    size=25,
    replace=False
)

standard_error = np.std(sample, ddof=1) / np.sqrt(len(sample))

print("\nSample Standard Deviation:", np.std(sample, ddof=1))
print("Estimated Standard Error:", standard_error)
