"""
submits:
- date: 2021-01-20
  minutes: 9
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (39.33%)
# Likes:    1314
# Dislikes: 198
# Total Accepted:    138.5K
# Total Submissions: 344.6K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
#
#
#
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
#
#
# Example:
#
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#
#
#
# Note:
#
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
#
#
#

from typing import List

# @lc code=start


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                self.matrix[row][col] = (
                    self._get_area(row, col - 1) + self._get_area(row - 1, col) - self._get_area(row - 1, col - 1) + matrix[row][col]
                )

    def _get_area(self, row, col):
        if row < 0 or col < 0:
            return 0
        else:
            return self.matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._get_area(row2, col2)
            - self._get_area(row1 - 1, col2)
            - self._get_area(row2, col1 - 1)
            + self._get_area(row1 - 1, col1 - 1)
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
if __name__ == "__main__":
    from tool import t

    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    f = NumMatrix(matrix)

    t(f.sumRegion(2, 1, 4, 3), 8)
    t(f.sumRegion(1, 1, 2, 2), 11)
    t(f.sumRegion(1, 2, 2, 4), 12)

