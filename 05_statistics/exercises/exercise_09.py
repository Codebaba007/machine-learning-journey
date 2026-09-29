import numpy as np

study_hours = np.array([1, 2, 3, 4, 5, 6])
exam_scores = np.array([45, 50, 55, 65, 70, 80])

covariance = np.cov(study_hours, exam_scores)[0, 1]
correlation = np.corrcoef(study_hours, exam_scores)[0, 1]

print("Covariance:", covariance)
print("Correlation:", correlation)