import numpy as np
import pandas as pd

# 1. Positive covariance
study_hours = np.array([1, 2, 3, 4, 5])
exam_scores = np.array([40, 50, 60, 70, 80])

positive_covariance = np.cov(study_hours, exam_scores)[0, 1]

print("Positive Covariance:", positive_covariance)


# 2. Negative covariance
temperature = np.array([10, 15, 20, 25, 30])
heating_usage = np.array([90, 75, 60, 40, 20])

negative_covariance = np.cov(temperature, heating_usage)[0, 1]

print("Negative Covariance:", negative_covariance)


# 3. Zero covariance
x = np.array([-2, -1, 0, 1, 2])
y = x ** 2

zero_covariance = np.cov(x, y)[0, 1]

print("Covariance:", zero_covariance)


# 4. Pearson correlation
correlation = np.corrcoef(study_hours, exam_scores)[0, 1]

print("Pearson Correlation:", correlation)


# 5. Covariance and correlation using Pandas
data = pd.DataFrame({
    "Study Hours": study_hours,
    "Exam Scores": exam_scores
})

print("Pandas Covariance:")
print(data.cov())

print("\nPandas Correlation:")
print(data.corr())