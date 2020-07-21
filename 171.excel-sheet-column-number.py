"""
submits:
  - date: 2020-04-13
    cheating: false
"""

#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (53.35%)
# Likes:    805
# Dislikes: 139
# Total Accepted:    268.6K
# Total Submissions: 502K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
#
# For example:
#
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#
#

# @lc code=start


def char_to_base10(c: str) -> int:
    return ord(c) - ord("A") + 1


def base26_to_base10(s: str) -> int:
    result = 0
    for i, c in enumerate(reversed(s)):
        result += (26 ** i) * char_to_base10(c)
    return result


class Solution:
    def titleToNumber(self, s: str) -> int:
        return base26_to_base10(s)


# @lc code=end
if __name__ == "__main__":
    assert base26_to_base10("AB") == 28
    assert base26_to_base10("ZY") == 701
