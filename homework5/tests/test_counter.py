import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework5')
import pytest
from tasks.counter import instances_counter



@instances_counter
class User:
    pass


def test_get_created_instances():
    """Tests whether get_created_instances() counts the number of instances correctly"""
    assert User.get_created_instances() == 0
    user1, user2, user3 = User(), User(), User()
    assert user1.get_created_instances() == 3
    user1.reset_instances_counter()


def test_reset_instances_counter():
    """Tests whether reset_instances_counter() works correctly"""
    user21, user22, user23 = User(), User(), User()
    count = user21.reset_instances_counter()
    assert count == 3
    assert user21.get_created_instances() == 0


if __name__ == '__main__':
    pytest.main()
