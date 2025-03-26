import math


def area(r):
    if r < 0:
        return "Incorrect input: negative number"
    else:
        return math.pi * r * r


def perimeter(r):
    if r < 0:
        return "Incorrect input: negative number"
    else:
        return 2 * math.pi * r
