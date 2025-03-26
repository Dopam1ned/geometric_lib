import math


def area(r):
    if not isinstance(r, (int, float)):
        return "Incorrect input: not a number"
    elif r < 0:
        return "Incorrect input: negative number"
    else:
        return math.pi * r * r


def perimeter(r):
    if not isinstance(r, (int, float)):
        return "Incorrect input: not a number"
    elif r < 0:
        return "Incorrect input: negative number"
    else:
        return 2 * math.pi * r
