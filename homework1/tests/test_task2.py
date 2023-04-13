import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/')
from tasks.task02 import check_fibonacci
import pytest


@pytest.mark.parametrize("array, expected_result", [([0], True),
                                                    ([0, 1], True),
                                                    ([0, 1, 1], True),
                                                    ([0, 1, 1, 2, 3, 5,
                                                     8, 13, 21], True),
                                                    ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765], True)])
def test_check_fibonacci_yes(array, expected_result):
    """Tests whether check_fibonacci returns True when it actuallly get fibbonaci sequunce"""
    assert check_fibonacci(array) == expected_result


@pytest.mark.parametrize("array, expected_result", [([1], False),
                                                    ([0, 2], False),
                                                    ([0, 1, 5], False),
                                                    ([0, 1, 1, 2, 3, 5,
                                                     100, 13, 21], False),
                                                    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 133, 245, 888], False)])
def test_check_fibonacci_no(array, expected_result):
    """Tests whether check_fibonacci returns False when it actuallly get usual list"""
    assert check_fibonacci(array) == expected_result


@pytest.mark.parametrize("array, expected_error", [(1, TypeError),
                                                   (2.5, TypeError),
                                                   (True, TypeError),
                                                   ("hey", TypeError),
                                                   ({"key": "value"}, TypeError),
                                                   (None, TypeError)])
def test_check_fibonacci_errors(array, expected_error):
    """Tests whether check_fibonacci returns correct error when it actuallly get something that is not a list"""
    with pytest.raises(expected_error):
        check_fibonacci(array)


if __name__ == '__main__':
    pytest.main()
