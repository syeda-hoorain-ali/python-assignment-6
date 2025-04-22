class Dog:
    """A class to represent a dog.
    Attributes:
        name (str): The name of the dog.
        breed (str): The breed of the dog.
    """
    
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self):
        """Prints a message including the dog's name."""
        print(f"{self.name} says: Woof! Woof!")


if __name__ == "__main__":
    my_dog = Dog(name="Buddy", breed="Golden Retriever")
    print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
    my_dog.bark()
