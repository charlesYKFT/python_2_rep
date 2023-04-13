import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

from tasks.hw2 import major_and_minor_elem
import pytest



@pytest.mark.parametrize("array, expected_result", [([3, 2, 3], (3, 2)),
                                                    ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
                                                    ([2, 5, 6, 6, 8, 7, 1,
                                                     8, 8, 7, 5, 2], (8, 1)),
                                                    ([1, 1, 1, 9, 9, 9, 9], (9, 1))])
def test_major_and_minor_element_yes(array, expected_result):
    """Tests whether major_and_minor_element() returns correct result"""
    assert major_and_minor_elem(array) == expected_result


@pytest.mark.parametrize("array, expected_error", [(1, TypeError),
                                                   ("1", TypeError),
                                                   ({1: 2}, TypeError),
                                                   ((1, 2, 3, 2), TypeError),
                                                   (major_and_minor_elem, TypeError)])
def test_major_and_minor_element_errors(array, expected_error):
    """Tests whether major_and_minor_element() returns correct error when it get something that is not a list"""
    with pytest.raises(expected_error):
        major_and_minor_elem(array)


if __name__ == '__main__':
    pytest.main()
