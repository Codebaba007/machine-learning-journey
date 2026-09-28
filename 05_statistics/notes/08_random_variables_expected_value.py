import numpy as np
import pandas as pd

# 1. Discrete random variable
die = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.full(6, 1 / 6)

print("Possible outcomes:", die)
print("Probabilities:", probabilities)
print("Probability sum:", probabilities.sum())


# 2. Expected value of a fair die
expected_value = np.sum(die * probabilities)

print("Expected value:", expected_value)


# 3. Expected value using a probability table
rewards = np.array([0, 10, 20])
reward_probabilities = np.array([0.5, 0.3, 0.2])

expected_reward = np.sum(rewards * reward_probabilities)

print("Expected reward:", expected_reward)


# 4. Delivery probability distribution
deliveries = np.array([2, 3, 4, 5])
delivery_probabilities = np.array([0.2, 0.3, 0.4, 0.1])

expected_deliveries = np.sum(
    deliveries * delivery_probabilities
)

print("Expected deliveries:", expected_deliveries)


# 5. Continuous random variable example
delivery_times = np.array([10.5, 12.0, 15.5, 18.0, 20.0])

print("Average delivery time:", np.mean(delivery_times))