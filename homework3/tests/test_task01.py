import pytest
import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework3/')
from tasks.task01 import cache

@cache(times=2)
def square(x):
    """This function returns the square of the number"""
    is_cached = False
    return (x**2, is_cached)

@cache(times=3)
def math_operation(x):
    """This function returns the result of a mathematical operation."""
    is_cached = False
    return (((x[0]+x[1])*2)**3, is_cached)

@pytest.mark.parametrize('input_to_function, expected_result, is_cached',[(3, 9, False),
                                                                         (3, 9, True),
                                                                         (3, 9, True),
                                                                         (3, 9, False)])

def test_square_cache(input_to_function, expected_result, is_cached):
    """Tests whether a square function returns the correct result with a correct number of cached results"""

    assert square(input_to_function) == (expected_result, is_cached)


@pytest.mark.parametrize('input_to_function, expected_result, is_cached',[((1,2), 216, False),
                                                                         ((1,2), 216, True),
                                                                         ((1,2), 216, True),
                                                                         ((1,2), 216, True),
                                                                         ((1,2), 216, False)])

def test_math_operation_cache(input_to_function, expected_result, is_cached):
    """Tests whether a math_operation function returns the correct result with a correct number of cached results"""
    assert math_operation(input_to_function) == (expected_result, is_cached)



if __name__ == '__main__':
    pytest.main()
