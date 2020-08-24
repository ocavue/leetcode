"""
- date: 2020-08-24
  cheating: false
  minutes: 10
comment: ""
"""


#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.32%)
# Likes:    1185
# Dislikes: 153
# Total Accepted:    194.7K
# Total Submissions: 526.1K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Example 1:
#
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
#
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        char2word = {}
        word2char = {}

        words = string.split(" ")
        if len(pattern) != len(words):
            return False

        for char, word in zip(pattern, words):
            if char not in char2word:
                char2word[char] = word
            elif char2word[char] != word:
                return False

            if word not in word2char:
                word2char[word] = char
            elif word2char[word] != char:
                return False
        return True


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().wordPattern

    t.assertTrue(f("abba", "dog cat cat dog"))
    t.assertFalse(f("abba", "dog cat cat fish"))
    t.assertFalse(f("aaaa", "dog cat cat dog"))
    t.assertFalse(f("abba", "dog dog dog dog"))
