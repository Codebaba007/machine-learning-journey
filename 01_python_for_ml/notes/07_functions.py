def greet(name):
    print("Welcome to Python", name)


name = input("Enter your name: ")

greet(name)

def add(a, b):
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum =", result)

def square(number):
    return number * number


number = int(input("Enter a number: "))

result = square(number)

print("Square =", result)

def chec_even(num):
    if number % 2 ==0:
        return "Even"
    else:
        return "odd"

num = int(input("Enter a number: "))

result = chec_even(num)
print(result)

def max(a, b):
    if a>b:
        return a
    else:
        return b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest = max(num1, num2)

print("Largest Number =", largest)