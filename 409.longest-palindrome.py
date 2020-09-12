#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (49.58%)
# Likes:    1240
# Dislikes: 90
# Total Accepted:    176.4K
# Total Submissions: 340.6K
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
#
#
# Example 1:
#
#
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 1
#
#
# Example 3:
#
#
# Input: s = "bb"
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consits of lower-case and/or upper-case English letters only.
#
#
#

# @lc code=start

from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        length = 0
        used_odd = False
        for c, num in counter.items():
            if num % 2 == 0:
                length += num
            else:
                if used_odd:
                    length += num - 1
                else:
                    length += num
                    used_odd = True
        return length


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    f = Solution().longestPalindrome

    t.assertEqual(f("abccccdd"), 7)
    t.assertEqual(f("a"), 1)
    t.assertEqual(f("bb"), 2)
    t.assertEqual(f("ccc"), 3)
    t.assertEqual(f("cdc"), 3)
    t.assertEqual(f("testingwhethe"), 7)
