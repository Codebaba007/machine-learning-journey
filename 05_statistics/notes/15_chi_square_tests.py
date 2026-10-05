import numpy as np
import pandas as pd
from scipy import stats


# 1. Observed and expected frequencies

observed = np.array([70, 60, 50, 20])
expected = np.array([50, 50, 50, 50])

print("Observed:", observed)
print("Expected:", expected)


# 2. Manual Chi-Square calculation

chi_square_manual = np.sum(
    (observed - expected) ** 2 / expected
)

print("\nManual Chi-Square:", chi_square_manual)


# 3. Goodness-of-fit test

result = stats.chisquare(
    f_obs=observed,
    f_exp=expected
)

print("\nGoodness-of-Fit Test")
print("Chi-Square:", result.statistic)
print("P-value:", result.pvalue)


# 4. Degrees of freedom

categories = len(observed)
df = categories - 1

print("\nDegrees of Freedom:", df)


# 5. Chi-Square distribution

p_value_manual = stats.chi2.sf(
    chi_square_manual,
    df=df
)

print("Manual P-value:", p_value_manual)


# 6. Contingency table

table = np.array([
    [40, 10],
    [25, 25]
])

print("\nContingency Table")
print(table)


# 7. Independence test

chi2, p_value, dof, expected_table = (
    stats.chi2_contingency(
        table,
        correction=False
    )
)

print("\nChi-Square Independence Test")
print("Chi-Square:", chi2)
print("P-value:", p_value)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:")
print(expected_table)


# 8. Expected frequencies manually

row_totals = table.sum(axis=1)
column_totals = table.sum(axis=0)
grand_total = table.sum()

manual_expected = np.outer(
    row_totals,
    column_totals
) / grand_total

print("\nManually Calculated Expected Frequencies")
print(manual_expected)


# 9. Statistical decision

alpha = 0.05

if p_value <= alpha:
    print("\nReject H0")
    print("The categorical variables are associated.")
else:
    print("\nFail to reject H0")
    print("Insufficient evidence of an association.")


# 10. Contingency table with Pandas

data = pd.DataFrame({
    "Study_Method": [
        "Online", "Online", "Offline",
        "Offline", "Online", "Offline"
    ],
    "Result": [
        "Pass", "Pass", "Fail",
        "Pass", "Fail", "Fail"
    ]
})

cross_table = pd.crosstab(
    data["Study_Method"],
    data["Result"]
)

print("\nPandas Contingency Table")
print(cross_table)


# 11. Cramer's V effect size

n = table.sum()
r, c = table.shape

cramers_v = np.sqrt(
    chi2 / (n * min(r - 1, c - 1))
)

print("\nCramer's V:", cramers_v)