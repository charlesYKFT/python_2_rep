"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
# cls = class in short


def instances_counter(cls):
    """A decorator that counts instances of the given class. It also can reset the number of this instances"""

    class WrapperClass(cls):
        """A wrapper class that do all the stuff"""
        _instance_count = 0  # class variable declaration, which will be used in all its functions

        def __new__(cls, *args, **kwargs):
            """Overriding the __new__() method. Adds to given class object an attribute '_instance_count'"""
            instance = super().__new__(cls)
            cls._instance_count += 1
            return instance

        @classmethod
        def get_created_instances(cls):
            """Returns the number of class objects that were created"""
            return cls._instance_count

        @classmethod
        def reset_instances_counter(cls):
            """Resets the number of class objects that were counted, returns the number of classes already counted"""
            count = cls._instance_count
            cls._instance_count = 0
            return count

    return WrapperClass


@instances_counter
class User:
    pass
