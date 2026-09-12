import matplotlib.pyplot as plt
'''
This is a simple example of how to use matplotlib to create a line plot.

days = [1, 2, 3, 4, 5]
scores = [60, 65, 72, 80, 88]
print("Days:", days)
print("Scores:", scores)
python_scores = [60, 65, 72, 80, 88]
numpy_scores = [55, 60, 68, 75, 82]

plt.plot(days, python_scores, label = "Python")
plt.plot(days, numpy_scores, label="Numpy")
plt.plot(days, scores)
plt.title("Learning progress")
plt.xlabel("Days")
plt.ylabel("Scores")

plt.legend()
plt.grid()
plt.show()

days = [1, 2, 3, 4, 5]

python_scores = [60, 65, 72, 80, 88]
numpy_scores = [55, 62, 68, 76, 84]

plt.figure(figsize=(8, 5))

plt.plot(days, python_scores, label="Python")
plt.plot(days, numpy_scores, label="NumPy")

plt.title("Learning Progress")
plt.xlabel("Days")
plt.ylabel("Score")

plt.legend()
plt.grid()
plt.savefig("learning_progress.png")
plt.show()
'''
import pandas as pd


data = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5],
    "Python": [60, 65, 72, 80, 88],
    "NumPy": [55, 62, 68, 76, 84]
})

print("Dataset")
print(data)

plt.figure(figsize=(8, 5))

plt.plot(data["Day"], data["Python"], label="Python")
plt.plot(data["Day"], data["NumPy"], label="NumPy")

plt.title("Learning Progress")
plt.xlabel("Days")
plt.ylabel("Score")

plt.legend()
plt.grid()

plt.savefig("learning_progress.png")
plt.show()