import numpy as np

scores = [45, 50, 52, 55, 60, 62, 64, 65, 67, 70, 72, 75, 80, 85, 90]

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard Deviation:", np.std(scores))
print("Q1:", np.percentile(scores, 25))
print("Q3:", np.percentile(scores, 75))