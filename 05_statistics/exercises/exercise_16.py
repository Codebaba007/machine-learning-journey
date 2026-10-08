import numpy as np
from scipy import stats


alpha = 0.05


# Exercise 1: Mann-Whitney U

group_a = np.array([14, 18, 20, 22, 25])
group_b = np.array([17, 21, 24, 27, 30])

u_stat, p_value = stats.mannwhitneyu(
    group_a,
    group_b,
    alternative="two-sided"
)

print("Exercise 1: Mann-Whitney U")
print("U statistic:", u_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Decision: Reject H0")
else:
    print("Decision: Fail to reject H0")


# Exercise 2: Wilcoxon Signed-Rank

before = np.array([55, 60, 62, 58, 65, 61])
after = np.array([59, 64, 66, 61, 69, 65])

w_stat, p_value = stats.wilcoxon(before, after)

print("\nExercise 2: Wilcoxon Signed-Rank")
print("Statistic:", w_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Decision: Reject H0")
else:
    print("Decision: Fail to reject H0")


# Exercise 3: Kruskal-Wallis

method_a = np.array([72, 75, 70, 74, 73])
method_b = np.array([80, 82, 79, 81, 83])
method_c = np.array([68, 70, 69, 71, 67])

h_stat, p_value = stats.kruskal(
    method_a,
    method_b,
    method_c
)

print("\nExercise 3: Kruskal-Wallis")
print("H statistic:", h_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Decision: Reject H0")
else:
    print("Decision: Fail to reject H0")


# Exercise 4: Friedman

model_a = np.array([6, 7, 8, 6, 7])
model_b = np.array([7, 8, 8, 7, 8])
model_c = np.array([8, 9, 9, 8, 9])

friedman_stat, p_value = stats.friedmanchisquare(
    model_a,
    model_b,
    model_c
)

print("\nExercise 4: Friedman")
print("Statistic:", friedman_stat)
print("p-value:", p_value)

if p_value <= alpha:
    print("Decision: Reject H0")
else:
    print("Decision: Fail to reject H0")