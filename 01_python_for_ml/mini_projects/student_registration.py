print("=" * 36)
print("      Student Registration")
print("=" * 36)

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = int(input("Enter your height (cm): "))
weight = int(input("Enter your weight (kg): "))
university = input("Enter your university: ")
department = input("Enter your department: ")
cgpa = float(input("Enter your CGPA: "))
country = input("Enter your country: ")


is_student = True

print("\n" + "=" * 36)
print("      Student Registration")
print("=" * 36)

print(f"Name        : {name}")
print(f"Age         : {age}")
print(f"Height      : {height} cm")
print(f"Weight      : {weight} kg")
print(f"University  : {university}")
print(f"Department  : {department}")
print(f"CGPA        : {cgpa}")
print(f"Country     : {country}")

print("\n" + "=" * 36)

print("\nData Types")
print(f"Name        -> {type(name)}")
print(f"Age         -> {type(age)}")
print(f"Height      -> {type(height)}")
print(f"Weight      -> {type(weight)}")
print(f"CGPA        -> {type(cgpa)}")
print(f"Is Student  -> {type(is_student)}")