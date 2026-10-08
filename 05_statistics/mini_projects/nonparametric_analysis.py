import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


np.random.seed(42)

alpha = 0.05


# 1. Mann-Whitney U Test
# Compare satisfaction between two independent customer groups

mobile_users = np.array([6, 7, 5, 8, 6, 7, 5, 6, 7, 8])
desktop_users = np.array([8, 9, 7, 8, 9, 8, 7, 9, 8, 9])

u_stat, p_value = stats.mannwhitneyu(
    mobile_users,
    desktop_users,
    alternative="two-sided"
)

print("Mann-Whitney U Test")
print("U statistic:", u_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Conclusion: The groups show a statistically significant difference.")
else:
    print("Conclusion: There is not enough evidence of a difference.")


# 2. Wilcoxon Signed-Rank Test
# Compare satisfaction before and after a redesign

before_redesign = np.array([5, 6, 6, 7, 5, 6, 7, 6, 5, 7])
after_redesign = np.array([7, 8, 7, 8, 7, 8, 8, 7, 6, 8])

w_stat, p_value = stats.wilcoxon(
    before_redesign,
    after_redesign
)

print("\nWilcoxon Signed-Rank Test")
print("Statistic:", w_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Conclusion: Satisfaction changed significantly after the redesign.")
else:
    print("Conclusion: There is not enough evidence of a change.")


# 3. Kruskal-Wallis Test
# Compare satisfaction across three independent subscription plans

basic = np.array([5, 6, 5, 7, 6, 5, 6])
standard = np.array([7, 8, 7, 8, 9, 7, 8])
premium = np.array([8, 9, 9, 8, 10, 9, 8])

h_stat, p_value = stats.kruskal(
    basic,
    standard,
    premium
)

print("\nKruskal-Wallis Test")
print("H statistic:", h_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Conclusion: At least one subscription group differs.")
else:
    print("Conclusion: There is not enough evidence of a difference.")


# 4. Friedman Test
# Compare three interface designs using the same customers

design_a = np.array([6, 7, 7, 8, 6, 7, 8, 7])
design_b = np.array([7, 8, 8, 9, 7, 8, 9, 8])
design_c = np.array([8, 9, 9, 9, 8, 9, 10, 9])

friedman_stat, p_value = stats.friedmanchisquare(
    design_a,
    design_b,
    design_c
)

print("\nFriedman Test")
print("Statistic:", friedman_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Conclusion: At least one interface design differs.")
else:
    print("Conclusion: There is not enough evidence of a difference.")


# Summary

summary = pd.DataFrame({
    "Metric": [
        "Mobile Mean",
        "Desktop Mean",
        "Before Redesign Mean",
        "After Redesign Mean",
        "Basic Mean",
        "Standard Mean",
        "Premium Mean"
    ],
    "Value": [
        mobile_users.mean(),
        desktop_users.mean(),
        before_redesign.mean(),
        after_redesign.mean(),
        basic.mean(),
        standard.mean(),
        premium.mean()
    ]
})

print("\nSummary")
print(summary)


# Visualization

plt.figure(figsize=(8, 5))

plt.boxplot(
    [mobile_users, desktop_users],
    tick_labels=["Mobile", "Desktop"]
)

plt.ylabel("Satisfaction Score")
plt.title("Customer Satisfaction by Device")

plt.tight_layout()
plt.show()