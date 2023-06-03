import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework6')
from tasks.hw2 import backspace_compare
import pytest



@pytest.mark.parametrize("first, second, expected_result", [
    ("ab#c", "ad#c", True),
    ("a##c", "#a#c", True),
    ("a#c", "b", False),
    ("", "", True),
    ("a", "b", False),
    ("a#", "b#", True),
    ("a#b", "c#d", False),
])
def test_backspace_compare(first, second, expected_result):
    """Tests whether backspace_compare() returns the correct result """
    assert backspace_compare(first, second) == expected_result


@pytest.mark.parametrize("first, second, exception",[
                             ("ab#c", 2, TypeError),
                             (list(), {"key", "value"}, TypeError),
                             (test_backspace_compare, backspace_compare, TypeError)])
def test_backspace_error(first, second, exception):
    """Tests whether backspace_compare() raises exception when it doen't recieve two strings"""
    with pytest.raises(exception):
        backspace_compare(first, second)

if __name__ == '__main__':
    pytest.main()
