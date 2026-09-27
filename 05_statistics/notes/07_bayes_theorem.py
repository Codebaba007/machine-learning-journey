# 1. Prior probability
prior_disease = 0.01

print("Prior Probability:", prior_disease)


# 2. Likelihood
sensitivity = 0.95
false_positive_rate = 0.05

print("Sensitivity:", sensitivity)
print("False Positive Rate:", false_positive_rate)


# 3. Evidence
prior_no_disease = 1 - prior_disease

probability_positive = (
    sensitivity * prior_disease
    + false_positive_rate * prior_no_disease
)

print("Probability of Positive Test:", probability_positive)


# 4. Bayes' Theorem
posterior_disease = (
    sensitivity * prior_disease
    / probability_positive
)

print("Posterior Probability:", posterior_disease)


# 5. Calculate using counts
total_people = 10000
disease_cases = 100
healthy_people = total_people - disease_cases

true_positives = int(disease_cases * sensitivity)
false_positives = int(healthy_people * false_positive_rate)

total_positive = true_positives + false_positives

posterior_from_counts = true_positives / total_positive

print("True Positives:", true_positives)
print("False Positives:", false_positives)
print("Total Positive Results:", total_positive)
print("Posterior from Counts:", posterior_from_counts)