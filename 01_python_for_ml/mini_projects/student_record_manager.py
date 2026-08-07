print("====================================")
print("      Student Record Manager")
print("====================================")

students = []

while True:

    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. View Students")
    print("4. Total Students")
    print("5. Exit")

    choice = int(input("\nChoose an option: "))

    if choice == 1:

        name = input("Enter student name: ")

        students.append(name)

        print("Student added successfully.")

    elif choice == 2:

        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    elif choice == 3:

        if len(students) == 0:
            print("No students available.")

        else:
            print("\n===== Student List =====")

            count = 1

            for student in students:
                print(count, ".", student)
                count = count + 1

            print("========================")

    elif choice == 4:

        print("Total Students =", len(students))

    elif choice == 5:

        print("Thank you for using Student Record Manager.")
        break

    else:

        print("Invalid option. Please try again.")