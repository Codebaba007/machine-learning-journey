grades = {}

for i in range(4):
    subject = input("Enter subject: ")
    mark = int(input("Enter mark: "))

    grades[subject] = mark

print()
print("=================================")
print("          Student Grade Book")
print("=================================")

for subject, mark in grades.items():
    print(subject, ":", mark)

total = 0

for mark in grades.values():
    total = total + mark

average = total / len(grades)

highest = 0
highest_subject = ""

for subject, mark in grades.items():
    if mark > highest:
        highest = mark
        highest_subject = subject

print("---------------------------------")
print("Total Marks     :", total)
print("Average         :", average)
print("Highest Mark    :", highest)
print("Highest Subject :", highest_subject)
print("=================================")