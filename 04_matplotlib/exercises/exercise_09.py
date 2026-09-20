import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
scores = [50, 55, 61, 68, 72, 79, 85]

plt.figure(figsize=(8, 5))

plt.plot(days, scores, marker="o")

plt.title("Learning Progress")
plt.xlabel("Day")
plt.ylabel("Score")
plt.grid()

plt.annotate(
    "Highest Score",
    xy=(7, 85),
    xytext=(-80, 30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.show()