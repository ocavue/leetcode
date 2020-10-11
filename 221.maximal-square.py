"""
submits:
- date: 2020-10-11
  minute: 18
  cheating: false
labels:
- dp
"""
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (35.42%)
# Likes:    3557
# Dislikes: 92
# Total Accepted:    292K
# Total Submissions: 768.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#
#

# @lc code=start


class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0

        # dp[i][j] 表示以 matrix[i][j] 作为方形的右下角，最大的边长是多少
        # 这里 dp 和 matrix 共用同一个列表，节约内存。

        dp = matrix

        max_len = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        left_top = dp[i - 1][j - 1]
                        left = dp[i - 1][j]
                        top = dp[i][j - 1]

                        if left >= left_top and top >= left_top:
                            dp[i][j] = left_top + 1
                        else:
                            dp[i][j] = min(left, top) + 1

                max_len = max(max_len, dp[i][j])

        return max_len * max_len


# @lc code=end

if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().maximalSquare
    t.assertEqual(f([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]), 4)

