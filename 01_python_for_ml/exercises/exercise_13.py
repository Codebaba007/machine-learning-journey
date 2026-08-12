try: 
    age = int(input("Enter your age: "))
    print(age)

except:
    print("Invaild Input")

try:
    num1=int(input("Enter the first Number: "))
    num2=int(input("Enter the second Number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Cant divide by zero")    

numbers = [10, 20, 30]

try:
    index = int(input("Enter an index: "))
    print("Value:", numbers[index])

except IndexError:
    print("Index does not exist.")

student = {
    "name": "Mehedi",
    "age": 23,
    "department": "CSE"
}

try:
    key = input("Enter a key: ")
    print("Value:", student[key])

except KeyError:
    print("Key does not exist.")

try:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    result = first / second

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")