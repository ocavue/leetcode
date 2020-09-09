"""
submits:
- date: 2020-09-09
  minute: 13
  cheating: false
comment: |
  只要知道首尾的位置，就能直接得到数据
"""

# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (57.08%)
# Likes:    1135
# Dislikes: 170
# Total Accepted:    94.1K
# Total Submissions: 162K
# Testcase Example:  '[1,2,3,4]'
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
# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means
# that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.
#
#
# Example:
#
#
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.
#
#
#

# @lc code=start
from typing import List


def group_diff(diffs: List[int]):
    assert len(diffs) >= 1
    last_diff = diffs[0]
    diff_count = 1
    for diff in diffs[1:]:
        if diff == last_diff:
            diff_count += 1
        else:
            if diff_count >= 2:
                yield last_diff, diff_count
            last_diff = diff
            diff_count = 1
    if diff_count >= 2:
        yield last_diff, diff_count


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) <= 2:
            return 0

        diffs = [A[i + 1] - A[i] for i in range(0, len(A) - 1)]

        count = 0
        for diff, diff_count in group_diff(diffs):
            count += (diff_count * (diff_count - 1)) // 2
        return count


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().numberOfArithmeticSlices
    t.assertEqual(f([1, 2, 3, 4]), 3)
    t.assertEqual(f([1, 2, 3]), 1)
    t.assertEqual(f([1, 2, 3, 4, 6, 8, 10]), 6)
