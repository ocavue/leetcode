"""
submits:
  - date: 2020-07-26
    cheating: true
    minutes: 120
comments: |
  这道题重点是构造出状态转移函数。
  状态：以 dp[i][j] 表示 s[i:j+1] 可以找到的 Longest Palindromic Subsequence
  状态转移：
        如果 s[i] == s[j]，那么最长回数长度就是 2 + 子串长度
        如果 s[i] != s[j]，那么最长回数长度就是 max(dp[i][j-1] + dp[i+1][j])
  同时要注意这道题和 5.longest-palindromic-substring 是不一样的。subsequence 中的元素是可以离散的，但是 substring 中的元素是紧挨着的。
labals: [dp]

"""

#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (50.63%)
# Likes:    1995
# Dislikes: 178
# Total Accepted:    119.8K
# Total Submissions: 226.3K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
#
#
# "bbbab"
#
# Output:
#
#
# 4
#
# One possible longest palindromic subsequence is "bbbb".
#
#
#
# Example 2:
# Input:
#
#
# "cbbd"
#
# Output:
#
#
# 2
#
# One possible longest palindromic subsequence is "bb".
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
#
#
#


from typing import List

# @lc code=start


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            return 2 if s[0] == s[1] else 1

        # dp 是一个二维数组，dp[i][j] 表示从 s 的第 i 项到第 j 项，Longest Palindromic Subsequence 的长度是多少
        # 其中 0 <= i <= j < len(s)
        dp: List[List[int]] = []
        for _ in range(len(s)):
            dp.append([0] * len(s))
        # assert len(dp) == len(dp[0]) == len(s)

        # 当 i == j 的时候
        for i in range(len(s)):
            dp[i][i] = 1

        # 当 j-i == 1 的时候
        for j in range(1, len(s)):
            i = j - 1
            dp[i][j] = 2 if s[i] == s[j] else 1

        # 当 l = j-i >= 2 的时候
        for l in range(2, len(s)):
            for j in range(2, len(s)):
                i = j - l

                ############ 状态转移 ############
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]


# @lc code=end

if __name__ == "__main__":
    f = Solution().longestPalindromeSubseq

    for case, expected in [
        ("abcba", 5),
        ("pppabcbaqqq", 5),
        ("bbbab", 4),
        ("a", 1),
        ("aa", 2),
    ]:
        received = f(case)
        assert received == expected, "wrong answer for {}\nexpected: {}\nreceived: {}".format(repr(case), repr(expected), repr(received))

