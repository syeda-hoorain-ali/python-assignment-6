class Countdown:
    """A custom iterable class that counts down from a given starting number to 0.
    Attributes:
        current (int): The current number in the countdown.
    """

    def __init__(self, start_num: int):
        self.current = start_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


if __name__ == '__main__':
    countdown = Countdown(10)
    for num in countdown:
        print(num)
