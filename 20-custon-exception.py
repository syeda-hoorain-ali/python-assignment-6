class InvalidAgeError(Exception):
    pass

def check_age(age: int):
    if age < 18:
        raise InvalidAgeError("Age must be 18+")    
    return True


if __name__ == '__main__':
    try:
        check_age(15)
    except InvalidAgeError as e:
        print(f"Error: {e}")
