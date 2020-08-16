"""
submits:
- date: 2020-08-16
  minutes: 27
  cheating: false
"""
#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (32.80%)
# Likes:    2563
# Dislikes: 578
# Total Accepted:    384.1K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#


from typing import List

# @lc code=start

RIGHT = 0
BOTTOM = 1
LEFT = 2
UP = 3


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []
        if not matrix[0]:
            return []

        direction = RIGHT

        max_i = len(matrix) - 1
        max_j = len(matrix[0]) - 1
        i, j = 0, 0
        result = [matrix[0][0]]

        matrix[0][0] = None

        def move(i: int, j: int, direction: int):
            if direction == RIGHT:
                if j < max_j and matrix[i][j + 1] != None:
                    return i, j + 1
            elif direction == BOTTOM:
                if i < max_i and matrix[i + 1][j] != None:
                    return i + 1, j
            elif direction == LEFT:
                if j >= 1 and matrix[i][j - 1] != None:
                    return i, j - 1
            else:
                if i >= 1 and matrix[i - 1][j] != None:
                    return i - 1, j
            return False

        rotate_time = 0
        while rotate_time <= 2:

            # assert matrix[i][j] == None

            move_result = move(i, j, direction)
            if move_result:
                i, j = move_result
                result.append(matrix[i][j])
                matrix[i][j] = None
                rotate_time = 0
            else:
                direction = (direction + 1) % 4
                rotate_time += 1

        return result


# @lc code=end
if __name__ == "__main__":
    f = Solution().spiralOrder

    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5])
    t.assertEqual(f([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    t.assertEqual(
        f([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    )
