"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*lists):
    "Return combinations"
    for element in lists:
        if not isinstance(element, list):
            raise TypeError("The input must be a list")

    if len(lists) == 1:
        return [[x] for x in lists[0]]
    else:
        result = []
        for i in range(len(lists[0])):
            for combination in combinations(*lists[1:]):
                result.append([lists[0][i]] + combination)
        return result
