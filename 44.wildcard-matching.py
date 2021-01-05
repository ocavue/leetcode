"""
submits:
- minutes: 49
  date: 2020-01-05
  cheating: true
labels: [dp]
"""
#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (25.00%)
# Likes:    2596
# Dislikes: 126
# Total Accepted:    279.2K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
#
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
#
#
# Example 4:
#
#
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
#
#
# Example 5:
#
#
# Input: s = "acdcb", p = "a*c?b"
# Output: false
#
#
#
# Constraints:
#
#
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
#
#
#

# @lc code=start

from functools import lru_cache

from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] 表示 s[:i] 能不能使用 p[:j] 表示
        # 其中
        # 0 <= i <= len(s)
        # 0 <= j <= len(p)

        if len(p) - p.count("*") > len(s):
            return False

        dp: List[List[bool]] = []
        for i in range(len(s) + 1):
            dp.append([None] * (len(p) + 1))

        @lru_cache
        def match(i: int, j: int):
            assert 0 <= i <= len(s)
            assert 0 <= j <= len(p)

            if dp[i][j] is not None:
                return dp[i][j]

            if j == 0:
                dp[i][j] = s[:i] == ""
                return dp[i][j]
            if i == 0:
                dp[i][j] = p[:j] == "" or set(p[:j]) == set(["*"])
                return dp[i][j]

            ss = s[i - 1]
            pp = p[j - 1]
            if pp == "?":
                dp[i][j] = match(i - 1, j - 1)
                return dp[i][j]
            if pp == "*":
                dp[i][j] = match(i - 1, j - 1) or match(i - 1, j) or match(i, j - 1)
                return dp[i][j]
            else:
                dp[i][j] = ss == pp and match(i - 1, j - 1)
                return dp[i][j]

        # for i in range(0, len(s) + 1):
        #     for j in range(0, len(p) + 1):
        #         match(i, j)

        return match(len(s), len(p))


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().isMatch
    t(f("aa", "a"), False)
    t(f("aa", "*"), True)
    t(f("aa", "??"), True)
    t(f("aa", "?*?"), True)
    t(f("aa", "a*"), True)
    t(f("adceb", "*a*b"), True)
    t(f("acdcb", "a*c?b"), False)
