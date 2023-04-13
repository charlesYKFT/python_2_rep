import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

import pytest
from tasks.hw3 import combinations



def test_combinations_yes():
    """Tests whether combinations() returns correct result"""
    assert combinations([1, 10], [2, 20]) == [
        [1, 2], [1, 20], [10, 2], [10, 20]]
    assert combinations([1, 2], [3, 4], [5, 6]) == [[1, 3, 5], [1, 3, 6], [
        1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]


@pytest.mark.parametrize("wrong_arguments, excepted_error", [(1, TypeError),
                                                             ("5", TypeError),
                                                             ({"key": "value"},
                                                              TypeError)
                                                             ])
def test_combinations_error(wrong_arguments, excepted_error):
    """Tests whether combinations() returns the correct exception"""
    with pytest.raises(excepted_error):
        combinations(wrong_arguments)


if __name__ == '__main__':
    pytest.main()
