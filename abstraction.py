from abc import ABC, abstractmethod

# Abstract base class for Shape
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class: Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class: Square
class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# Usage of the Shape classes
circle = Circle("red", 5)
square = Square("blue", 4)

print(f"Circle Area: {circle.area()}")        # Output: Circle Area: 78.5
print(f"Circle Perimeter: {circle.perimeter()}")  # Output: Circle Perimeter: 31.400000000000002
print(f"Square Area: {square.area()}")        # Output: Square Area: 16
print(f"Square Perimeter: {square.perimeter()}")  # Output: Square Perimeter: 16
