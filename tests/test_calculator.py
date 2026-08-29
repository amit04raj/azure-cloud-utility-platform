import pytest

from app.calculator import calculate


def test_addition():
    assert calculate("addition", 25, 10) == 35


def test_subtraction():
    assert calculate("subtraction", 25, 10) == 15


def test_multiplication():
    assert calculate("multiplication", 12, 5) == 60


def test_division():
    assert calculate("division", 100, 4) == 25


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate("division", 10, 0)


def test_unsupported_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        calculate("something", 10, 5)