"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""


def cache(times):
    """A parammetrized decorator that accepts number of times to cache value. For the test purposes it also tells whether a value was cached or not"""

    caches = {'value': None, 'count': times}

    def caching_process(func: callable):
        def wrapper(*args, **kwargs):
            if caches['count'] > 0 and caches.get('value'):
                caches['count'] -= 1
                is_cashed_call = True
                return (caches['value'], is_cashed_call)
            else:
                (caches['value'], is_cashed_call) = func(*args, **kwargs)
                return (caches['value'], is_cashed_call)
        return (wrapper)
    return caching_process


"""
Additional_Info:
is_cached_call returns True if the value was taken from the cashes dictionary. If the value was calculated by the function, is_cached_call = False. This was done just to test this function, but I decided to show it to you because it totally proves a work of this function.
"""
