import matplotlib.pyplot as plt

scores = [
    45, 52, 55, 58, 60,
    61, 62, 64, 65, 67,
    68, 70, 71, 72, 74,
    75, 78, 80, 85, 90
]

plt.figure(figsize=(8, 5))
plt.hist(scores, bins=5, edgecolor="black")

plt.title("Exam Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.grid(axis="y")

plt.show()