"""
submits:
- date: 2020-09-03
  cheating: false
  minutes: 38
labels:
- dfs
- bfs
"""

# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#
# https://leetcode.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (44.60%)
# Likes:    471
# Dislikes: 15
# Total Accepted:    19.3K
# Total Submissions: 41.9K
# Testcase Example:  '[[1,0],[0,1]]'
#
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
#
# After, what is the size of the largest island? (An island is a
# 4-directionally connected group of 1s).
#
# Example 1:
#
#
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
# area = 3.
#
#
# Example 2:
#
#
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island
# with area = 4.
#
# Example 3:
#
#
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
#
#
# Notes:
#
#
# 1 <= grid.length = grid[0].length <= 50.
# 0 <= grid[i][j] <= 1.
#
#
#
#
#

# @lc code=start

from typing import List, Dict
from queue import Queue


def bfs(grid: List[List[int]], i: int, j: int, n: int, island_id: int, area_map: Dict[int, int]):
    val = grid[i][j]

    if val == 0:  # 海洋
        return island_id
    if val < 0:  # 已被标记过的岛屿
        return island_id
    assert val == 1  # 未被标记过的岛屿

    q = Queue()
    assert island_id not in area_map
    area_map[island_id] = 1
    grid[i][j] = island_id
    q.put((i, j))

    while not q.empty():
        i, j = q.get()

        for ii, jj in [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
        ]:
            if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 1:
                area_map[island_id] += 1
                grid[ii][jj] = island_id
                q.put((ii, jj))

    return island_id - 1


def build_area_map(grid: List[List[int]], area_map: Dict[int, int]) -> int:
    n = len(grid)
    next_island_id = -1
    for i in range(n):
        for j in range(n):
            next_island_id = bfs(grid, i, j, n, next_island_id, area_map)

    island_count = abs(next_island_id) - 1
    print(f"there is {island_count} islands", area_map)
    return island_count


def find_best_bridge(grid: List[List[int]], area_map: Dict[int, int]) -> int:
    n = len(grid)

    best_neighber_area = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:

                neighber_island_ids = set()

                for ii, jj in [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                ]:
                    if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] != 0:
                        assert grid[ii][jj] < 0
                        neighber_island_ids.add(grid[ii][jj])

                neighber_area = 0
                for island_id in neighber_island_ids:
                    neighber_area += area_map[island_id]
                best_neighber_area = max(best_neighber_area, neighber_area)

    return best_neighber_area


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        assert 1 <= len(grid) == len(grid[0]) <= 50

        area_map: Dict[int, int] = {}
        build_area_map(grid, area_map)

        if not area_map:  # 地图上没有一座岛
            return 1

        best_area = find_best_bridge(grid, area_map)
        if best_area == 0:  # 地图上没有一滴水 或者 没有一座岛。因为之前已经处理过无岛情况，所以这里没有一滴水
            return len(grid) ** 2
        return best_area + 1


# @lc code=end

if __name__ == "__main__":
    f = Solution().largestIsland

    import unittest

    t = unittest.TestCase("__init__")

    # fmt:off
    t.assertEqual(
        f([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]),
        2
    )
    t.assertEqual(
        f([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]),
        3
    )
    t.assertEqual(
        f([
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
        ]),
        7
    )
    t.assertEqual(f([[1, 0], [0, 1]]), 3)
    t.assertEqual(f([[1, 1], [1, 0]]), 4)
    t.assertEqual(f([[1, 1], [1, 1]]), 4)
    t.assertEqual(f([[0, 0], [0, 0]]), 1)
