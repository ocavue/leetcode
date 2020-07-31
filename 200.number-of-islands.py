"""
submits:
  - date: 2020-07-31
    cheating: false
    minutes: 26
labels: [bfs, dfs]
comment: 这道题除了 bfs 外，也可以使用 dfs
"""

# 12:02 12:28

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.90%)
# Likes:    4261
# Dislikes: 157
# Total Accepted:    563.7K
# Total Submissions: 1.3M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#

# @lc code=start

from queue import Queue
from typing import List, Union

NEW_LAND = "1"
WATER = "0"


# 将连接某一个点的所有陆地，都标记为 island_code
def bfs(grid: List[List[Union[str, int]]], start_i: int, start_j: int, island_code: int):
    queue_i: Queue[int] = Queue()
    queue_j: Queue[int] = Queue()
    queue_i.put(start_i)
    queue_j.put(start_j)

    grid[start_i][start_j] = island_code

    while not queue_i.empty():
        i = queue_i.get()
        j = queue_j.get()
        # assert island_code == grid[i][j]

        for x, y in [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
        ]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == NEW_LAND:
                grid[x][y] = island_code
                queue_i.put(x)
                queue_j.put(y)


def dfs(grid: List[List[Union[str, int]]], i: int, j: int, island_code: int):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == NEW_LAND:
        grid[i][j] = island_code
        dfs(grid, i - 1, j, island_code)
        dfs(grid, i + 1, j, island_code)
        dfs(grid, i, j - 1, island_code)
        dfs(grid, i, j + 1, island_code)


class Solution:
    def numIslands(self, grid: List[List[Union[str, int]]]) -> int:
        if not grid:
            return 0

        island_code = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == NEW_LAND:
                    dfs(grid, i, j, island_code)
                    island_code += 1

        return island_code


# @lc code=end
if __name__ == "__main__":

    import unittest

    t = unittest.TestCase("__init__")

    f = Solution().numIslands

    t.assertEqual(f([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]), 1)
    t.assertEqual(f([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]), 3)
    t.assertEqual(f([]), 0)
