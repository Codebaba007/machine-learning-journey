import numpy as np
from scipy import stats


group_a = np.array([12, 18, 25, 30, 35])
group_b = np.array([15, 20, 28, 40, 45])

print("Group A:", group_a)
print("Group B:", group_b)


# Mann-Whitney U Test

u_stat, p_value = stats.mannwhitneyu(
    group_a,
    group_b,
    alternative="two-sided"
)

print("\nMann-Whitney U Test")
print("U statistic:", u_stat)
print("p-value:", p_value)


# Wilcoxon Signed-Rank Test

before = np.array([60, 65, 70, 72, 68])
after = np.array([64, 69, 75, 76, 73])

w_stat, p_value = stats.wilcoxon(before, after)

print("\nWilcoxon Signed-Rank Test")
print("Statistic:", w_stat)
print("p-value:", p_value)


# Kruskal-Wallis Test

group_1 = np.array([12, 15, 14, 13, 16])
group_2 = np.array([18, 20, 19, 21, 17])
group_3 = np.array([10, 11, 12, 9, 13])

h_stat, p_value = stats.kruskal(
    group_1,
    group_2,
    group_3
)

print("\nKruskal-Wallis Test")
print("H statistic:", h_stat)
print("p-value:", p_value)


# Friedman Test

version_a = np.array([7, 8, 6, 9, 7])
version_b = np.array([8, 9, 7, 9, 8])
version_c = np.array([9, 9, 8, 10, 9])

friedman_stat, p_value = stats.friedmanchisquare(
    version_a,
    version_b,
    version_c
)

print("\nFriedman Test")
print("Statistic:", friedman_stat)
print("p-value:", p_value)