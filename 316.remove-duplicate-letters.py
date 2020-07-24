"""
submits:
  - cheating: false
    date: 2020-07-24
    minutes: 60
comment: "这道题我之前看过答案，不过这次还是花了很久才做出来"
"""

#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (34.32%)
# Likes:    1107
# Dislikes: 98
# Total Accepted:    71.4K
# Total Submissions: 206.6K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appears once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
#
# Example 1:
#
#
# Input: "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: "cbacdcbc"
# Output: "acdb"
#
#
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
#
#

from typing import List

# @lc code=start


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index_map = {}
        for i, c in enumerate(s):
            last_index_map[c] = i

        seq: List[str] = []

        for i, c in enumerate(s):
            if c not in seq:
                while seq and seq[-1] > c and last_index_map[seq[-1]] > i:
                    seq.pop()
                seq.append(c)
        return "".join(seq)


# @lc code=end

if __name__ == "__main__":
    f = Solution().removeDuplicateLetters

    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(f("bcabc"), "abc")
    t.assertEqual(f("cbacdcbc"), "acdb")
    t.assertEqual(f("aabbcc"), "abc")
    t.assertEqual(f(""), "")
    t.assertEqual(f("abcabcabcabc"), "abc")
    t.assertEqual(f("cbacbacba"), "abc")
    t.assertEqual(f("aaaaaaaaaaaaaaa"), "a")
