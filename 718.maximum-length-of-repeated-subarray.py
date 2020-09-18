"""
submits:
  - cheating: false
    date: 2020-07-25
    minutes: 18
comment: ""
labels: [dp]
"""

#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (48.56%)
# Likes:    1278
# Dislikes: 47
# Total Accepted:    63.2K
# Total Submissions: 128.3K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
#
# Example 1:
#
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#
#
# Note:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        # dp 是一个二维数组。dp[a][b] 表示以 A 的 a 项开始，以 B 的 b 项开始的最长的 subarray 的长度
        # 其中：
        # 0 <= a < len(A)
        # 0 <= b < len(B)

        len_a = len(A)
        len_b = len(B)

        dp = []
        for a in range(len_a):
            dp.append([0] * len_b)

        best_len = 0

        b = len_b - 1
        for a in range(0, len_a):
            dp[a][b] = A[a] == B[b]
        a = len_a - 1
        for b in range(0, len_b):
            dp[a][b] = A[a] == B[b]

        for a in range(len_a - 2, -1, -1):
            for b in range(len_b - 2, -1, -1):
                if A[a] == B[b]:
                    dp[a][b] = dp[a + 1][b + 1] + 1  # <--------- 这行是核心逻辑
                    best_len = max(best_len, dp[a][b])

        return best_len


# @lc code=end
if __name__ == "__main__":
    f = Solution().findLength

    assert f([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
    assert f([1, 2, 3, 2, 1], [3, 2, 5, 4, 7]) == 2
    assert f([69, 53, 93, 37, 79], [69, 53, 59, 26, 14]) == 2
