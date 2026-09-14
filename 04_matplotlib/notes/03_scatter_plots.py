import matplotlib.pyplot as plt
'''
hours = [1, 2, 3, 4, 5]
scores = [10, 20, 30, 40, 50]

#plt.scatter(hours, scores)
plt.scatter(hours, scores, s=100, alpha=0.7)


plt.title("Hours vs Scores")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.xticks(hours)
plt.grid()
plt.show()

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [45, 50, 58, 65, 72, 80]
students = [10, 20, 30, 40, 50, 60]

plt.scatter(hours, scores, s=[x * 5 for x in students], alpha=0.7)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.grid()

plt.show()


hours = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6]
scores = [45, 50, 52, 55, 58, 60, 62, 65, 68, 72, 75, 80]

plt.scatter(hours, scores, s=100, alpha=0.5)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.grid()

plt.show()'''
import pandas as pd

data = pd.DataFrame({
    'hours': [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6],
    'scores': [45, 50, 52, 55, 58, 60, 62, 65, 68, 72, 75, 80]

})
print("DataFrame:")
print(data)

plt.scatter(data['hours'], data['scores'], s=100, alpha=0.5)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()
plt.show()
plt.savefig("study_hours_vs_score.png")