import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


np.random.seed(42)


# 1. Generate customer data

n = 600

contract_types = np.random.choice(
    ["Monthly", "Quarterly", "Yearly"],
    size=n,
    p=[0.5, 0.3, 0.2]
)

churn_probabilities = {
    "Monthly": 0.40,
    "Quarterly": 0.25,
    "Yearly": 0.10
}

churn = [
    np.random.choice(
        ["Yes", "No"],
        p=[
            churn_probabilities[contract],
            1 - churn_probabilities[contract]
        ]
    )
    for contract in contract_types
]


# 2. Create DataFrame

data = pd.DataFrame({
    "Contract_Type": contract_types,
    "Churn": churn
})

print("Dataset Preview")
print(data.head())

print("\nTotal Customers:", len(data))


# 3. Build contingency table

contingency_table = pd.crosstab(
    data["Contract_Type"],
    data["Churn"]
)

print("\nObserved Frequencies")
print(contingency_table)


# 4. Chi-Square independence test

chi2, p_value, dof, expected = (
    stats.chi2_contingency(
        contingency_table
    )
)

print("\nChi-Square Test")
print("Chi-Square Statistic:", chi2)
print("P-value:", p_value)
print("Degrees of Freedom:", dof)


# 5. Expected frequencies

expected_df = pd.DataFrame(
    expected,
    index=contingency_table.index,
    columns=contingency_table.columns
)

print("\nExpected Frequencies")
print(expected_df)


# 6. Statistical decision

alpha = 0.05

if p_value <= alpha:
    print("\nDecision: Reject H0")
    print("Evidence that contract type and churn are associated.")
else:
    print("\nDecision: Fail to reject H0")
    print("Insufficient evidence of an association.")


# 7. Effect size

total = contingency_table.to_numpy().sum()
rows, columns = contingency_table.shape

cramers_v = np.sqrt(
    chi2 / (total * min(rows - 1, columns - 1))
)

print("\nCramer's V:", cramers_v)


# 8. Churn rates by contract type

churn_rates = (
    data.groupby("Contract_Type")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print("\nChurn Rate (%)")
print(churn_rates)


# 9. Visualize observed frequencies

contingency_table.plot(
    kind="bar",
    figsize=(9, 5),
    edgecolor="black"
)

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 10. Visualize churn rates

churn_rates.plot(
    kind="bar",
    figsize=(8, 5),
    edgecolor="black"
)

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 11. Observed vs expected frequencies

observed_values = contingency_table.to_numpy()

fig, ax = plt.subplots(figsize=(8, 5))

positions = np.arange(observed_values.size)

ax.bar(
    positions - 0.2,
    observed_values.flatten(),
    width=0.4,
    label="Observed"
)

ax.bar(
    positions + 0.2,
    expected.flatten(),
    width=0.4,
    label="Expected"
)

labels = [
    f"{row}\n{col}"
    for row in contingency_table.index
    for col in contingency_table.columns
]

ax.set_xticks(positions)
ax.set_xticklabels(labels)

ax.set_title("Observed vs Expected Frequencies")
ax.set_ylabel("Frequency")
ax.legend()

plt.tight_layout()
plt.show()