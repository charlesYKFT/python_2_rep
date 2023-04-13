"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Returns the the most common and the least common elements from the array."""
    if not isinstance(inp, List):
        raise TypeError("The input must be a List!")
    symbol_freq = {}
    for symbol in inp:
        if symbol in symbol_freq:
            symbol_freq[symbol] += 1
        else:
            symbol_freq[symbol] = 1
    return (max(symbol_freq), min(symbol_freq))
