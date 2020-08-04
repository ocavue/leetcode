"""
submits:
  - data: 2020-08-04
    minutes: 240
    cheating: true
labels: [dp]
comment: |
  我发现这个答案的思路非常有用：https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
  总结一下就是：
  1. 动态规划 = 递归 + cache
  2. 递归如果没有尾递归优化的话会造成调用栈溢出，而动态规划没有这个问题
  3. 遇到不知道怎么做的题目，先尝试使用递归去实现，然后再增加动态规划所需要的 cache
"""

#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (41.39%)
# Likes:    4090
# Dislikes: 57
# Total Accepted:    286.9K
# Total Submissions: 641.9K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#

# @lc code=start

from functools import lru_cache


# 基于递归的实现（思路更清晰）
@lru_cache()
def min_distance_recursion(word1: str, word2: str) -> int:
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)

    if word1[0] == word2[0]:
        return min_distance_recursion(word1[1:], word2[1:])
    else:
        # Insert
        case1 = 1 + min_distance_recursion(word1[1:], word2)
        # Delete
        case2 = 1 + min_distance_recursion(word1, word2[1:])
        # Replace
        case3 = 1 + min_distance_recursion(word1[1:], word2[1:])
        return min(case1, case2, case3)


# 基于动态规划的实现（性能更好）
def min_distance_dp(word1: str, word2: str) -> int:
    len1 = len(word1)
    len2 = len(word2)

    # dp[i][j] 表示 word1[i:] 和 word2[j:] 之间的最短距离
    # 其中
    #   0 <= i <= len1
    #   0 <= j <= len2
    dp = []
    for i in range(len1 + 1):
        dp.append([None] * (len2 + 1))

    j = len2
    for i in range(len1 + 1):
        dp[i][j] = len1 - i
        # assert len(word2[j:]) == 0 and len(word1[i:]) == dp[i][j]
    i = len1
    for j in range(len2 + 1):
        dp[i][j] = len2 - j
        # assert len(word1[i:]) == 0 and len(word2[j:]) == dp[i][j]

    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                # Insert
                case1 = 1 + dp[i + 1][j]
                # Delete
                case2 = 1 + dp[i][j + 1]
                # Replace
                case3 = 1 + dp[i + 1][j + 1]
                dp[i][j] = min(case1, case2, case3)

    return dp[0][0]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return min_distance_recursion(word1, word2)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(min_distance_recursion("horse", "ros"), 3)
    t.assertEqual(min_distance_recursion("intention", "execution"), 5)

    t.assertEqual(min_distance_dp("horse", "ros"), 3)
    t.assertEqual(min_distance_dp("intention", "execution"), 5)
