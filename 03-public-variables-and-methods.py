class Car:
    """
    A class to represent a Car with a public variable and method.
    Attributes:
        brand (str): The brand of the car.
    """
   
    def __init__(self, brand: str):
        self.brand = brand  # Public variable

    def start(self):
        """Public method to simulate starting the car."""
        return f"The {self.brand} car has started."


if __name__ == '__main__':
    my_car = Car("Toyota")
    print(my_car.brand)
    print(my_car.start())
