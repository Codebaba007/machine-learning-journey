import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
scores = [55, 63, 70, 78, 85]

plt.figure(figsize=(8, 5))

plt.plot(
    days,
    scores,
    color="blue",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8
)

plt.title("Learning Progress")
plt.xlabel("Day")
plt.ylabel("Score")
plt.grid()

plt.show()

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [45, 50, 58, 65, 72, 80]

plt.scatter(
    hours,
    scores,
    color="red",
    s=100,
    alpha=0.7
)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()

plt.show()