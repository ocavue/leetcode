"""
submits:
- date: 2020-10-02
  minutes: 14
  cheating: true
comment: 这道题需要计算未匹配的左括号的数量
"""
#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (33.91%)
# Likes:    1997
# Dislikes: 54
# Total Accepted:    118.3K
# Total Submissions: 379.5K
# Testcase Example:  '"()"'
#
#
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#
#

# @lc code=start


class Solution:
    def checkValidString(self, s):
        min_left = max_left = 0

        for c in s:
            if c == "(":
                min_left += 1
                max_left += 1
            elif c == ")":
                max_left -= 1
                min_left = max(min_left - 1, 0)
                if max_left < 0:
                    return False
            else:
                max_left += 1
                min_left = max(min_left - 1, 0)

        return min_left == 0


# @lc code=end
if __name__ == "__main__":
    f = Solution().checkValidString

    assert f("(*()") is True
    assert f("()()") is True
    assert f("(") is False
    assert f(")(") is False
