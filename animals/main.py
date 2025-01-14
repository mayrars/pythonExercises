class Animal:
    def __init__(self, name, is_hungry):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    pass

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing.")
class Mouse(Animal):
    pass

dog = Dog("Fido",True)
cat = Cat("Whiskers",True)
mouse = Mouse("Jerry",True)

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()