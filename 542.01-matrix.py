"""
submits:
  - date: 2020-08-02
    minutes: 36
    cheating: false
labels: []
commnet: ""
"""

#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (38.42%)
# Likes:    1516
# Dislikes: 107
# Total Accepted:    89K
# Total Submissions: 223.9K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
#
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[0,0,0]]
#
# Output:
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
#
#
# Example 2:
#
#
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,1,1]]
#
# Output:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,2,1]]
#
#
#
#
# Note:
#
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#

# @lc code=start

from typing import List, Tuple
from queue import Queue

# UNKNOWN = -1


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        i_len = len(matrix)
        j_len = len(matrix[0])
        output: List[List[int]] = []
        for i in range(i_len):
            output.append([-1] * j_len)

        distance = 0
        next: List[Tuple[int, int]] = []
        for i in range(i_len):
            for j in range(j_len):
                if matrix[i][j] == 0:
                    next.append((i, j))
                    output[i][j] = distance

        while next:
            curr = next
            next = []
            distance += 1

            for i, j in curr:
                for p, q in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= p < i_len and 0 <= q < j_len and output[p][q] < 0:
                        next.append((p, q))
                        output[p][q] = distance

        return output


# @lc code=end
if __name__ == "__main__":
    f = Solution().updateMatrix

    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(f([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    t.assertEqual(f([[0, 0, 0], [0, 1, 0], [1, 1, 1]]), [[0, 0, 0], [0, 1, 0], [1, 2, 1]])
