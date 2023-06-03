"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str) -> bool:
    """Returns True if two strings are equal when both are typed into empty text editors"""
    if not (isinstance(first, str) and isinstance(second, str)):
        raise TypeError("Input must be string!")

    def process_string(string: str) -> str:
        """Returns the string without backspace characters"""
        stack = list()
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    return process_string(first) == process_string(second)
