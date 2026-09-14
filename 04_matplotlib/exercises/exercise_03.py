import matplotlib.pyplot as plt 

hours = [1, 2, 3, 4, 5, 6, 7,8]
Exam_Scores = [45, 50, 58, 65, 72, 80, 85, 90]
plt.scatter(hours, Exam_Scores, s=100, alpha=0.7)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()
plt.show()
plt.savefig("scatter_plot.png")