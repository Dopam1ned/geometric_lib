from geometric_lib.triangle import perimeter


def test_positive_sides():
    a, b, c = 3, 4, 5
    expected = 12
    result = perimeter(a, b, c)
    assert result == expected


def test_negative_sides():
    test_cases = [
        (-1, 2, 3, "Incorrect input: negative or equal to zero number"),
        (1, -2, 3, "Incorrect input: negative or equal to zero number"),
        (1, 2, -3, "Incorrect input: negative or equal to zero number")
    ]

    for a, b, c, expected in test_cases:
        result = perimeter(a, b, c)

        assert result == expected


def test_zero_sides():
    test_cases = [
        (0, 2, 3, "Incorrect input: negative or equal to zero number"),
        (1, 0, 3, "Incorrect input: negative or equal to zero number"),
        (1, 2, 0, "Incorrect input: negative or equal to zero number")
    ]

    for a, b, c, expected in test_cases:
        result = perimeter(a, b, c)

        assert result == expected


def test_impossible_triangle():
    test_cases = [
        (1, 2, 10, "Triangle doesn't exist"),
        (10, 1, 2, "Triangle doesn't exist"),
        (1, 10, 2, "Triangle doesn't exist")
    ]

    for a, b, c, expected in test_cases:
        result = perimeter(a, b, c)

        assert result == expected


def test_float_sides():
    a, b, c = 0.3, 0.4, 0.5
    expected = 1.2
    result = perimeter(a, b, c)
    assert abs(result - expected) < 1e-8


def test_mixed_arg():
    a, b, c = 3, 4, 5.1
    expected = 12.1
    result = perimeter(a, b, c)
    assert abs(result - expected) < 1e-8


def test_invalid_args():
    test_cases = [
        ("abc", 2, 3, "Incorrect input: not a number"),
        (1, "abc", 3, "Incorrect input: not a number"),
        (1, 2, "abc", "Incorrect input: not a number")
    ]

    for a, b, c, expected in test_cases:
        result = perimeter(a, b, c)

        assert result == expected
