'''class student: 
    pass

student1 = student()

student1.name = "Mehedi"
student1.age  = 23
student1.department = "CSE"

print(student1.name)
print(student1.age)
print(student1.department)'''

class student:
    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa
    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("I study", self.department)
        print("My Grades is: ", self.cgpa)

student1 = student("Mehedi", 23, "CSE", 3.52)

student2 = student("Rahim", 22 , "EEE", 3.9)

student1.introduce()
print("\n")
student2.introduce()