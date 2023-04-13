import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/')

from tasks.task04 import check_sum_of_four
import pytest


@pytest.mark.parametrize("a,b,c,d, expected_result", [([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
                                                      ([1, 2, 3], [4, 5, 6], [
                                                       7, 8, 8], [10, 11, 12], 0),
                                                      ([1, 2, 3, 4], [-1, 2, -3, 4], [1, -2, 3, -4], [-1, -2, -3, 4], 22)])
def test_check_sum_of_four_yes(a, b, c, d, expected_result):
    """Tests whether check_sum_of_four returns the correct number of tuples (i,j,k,l) that A[i] + B[j] + C[k] + D[l] is zero"""
    assert check_sum_of_four(a, b, c, d) == expected_result


@pytest.mark.parametrize("a,b,c,d, expected_error", [([1, 2], ["-2", -1], [-1, 2], [0, 2], TypeError),
                                                     ("wrong_input",
                                                      [-2, -1], [-1, 2], [0, 2], TypeError),
                                                     ([1, 2], [-2.5, -1],
                                                      [-1, 2], [0, 2], TypeError),
                                                     ([1, 2], [-2, -1], (-1, 2), [0, 2], TypeError)])
def test_check_sum_of_four_error(a, b, c, d, expected_error):
    """Tests whether check_sum_of_four returns the error if it gets wrong arguments"""
    with pytest.raises(expected_error):
        check_sum_of_four(a, b, c, d)


if __name__ == '__main__':
    pytest.main()
