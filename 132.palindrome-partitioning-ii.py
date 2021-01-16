"""
submits:
- date: 2021-01-16
  minutes: 33
  cheating: true
labels:
- dp
"""
#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (30.52%)
# Likes:    1587
# Dislikes: 47
# Total Accepted:    147K
# Total Submissions: 474.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#
# Example 1:
#
#
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 0
#
#
# Example 3:
#
#
# Input: s = "ab"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consists of lower-case English letters only.
#
#
#

# @lc code=start

from functools import lru_cache
from collections import defaultdict


class Solution:
    def minCut(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        @lru_cache(None)
        def is_palindrome(i, j) -> bool:
            assert 0 <= i <= len(s)
            assert 0 <= j <= len(s)
            if j - i <= 1:
                return True
            return s[i] == s[j - 1] and is_palindrome(i + 1, j - 1)

        @lru_cache(None)
        def min_cut(j) -> int:
            assert 0 <= j <= len(s)
            best = j - 1
            for i in range(0, j):
                if is_palindrome(i, j):
                    best = min(best, min_cut(i) + 1)
            return best

        for j in range(len(s)):
            min_cut(j)

        return min_cut(len(s))


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().minCut)
    t(["aab"], 1)
    t(["a"], 0)
    t(["ab"], 1)

    t(["eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"], 42)

