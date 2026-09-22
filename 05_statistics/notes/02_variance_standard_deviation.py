import numpy as np

scores = [10, 20, 30]

variance = np.var(scores)

print(variance)

standard_deviation = np.std(scores)

print(standard_deviation)

simple_std_var = np.std(scores, ddof=1) 
print(simple_std_var)