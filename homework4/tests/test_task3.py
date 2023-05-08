import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/')
import pytest
from tasks.task_3_get_print_output import my_precious_logger



def test_my_precious_logger_stdout(capsys):
    """Tests whether my_precious_logger writes stdout"""
    my_precious_logger('info: everything is fine')
    out = capsys.readouterr()
    assert 'info: everything is fine' in out.out


def test_my_precious_logger_stderr(capsys):
    """Tests whether my_precious_logger writes stderr"""
    my_precious_logger('error: something went wrong')
    err = capsys.readouterr()
    assert 'error: something went wrong' in err.err


@pytest.mark.parametrize("inp, expected_error", [(3, TypeError),
                                                 ((2, 3), TypeError),
                                                 ({"key": "value"}, TypeError),
                                                 (my_precious_logger, TypeError),
                                                 (pytest, TypeError)])
def test_my_precious_logger_error(inp, expected_error):
    """Tests whether my_precious_logger returns TypeError output when it gets something that is not a string"""
    with pytest.raises(expected_error):
        my_precious_logger(inp)


if __name__ == '__main__':
    pytest.main()
