
student_name = input("Enter Student Name: ")
student_id = int(input("Enter Student ID: "))
department = input("Enter Department: ")
marks = float(input("Enter Marks (0-100): "))


if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks <= 89:
    grade = "B"
elif 70 <= marks <= 79:
    grade = "C"
elif 60 <= marks <= 69:
    grade = "D"
elif 40 <= marks <= 59:
    grade = "E"
elif 0 <= marks <= 39:
    grade = "F"
else:
    print("Invalid Marks!")
    exit()

# Determine Result
if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n=====================================")
print("        Student Grade Report")
print("=====================================\n")

print(f"Student Name : {student_name}")
print(f"Student ID   : {student_id}")
print(f"Department   : {department}")
print(f"Marks        : {marks}")

print(f"\nGrade        : {grade}")
print(f"Result       : {result}")