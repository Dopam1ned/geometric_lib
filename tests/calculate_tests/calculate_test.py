from geometric_lib.calculate import calc
import pytest


def test_int_valid_input():
    fig = "triangle"
    fun = "area"
    size = [3, 4, 5]
    expected = 6
    result = calc(fig, fun, size)
    assert expected == result


def test_float_valid_input():
    fig = "square"
    fun = "perimeter"
    size = [2.5]
    expected = 10
    result = calc(fig, fun, size)
    assert expected == result


def test_invalid_input():
    fig = "unknown"
    fun = "area"
    size = [2.5]
    with pytest.raises(AssertionError):
        calc(fig, fun, size)
