"""
submits:
- date: 2020-10-07
  minutes: 16
  cheating: true
labels:
- divide-and-conquer

"""

#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (40.26%)
# Likes:    1184
# Dislikes: 103
# Total Accepted:    68.7K
# Total Submissions: 169.9K
# Testcase Example:  '"aaabb"\n3'
#
#
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
#
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
#
#
#
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
#
#
#


# @lc code=start


from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        # 找到每个字符出现的次数
        counter = Counter(s)
        # 找到出现次数最少的字母的出现次数
        min_times, min_char = min((times, char) for char, times in counter.items())

        if min_times >= k:
            return len(s)

        return max(self.longestSubstring(part, k) for part in s.split(min_char))


# @lc code=end

