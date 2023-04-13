import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

import pytest
from tasks.hw1 import get_most_common_non_ascii_char



@pytest.mark.parametrize("file_path, expected_result", [('tests/test_task1/test_data.txt', "ä")])
def test_get_most_common_non_ascii_character_yes(file_path, expected_result):
    """Tests whether get_most_common_non_ascii_character returns correct result"""
    assert get_most_common_non_ascii_char(file_path) == expected_result


@pytest.mark.parametrize("file_path, expected_error", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/example.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/data1.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/text.txt', FileNotFoundError)])
def test_get_most_common_non_ascii_character_errors(file_path, expected_error):
    """Tests whether get_most_common_non_ascii_character returns correct error when it get something that is not a list"""
    with pytest.raises(expected_error):
        get_most_common_non_ascii_char(file_path)


if __name__ == '__main__':
    pytest.main()
