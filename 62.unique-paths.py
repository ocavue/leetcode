"""
submits:
  - date: 2020-07-23
    cheating: false
    minutes: 10
labels:
  - dp
comment: "这道题的解答还有内存优化空间，以为每次遍历 dp 的时候，其实只需要知道上一行的数据，所以不需要保存整个二维数组"
"""

#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (51.43%)
# Likes:    2591
# Dislikes: 183
# Total Accepted:    413K
# Total Submissions: 798K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
#
# Example 1:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: m = 7, n = 3
# Output: 28
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
#
#
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp 是一个二维数组。dp[x][y] 表示机器人有多少种 unique paths 移动到 (x,y) 坐标。
        # 其中 1 <= x <= m; 1 <= y <= n;
        dp = []
        for x in range(m + 1):
            dp.append([0] * (n + 1))

        dp[1][1] = 1  # 机器人的初始位置在左上角

        for x in range(1, m + 1):
            for y in range(1, n + 1):
                dp[x][y] += dp[x - 1][y] + dp[x][y - 1]

        return dp[m][n]


# @lc code=end
if __name__ == "__main__":
    f = Solution().uniquePaths

    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(f(3, 2), 3)
    t.assertEqual(f(7, 3), 28)
