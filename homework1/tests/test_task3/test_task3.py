import pytest
import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/')

from tasks.task03 import find_maximum_and_minimum

@pytest.mark.parametrize("file_name, expected_result", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/tests/test_task3/test_data1.txt', ([1], [9])), ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/tests/test_task3/test_data2.txt', ([4, 1, -4], [10, 102, 67])), ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/tests/test_task3/test_data3.txt', ([23, -10, 1], [75, 89, 670]))])
def test_find_maximum_and_minimum_yes(file_name: str, expected_result: tuple[int, int]):
    """Tests whether find_maximum_and_minimum returns correct min and max values"""
    assert find_maximum_and_minimum(file_name) == expected_result


@pytest.mark.parametrize("file_name, expected_error", [('test.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/tests/test_task3/hello.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework1/tests/test_task3/godsy.txt', FileNotFoundError),
                                                       (234, TypeError),
                                                       (find_maximum_and_minimum, TypeError)])
def test_find_maximum_and_minimum_error(file_name, expected_error):
    """Tests whether find_maximum_and_minimum returns the correct mistake"""
    with pytest.raises(expected_error):
        find_maximum_and_minimum(file_name)


if __name__ == '__main__':
    pytest.main()
