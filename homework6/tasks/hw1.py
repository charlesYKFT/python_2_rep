"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Find all occurrences of the given element in the tree and then return the number of these occurences"""
    count = 0
    for value in tree.values():
        if value == element:
            count += 1
        elif isinstance(value, (list, tuple, set)):
            for item in value:
                if item == element:
                    count += 1
                elif isinstance(item, dict):
                    count += find_occurrences(item, element)
        elif isinstance(value, dict):
            count += find_occurrences(value, element)
    return count
