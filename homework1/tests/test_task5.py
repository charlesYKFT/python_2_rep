import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python ideal repo/homework1/')

from tasks.task05 import find_maximal_subarray_sum
import pytest


@pytest.mark.parametrize("array, k, expected_result", [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
                                                       ([1, 2, 3, 4, 5], 2, 9),
                                                       ([-1, -2, 3, -4, 5, 56], 4, 60),
                                                       ([95, 31, 86, 48, 93, 64,
                                                        44, 36, 78, 81], 6, 396),
                                                       ([52, 19, 88, 9, 10, 66, 22, 84, 52, 80], 5, 304)])
def test_find_max_subarray_sum_yes(array, k, expected_result):
    """Tests whether find_max_subarray_sum returns the max sum of subarray """
    assert find_maximal_subarray_sum(array, k) == expected_result


@pytest.mark.parametrize("array, k, expected_error", [(5, 2, TypeError),
                                                      ([1, 2, "3"], 4, TypeError),
                                                      ([1, 2, 3, 4, 5], 2.5, TypeError)])
def test_find_maximal_subarray_sum_errors(array, k, expected_error):
    """Tests whether find_max_subarray_sum returns the correct error"""
    with pytest.raises(expected_error):
        find_maximal_subarray_sum(array, k)


if __name__ == '__main__':
    pytest.main()
