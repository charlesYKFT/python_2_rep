from tasks.save_original_info import *
import pytest
import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework5')


@pytest.mark.parametrize("input_args, expected_output", [([1, 2, 3, 4], 10),
                                                         ([1, 2, 3], 6),
                                                         ([1, 2, 3, 4, 5], 15),
                                                         ([2, 10, 25, 12], 49),
                                                         ((3, 4, 5, 6), 18)])
def test_custom_sum_yes(input_args, expected_output):
    """Testhe whether custom_sum() returns the correct value of sum"""
    assert custom_sum(*input_args) == expected_output


@pytest.mark.parametrize("input_args, expected_output", [([], TypeError),
                                                         (pytest, TypeError),
                                                         (custom_sum, TypeError)])
def test_custom_sum_error(input_args, expected_output):
    """Testhe whether custom_sum() returns the TypeError when it gets wrong arguments"""
    with pytest.raises(TypeError):
        custom_sum(*input_args)


def test_original_info():
    """Tests original_info()"""
    @preserve_info(custom_sum)
    def new_func(*args):
        pass

    assert new_func.__name__ == "custom_sum"
    assert new_func.__doc__ == "This function can sum any objects which have __add___"
    assert new_func.__original_func == custom_sum


def test_without_print():
    """Tests without_print() function"""
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10


if __name__ == '__main__':
    pytest.main()
