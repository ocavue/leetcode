"""
submits:
  - date: 2020-07-26
    cheating: true
    minutes: 120
  - date: 2020-09-19
    cheating: true
    minutes: 23
comment: |
  这道题重点是构造出状态转移函数。
  状态：以 dp[i][j] 表示 s[i:j+1] 可以找到的 Longest Palindromic Subsequence
  状态转移：
        如果 s[i] == s[j]，那么最长回数长度就是 2 + 子串长度
        如果 s[i] != s[j]，那么最长回数长度就是 max(dp[i][j-1] + dp[i+1][j])
  同时要注意这道题和 5.longest-palindromic-substring 是不一样的。subsequence 中的元素是可以离散的，但是 substring 中的元素是紧挨着的。

  这道题也告诉我，在 Leetcode 里，达到 1000*1000 数量级的 DP cache 是可以接受的
labels: [dp]

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
        # dp[i][j] 表示 s[i:j+1] 中最长的 palindromic subsequence 是多少

        dp: List[List[int]] = []
        for _ in range(len(s)):
            dp.append([0] * (len(s)))

        def cal(i: int, j: int):
            assert 0 <= i <= j < len(s)

            if i == j:
                return 1
            if i == j - 1:
                return 2 if s[i] == s[j] else 1

            if s[i] == s[j]:
                return 2 + cal_with_cache(i + 1, j - 1)
            else:
                return max(cal_with_cache(i + 1, j), cal_with_cache(i, j - 1))

        def cal_with_cache(i: int, j: int):
            if dp[i][j] == 0:
                dp[i][j] = cal(i, j)
            return dp[i][j]

        return cal_with_cache(0, len(s) - 1)


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

