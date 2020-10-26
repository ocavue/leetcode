"""
submits:
- date: 2020-10-26
  minutes: 15
  cheating: false
labels: [dp]
"""
# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
#
# algorithms
# Medium (35.83%)
# Likes:    663
# Dislikes: 91
# Total Accepted:    26.9K
# Total Submissions: 75K
# Testcase Example:  '"a"'
#
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
#
# Now we have another string p. Your job is to find out how many unique
# non-empty substrings of p are present in s. In particular, your input is the
# string p and you need to output the number of different non-empty substrings
# of p in the string s.
#
# Note: p consists of only lowercase English letters and the size of p might be
# over 10000.
#
# Example 1:
#
# Input: "a"
# Output: 1
#
# Explanation: Only the substring "a" of string "a" is in the string s.
#
#
#
# Example 2:
#
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string
# s.
#
#
#
# Example 3:
#
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
# string "zab" in the string s.
#
#
#

# @lc code=start

from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0

        # dp[i] = k 表示以 p[i] 为起始字符，最长的 substring 的长度是 k
        #
        # dp = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}

        dp = [0] * len(p)
        dp[-1] = 1

        for i in range(len(p) - 2, -1, -1):
            curr_char = p[i]
            next_char = p[i + 1]

            if (ord(curr_char) + 1 == ord(next_char)) or (curr_char == "z" and next_char == "a"):
                dp[i] = dp[i + 1] + 1
            else:
                dp[i] = 1

        map = defaultdict(int)
        for i in range(len(p)):
            char = p[i]
            map[char] = max(map[char], dp[i])

        return sum(map.values())


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()

    f = Solution().findSubstringInWraproundString

    t.assertEqual(f("cac"), 2)
