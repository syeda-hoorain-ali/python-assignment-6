class Product:
    """A class to manage product price with property decorators.
    Attributes:
        name (str) : The Name of the product
        price (float) : Price of the product
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = price

    @property
    def price(self) -> float:
        """Get the price of the product."""
        return self.__price

    @price.setter
    def price(self, price: float):
        """Set the price of the product. Raises ValueError if price is non-positive."""
        if price <= 0:
            raise ValueError("Price cannot be negative or zero")
        self.__price = price

    @price.deleter
    def price(self):
        """Delete the price of the product."""
        print("Removing price...")
        del self.__price


if __name__ == '__main__':
    obj = Product("Book", 100)
    print(obj.price)
    
    # obj.price = 0 #! Raises ValueError 
    obj.price = 200
    print(obj.price)
    
    del obj.price
    # obj.price    #! Raises AttributeError
    