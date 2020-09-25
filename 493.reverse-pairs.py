"""
submits:
- date: 2020-09-25
  minute: 30
  cheating: false
labels:
- divide-and-conquer
comment: |
  这道题我看到题干中有 divide-and-conquer 就很快想到做法了。
"""

#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (24.40%)
# Likes:    853
# Dislikes: 118
# Total Accepted:    38.1K
# Total Submissions: 151.7K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and
# nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
#
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
#
# Note:
#
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
#
#
#

# @lc code=start

from typing import List


def log(f):
    def new_f(nums, i, j):
        result = f(nums, i, j)
        print(f"reverse_pairs({nums}, {i}, {j}) = {result}")
        return result

    return new_f


# @log
def reverse_pairs(nums: List[int], i: int, j: int) -> int:

    assert 0 <= i <= j <= len(nums)
    if j - i == 0:
        return 0
    if j - i == 1:
        return 0
    if j - i == 2:
        return 1 if nums[i] > nums[i + 1] * 2 else 0

    half = (j - i) // 2 + i

    result = reverse_pairs(nums, i, half) + reverse_pairs(nums, half, j)
    left, right = sorted(nums[i:half]), sorted(nums[half:j])

    a, b = len(left) - 1, len(right) - 1
    while a >= 0 and b >= 0:
        if left[a] > 2 * right[b]:
            # for all k which 0<=k<=b, left[a] > 2*right[k]
            result += b + 1
            a -= 1
        else:
            b -= 1

    return result


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return reverse_pairs(nums, 0, len(nums))


# @lc code=end
if __name__ == "__main__":
    import unittest

    f = Solution().reversePairs
    t = unittest.TestCase("__init__")
    t.assertEqual(f([1, 3, 2, 3, 1]), 2)
    t.assertEqual(f([2, 4, 3, 5, 1]), 3)

