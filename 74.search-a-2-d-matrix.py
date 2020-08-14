#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.90%)
# Likes:    1917
# Dislikes: 162
# Total Accepted:    336.2K
# Total Submissions: 920.5K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#
#

from typing import List

# @lc code=start


def binary_search(lo: int, hi: int, target: int, get_item):
    assert lo <= hi
    if get_item(lo) <= target <= get_item(hi):

        while lo < hi - 1:
            mi = (hi + lo) // 2
            if get_item(mi) <= target:
                lo = mi
            else:
                hi = mi

        for i in [lo, hi]:
            if get_item(i) == target:
                return i
        return lo
    return 0


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False

        row_len = len(matrix[0])

        def get_item(i):
            row = i // row_len
            col = i % row_len
            print("get_item", i, matrix[row][col])
            return matrix[row][col]

        received = get_item(binary_search(0, len(matrix) * len(matrix[0]) - 1, target, get_item))
        print(received)
        return received == target


# @lc code=end
if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    f = Solution().searchMatrix
    assert f(matrix, target) is True
