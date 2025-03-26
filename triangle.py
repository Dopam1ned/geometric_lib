import math


def area(a, b, c):
    if (
        not isinstance(a, (int, float))
        or not isinstance(b, (int, float))
        or not isinstance(c, (int, float))
    ):
        return "Incorrect input: not a number"
    elif (a < 0) or (b < 0) or (c < 0):
        return "Incorrect input: negative number"
    elif (a + b <= c) or (c + b <= a) or (a + c <= b):
        return "Triangle doesn't exist"
    else:
        p = (a + b + c) / 2
        return math.sqrt(p*(p - a)*(p - b)*(p - c))


def perimeter(a, b, c):
    if (
        not isinstance(a, (int, float))
        or not isinstance(b, (int, float))
        or not isinstance(c, (int, float))
    ):
        return "Incorrect input: not a number"
    elif (a <= 0) or (b <= 0) or (c <= 0):
        return "Incorrect input: negative or equal to zero number"
    elif (a + b <= c) or (c + b <= a) or (a + c <= b):
        return "Triangle doesn't exist"
    else:
        return a + b + c
