from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class ShapeAreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()

# Exemplo de uso
calculator = ShapeAreaCalculator()
rectangle = Rectangle(4.0, 5.0)
circle = Circle(3.0)

print(calculator.calculate_area(rectangle))  # Output: 20.0
print(calculator.calculate_area(circle))  # Output: 28.26