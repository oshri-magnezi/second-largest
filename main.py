def second_largest(numbers):
    unique = sorted(set(numbers))
    if len(unique) < 2:
        raise ValueError("Need at least two distinct numbers")
    return unique[-2]

class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(4, 5)
    print("Rectangle area =", rect.area())
