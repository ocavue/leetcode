"""
submits:
  - date: 2020-08-04
    minutes: 240
    cheating: true
  - date: 2020-09-19
    minutes: 30
    cheating: false
labels: [dp]
comment: |
  我发现这个答案的思路非常有用：https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
  总结一下就是：
  1. 动态规划 = 递归 + cache
  2. 递归如果没有尾递归优化的话会造成调用栈溢出，而动态规划没有这个问题
  3. 遇到不知道怎么做的题目，先尝试使用递归去实现，然后再增加动态规划所需要的 cache

  第二次做题的时候，一开始状态函数一直找不出来，然后用一个矩阵把 horse => ros 需要的步骤全画出来了，很快就理清楚了逻辑。所以通过例子去寻找规律是非常有用的。
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

from typing import List
from functools import lru_cache


# 基于动态规划的实现（性能更好）
def min_distance_dp(word1: str, word2: str) -> int:
    len1, len2 = len(word1), len(word2)

    # dp[i][j] 表示 word1[:i] 和 word2[:j] 之间至少需要多少个转换步骤
    dp: List[List[int]] = []
    for i in range(len1 + 1):
        dp.append([-1] * (len2 + 1))

    def cal_with_cache(i: int, j: int) -> int:
        if i <= 0:
            return max(j, 0)
        if j <= 0:
            return max(i, 0)

        if dp[i][j] == -1:
            dp[i][j] = cal(i, j)
        return dp[i][j]

    def cal(i: int, j: int) -> int:
        char1 = word1[i - 1]
        char2 = word2[j - 1]

        if char1 == char2:
            return cal_with_cache(i - 1, j - 1)
        else:
            # fmt:off
            return min(
                cal_with_cache(i - 1, j),
                cal_with_cache(i, j - 1),
                cal_with_cache(i - 1, j - 1),
            ) + 1
            # fmt:on

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            cal_with_cache(i, j)
    return cal_with_cache(len1, len2)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return min_distance_dp(word1, word2)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(min_distance_dp("horse", "ros"), 3)
    t.assertEqual(min_distance_dp("intention", "execution"), 5)
