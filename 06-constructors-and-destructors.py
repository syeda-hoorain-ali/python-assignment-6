class Logger:
    """
    Logger class demonstrates the use of constructors and destructors in Python.
    """
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")


if __name__ == '__main__':
    obj = Logger()
    del obj
