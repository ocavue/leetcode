"""
submits:
- date: 2020-09-22
  minutes: 20
  cheating: false
labels: [dp]
comment: 一道比较典型的 DP 题目

"""
#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (36.88%)
# Likes:    977
# Dislikes: 49
# Total Accepted:    124.8K
# Total Submissions: 338.4K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# Example 2:
#
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
#
#
#

# @lc code=start

from typing import List
from pprint import pprint


class Solution:
    def numDistinct(self, S: str, T: str) -> int:

        # dp[s][t] = x
        # 表示使用 S[0:s] 去凑成 T[0:t] 有 x 中可能
        # 0 <= s <= len(S)
        # 0 <= t <= len(T)
        #
        dp: List[List[int]] = []
        for i in range(len(S) + 1):
            dp.append([-1] * (len(T) + 1))

        def cal_with_cache(s: int, t: int) -> int:
            if s < t:
                return 0
            if t == 0:
                return 1

            if dp[s][t] == -1:
                dp[s][t] = cal(s, t)
            return dp[s][t]

        def cal(s: int, t: int) -> int:
            assert s >= t > 0
            assert 0 <= s <= len(S)
            assert 0 <= t <= len(T)

            char_s = S[s - 1]
            char_t = T[t - 1]
            if char_s == char_t:
                return cal_with_cache(s - 1, t - 1,) + cal_with_cache(s - 1, t)
            else:
                return cal_with_cache(s - 1, t)

        for s in range(len(S) + 1):
            for t in range(min(s + 1, len(T) + 1)):
                cal_with_cache(s, t)
        # result = cal_with_cache(len(S), len(T))
        # pprint(dp)
        return cal_with_cache(len(S), len(T))


# @lc code=end
if __name__ == "__main__":
    import unittest

    f = Solution().numDistinct
    t = unittest.TestCase("__init__")
    t.assertEqual(f("rabbbit", "rabbit"), 3)
    t.assertEqual(f("babgbag", "bag"), 5)
