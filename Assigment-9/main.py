# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating rectangle objects and printing their areas
rectangle_one = Rectangle(5, 7)
print(f"Area of rectangle_one: {rectangle_one.area()}")

rectangle_two = Rectangle(5, 4)
print(f"Area of rectangle_two: {rectangle_two.area()}")

rectangle_three = Rectangle(8, 6)
print(f"Area of rectangle_three: {rectangle_three.area()}")
