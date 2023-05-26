from tasks.oop_1 import *
import pytest
import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework5')


@pytest.mark.parametrize("text, deadline, expected_result", [("Python homework", 5, True),
                                                             ("Algebra homework", -1, False),
                                                             ("Biology homework",
                                                              1, True),
                                                             ("Astranomy homework", -10, False)])
def test_homework_is_active(text, deadline, expected_result):
    """Tests whether is_active function correts the correct result depending of the value of the deadline"""
    homework = Homework(text, deadline)
    assert homework.is_active() == expected_result


@pytest.mark.parametrize("last_name, first_name, expected_result", [("Marshlow", "Ann", "Marshlow Ann"),
                                                                    ("Smith", "Alex",
                                                                     "Smith Alex"),
                                                                    ("Nofelix", "Boris",
                                                                     "Nofelix Boris"),
                                                                    ("Romanenko", "Ivan", "Romanenko Ivan")])
def test_student_full_name(last_name, first_name, expected_result):
    """Tests whether Student class returns the correct value of full_name"""
    student = Student(last_name, first_name)
    assert student.first_name + " " + student.last_name == expected_result


def test_student_do_homework():
    """Tests whether do_homework() returns the correct result depending on the homework"""
    student = Student("Marshlow", "Ann")
    homework = Homework("Python homework", 5)
    assert student.do_homework(homework) == homework
    homework = Homework("Algebra homework", -1)
    assert student.do_homework(homework) == None
    student = Student("Nofelix", "Boris")
    homework = Homework("Biology homework", 1)
    assert student.do_homework(homework) == homework
    homework = Homework("Astranomy homework", -10)
    assert student.do_homework(homework) == None


@pytest.mark.parametrize("last_name, first_name, text, deadline", [("Marshlow", "Ann", "Python homework", 5),
                                                                   ("Smith", "Alex",
                                                                    "Algebra homework", -1),
                                                                   ("Nofelix", "Boris",
                                                                    "Biology homework", 1),
                                                                   ("Romanenko", "Ivan", "Biology homework", -10)])
def test_teacher_create_homework(last_name, first_name, text, deadline):
    """Tests whether Teacher class works correctly: retruns the Homework instance, containing the text of task and its deadline"""
    teacher = Teacher(last_name, first_name)
    homework = teacher.create_homework(text, deadline)
    assert homework.text == text
    assert homework.deadline == datetime.timedelta(days=deadline)


if __name__ == '__main__':
    pytest.main()
