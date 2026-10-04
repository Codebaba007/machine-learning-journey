import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


np.random.seed(42)


# Generate student scores

traditional = np.random.normal(
    loc=70,
    scale=6,
    size=40
)

online = np.random.normal(
    loc=74,
    scale=6,
    size=40
)

hybrid = np.random.normal(
    loc=78,
    scale=6,
    size=40
)


# Create DataFrame

data = pd.DataFrame({
    "Traditional": traditional,
    "Online": online,
    "Hybrid": hybrid
})

print("Group means")
print(data.mean())


# One-way ANOVA

f_statistic, p_value = stats.f_oneway(
    traditional,
    online,
    hybrid
)

print("\nANOVA Results")
print("F-statistic:", f_statistic)
print("P-value:", p_value)


# Statistical decision

alpha = 0.05

if p_value <= alpha:
    print("\nDecision: Reject H0")
    print("At least one teaching method has a different population mean.")
else:
    print("\nDecision: Fail to reject H0")
    print("There is not enough evidence that the population means differ.")


# Group statistics

summary = pd.DataFrame({
    "Mean": data.mean(),
    "Standard Deviation": data.std(),
    "Sample Size": data.count()
})

print("\nGroup Summary")
print(summary)


# Boxplot

data.boxplot()

plt.title("Student Scores by Teaching Method")
plt.ylabel("Score")
plt.show()


# Histograms

data.plot(
    kind="hist",
    bins=10,
    alpha=0.6
)

plt.title("Distribution of Student Scores")
plt.xlabel("Score")
plt.show()