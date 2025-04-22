from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for geometric shapes."""

    def __init__(self, width: float, height: float):
        ...

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape and implements the area method.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.width * self.height


if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print(f"The area of the rectangle is: {rect.area()}")
