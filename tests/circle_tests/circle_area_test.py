import math
import pytest
from geometric_lib.circle import area


def test_positive_input():
    radius = 3
    expected = math.pi * 3 * 3
    result = area(radius)
    assert result == expected


def test_zero_input():
    radius = 0
    expected = 0
    result = area(radius)
    assert result == expected


def test_negative_input():
    radius = -4
    expected = "Incorrect input: negative number"
    result = area(radius)
    assert result == expected


def test_float_input():
    radius = 2.5
    expected = math.pi * 2.5 * 2.5
    result = area(radius)
    assert result == expected


def test_nan_input():
    radius = "abc"
    with pytest.raises(TypeError):
        area(radius)
