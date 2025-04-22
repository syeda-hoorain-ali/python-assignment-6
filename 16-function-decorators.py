from typing import Callable

def log_function_call(func: Callable) -> Callable:
    """
    A decorator that logs a message before calling the decorated function.
    """
    def wrapper():
        print("Function is being called")
        func()
    return wrapper


@log_function_call
def say_hello():
    print("Hello, World!")


if __name__ == '__main__':
    say_hello()
