"""
submits:
- date: 2020-09-14
  minutes: 100
  cheating: false
labels:
- dp
"""
# @lc app=leetcode id=446 lang=python3
#
# [446] Arithmetic Slices II - Subsequence
#
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
#
# algorithms
# Hard (31.93%)
# Likes:    526
# Dislikes: 59
# Total Accepted:    22.1K
# Total Submissions: 67.2K
# Testcase Example:  '[2,4,6,8,10]'
#
# A sequence of numbers is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
#
# For example, these are arithmetic sequences:
#
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
#
# The following sequence is not arithmetic.
#
#
# 1, 1, 2, 5, 7
#
#
# A zero-indexed array A consisting of N numbers is given. A subsequence slice
# of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0
# < P1 < ... < Pk < N.
#
# A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the
# sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this
# means that k ≥ 2.
#
# The function should return the number of arithmetic subsequence slices in the
# array A.
#
# The input contains N integers. Every integer is in the range of -2^31 and
# 2^31-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 2^31-1.
#
#
# Example:
#
#         0  1  2  3  4
# Input: [2, 4, 6, 8, 10]
#
# Output: 7
#
# Explanation:
# All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#
#
#

# @lc code=start

from typing import List, Tuple, Dict
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # dp1[(i, d)] = x
        # 表示以 A[i] 为最后一个元素，每两个元素之间的值相差 d 的等差数列有 x 个
        # 其中我们规定一个等差数列至少要有2个元素
        #
        dp1: Dict[Tuple[int, int], int] = defaultdict(lambda: 0)

        count = 0
        for j in range(0, len(A)):
            for i in range(0, j):
                d = A[j] - A[i]

                dp1[(j, d)] += 1

                before = dp1.get((i, d), 0)

                dp1[(j, d)] += before
                count += before

        return count



# @lc code=end
if __name__ == "__main__":
    import unittest

    f = Solution().numberOfArithmeticSlices

    t = unittest.TestCase("__init__")
    t.assertEqual(f([0, 1, 2, 3, 4]), 7)
    t.assertEqual(f([1, 2, 3, 4, 5]), 7)
    t.assertEqual(f([2, 4, 6, 8, 10]), 7)
    t.assertEqual(f([2, 3, 4]), 1)
    t.assertEqual(f([2, 3, -99, 4]), 1)
    t.assertEqual(f([2, 2, 3, 4]), 2)

    # t.assertEqual(f([1, 1, 1, 1, 1]), 6)
    # t.assertEqual(f([1, 1, 1, 1]), 3)
    # t.assertEqual(f([1, 1, 1]), 1)
