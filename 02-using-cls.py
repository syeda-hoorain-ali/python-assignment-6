class Counter:
    """
    A class to keep track of the number of instances created.
    Attributes:
        count (int): A class-level attribute that keeps track of the total number of Counter instances.
    """
    
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        """Class method that returns the current count of Counter instances."""
        return cls.count


if __name__ == '__main__':
    obj1 = Counter()
    obj2 = Counter()

    print("Number of Counter objects created:", Counter.get_count())
