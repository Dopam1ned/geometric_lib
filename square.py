
def area(a):
    if not isinstance(a, (int, float)):
        return "Incorrect input: not a number"
    elif a < 0:
        return "Incorrect input: negative number"
    else:
        return a * a


def perimeter(a):
    if not isinstance(a, (int, float)):
        return "Incorrect input: not a number"
    elif a < 0:
        return "Incorrect input: negative number"
    else:
        return 4 * a