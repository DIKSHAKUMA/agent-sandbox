import pytest

from calculator import average, divide


def test_divide_works():
    assert divide(10, 2) == 5


def test_average_works():
    assert average([2, 4, 6]) == 4


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_average_of_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        average([])
