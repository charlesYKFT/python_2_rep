import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework3/')
from tasks.task04 import is_armstrong_number
import pytest



@pytest.mark.parametrize("number, expected_result", [(1, True),
                                                     (153, True),
                                                     (370, True),
                                                     (371, True),
                                                     (407, True),
                                                     ])
def test_is_armstrong_number_yes(number, expected_result):
    """Tests whether is_armstrong_number returns True when it actuallly get an armstrong number"""
    assert is_armstrong_number(number) == expected_result


@pytest.mark.parametrize("number, expected_result", [(88, False),
                                                     (163, False),
                                                     (400, False),
                                                     (490, False),
                                                     (1000, False)])
def test_is_armstrong_number_no(number, expected_result):
    """Tests whether is_armstrong_number returns False when it actuallly get usual number"""
    assert is_armstrong_number(number) == expected_result


@pytest.mark.parametrize("number, expected_error", [(1.5, TypeError),
                                                    ("2", TypeError),
                                                    ([1, 2, 3, 4], TypeError),
                                                    ({"key": "value1",
                                                     "key2": "value2"}, TypeError),
                                                    (test_is_armstrong_number_yes,
                                                     TypeError),
                                                    ((1, 2, 3), TypeError)])
def test_is_armstrong_number_errors(number, expected_error):
    """Tests whether is_armstrong_number returns correct error when it actuallly get something that is not an int number"""
    with pytest.raises(expected_error):
        is_armstrong_number(number)


if __name__ == '__main__':
    pytest.main()
