import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework7/')
import pytest
from pathlib import Path
from typing import List, Union, Iterator

from tasks.hw1 import merge_sorted_files


@pytest.mark.parametrize("file_list, expected", [
    (["tests/test_hm1/file1.txt", "tests/test_hm1/file2.txt"], [1, 2, 3, 4, 5, 6]),
    (["tests/test_hm1/file3.txt", "tests/test_hm1/file4.txt"], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (["tests/test_hm1/file5.txt"], [1, 2, 3, 4, 5]),
    ([], []),
])
def test_merge_sorted_files(file_list: List[Union[Path, str]], expected: List[int]):
    """Tests whether merge_sorted_files() returns the correct iterator """
    result = list(merge_sorted_files(file_list))
    assert result == expected

if __name__ == '__main__':
    pytest.main()
