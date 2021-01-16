"""
submits:
- date: 2021-01-16
  minutes: 29
  cheating: false
comment: |
  我实在没有看出来这个和 dp 有什么关系

"""
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string/description/
#
# algorithms
# Hard (34.10%)
# Likes:    694
# Dislikes: 768
# Total Accepted:    118.8K
# Total Submissions: 345.1K
# Testcase Example:  '"great"\n"rgeat"'
#
# We can scramble a string s to get a string t using the following
# algorithm:
#
#
# If the length of the string is 1, stop.
# If the length of the string is > 1, do the following:
#
# Split the string into two non-empty substrings at a random index, i.e., if
# the string is s, divide it to x and y where s = x + y.
# Randomly decide to swap the two substrings or to keep them in the same order.
# i.e., after this step, s may become s = x + y or s = y + x.
# Apply step 1 recursively on each of the two substrings x and y.
#
#
#
#
# Given two strings s1 and s2 of the same length, return true if s2 is a
# scrambled string of s1, otherwise, return false.
#
#
# Example 1:
#
#
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings
# and keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both
# substrings. divide at ranom index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first
# substring and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively,
# divide "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both
# substrings in the same order.
# The algorithm stops now and the result string is "rgeat" which is s2.
# As there is one possible scenario that led s1 to be scrambled to s2, we
# return true.
#
#
# Example 2:
#
#
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
#
#
# Example 3:
#
#
# Input: s1 = "a", s2 = "a"
# Output: true
#
#
#
# Constraints:
#
#
# s1.length == s2.length
# 1 <= s1.length <= 30
# s1 and s2 consist of lower-case English letters.
#
#
#

# @lc code=start

from functools import lru_cache
from collections import Counter


@lru_cache(None)
def is_scramble(s1, s2):
    # assert Counter(s1) == Counter(s2)

    if (len(s1) == 0 or len(s1) == 1) and s1 == s2:
        return True

    result = False
    for i in range(1, len(s1)):
        c1 = Counter(s1[:i])
        c2x = Counter(s2[:i])
        c2y = Counter(s2[-i:])

        if c1 == c2x and not result:
            result = is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])
        if c1 == c2y and not result:
            result = is_scramble(s1[:i], s2[-i:]) and is_scramble(s1[i:], s2[:-i])
        if result:
            return result

    return result


class Solution:
    def isScramble(self, s1, s2):
        if Counter(s1) != Counter(s2):
            return False
        return is_scramble(s1, s2)


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().isScramble)
    t(("great", "rgeat"), True)
    t(("abcde", "caebd"), False)
    t(("a", "a"), True)
    t(("a", "b"), False)
    t(("abcdd", "abdac"), False)
