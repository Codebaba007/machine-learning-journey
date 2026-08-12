try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = first_number + second_number

    elif operation == "-":
        result = first_number - second_number

    elif operation == "*":
        result = first_number * second_number

    elif operation == "/":
        result = first_number / second_number

    else:
        print("Invalid operation.")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Calculation finished.")