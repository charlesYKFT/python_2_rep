import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

import pytest
from tasks.hw5 import custom_range
import string



def test_custom_range_yes():
    """Tests whether custom_range() returns the correct result."""
    assert custom_range(string.ascii_lowercase, 'g') == [
        'a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == [
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p',
                        'g', -2) == ['p', 'n', 'l', 'j', 'h']


def test_custom_range_error():
    """Tests whether custom_range() returns the correct exception"""
    assert custom_range(2, 'g') == TypeError
    assert custom_range(custom_range, 'g', 'p') == TypeError
    assert custom_range(string, 'g', 'p', -2) == TypeError


if __name__ == '__main__':
    pytest.main()
