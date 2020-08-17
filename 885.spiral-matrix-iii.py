"""
submits:
- date: 2020-08-17
  minutes: 36
  cheating: false
comment: |
  这道题一定要在纸上作图才能弄明白。我怀疑要是不画图，我过几天就看不懂我的答案了。
"""
#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#
# https://leetcode.com/problems/spiral-matrix-iii/description/
#
# algorithms
# Medium (67.83%)
# Likes:    226
# Dislikes: 293
# Total Accepted:    20.4K
# Total Submissions: 29.4K
# Testcase Example:  '1\n4\n0\n0'
#
# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0)
# facing east.
#
# Here, the north-west corner of the grid is at the first row and column, and
# the south-east corner of the grid is at the last row and column.
#
# Now, we walk in a clockwise spiral shape to visit every position in this
# grid.
#
# Whenever we would move outside the boundary of the grid, we continue our walk
# outside the grid (but may return to the grid boundary later.)
#
# Eventually, we reach all R * C spaces of the grid.
#
# Return a list of coordinates representing the positions of the grid in the
# order they were visited.
#
#
#
# Example 1:
#
#
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
#
#
#
#
#
#
# Example 2:
#
#
# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output:
# [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
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
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
#
#
#
#

# @lc code=start

from typing import List

RIGHT = 0
BOTTOM = 1
LEFT = 2
UP = 3


def move_a_cirle(r: int, c: int, n: int):
    """
    顺时针转转一整圈，并返回说经过的点。
    从右上角下面那个点开始，向下走，并最终转到右上角。
    这一圈一共经过了 4 * n 个点
    """

    yield [r, c]
    for _ in range(n - 1):
        r += 1
        yield [r, c]
    for _ in range(n):
        c -= 1
        yield [r, c]
    for _ in range(n):
        r -= 1
        yield [r, c]
    for _ in range(n):
        c += 1
        yield [r, c]


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        result: List[List[int]] = []
        if 0 <= r0 < R and 0 <= c0 < C:
            result.append([r0, c0])

        n = 2
        r, c = r0, c0 + 1
        while True:
            if len(result) == R * C:
                return result

            for pair in move_a_cirle(r, c, n):
                # print(f'n = {n}; pair = {pair}')
                if 0 <= pair[0] < R and 0 <= pair[1] < C:
                    result.append(pair)
                    if len(result) == R * C:
                        return result

            n += 2
            r -= 1
            c += 1

            if n >= max([R, C]) * 2 + 3:
                raise Exception("something went wrong")
        return result


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    f = Solution().spiralMatrixIII

    t.assertEqual(f(R=1, C=4, r0=0, c0=0), [[0, 0], [0, 1], [0, 2], [0, 3]])
    t.assertEqual(f(R=1, C=1, r0=0, c0=0), [[0, 0]])
    t.assertEqual(
        f(R=5, C=6, r0=1, c0=4),
        [
            [1, 4],
            [1, 5],
            [2, 5],
            [2, 4],
            [2, 3],
            [1, 3],
            [0, 3],
            [0, 4],
            [0, 5],
            [3, 5],
            [3, 4],
            [3, 3],
            [3, 2],
            [2, 2],
            [1, 2],
            [0, 2],
            [4, 5],
            [4, 4],
            [4, 3],
            [4, 2],
            [4, 1],
            [3, 1],
            [2, 1],
            [1, 1],
            [0, 1],
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
        ],
    )

