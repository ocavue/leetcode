"""
submits:
  - date: 2020-07-26
    cheating: false
    minutes: 19
comments: |
  这道题和 516 类似
labals: [dp]
"""

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.80%)
# Likes:    5654
# Dislikes: 475
# Total Accepted:    818.2K
# Total Submissions: 2.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp 是一个二维数组。dp[i][j] 表示 s[i:j+1] 的回文字符串长度。如果 s[i:j+1] 并不是回文的话，那么 dp[i][j] 就是 0。
        #
        # 0 <= i <= j < len(s)

        dp = []
        for _ in range(len(s)):
            dp.append([0] * len(s))

        # l == j - i == 0
        for i in range(len(s)):
            dp[i][i] = 1

        # l == j - i == 1
        for j in range(1, len(s)):
            i = j - 1
            dp[i][j] = 2 if s[i] == s[j] else 0

        # l == j - i >= 2
        for l in range(2, len(s)):
            for j in range(l, len(s)):
                i = j - l
                if dp[i + 1][j - 1]:
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i + 1][j - 1]

        best_i, best_j, best_l = 0, 0, 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if dp[i][j] >= best_l:
                    best_l = dp[i][j]
                    best_i = i
                    best_j = j

        return s[best_i : best_j + 1]


# @lc code=end


if __name__ == "__main__":
    f = Solution().longestPalindrome

    for case, expected in [
        ("babad", "aba"),
        ("cbbd", "bb"),
        ("bbbbbb", "bbbbbb"),
        ("axyzyxb", "xyzyx"),
    ]:
        received = f(case)
        assert received == expected, "wrong answer for {}\nexpected: {}\nreceived: {}".format(repr(case), repr(expected), repr(received))
