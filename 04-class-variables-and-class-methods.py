class Bank:
    """
    A class representing a bank with a class variable for the bank name and a class method to modify it.
    Attributes:
        bank_name (str): The name of the bank. This is a class variable shared across all instances.
    """
    bank_name: str = "My Bank"
    
    @classmethod
    def change_bank_name(cls, name: str):
        """Changes the name of the bank by modifying the class variable `bank_name`."""
        Bank.bank_name = name


if __name__ == '__main__':
    bank1 = Bank()
    bank2 = Bank()

    print(f"Initial bank name (bank1): {bank1.bank_name}")
    print(f"Initial bank name (bank2): {bank2.bank_name}")

    Bank.change_bank_name("Global Bank")
    print(f"Updated bank name (bank1): {bank1.bank_name}")
    print(f"Updated bank name (bank2): {bank2.bank_name}")
