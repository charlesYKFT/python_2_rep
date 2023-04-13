"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Return longest diverse words consisting from largest amount of unique symbols"""
    with open(file_path) as f:
        text = f.read().rstrip()
        array_of_words = text.split()
    sorted_words = list()
    for word in array_of_words:
        counter = 0
        for character in word:
            if character not in word[0:counter]:
                counter += 1
        sorted_words.append((word, counter))
    sorted_words.sort(key=lambda x: x[1], reverse=True)
    return [word[0] for word in sorted_words[:10]]


def get_rarest_char(file_path: str) -> str:
    """Finds the rarest symbol in the document"""
    symbol_freq = {}
    with open(file_path) as f:
        text = f.read()
    symbols = list(text)
    for symbol in symbols:
        if symbol == ' ' or symbol == '\n':
            continue
        else:
            if symbol in symbol_freq:
                symbol_freq[symbol] += 1
            else:
                symbol_freq[symbol] = 1
    min_freq_symbpol = min(symbol_freq)
    return min_freq_symbpol


def count_punctuation_chars(file_path: str) -> int:
    """Return the number of all punctuation chars in the file."""
    punctuation_chars = string.punctuation
    with open(file_path) as f:
        text = f.read()
    symbols = list(text)
    num_of_punct_char = 0
    for symbol in symbols:
        if symbol in punctuation_chars:
            num_of_punct_char += 1
    return num_of_punct_char


def count_non_ascii_chars(file_path: str) -> int:
    """Function that counts the number of non ascii characters."""
    with open(file_path) as f:
        text = f.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        total_count = len(text)
        ascii_count = len(text.encode("ascii", "ignore"))
        return total_count - ascii_count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Functions that finds the most common non ascii charater in the file """
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        frequency = {}
        for char in text:
            if char in string.printable:
                continue
            elif char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        rarest = max(frequency, key=frequency.get)
        return rarest
