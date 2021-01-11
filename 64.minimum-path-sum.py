"""
submits:
- date: 2020-01-11
  minutes: 12
  cheating: false
labels: [dp]
"""
#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (55.14%)
# Likes:    4040
# Dislikes: 77
# Total Accepted:    491.1K
# Total Submissions: 880.5K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#
# Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
#
#
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    grid[0][0] = -grid[0][0]
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] - grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] - grid[i][j]
                else:
                    grid[i][j] = max(grid[i][j - 1], grid[i - 1][j]) - grid[i][j]
                # assert grid[i][j] <= 0, debug
        return -grid[len(grid) - 1][len(grid[0]) - 1]


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().minPathSum
    t(f([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
    t(f([[1, 2, 3], [4, 5, 6]]), 12)

