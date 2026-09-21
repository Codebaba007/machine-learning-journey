import numpy as np
import statistics

scores = [55, 60, 62, 65, 68, 70, 72, 78, 85, 90]

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Mode:", statistics.mode(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Range:", np.ptp(scores))