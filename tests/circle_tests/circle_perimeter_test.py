import math
import pytest
from geometric_lib import circle

def test_positive_input():
    side = 3
    expected = 2 * math.pi * 3
    result = perimeter(side)
    assert result == expected

def test_zero_input():
    side = 0
    expected = 0
    result = perimeter(side)
    assert result == expected

def test_negative_input():
    side = -4
    expected = "Incorrect input: negative number"
    result = perimeter(side)
    assert result == expected

def test_float_input():
    side = 2.5
    expected = 2 * math.pi * 2.5
    result = perimeter(side)
    assert result == expected

def test_nan_input():
    side = "abc"
    expected = "Incorrect input: not a number"
    result = perimeter(side)
    assert result == expected