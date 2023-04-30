import pytest
import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework3/')

from tasks.task03 import Filter, make_filter, sample_data

def test_positive_even():
    """Tests whether the positive_even.apply(range(100)) returns only even numbers from 0 to 99"""
    positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
    assert positive_even.apply(range(100)) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

def test_sample_data():
    """Tests whether make_filter(name='polly', type='bird').apply(sample_data) returns only second entry from the list"""
    assert make_filter(name='polly', type='bird').apply(sample_data) == [sample_data[1]]

if __name__ == '__main__':
    pytest.main()
