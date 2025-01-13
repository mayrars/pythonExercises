class Student:

    class_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
student1 = Student("John", 20)
student2 = Student("Jane", 22)
student3 = Student("Bob", 21)

print(student1.name)
print(student2.age)
print(student3.class_year)