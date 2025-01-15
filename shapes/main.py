class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"This shape is {self.color} and is {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2} and a circumference of {2 * 3.14 * self.radius}")
        super().describe()
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
square = Square("blue", False, 10)

circle.describe()