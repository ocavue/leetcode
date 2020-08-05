"""
submits:
  - date: 2020-08-05
    minutes: 60
    cheating: false
comment: "这道题可以使用 84.largest-rectangle-in-histogram 的思路去做"
labels: []
"""

#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (36.02%)
# Likes:    2896
# Dislikes: 71
# Total Accepted:    181.9K
# Total Submissions: 483K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
#
#
#

from typing import List


# @lc code=start


def max_rect(matrix: List[List[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])

    dpi = []
    dpj = []
    for _ in range(m):
        dpi.append([0] * n)
        dpj.append([0] * n)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                dpi[i][j] = dpi[i - 1][j] + 1 if i >= 1 else 1
                dpj[i][j] = dpj[i][j - 1] + 1 if j >= 1 else 1

    best_area = 0
    for max_i in range(m):
        for max_j in range(n):
            if matrix[max_i][max_j] == "1":
                min_i = max_i - dpi[max_i][max_j] + 1

                i = max_i
                len_j = dpj[i][max_j]
                while i >= min_i:
                    len_j = min(len_j, dpj[i][max_j])
                    len_i = max_i - i + 1
                    best_area = max(best_area, len_j * len_i)
                    i -= 1
    return best_area


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        return max_rect(matrix)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(
        6, max_rect([["1", "0", "1", "0", "1"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"],])
    )
    t.assertEqual(1, max_rect([["1"]]))
    t.assertEqual(1, max_rect([["1", "0"]]))
