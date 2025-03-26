from geometric_lib.triangle import area
import math

def test_positive_sides():
    a, b, c = 3, 4, 5
    expected = 6
    result = area(a, b, c)
    assert result == expected

def test_negative_sides():
    test_cases = [
        (-1, 2, 3, "Incorrect input: negative number"),
        (1, -2, 3, "Incorrect input: negative number"),
        (1, 2, -3, "Incorrect input: negative number")
    ]
    
    for a, b, c, expected in test_cases:
        result = area(a, b, c)
        
        assert result == expected

def test_zero_sides():
    test_cases = [
        (0, 2, 3, "Triangle doesn't exist"),
        (1, 0, 3, "Triangle doesn't exist"),
        (1, 2, 0, "Triangle doesn't exist")
    ]
    
    for a, b, c, expected in test_cases:
        result = area(a, b, c)
        
        assert result == expected

def test_impossible_triangle():
    test_cases = [
        (1, 2, 10, "Triangle doesn't exist"),
        (10, 1, 2, "Triangle doesn't exist"),
        (1, 10, 2, "Triangle doesn't exist")
    ]
    
    for a, b, c, expected in test_cases:
        result = area(a, b, c)
        
        assert result == expected

def test_float_sides():
    a, b, c = 0.3, 0.4, 0.5
    expected = 0.06
    result = area(a, b, c)
    assert abs(result - expected) < 1e-8

def test_mixed_arg():
    a, b, c = 3, 4, 5.1
    expected = (11 * math.sqrt(47519)) / 400
    result = area(a, b, c)
    assert abs(result - expected) < 1e-8

def test_invalid_args():
    test_cases = [
        ("abc", 2, 3, "Incorrect input: not a number"),
        (1, "abc", 3, "Incorrect input: not a number"),
        (1, 2, "abc", "Incorrect input: not a number")
    ]
    
    for a, b, c, expected in test_cases:
        result = area(a, b, c)
        
        assert result == expected

