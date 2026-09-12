import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

dsa_scores = [55, 63, 70, 78, 85]
ml_scores = [50, 60, 68, 75, 82]

plt.figure(figsize=(8, 5))

plt.plot(days, dsa_scores, label="DSA")
plt.plot(days, ml_scores, label="ML")

plt.title("Learning Progress")
plt.xlabel("Days")
plt.ylabel("Score")

plt.legend()
plt.grid()

plt.savefig("dsa_ml_progress.png")
plt.show()