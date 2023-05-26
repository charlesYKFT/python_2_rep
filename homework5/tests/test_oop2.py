from tasks.oop_2 import *
import pytest
import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework5')


@pytest.mark.parametrize("solution, expected", [("solution1", True),
                                                ("solution2", True),
                                                ("abc", False),
                                                ("aghj", False)])
def test_check_homework(solution, expected):
    teacher = Teacher("Marshlow", "Ann")
    homework = teacher.create_homework("Test homework", 5)
    student = Student("Smith", "Alex")
    homework_result = student.do_homework(homework, solution)
    assert teacher.check_homework(homework_result) == expected


if __name__ == '__main__':
    pytest.main()
