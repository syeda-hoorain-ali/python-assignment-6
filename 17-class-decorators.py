from typing import Type, TypeVar

T = TypeVar('T', bound=Type)

def add_greeting(cls: T) -> T:
    """
    A class decorator that adds a 'greet' method to the class.
    """

    def greet(self: object) -> str:
        """
        A greeting method added by the decorator.
        
        Returns:
            str: A greeting message.
        """
        return "Hello from Decorator!"
    
    setattr(cls, 'greet', greet)
    return cls


@add_greeting
class Person:
    """
    A simple class representing a person.
    
    Attributes:
        name (str): The name of the person.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes a Person instance with a name.
        
        Args:
            name (str): The name of the person.
        """
        self.name = name


# Create an instance of Person and call the greet method
obj = Person('a')
print(obj.greet())



