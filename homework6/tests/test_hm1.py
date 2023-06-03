import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework6')
import pytest
from tasks.hw1 import find_occurrences


@pytest.mark.parametrize("tree, element, expected_count", [
                                            ({'a': 'RED', 'b': 'GREEN', 'c': 'BLUE'}, 'RED', 1),
                                            ({'a': 'RED', 'b': ['RED', 'GREEN'], 'c': {'d': 'RED'}}, 'RED', 3),
                                            ({'a': 'RED', 'b': ['RED', 'GREEN'], 'c': {'d': 'RED'}}, 'GREEN', 1),
                                            ({'a': 'RED', 'b': ['RED', 'GREEN'], 'c': {'d': 'RED'}}, 'YELLOW', 0),])
def test_find_occurrences(tree, element, expected_count):
    """Tests whether find_occurences returns the correct number of occurences"""
    assert find_occurrences(tree, element) == expected_count



if __name__ == '__main__':
    pytest.main()
