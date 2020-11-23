"""
submits:
- date: 2020-11-23
  minutes: 10
  cheating: false
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (51.59%)
# Likes:    894
# Dislikes: 79
# Total Accepted:    102.6K
# Total Submissions: 198.3K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
#
# Example 1:
#
#
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
#
# Example 2:
#
#
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
#
# Example 3:
#
#
# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#
#
#
# Constraints:
#
#
# 0 <= words.length <= 10^3
# 0 <= words[i].length <= 10^3
# words[i] consists only of lowercase English letters.
#
#
#

# @lc code=start


def word_to_num(word):
    num = 0
    for char in word:
        bit = ord(char) - ord("a")
        num |= 1 << bit
    return num


class Solution:
    def maxProduct(self, words) -> int:
        l = len(words)
        nums = [word_to_num(word) for word in words]
        best = 0
        for i in range(l - 1):
            for j in range(i + 1, l):
                if not (nums[i] & nums[j]):
                    best = max(best, len(words[i]) * len(words[j]))
        return best


# @lc code=end

