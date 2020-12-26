"""
submits:
- date: 2020-12-26
  minutes: 3
  cheating: false
"""
#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#
# https://leetcode.com/problems/toeplitz-matrix/description/
#
# algorithms
# Easy (65.41%)
# Likes:    1235
# Dislikes: 86
# Total Accepted:    114.2K
# Total Submissions: 173.8K
# Testcase Example:  '[[1,2,3,4],[5,1,2,3],[9,5,1,2]]'
#
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
# return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
# same elements.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
#
#
# Example 2:
#
#
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
#
#
#
# Follow up:
#
#
# What if the matrix is stored on disk, and the memory is limited such that you
# can only load at most one row of the matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into
# the memory at once?
#
#
#

from typing import List

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            r1 = matrix[i]
            r2 = matrix[i + 1]
            for j in range(len(r1) - 1):
                if r1[j] != r2[j + 1]:
                    return False
        return True


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().isToeplitzMatrix
    t(f([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)
    t(f([[1, 2], [2, 2]]), False)

