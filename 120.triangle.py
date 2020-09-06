"""
submits:
- date: 2020-09-06
  minutes: 15
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (42.42%)
# Likes:    2205
# Dislikes: 260
# Total Accepted:    259K
# Total Submissions: 582.8K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        assert len(triangle) == len(triangle[-1])

        # dp[i][j] 是选择 triangle[i][j] 后能获得的最好 sum 是什么
        dp = []
        for row in triangle:
            dp.append([0] * len(row))

        for i in range(len(triangle) - 1, -1, -1):
            row = triangle[i]
            for j, cell in enumerate(row):
                if i + 1 < len(triangle):
                    dp[i][j] = cell + min(dp[i + 1][j], dp[i + 1][j + 1])
                else:
                    dp[i][j] = cell
        # print(dp)
        return dp[0][0]


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().minimumTotal
    t.assertEqual(f([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11)

