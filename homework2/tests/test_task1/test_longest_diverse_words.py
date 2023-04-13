import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

import pytest
from tasks.hw1 import get_longest_diverse_words



@pytest.mark.parametrize("file_path, expected_result", [('tests/test_task1/test_data.txt', ['Bev\\u00f6lkerungsabschub,', 'Werkst\\u00e4ttenlandschaft', 'Werkst\\u00e4ttenlandschaft', 'unmi\\u00dfverst\\u00e4ndliche', 'Zahlenverh\\u00e4ltnisse,', 'Machtbewu\\u00dftsein,', 'D\\u00e4monengeschichte', 'Selbstverst\\u00e4ndlich', 'Millionenbev\\u00f6lkerung', 'r\\u00e9sistance-Bewegungen,'])])
def test_get_longest_diverse_words_yes(file_path, expected_result):
    """Tests whether get_longest_diverse_words() returns correct result"""
    assert get_longest_diverse_words(file_path) == expected_result


@pytest.mark.parametrize("file_path, expected_error", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/example.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/data1.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/text.txt', FileNotFoundError)])
def test_get_longest_diverse_wors_error(file_path, expected_error):
    """Tests whether get_longest_diverse_words() returns correct error when it get something that is not a list"""
    with pytest.raises(expected_error):
        get_longest_diverse_words(file_path)


if __name__ == '__main__':
    pytest.main()
