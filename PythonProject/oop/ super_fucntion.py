# super = function used in a child class to call methods from a parent class (superclass).
#         Allows you to extend the funtionality of the inherited methods

class Shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self): #overide
        print(f"It is a circle with an area of {3.1415926 * (self.radius * self.radius):.2f} cm²")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self): #overide
        print(f"It is a square with an area of {self.width * self.width:.2f} cm²")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, heigth):
        super().__init__(color, is_filled)
        self.width = width
        self.heigth = heigth

    def describe(self): #overide
        print(f"It is a triangle with an area of {(self.width * self.heigth / 2):.2f} cm²")
        super().describe()

circle = Circle("Red", True, 5)
square = Square("Blue", False, 6)
triangle = Triangle("Yellow", True, 3, 4)


circle.describe()
square.describe()
triangle.describe()