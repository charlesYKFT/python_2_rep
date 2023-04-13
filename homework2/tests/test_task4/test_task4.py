import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

from tests.test_task4.test_functions import *
from tasks.hw4 import cache
import pytest



def test_cache_function():
    """Test cache_function() with different functions from a file"""
    cached_sum_of_two = cache(sum_of_two)
    result1 = cached_sum_of_two(5, 2)
    cashed_multiply = cache(multiply)
    result2 = cashed_multiply(10, 2)
    cashed_squaring = cache(squaring)
    result3 = cashed_squaring(256)
    cashed_gcd = cache(gcd)
    result4 = cashed_gcd(100, 60)

    assert sum_of_two(5, 2) == cached_sum_of_two(5, 2)
    assert multiply(10, 2) == cashed_multiply(10, 2)
    assert squaring(256) == cashed_squaring(256)
    assert gcd(100, 60) == cashed_gcd(100, 60)


if __name__ == '__main__':
    pytest.main()
