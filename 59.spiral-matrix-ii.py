"""
submits:
- date: 2020-08-16
  cheating: false
  minutes: 9
"""
#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (51.40%)
# Likes:    1055
# Dislikes: 115
# Total Accepted:    198.7K
# Total Submissions: 368.2K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
#

from typing import List

# @lc code=start


RIGHT = 0
BOTTOM = 1
LEFT = 2
UP = 3


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        # if n == 1:
        #     return [[1]]
        # if n == 2:
        #     return [[1, 2], [4, 3]]

        matrix = []
        for i in range(n):
            matrix.append([0] * n)

        max_i = max_j = n - 1
        i = j = 0
        matrix[0][0] = 1
        next_num = 2
        direction = RIGHT

        def move(i: int, j: int, direction: int):
            if direction == RIGHT:
                if j < max_j and matrix[i][j + 1] == 0:
                    return i, j + 1
            elif direction == BOTTOM:
                if i < max_i and matrix[i + 1][j] == 0:
                    return i + 1, j
            elif direction == LEFT:
                if j >= 1 and matrix[i][j - 1] == 0:
                    return i, j - 1
            else:
                if i >= 1 and matrix[i - 1][j] == 0:
                    return i - 1, j
            return False

        rotate_time = 0

        while rotate_time <= 2:

            assert matrix[i][j] >= 1

            move_result = move(i, j, direction)
            if move_result:
                i, j = move_result
                matrix[i][j] = next_num
                next_num += 1
                rotate_time = 0
            else:
                direction = (direction + 1) % 4
                rotate_time += 1

        return matrix


# @lc code=end
if __name__ == "__main__":

    f = Solution().generateMatrix

    import unittest

    t = unittest.TestCase("__init__")

    # fmt: off

    t.assertEqual(
        f(3),
        [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ]
    )
