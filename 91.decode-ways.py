"""
submits:
- date: 2020-12-08
  minutes: 10
  cheating: true
labels:
- dp
"""
#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (25.18%)
# Likes:    3531
# Dislikes: 3249
# Total Accepted:    478.1K
# Total Submissions: 1.9M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: s = "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
#
#
# Example 3:
#
#
# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with
# '0'. We cannot ignore a zero when we face it while decoding. So, each '0'
# should be part of "10" --> 'J' or "20" --> 'T'.
#
#
# Example 4:
#
#
# Input: s = "1"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).
#
#
#

# @lc code=start

valid_numbers = set([str(i) for i in range(1, 27)])


class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] 表示 s[i:] 能够表示为多少个单词
        dp = [0] * (len(s) + 1)

        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] in valid_numbers:
                dp[i] += dp[i + 1]
            if i != len(s) - 1 and s[i : i + 2] in valid_numbers:
                dp[i] += dp[i + 2]
        return dp[0]


# @lc code=end

if __name__ == "__main__":
    from tool import t

    f = Solution().numDecodings
    t(f("12"), 2)
    t(f("226"), 3)

