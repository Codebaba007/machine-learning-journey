def get_grade(marks):
    """Returns the grade based on the marks."""
    if 90 <= marks <= 100:
        return "A"
    elif 80 <= marks <= 89:
        return "B"
    elif 70 <= marks <= 79:
        return "C"
    elif 60 <= marks <= 69:
        return "D"
    elif 40 <= marks <= 59:
        return "E"
    else:
        return "F"


def get_result(marks):
    """Returns Pass or Fail based on the marks."""
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


def display_report(name, student_id, department, marks, grade, result):
    """Displays the student grade report."""
    print("=" * 37)
    print("      Student Grade Report")
    print("=" * 37)
    print(f"Student Name : {name}")
    print(f"Student ID   : {student_id}")
    print(f"Department   : {department}")
    print(f"Marks        : {marks}")
    print()
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")
    print()
    print("=" * 37)


# Main Program
student_name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
department = input("Enter Department: ")
marks = float(input("Enter Marks: "))

grade = get_grade(marks)
result = get_result(marks)

display_report(student_name, student_id, department, marks, grade, result)