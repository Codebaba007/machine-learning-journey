def add_student():
    name = input("Enter student name: ")
    department = input("Enter department: ")
    cgpa = input("Enter CGPA: ")

    with open("students.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Department: {department}\n")
        file.write(f"CGPA: {cgpa}\n")
        file.write("--------------------\n")

    print("Student information saved.")


def view_students():
    try:
        with open("students.txt", "r") as file:
            content = file.read()

        print("\nStudent Records")
        print("--------------------")
        print(content)

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\nStudent Data File Manager")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program finished.")
        break

    else:
        print("Invalid choice.")