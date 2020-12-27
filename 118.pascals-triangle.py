"""
submits:
- date: 2020-12-27
  minutes: 4
  cheating: false
"""
#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (53.40%)
# Likes:    1960
# Dislikes: 122
# Total Accepted:    432.2K
# Total Submissions: 802.4K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#

# @lc code=start


def pascal_triangle():
    row = [1]
    while True:
        yield row
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        row = next_row


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = []
        for row in pascal_triangle():

            res.append(row)
            if len(res) == numRows:
                return res


# @lc code=end

