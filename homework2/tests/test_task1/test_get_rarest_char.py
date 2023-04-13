import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/')

import pytest
from tasks.hw1 import get_rarest_char



@pytest.mark.parametrize("file_path, expected_result", [('tests/test_task1/test_data.txt', '\'')])
def test_get_rarest_char_yes(file_path, expected_result):
    """Tests whether get_rarest_char() returns correct result"""
    assert get_rarest_char(file_path) == expected_result


@pytest.mark.parametrize("file_path, expected_error", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/example.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/data1.txt', FileNotFoundError),
                                                       ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework2/tests/test_task1/text.txt', FileNotFoundError)])
def test_get_rarest_char_yes_errors(file_path, expected_error):
    """Tests whether get_rarest_char() returns correct error when it get something that is not a list"""
    with pytest.raises(expected_error):
        get_rarest_char(file_path)


if __name__ == '__main__':
    pytest.main()
