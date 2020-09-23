"""
submits:
- date: 2020-09-23
  minute: 3
  cheating: false
labels: [PQ]
comment: |
  这道题也能使用 PQ 去做
"""
#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (58.96%)
# Likes:    1820
# Dislikes: 133
# Total Accepted:    212K
# Total Submissions: 334.7K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
#
#
#
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
#
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        pairs = [(count, c) for c, count in counter.items()]
        pairs.sort(reverse=True)
        result = ""
        for count, c in pairs:
            result += c * count
        return result


# @lc code=end

