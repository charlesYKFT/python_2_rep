import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework6')
from tasks.hw3 import tic_tac_toe_checker
import pytest



@pytest.mark.parametrize("board, expected_result", [
    ([['o', 'o', 'x'],
     ['-', 'x', '-'],
     ['x', '-', '-']], 'x wins!'),

    ([['x', 'o', 'o'],
     ['x', 'x', '-'],
     ['x', '-', 'o']], 'x wins!'),

    ([['o', 'x', 'x'],
     ['x', 'x', 'o'],
     ['o', 'x', 'o']], 'x wins!'),

    ([['x', '-', 'o'],
      ['-', 'o', 'x'],
      ['o', 'x', '-']], 'o wins!'),

    ([['x', 'o', 'x'],
      ['x', 'o', '-'],
      ['o', 'o', 'x']], 'o wins!'),

    ([['o', 'x', 'x'],
      ['x', 'o', 'o'],
      ['x', 'o', 'o']], 'o wins!'),

    ([['o', 'o', 'x'],
      ['x', 'x', 'o'],
      ['o', 'x', 'x']], 'draw!'),

    ([['-', '-', '-'],
      ['-', '-', '-'],
      ['-', '-', '-']], 'The board is unfinished!')])
def test_tic_tac_toe_checker(board, expected_result):
    """Tests whether tic_tac_toe_checker() returns the correct result of the game"""
    assert tic_tac_toe_checker(board) == expected_result


@pytest.mark.parametrize("board, exception",[
                             ("ght", TypeError),
                             (tic_tac_toe_checker, TypeError),
                             ([1,2,3], TypeError),
                             (1, TypeError),
                             ({"key":1}, TypeError)])
def test_backspace_error(board, exception):
    """Tests whether backspace_compare() raises exception when it doen't recieve two strings"""
    with pytest.raises(exception):
        tic_tac_toe_checker(board)


if __name__ == '__main__':
    pytest.main()
