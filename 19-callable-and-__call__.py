class Multiplier:
    """
    A callable class that multiplies a given number by a predefined factor.            
    """
    
    def __init__(self, factor: int):
        self.factor = factor
    
    def __call__(self, num: int):
        """Multiplies the input number by the factor and returns the result."""
        return self.factor * num


if __name__ == '__main__':
    mutiply_5 = Multiplier(5)

    print(f"5 multiply by 5 is {mutiply_5(5)}")
    print(f"5 multiply by 3 is {mutiply_5(3)}")
    print(f"multiply_5 is callable {callable(mutiply_5)}")
