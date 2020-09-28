"""
submits:
- date: 2020-09-28
  minutes: 10
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (57.70%)
# Likes:    1922
# Dislikes: 25
# Total Accepted:    140.7K
# Total Submissions: 240.9K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
#
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
#
#
#
# If there is no common subsequence, return 0.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dp[i][j] 表示 text1[0:i+1] 和 text2[0:j+1] 的 Longest Common Subsequence 的长度
        # 其中 0 <= i < len(text1)
        # 其中 0 <= j < len(text2)
        dp: List[List[int]] = []
        for i in range(len(text1)):
            dp.append(len(text2) * [-1])

        def cal_with_cache(i: int, j: int):
            if i < 0 or j < 0:
                return 0

            if dp[i][j] == -1:
                dp[i][j] = cal(i, j)
            return dp[i][j]

        def cal(i: int, j: int):
            if i == 0 and j == 0:
                return 1 if text1[i] == text2[j] else 0

            if text1[i] == text2[j]:
                return cal_with_cache(i - 1, j - 1) + 1
            else:
                return max(cal_with_cache(i - 1, j), cal_with_cache(i, j - 1))

        for i in range(len(text1)):
            for j in range(len(text2)):
                cal_with_cache(i, j)

        return cal_with_cache(len(text1) - 1, len(text2) - 1)


# @lc code=end

