import pytest
from geometric_lib import square

def test_positive_input():
    side = 5
    expected = 5 * 5
    result = area(side)
    assert result == expected

def test_zero_input():
    side = 0
    expected = 0
    result = area(side)
    assert result == expected

def test_negative_input():
    side = -4
    expected = "Incorrect input: negative number"
    result = area(side)
    assert result == expected

def test_float_input():
    side = 2.5
    expected = 2.5 * 2.5
    result = area(side)
    assert result == expected

def test_nan_input():
    side = "abc"
    expected = "Incorrect input: not a number"
    result = area(side)
    assert result == expected