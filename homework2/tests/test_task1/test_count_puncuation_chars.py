import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

import pytest
from tasks.hw1 import count_punctuation_chars



@pytest.mark.parametrize("file_path, expected_result", [('tests/test_task1/test_data.txt', 8277)])
def test_count_punctuation_chars_yes(file_path, expected_result):
    """Tests whether count_punctuation_chars() returns correct result"""
    assert count_punctuation_chars(file_path) == expected_result


@pytest.mark.parametrize("file_path, expected_error", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/example.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/data1.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/text2.txt', FileNotFoundError)])
def test_count_punctuation_chars_errors(file_path, expected_error):
    """Tests whether count_punctuation_chars() returns correct error when it get something that is not a list"""
    with pytest.raises(expected_error):
        count_punctuation_chars(file_path)


if __name__ == '__main__':
    pytest.main()
