"""
submits:
- date: 2020-12-10
  minutes: 21
  cheating: false
"""
#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (48.68%)
# Likes:    936
# Dislikes: 360
# Total Accepted:    99.1K
# Total Submissions: 202.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
#
#
#
# Example:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Explanation:
#
#
#
#
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.
#
#

from typing import List

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        result: List[int] = []

        for line in range(0, (m + n) - 1):
            if line % 2 == 0:
                if line < m:
                    i = line
                    j = 0
                else:
                    i = m - 1
                    j = line - i

                assert i + j == line

                while 0 <= i < m and 0 <= j < n:
                    result.append(matrix[i][j])
                    i -= 1
                    j += 1
            else:
                if line < n:
                    i = 0
                    j = line
                else:
                    j = n - 1
                    i = line - j

                assert i + j == line

                while 0 <= i < m and 0 <= j < n:
                    result.append(matrix[i][j])
                    i += 1
                    j -= 1
        return result
        return result


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().findDiagonalOrder
    t(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 4, 7, 5, 3, 6, 8, 9])
    t(f([[2,3]]), [2,3])
