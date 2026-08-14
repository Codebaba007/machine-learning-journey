class Student:
    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("CGPA:", self.cgpa)
        print("--------------------")


students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    department = input("Enter department: ")
    cgpa = float(input("Enter CGPA: "))

    student = Student(name, age, department, cgpa)
    students.append(student)

    print("Student added successfully.")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\nStudent Records")
    print("====================")

    for student in students:
        student.show_info()


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student.name.lower() == name.lower():
            print("\nStudent Found")
            print("====================")
            student.show_info()
            return

    print("Student not found.")


while True:
    print("\nStudent Management System")
    print("=========================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program finished.")
        break

    else:
        print("Invalid choice.")