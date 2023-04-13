import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

import pytest
from tasks.hw1 import count_non_ascii_chars



@pytest.mark.parametrize("file_path, expected_result", [('tests/test_task1/test_data.txt', 2972)])
def test_count_non_ascii_charschar_yes(file_path, expected_result):
    """Tests whether count_non_ascii_charschar() returns correct result"""
    assert count_non_ascii_chars(file_path) == expected_result


@pytest.mark.parametrize("file_path, expected_error", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/example.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/data1.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/text.txt', FileNotFoundError)])
def test_count_non_ascii_chars_errors(file_path, expected_error):
    """Tests whether count_non_ascii_charschar() returns correct error when it get something that is not a list"""
    with pytest.raises(expected_error):
        count_non_ascii_chars(file_path)


if __name__ == '__main__':
    pytest.main()
