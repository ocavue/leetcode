"""
submits:
- date: 2020-10-10
  minutes: 7
  cheating: false
labels:
- hash-table
"""
# 50
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#
# https://leetcode.com/problems/brick-wall/description/
#
# algorithms
# Medium (49.13%)
# Likes:    893
# Dislikes: 46
# Total Accepted:    57.7K
# Total Submissions: 115.3K
# Testcase Example:  '[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]'
#
# There is a brick wall in front of you. The wall is rectangular and has
# several rows of bricks. The bricks have the same height but different width.
# You want to draw a vertical line from the top to the bottom and cross the
# least bricks.
#
# The brick wall is represented by a list of rows. Each row is a list of
# integers representing the width of each brick in this row from left to
# right.
#
# If your line go through the edge of a brick, then the brick is not considered
# as crossed. You need to find out how to draw the line to cross the least
# bricks and return the number of crossed bricks.
#
# You cannot draw a line just along one of the two vertical edges of the wall,
# in which case the line will obviously cross no bricks.
#
#
#
# Example:
#
#
# Input: [[1,2,2,1],
# ⁠       [3,1,2],
# ⁠       [1,3,2],
# ⁠       [2,4],
# ⁠       [3,1,2],
# ⁠       [1,3,1,1]]
#
# Output: 2
#
# Explanation:
#
#
#
#
#
# Note:
#
#
# The width sum of bricks in different rows are the same and won't exceed
# INT_MAX.
# The number of bricks in each row is in range [1,10,000]. The height of wall
# is in range [1,10,000]. Total number of bricks of the wall won't exceed
# 20,000.
#
#
#

# @lc code=start

from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:
            return 0

        total_width = -1

        map = defaultdict(int)

        for row in wall:
            width = 0
            for cell in row:
                width += cell
                map[width] += 1
            if total_width == -1:
                total_width = width

        del map[total_width]

        if map:
            return len(wall) - max(map.values())
        return len(wall)


# @lc code=end

if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().leastBricks
    t.assertEqual(f([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]), 2)
    t.assertEqual(f([[1], [1], [1]]), 3)

