import numpy as np
import matplotlib.pyplot as plt

# Distribution
data = [45, 50, 52, 55, 60, 62, 64, 65, 67, 70, 72, 75, 80, 85, 90]

print("Data:", data)

# Basic statistics
print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

# Percentiles
print("\n25th Percentile:", np.percentile(data, 25))
print("50th Percentile:", np.percentile(data, 50))
print("75th Percentile:", np.percentile(data, 75))

# Histogram
plt.hist(data, bins=6)
plt.title("Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Right-skewed example
right_skewed = [10, 12, 13, 14, 15, 16, 18, 20, 25, 40, 80]

print("\nRight-Skewed Data")
print("Mean:", np.mean(right_skewed))
print("Median:", np.median(right_skewed))

plt.hist(right_skewed, bins=6)
plt.title("Right-Skewed Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Left-skewed example
left_skewed = [20, 60, 75, 80, 82, 84, 85, 87, 88, 90, 92]

print("\nLeft-Skewed Data")
print("Mean:", np.mean(left_skewed))
print("Median:", np.median(left_skewed))

plt.hist(left_skewed, bins=6)
plt.title("Left-Skewed Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()