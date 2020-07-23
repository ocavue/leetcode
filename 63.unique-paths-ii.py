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
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.94%)
# Likes:    1404
# Dislikes: 219
# Total Accepted:    268.2K
# Total Submissions: 789.7K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
#

from typing import List

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacles: List[List[int]]) -> int:

        if obstacles[0][0] == 1:
            return 0

        # dp 是一个二维数组。dp[x][y] 表示机器人有多少种 unique paths 移动到 (x,y) 坐标。
        # 其中 X = len(obstacle); Y = len(obstacle[0]); 0 <= x < X; 0 <= y < Y;

        X, Y = len(obstacles), len(obstacles[0])

        dp: List[List[int]] = []
        for x in range(X):
            dp.append([0] * Y)

        dp[0][0] = 1

        for x in range(X):
            for y in range(Y):
                if obstacles[x][y] == 0:
                    from_x_paths = dp[x - 1][y] if x - 1 >= 0 else 0
                    from_y_paths = dp[x][y - 1] if y - 1 >= 0 else 0
                    dp[x][y] += from_x_paths + from_y_paths

        return dp[X - 1][Y - 1]


# @lc code=end
if __name__ == "__main__":

    f = Solution().uniquePathsWithObstacles

    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(f([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
