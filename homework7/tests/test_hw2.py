import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework7/')
import pytest
from tasks.hw2 import supressor, supressor_generator


@pytest.mark.parametrize("suppressor_type", [supressor, supressor_generator])
def test_suppressor(suppressor_type):
    """Tests whether suppressor works correctly"""
    with suppressor_type(IndexError):
        assert [][2] is None

if __name__ == '__main__':
    pytest.main()
