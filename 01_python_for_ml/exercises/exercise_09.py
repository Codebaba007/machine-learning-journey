Student = ("Mehedi",22,"CSE","UITS")
print(Student[0])

subjects = ("Python", "Mathematics", "Statistics", "Machine Learning")

for subject in subjects:
    print(subject)

numbers = (10, 20, 10, 30, 10, 40)

count = numbers.count(10)

print("10 appears", count, "times")
languages = ("Python", "Java", "C++", "JavaScript")

position = languages.index("C++")

print("C++ is at index", position)

numbers_list = [10, 20, 30]
numbers_tuple = (10, 20, 30)

numbers_list[0] = 100

print(numbers_list)

numbers_tuple[0] = 100

print(numbers_tuple)

marks = (75, 82, 91, 68, 88)

total = 0

for mark in marks:
    total = total + mark

print("Total Marks =", total)