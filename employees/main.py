class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}."
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["developer", "designer", "manager"]
        return position in valid_positions
    
employee1 = Employee("John", "developer")
employee2 = Employee("Jane", "designer")
employee3 = Employee("Bob", "Cook")
print(employee1.is_valid_position("developer"))
print(employee2.is_valid_position("developer"))
print(employee3.is_valid_position("Cook"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
