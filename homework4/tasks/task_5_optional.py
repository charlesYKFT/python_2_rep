"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import List, Generator


def fizzbuzz_optional(n: int) -> List[str]:
    """Write a function that takes a number N as an input and returns N FizzBuzz numbers. And no any if-constructions"""
    try:
        assert isinstance(n, int)
    except:
        raise TypeError
    else:
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) for i in range(1, n + 1)]

# To avoid using if in this function, I have made a try-except block here. However, using assert to check something in last version of code is not ok in general. But your task was clear: 'no if'.
