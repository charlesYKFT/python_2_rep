"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Finds minimum and maximum values from a file"""
    if not isinstance(file_name, str):
        raise TypeError

    min_values = list()
    max_values = list()
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            numbers = [int(number) for number in line.split()]
            min_values.append(min(numbers))
            max_values.append(max(numbers))
        return (min_values, max_values)
