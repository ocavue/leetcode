"""
submits:
- date: 2020-08-19
  minutes: 120
  cheating: false

labels:
- max/min elements in sliding window

comment: |
  这篇答案讲的比较详细：
  https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary
  看了答案之后，依然只有模糊的印象，没有明确的思路。
  接下来把下面这些题都做一遍：
    LC84. Largest Rectangle in Histogram
    LC239. Sliding Window Maximum
    LC739. Daily Temperatures
    LC862. Shortest Subarray with Sum at Least K
    LC901. Online Stock Span
    LC907. Sum of Subarray Minimums

"""
#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (23.27%)
# Likes:    1226
# Dislikes: 32
# Total Accepted:    34.3K
# Total Submissions: 139.4K
# Testcase Example:  '[1]\n1'
#
# Return the length of the shortest, non-empty, contiguous subarray of A with
# sum at least K.
#
# If there is no non-empty subarray with sum at least K, return -1.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: A = [1], K = 1
# Output: 1
#
#
#
# Example 2:
#
#
# Input: A = [1,2], K = 4
# Output: -1
#
#
#
# Example 3:
#
#
# Input: A = [2,-1,2], K = 3
# Output: 3
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
#
#
#
#
#
#

# @lc code=start

from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for a in nums:
            prefix_sum.append(prefix_sum[-1] + a)

        q = deque()

        res = float("inf")
        for i, sum in enumerate(prefix_sum):
            if not q:
                q.append(i)
            else:
                while q and prefix_sum[q[-1]] > sum:
                    q.pop()
                while q and prefix_sum[q[0]] <= sum - k:
                    res = min(res, i - q[0])
                    q.popleft()
                q.append(i)

        return res if res < float("inf") else -1


# @lc code=end
if __name__ == "__main__":

    import unittest

    t = unittest.TestCase("__init__")

    f = Solution().shortestSubarray

    t.assertEqual(f([1], 1), 1)
    t.assertEqual(f([2, -1, 2], 3), 3)
