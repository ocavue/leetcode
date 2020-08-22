"""
comment: |
  这道题有趣的地方在于它的算法复杂度分析。虽然两个 for loop 看起来算法复杂度是 O(n*n)，但是实际上的时间复杂度是 O(32*n)。
  原因在于 prev_results 的长度最大是 32：在做内层的遍历时，只有增加一个 1 才会增加一条记录，又由于题目中的二进制数字最大
  只有 32 位，所以最多只增加 32 的元素。
labels:
- bitwise
submits:
- date: 2020-08-22
  minutes: 20
  cheating: true

"""
#
# @lc app=leetcode id=898 lang=python3
#
# [898] Bitwise ORs of Subarrays
#
# https://leetcode.com/problems/bitwise-ors-of-subarrays/description/
#
# algorithms
# Medium (36.52%)
# Likes:    508
# Dislikes: 109
# Total Accepted:    15.5K
# Total Submissions: 44.7K
# Testcase Example:  '[0]'
#
# We have an array A of non-negative integers.
#
# For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j),
# we take the bitwise OR of all the elements in B, obtaining a result A[i] |
# A[i+1] | ... | A[j].
#
# Return the number of possible results.  (Results that occur more than once
# are only counted once in the final answer.)
#
#
#
#
# Example 1:
#
#
# Input: [0]
# Output: 1
# Explanation:
# There is only one possible result: 0.
#
#
#
# Example 2:
#
#
# Input: [1,1,2]
# Output: 3
# Explanation:
# The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.
#
#
#
# Example 3:
#
#
# Input: [1,2,4]
# Output: 6
# Explanation:
# The possible results are 1, 2, 3, 4, 6, and 7.
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 50000
# 0 <= A[i] <= 10^9
#
#
#

# @lc code=start
from typing import List, Set


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        all_results: Set[int] = set()
        prev_results: Set[int] = set()

        for i in A:
            curr_results: Set[int] = set()
            curr_results.add(i)

            for j in prev_results:
                curr_results.add(j | i)

            all_results |= curr_results
            prev_results = curr_results
        return len(all_results)


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().subarrayBitwiseORs
    t.assertEqual(f([0]), 1)
    t.assertEqual(f([1, 1, 2]), 3)
    t.assertEqual(f([1, 2, 4]), 6)
