"""
submits:
- date: 2021-01-03
  minutes: 2
  cheating: false
"""
#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (53.13%)
# Likes:    754
# Dislikes: 221
# Total Accepted:    245.3K
# Total Submissions: 461K
# Testcase Example:  '"a"\n"b"'
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
#
# Each letter in the magazine string can only be used once in your ransom
# note.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# You may assume that both strings contain only lowercase letters.
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        for char in ransomNote:
            if char in m and m[char] >= 1:
                m[char] -= 1
            else:
                return False
        return True


# @lc code=end

