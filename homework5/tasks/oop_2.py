"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """An own exception to raise it when the deadline comes around"""
    pass


class Person:
    """Simulates a usual Person. A parent class to Student and Homework class"""

    def __init__(self, last_name, first_name) -> None:
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    """Represents a typical homework which can be given to the student"""

    def __init__(self, text, deadline) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        """Checks whether the homework is still active (the deadline has not yet passed) """
        return datetime.datetime.now() < self.created + self.deadline


class Student(Person):
    """A representation of the typical student, which can do homework"""

    def do_homework(self, homework, solution):
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    """A representation of the typical teacher which can give a homework to students"""
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text, deadline):
        """Creates an object of Homework class"""
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_result):
        """Chechs whether the homework is done correctly"""
        if len(homework_result.solution) > 5:
            cls.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        """Reset homeworks"""
        if homework is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework, None)


class HomeworkResult:
    """Represents a Homework result"""

    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError('You have given an object that is not a Homework')
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()
