"""
submits:
- date: 2020-10-22
  minutes: 18
  cheating: false
"""
#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (63.37%)
# Likes:    2306
# Dislikes: 86
# Total Accepted:    178.5K
# Total Submissions: 281.3K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
#
# Example 1:
#
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
#
# Example 2:
#
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
#
# Note: The length of each dimension in the given grid does not exceed 50.
#
#

# @lc code=start

LAND_MARK = -1


def mark_land(grid, i, j):
    if grid[i][j] == 0:
        return 0
    if grid[i][j] == -1:
        return 0
    if grid[i][j] == 1:
        grid[i][j] = -1
        size = 1
        for x, y in [
            [i - 1, j],
            [i + 1, j],
            [i, j - 1],
            [i, j + 1],
        ]:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                continue
            size += mark_land(grid, x, y)
        return size


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                best = max(best, mark_land(grid, i, j))
        return best


# @lc code=end
