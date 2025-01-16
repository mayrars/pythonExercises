class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} is {self.age} years old and has a GPA of {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No students"
        else:
            return f"Average GPA: {cls.total_gpa / cls.count}"
    
student1 = Student("John", 20, 3.5)
student2 = Student("Jane", 22, 3.8)
student3 = Student("Bob", 21, 3.2)

print(Student.get_count())
print(Student.get_average_gpa())