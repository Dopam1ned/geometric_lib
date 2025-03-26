from geometric_lib.calculate import calc
import pytest
import math

def test_int_valid_input():
    fig = "circle"
    fun = "area"
    size = [5]
    expected = math.pi * 5 * 5
    result = calc(fig, fun, size)
    assert expected == result

def test_float_valid_input():
    fig = "circle"
    fun = "area"
    size = [2.5]
    expected = math.pi * 2.5 * 2.5
    result = calc(fig, fun, size)
    assert expected == result

def test_invalid_input():
    fig = "unknown"
    fun = "area"
    size = [2.5]
    with pytest.raises(TypeError):
        calc(fig, fun, size)