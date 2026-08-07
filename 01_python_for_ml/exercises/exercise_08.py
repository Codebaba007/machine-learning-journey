lan = ["java","Python","C"]
print(lan)
print(lan[0])
print(lan[-1])

num = [10, 20, 30, 40, 50]
print(num)
num.append(68)
num.insert(1,15)
num.remove(40)
print(num)

students = [
    "Mehedi",
    "Hasan",
    "Rahim",
    "Karim",
    "Sakib"
]
for student in students:
    print(student)


marks = [75, 82, 91, 68, 88]

total = 0

for mark in marks:
    total = total + mark

print("Total Marks: ",total)

marks = [75, 82, 91, 68, 88]

highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

print("Highest Mark =", highest)