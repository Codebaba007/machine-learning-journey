# Day 13 — Exception Handling

# ValueError

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Invalid age.")


# ZeroDivisionError

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# IndexError

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Index does not exist.")


# KeyError

student = {
    "name": "Mehedi",
    "age": 23
}

try:
    print(student["cgpa"])
except KeyError:
    print("Key does not exist.")