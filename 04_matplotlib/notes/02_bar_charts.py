import matplotlib.pyplot as plt
'''
subjects = ["Python", "Java", "C++", "JavaScript", "Ruby"]
scores = [85, 78, 92, 88, 76]
plt.bar(subjects, scores)

plt.title("Student Scores in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")

plt.show()


import matplotlib.pyplot as plt

subjects = ["Python", "NumPy", "Pandas", "ML"]
scores = [85, 78, 92, 88]

plt.bar(subjects, scores, width=0.5)

plt.title("Learning Scores")
plt.xlabel("Subjects")
plt.ylabel("Score")

plt.grid(axis="y")

plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Subject": ["Python", "NumPy", "Pandas", "Matplotlib"],
    "Score": [85, 78, 92, 90]
})

plt.bar(data["Subject"], data["Score"])

plt.title("Subject Scores")
plt.xlabel("Subject")
plt.ylabel("Score")

plt.grid(axis="y")

plt.show()