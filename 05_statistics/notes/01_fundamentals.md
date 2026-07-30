# 📝 Notes: Statistics Fundamentals

## 1. Descriptive Statistics
- **Measures of Central Tendency**: Mean (average), Median (middle value, robust to outliers), Mode (most frequent).
- **Measures of Dispersion**: Variance (spread from mean), Standard Deviation (sqrt of variance, same units as data), IQR (interquartile range, robust spread).

## 2. Probability Distributions
- **Normal (Gaussian) Distribution**: The bell curve. Characterized by mean $\mu$ and standard dev $\sigma$. 68-95-99.7 rule.
- **Binomial**: Number of successes in a sequence of $n$ independent yes/no experiments.

## 3. Hypothesis Testing
Used to determine if results are statistically significant or due to chance.
- **Null Hypothesis ($H_0$)**: No effect / no difference.
- **Alternative Hypothesis ($H_A$)**: There is an effect.
- **p-value**: Probability of observing the data given $H_0$ is true. If $p < 0.05$ (alpha), we reject $H_0$.

## 4. Correlation vs Causation
- **Pearson Correlation ($r$)**: Measures linear relationship between -1 and 1.
- Correlation does not imply causation; confounding variables might be at play.

## 5. Bayes' Theorem
$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
Updates the probability of a hypothesis (A) based on new evidence (B). Foundational for Naive Bayes classifiers and Bayesian inference.
