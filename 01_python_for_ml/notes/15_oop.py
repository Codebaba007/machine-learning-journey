# Day 15 — Object-Oriented Programming (OOP)


# ============================================================
# 1. What is Object-Oriented Programming?
# ============================================================

# OOP is a programming approach where we organize code using
# classes and objects.

# A class is a blueprint.
# An object is an actual instance created from that blueprint.

# Example:
# Class  -> Student
# Object -> student1, student2


# ============================================================
# 2. Creating a Class
# ============================================================

class Student:
    pass


# Creating objects from the Student class

student1 = Student()
student2 = Student()

print(student1)
print(student2)


# ============================================================
# 3. Attributes
# ============================================================

# Attributes are data that belong to an object.

student1.name = "Mehedi"
student1.age = 23
student1.department = "CSE"
student1.cgpa = 3.50

print(student1.name)
print(student1.age)
print(student1.department)
print(student1.cgpa)


# Different objects can have different attributes/data.

student2.name = "Rahim"
student2.age = 24
student2.department = "CSE"
student2.cgpa = 3.70

print(student2.name)
print(student2.age)
print(student2.department)
print(student2.cgpa)


# ============================================================
# 4. The __init__() Method
# ============================================================

# __init__() is used to initialize an object when it is created.

class Student:

    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa


student1 = Student("Mehedi", 23, "CSE", 3.50)
student2 = Student("Rahim", 24, "CSE", 3.70)

print(student1.name)
print(student2.name)


# ============================================================
# 5. Understanding self
# ============================================================

# self refers to the current object.

# When we create:
#
# student1 = Student("Mehedi", 23, "CSE", 3.50)
#
# self refers to student1.
#
# When we create:
#
# student2 = Student("Rahim", 24, "CSE", 3.70)
#
# self refers to student2.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Mehedi", 23)
student2 = Student("Rahim", 24)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# ============================================================
# 6. Methods
# ============================================================

# A method is a function that belongs to a class.

class Student:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def introduce(self):
        print("My name is", self.name)
        print("I study", self.department)


student1 = Student("Mehedi", "CSE")

student1.introduce()


# ============================================================
# 7. Methods Using Attributes
# ============================================================

class Student:

    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def show_cgpa(self):
        print("CGPA:", self.cgpa)


student1 = Student("Mehedi", 23, 3.50)

student1.introduce()
student1.show_cgpa()


# ============================================================
# 8. Methods with Parameters
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name

    def study(self, subject):
        print(self.name, "is studying", subject)


student1 = Student("Mehedi")

student1.study("Python")
student1.study("Machine Learning")


# ============================================================
# 9. Updating Attributes
# ============================================================

class Student:

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def show_info(self):
        print("Name:", self.name)
        print("CGPA:", self.cgpa)


student1 = Student("Mehedi", 3.50)

student1.show_info()

# Updating an attribute

student1.cgpa = 3.60

student1.show_info()


# ============================================================
# 10. Multiple Objects
# ============================================================

class Student:

    def __init__(self, name, department, cgpa):
        self.name = name
        self.department = department
        self.cgpa = cgpa

    def show_info(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("CGPA:", self.cgpa)


student1 = Student("Mehedi", "CSE", 3.50)
student2 = Student("Rahim", "CSE", 3.70)
student3 = Student("Karim", "SWE", 3.40)

student1.show_info()
print()

student2.show_info()
print()

student3.show_info()


# ============================================================
# 11. Returning Values from Methods
# ============================================================

class Student:

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


student1 = Student("Mehedi", 3.50)

result = student1.get_cgpa()

print("CGPA:", result)


# ============================================================
# 12. Combining Conditions with Methods
# ============================================================

class Student:

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def check_result(self):

        if self.cgpa >= 3.00:
            return "Good standing"

        else:
            return "Needs improvement"


student1 = Student("Mehedi", 3.50)
student2 = Student("Rahim", 2.80)

print(student1.name, "-", student1.check_result())
print(student2.name, "-", student2.check_result())


# ============================================================
# 13. Important OOP Vocabulary
# ============================================================

# Class
# A blueprint/template used to create objects.

# Object
# An actual instance of a class.

# Attribute
# Data belonging to an object.

# Method
# A function belonging to a class.

# __init__()
# Initializes an object when it is created.

# self
# Refers to the current object.


# ============================================================
# 14. Basic OOP Structure
# ============================================================

class Example:

    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(self.value)


example = Example(100)

example.show_value()


# ============================================================
# 15. OOP and Machine Learning
# ============================================================

# Machine Learning libraries heavily use classes and objects.

# A model can be represented as an object:

# model = SomeModel()

# The model can then have methods such as:

# model.fit(...)
# model.predict(...)

# The general idea is:

# Model class
#      |
#      v
# Model object
#      |
#      +---- fit()
#      |
#      +---- predict()

# This style will become very familiar when we later work
# with libraries such as scikit-learn and other ML frameworks.