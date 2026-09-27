import pandas as pd

data = pd.DataFrame({
    "Disease": ["Yes", "Yes", "No", "No"],
    "Test": ["Positive", "Negative", "Positive", "Negative"],
    "Count": [95, 5, 495, 9405]
})

total_people = data["Count"].sum()

disease_cases = data.loc[
    data["Disease"] == "Yes", "Count"
].sum()

positive_cases = data.loc[
    data["Test"] == "Positive", "Count"
].sum()

true_positives = data.loc[
    (data["Disease"] == "Yes") &
    (data["Test"] == "Positive"), "Count"
].sum()

prior = disease_cases / total_people

likelihood = true_positives / disease_cases

evidence = positive_cases / total_people

posterior = (likelihood * prior) / evidence

print("Medical Test Bayes' Theorem Analysis")
print("Total People:", total_people)
print("Disease Cases:", disease_cases)
print("Positive Test Results:", positive_cases)

print("\nBayes' Theorem")
print("Prior:", prior)
print("Likelihood:", likelihood)
print("Evidence:", evidence)
print("Posterior:", posterior)

print("\nProbability of Disease Given Positive Test:")
print(f"{posterior:.2%}")