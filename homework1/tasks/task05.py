"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Finds a maximum subarray in an array"""

    if not isinstance(k, int):
        raise TypeError

    if not isinstance(nums, list):
        raise TypeError

    for num in nums:
        if not isinstance(num, int):
            raise TypeError

    max_sum = 0
    for index_i, item_i in enumerate(nums):
        curr_sum = 0
        for index_j, item_j in enumerate(nums):
            if index_i - index_j < k:
                curr_sum += nums[index_j]
            max_sum = curr_sum
    return max_sum
