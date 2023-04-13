"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(iterable, *args):
    "The function that behaves like a range function"
    try:
        some_object_iterator = iter(iterable)
    except TypeError:
        return TypeError
    else:
        start = 0
        stop = len(iterable)
        step = 1
        if len(args) == 1:
            stop = iterable.index(args[0])
        elif len(args) == 2:
            start = iterable.index(args[0])
            stop = iterable.index(args[1])
        elif len(args) == 3:
            start = iterable.index(args[0])
            stop = iterable.index(args[1])
            step = args[2]

        return [iterable[i] for i in range(start, stop, step)]
