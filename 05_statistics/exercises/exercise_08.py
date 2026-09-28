import numpy as np

outcomes = np.array([0, 10, 20, 50])
probabilities = np.array([0.4, 0.3, 0.2, 0.1])

expected_value = np.sum(outcomes * probabilities)

print("Expected value:", expected_value)
print("Probability sum:", probabilities.sum())