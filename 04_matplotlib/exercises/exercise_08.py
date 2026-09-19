import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
scores = [50, 55, 61, 68, 72, 79, 85]

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